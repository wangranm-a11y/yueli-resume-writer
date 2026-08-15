#!/usr/bin/env python3
"""Export a Yueli-style Markdown resume to an A4 PDF."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
KEYWORD_BULLET_RE = re.compile(r"^\s*-\s+\*\*([^*\n：:]{2,16})：\*\*\s*(.+)$")


@dataclass
class Entry:
    title: str
    bullets: list[str]


@dataclass
class Section:
    title: str
    entries: list[Entry]


@dataclass(frozen=True)
class LayoutPreset:
    name_size: float
    meta_size: float
    section_size: float
    entry_size: float
    date_size: float
    bullet_size: float
    bullet_leading: float
    body_size: float
    body_leading: float
    left_margin_mm: float
    right_margin_mm: float
    top_margin_mm: float
    bottom_margin_mm: float
    after_name: float
    after_meta: float
    after_rule: float
    before_section: float
    after_section: float
    after_entry: float
    after_bullet: float


PRESETS = [
    LayoutPreset(33, 11.0, 12.8, 11.4, 10.5, 10.7, 15.2, 10.5, 14.7, 11.8, 11.8, 10.6, 10.4, 4, 2.5, 5, 8, 4, 2.5, 1.8),
    LayoutPreset(32, 10.9, 12.5, 11.2, 10.4, 10.5, 14.9, 10.4, 14.5, 11.5, 11.5, 10.2, 10.0, 4, 2.5, 5, 7, 3.5, 2.2, 1.5),
    LayoutPreset(31, 10.7, 12.3, 11.0, 10.3, 10.3, 14.6, 10.2, 14.2, 11.2, 11.2, 10.0, 9.8, 3.5, 2.2, 4.5, 6.5, 3.2, 2.0, 1.4),
    LayoutPreset(30, 10.6, 12.1, 10.9, 10.2, 10.1, 14.2, 10.0, 13.9, 10.9, 10.9, 9.8, 9.6, 3.2, 2.0, 4.0, 6.0, 3.0, 1.8, 1.2),
    LayoutPreset(29, 10.4, 12.0, 10.8, 10.1, 9.9, 13.9, 9.9, 13.6, 10.6, 10.6, 9.5, 9.3, 3.0, 1.8, 3.8, 5.5, 2.8, 1.6, 1.0),
]


def escape_with_links(text: str) -> str:
    parts: list[str] = []
    last = 0
    for match in LINK_RE.finditer(text):
        parts.append(html.escape(text[last:match.start()]))
        label = html.escape(match.group(1))
        href = html.escape(match.group(2), quote=True)
        parts.append(f'<link href="{href}" color="#1f4e79">{label}</link>')
        last = match.end()
    parts.append(html.escape(text[last:]))
    return "".join(parts)


def parse_resume_markdown(path: Path) -> tuple[str, list[str], list[Section]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("resume markdown must start with '# 姓名'")

    name = lines[0][2:].strip()
    meta_lines: list[str] = []
    sections: list[Section] = []
    current_section: Section | None = None
    current_entry: Entry | None = None
    in_header = True

    for raw_line in lines[1:]:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("## "):
            in_header = False
            current_entry = None
            current_section = Section(title=stripped[3:].strip(), entries=[])
            sections.append(current_section)
            continue

        if in_header:
            meta_lines.append(stripped)
            continue

        if current_section is None:
            continue

        if stripped.startswith("- "):
            if current_entry is None:
                current_entry = Entry(title="", bullets=[])
                current_section.entries.append(current_entry)
            current_entry.bullets.append(stripped)
            continue

        current_entry = Entry(title=stripped, bullets=[])
        current_section.entries.append(current_entry)

    return name, meta_lines, sections


def split_title_and_date(title: str) -> tuple[str, str]:
    if " | " not in title:
        return title, ""
    left, right = title.rsplit(" | ", 1)
    return left.strip(), right.strip()


def register_fonts() -> None:
    regular_candidates = [
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    bold_candidates = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]

    regular_path = next((path for path in regular_candidates if os.path.exists(path)), None)
    bold_path = next((path for path in bold_candidates if os.path.exists(path)), None)

    if not regular_path or not bold_path:
        raise FileNotFoundError("No supported Chinese font found for PDF export")

    pdfmetrics.registerFont(TTFont("ResumeSans", regular_path))
    pdfmetrics.registerFont(TTFont("ResumeSans-Bold", bold_path))
    pdfmetrics.registerFontFamily(
        "ResumeSans",
        normal="ResumeSans",
        bold="ResumeSans-Bold",
        italic="ResumeSans",
        boldItalic="ResumeSans-Bold",
    )


def build_styles(preset: LayoutPreset) -> StyleSheet1:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="ResumeName",
            fontName="ResumeSans-Bold",
            fontSize=preset.name_size,
            leading=preset.name_size + 1.5,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111111"),
            spaceAfter=preset.after_name,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeMeta",
            fontName="ResumeSans",
            fontSize=preset.meta_size,
            leading=preset.meta_size + 2.2,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#2c2c2c"),
            spaceAfter=preset.after_meta,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            fontName="ResumeSans-Bold",
            fontSize=preset.section_size,
            leading=preset.section_size + 1.2,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#0f2742"),
            spaceBefore=preset.before_section,
            spaceAfter=preset.after_section,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="EntryTitle",
            fontName="ResumeSans-Bold",
            fontSize=preset.entry_size,
            leading=preset.entry_size + 1.4,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#161616"),
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="EntryDate",
            fontName="ResumeSans",
            fontSize=preset.date_size,
            leading=preset.date_size + 1.2,
            alignment=TA_RIGHT,
            textColor=colors.HexColor("#555555"),
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeBullet",
            fontName="ResumeSans",
            fontSize=preset.bullet_size,
            leading=preset.bullet_leading,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#161616"),
            leftIndent=10,
            firstLineIndent=-10,
            spaceAfter=preset.after_bullet,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyTextCompact",
            fontName="ResumeSans",
            fontSize=preset.body_size,
            leading=preset.body_leading,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#222222"),
            wordWrap="CJK",
        )
    )
    return styles


def scaled_photo_size(photo_path: Path, max_width: float, max_height: float) -> tuple[float, float]:
    reader = ImageReader(str(photo_path))
    raw_width, raw_height = reader.getSize()
    scale = min(max_width / raw_width, max_height / raw_height)
    width = raw_width * scale
    height = raw_height * scale
    return width, height


def render_bullet(line: str, styles: StyleSheet1) -> Paragraph:
    match = KEYWORD_BULLET_RE.match(line)
    if match:
        keyword = html.escape(match.group(1))
        content = escape_with_links(match.group(2))
        text = f'- <b>{keyword}：</b> {content}'
    else:
        text = f"- {escape_with_links(line[2:].strip())}"
    return Paragraph(text, styles["ResumeBullet"])


def build_story(
    name: str,
    meta_lines: list[str],
    sections: list[Section],
    styles: StyleSheet1,
) -> list:
    story: list = [Paragraph(html.escape(name), styles["ResumeName"])]
    for meta_line in meta_lines:
        story.append(Paragraph(escape_with_links(meta_line), styles["ResumeMeta"]))

    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#c7cdd5"), spaceAfter=styles["ResumeMeta"].spaceAfter + 1))

    for section in sections:
        story.append(Paragraph(html.escape(section.title), styles["SectionTitle"]))
        for entry in section.entries:
            if entry.title:
                left_title, right_date = split_title_and_date(entry.title)
                if right_date:
                    table = Table(
                        [[Paragraph(escape_with_links(left_title), styles["EntryTitle"]), Paragraph(html.escape(right_date), styles["EntryDate"])]],
                        colWidths=[118 * mm, 60 * mm],
                    )
                    table.setStyle(
                        TableStyle(
                            [
                                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                ("TOPPADDING", (0, 0), (-1, -1), 0),
                                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                            ]
                        )
                    )
                    story.append(table)
                else:
                    story.append(Paragraph(escape_with_links(left_title), styles["EntryTitle"]))

            if entry.bullets:
                for bullet in entry.bullets:
                    story.append(render_bullet(bullet, styles))
                story.append(Spacer(1, styles["ResumeBullet"].spaceAfter + 0.5))
            elif entry.title:
                story.append(Spacer(1, styles["BodyTextCompact"].leading / 4))
    return story


def draw_header_photo(canvas, doc, photo_path: Path) -> None:
    photo_width, photo_height = scaled_photo_size(photo_path, max_width=21 * mm, max_height=27 * mm)
    page_width, page_height = doc.pagesize
    x = page_width - doc.rightMargin - photo_width
    y = page_height - doc.topMargin - photo_height + 2
    canvas.drawImage(str(photo_path), x, y, width=photo_width, height=photo_height, preserveAspectRatio=True, mask="auto")


def detect_pages(pdf_path: Path, pdfinfo_path: str | None) -> int:
    tool = pdfinfo_path or shutil.which("pdfinfo")
    if not tool:
        raise FileNotFoundError("pdfinfo not found; cannot verify PDF page count")

    result = subprocess.run([tool, str(pdf_path)], check=True, capture_output=True, text=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if not match:
        raise RuntimeError("Failed to parse page count from pdfinfo output")
    return int(match.group(1))


def export_with_preset(
    source: Path,
    output: Path,
    preset: LayoutPreset,
    pdfinfo_path: str | None,
    photo_path: Path | None,
) -> int:
    name, meta_lines, sections = parse_resume_markdown(source)
    styles = build_styles(preset)
    story = build_story(name, meta_lines, sections, styles)

    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=preset.left_margin_mm * mm,
        rightMargin=preset.right_margin_mm * mm,
        topMargin=preset.top_margin_mm * mm,
        bottomMargin=preset.bottom_margin_mm * mm,
        title=f"{name} Resume",
        author=name,
    )
    if photo_path:
        doc.build(story, onFirstPage=lambda canvas, page_doc: draw_header_photo(canvas, page_doc, photo_path))
    else:
        doc.build(story)
    return detect_pages(output, pdfinfo_path)


def choose_and_export(
    source: Path,
    output: Path,
    target_pages: int,
    pdfinfo_path: str | None,
    photo_path: Path | None,
) -> tuple[int, LayoutPreset]:
    best_pages = sys.maxsize
    best_preset = PRESETS[-1]
    best_pdf: bytes | None = None

    for preset in PRESETS:
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            pages = export_with_preset(source, tmp_path, preset, pdfinfo_path, photo_path)
            pdf_bytes = tmp_path.read_bytes()
            if pages < best_pages:
                best_pages = pages
                best_preset = preset
                best_pdf = pdf_bytes
            if pages <= target_pages:
                output.write_bytes(pdf_bytes)
                return pages, preset
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    if best_pdf is None:
        raise RuntimeError("Failed to export any PDF output")

    output.write_bytes(best_pdf)
    return best_pages, best_preset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a Yueli-style Markdown resume to PDF")
    parser.add_argument("resume_md", type=Path, help="Input Markdown resume path")
    parser.add_argument("resume_pdf", type=Path, help="Output PDF path")
    parser.add_argument("--target-pages", type=int, default=1, help="Preferred maximum page count")
    parser.add_argument("--pdfinfo-path", type=str, default=None, help="Explicit pdfinfo binary path")
    parser.add_argument("--photo", type=Path, default=None, help="Optional photo/avatar path for top-right header placement")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    register_fonts()
    pages, preset = choose_and_export(args.resume_md, args.resume_pdf, args.target_pages, args.pdfinfo_path, args.photo)
    print(f"Exported {args.resume_pdf} ({pages} page(s), bullet font {preset.bullet_size} pt)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
