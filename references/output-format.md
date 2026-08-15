# Output Format Rules

Use this file for every resume writing, rewriting, polishing, or PDF/export task.

## Mandatory Chinese Bullet Shape

Every bullet under `实习经历`, `工作经历`, `项目经历`, `校园经历`, `创业经历`, or similar experience sections must use:

```markdown
- **关键词：** 事实背景/任务 + 行动方法 + 结果证据 + 岗位相关性。
```

Rules:

- Start every experience bullet with `- **`.
- End the keyword lead with a full-width Chinese colon inside bold text: `：**`.
- Use concise product/role keywords such as `用户洞察`, `路径优化`, `需求定义`, `MVP 落地`, `数据分析`, `增长验证`, `机制设计`, `复盘分析`, `跨团队协作`, `内容策略`, `行业研究`.
- Do not write experience paragraphs without bullets.
- Do not write bullets that only say what the user was responsible for. Each bullet needs evidence, method, output, or a concrete decision.
- Do not stop at a short one-line task label. Core experience bullets should normally occupy about 1.5-2 rendered lines in the exported A4 resume layout.

## Experience Expansion Principle

Every small experience point should be compact but sufficiently developed.

Target length:

- Core experience bullets: about 1.5-2 resume lines, usually 85-130 Chinese characters.
- Secondary experience bullets: usually 70-110 Chinese characters.
- Short one-line bullets are acceptable only for low-priority secondary items when the page is already dense.
- Short core internship/work/entrepreneurship bullets should be fixed. Short project/campus bullets may remain only when space is tight.
- If most core bullets still render as one short line in the final PDF/HTML, treat that as a layout/content failure and revise by cutting lower-priority experiences before shrinking the writing.

Each core bullet should include at least three of these:

- Context or task.
- Action or method.
- Output, evidence, metric, user feedback, or deliverable.
- Target-role meaning.

Expansion sources:

- Real method or workflow.
- Scope, user group, channel, product module, or data dimension.
- Collaboration details.
- Concrete output such as PRD, prototype, report, SOP, demo, dashboard, interview notes, or review.
- Result, metric, user feedback, or conservative qualitative evidence.

Do not expand with:

- Generic self-evaluation.
- Empty adjectives.
- Invented metrics.
- Unsupported ownership claims.

## Section Format

Use dense, scannable section anchors:

```markdown
公司 / 组织 — 岗位名称 | YYYY.MM - YYYY.MM
- **关键词：** 内容...
```

For projects:

```markdown
项目名称 — 角色 | YYYY.MM - YYYY.MM
- **关键词：** 内容...
```

## One-Page Principle

Default output is exactly one A4 page unless the user explicitly asks for a complete multi-page version.

One-page means:

- Exactly one exported page for PDF/HTML resumes.
- Visually full enough; avoid a large blank lower third when usable factual content exists.
- Readable at normal resume scale; do not solve overflow with tiny text.
- No cropped or hidden content.
- No silent switch to multi-page mode.

When the user asks for "PDF", "正式版", "可投递", "排版", or does not specify length, produce a one-page compact version first.

Only use multi-page mode when:

- The user explicitly asks for a complete version.
- The user says not to cut content.
- The user asks to preserve all material.
- A one-page compact version has already been produced and the user asks for more detail.

## One-Page Balance Rule

Do not require every bullet on the page to have the same visual thickness.

For a strong one-page Chinese resume:

- The strongest 6-8 bullets should usually read as short evidence paragraphs and often occupy about 1.5-2 rendered lines.
- Secondary bullets may be slightly shorter when they support page balance and section hierarchy.
- The page should look full but not cramped.
- Use education details, grouped skills, and one compact secondary section to complete the page when needed.
- Prefer a clear hierarchy of `primary sections thicker, secondary sections lighter` over uniform but weak density.

## Typography And Spacing Rule For A4

When producing HTML/PDF, use typography as part of the one-page fit instead of treating it as an afterthought.

Recommended Chinese resume ranges:

- Page padding: 9-11 mm vertical and 10.5-12 mm horizontal.
- Name: 30-34 px.
- Target/contact/meta: 10.5-11.2 px.
- Section title: 12-13 px.
- Entry title: 11-11.6 px.
- Date: 10.2-10.8 px.
- Experience bullet body: 10.2-10.8 px with 1.42-1.52 line-height.
- Skills/footer: 9.8-10.4 px with 1.35-1.45 line-height.

If the page has a visible empty lower area while the content is already well selected:

1. Increase bullet/body font size and line-height within the readable range.
2. Increase entry titles, section titles, meta, and skills slightly.
3. Adjust page padding by small increments.
4. Add more content only after typography is already near the upper readable range.

If the resume overflows:

1. Trim weak content first.
2. Reduce secondary section density.
3. Reduce typography only within the readable range.

Never use tiny text to fake a one-page fit, and never leave a sparse page when font size is still below the readable upper range.

## Density Targets

For a Chinese one-page resume:

- Top 2-3 experiences: usually 3 substantial bullets each.
- Other strong experiences: usually 2 substantial bullets each.
- Secondary campus/project experiences: 1-2 bullets only if they still add clear role-fit evidence.
- Core bullets should usually be 85-130 Chinese characters and occupy about 1.5-2 resume lines.
- Secondary bullets should usually be 70-110 Chinese characters.
- Not every bullet must hit the same line count; aim for `full core bullets + balanced full page`.
- If the page is visibly underfilled, expand with real method/process/evidence before increasing font size.
- If the page is visibly sparse after factual expansion, add relevant secondary experience before enlarging fonts.
- If the page is crowded, prefer fewer sections with fuller bullets instead of keeping many compressed entries.

## Expansion Order When Underfilled

When the resume does not fill an A4 page:

1. Expand core internships to 1.5-2 line bullets with methods, user groups, data dimensions, collaboration process, or outputs already present in the source.
2. Add relevant projects or campus experiences that show user research, growth, product thinking, leadership, or execution.
3. Add education details such as language scores, courses, awards, competitions, or links if factual.
4. Add compact skills grouped by real capability.
5. Add a specific 2-line summary only if factual content remains insufficient.
6. Tune layout spacing after content expansion, not before.

Useful fillers before adding an entirely new experience:

- Education details with factual scores, courses, awards, or language ability.
- A compact but relevant campus/leadership item.
- Stronger project outputs, user feedback, or deliverables.
- Better-grouped skills with clearer role relevance.

Never invent facts to fill space.

## Compression Order When Overflowing

When the resume overflows:

1. Remove generic summary.
2. Remove weak or unsupported skills.
3. Merge repeated bullets.
4. Reduce secondary projects/campus experiences.
5. Keep internships/work experience and education intact.
6. Export the strongest one-page compact version.
7. Offer a complete multi-page version separately rather than cropping or silently switching modes.

## Visual QA Shortcut

Before final delivery, ask:

- If I squint at the PDF, do the top internship bullets read like short evidence paragraphs rather than labels?
- Are there too many sections forcing every bullet to stay on one short line?
- Would removing one weaker section make the strongest bullets noticeably fuller and more convincing?

If the answer shows crowding, cut content first and re-export.

## PDF/HTML Verification

When producing designed output:

- Use A4 print CSS or equivalent page setup.
- Export the PDF before final delivery.
- Confirm page count with available tooling.
- Render or visually inspect the PDF when possible.
- Confirm typography is in the expected range and the page is neither cramped nor visibly underfilled.
- If the page count is not exactly one in compact mode, revise and re-export.
