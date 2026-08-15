---
name: yueli-resume-writer
description: Create, rewrite, polish, and export fact-first resumes from existing resumes, raw notes, portfolios, links, target roles, or JDs. Use when the user wants an agent-native resume workflow that preserves truth, prioritizes internships/projects, applies STAR writing, targets a role, controls density, and exports a polished Chinese or English Markdown plus PDF resume without relying on a resume-builder UI.
---

# Yueli Resume Writer

## Purpose

Turn scattered real experiences into a credible, dense, role-matched resume.

The resume should feel human-written, specific, and ready to submit. It should not feel like a generic AI rewrite. The core method is:

`facts first -> role translation -> experience selection -> STAR bullets -> layout verification -> export`

Default delivery expectation when tooling is available:

`Markdown source + A4 PDF export + page-count verification`

## Non-Negotiables

- Preserve facts. Never invent schools, companies, roles, dates, awards, metrics, tools, links, products, competitions, or responsibilities.
- If a fact is missing, use conservative wording or ask one concise question. Do not fill gaps with confident fiction.
- Keep internships as internships. Any experience with a company, organization, formal role, work period, client, or team belongs in `实习经历` / `Work Experience`, not `项目经历`, unless the user explicitly says it was only a project.
- Default to a one-page resume unless the user explicitly asks for a complete multi-page version. Treat one-page output as a delivery requirement, not a casual preference.
- Experiences matter most. Use `个人概述` and `技能` only when core experiences, education, projects, campus, entrepreneurship, and portfolio content are still insufficient or when the target role requires a quick skill scan.
- Sort by target relevance first, then recency. If relevance is equal, put newer experiences above older ones.
- Every major experience must show dates when known. If exact dates are missing, use the most conservative available period, e.g. `2026.03 - 2026.06`, `2026`, or `时间待补充`.
- Every resume experience must be written as bullet points. Do not write experience descriptions as prose paragraphs.
- Every Chinese resume bullet under internships, work, projects, campus, or entrepreneurship must start with a bold keyword lead in this shape: `- **用户洞察：** ...`. Do not omit the keyword lead.
- Every bullet must be evidence-bearing: keyword + factual context/task + action/method + output/result/evidence + role-fit meaning when space allows.
- Every core experience bullet should be expanded so that it visibly wraps to about 1.5-2 lines in the final A4 PDF/HTML output. Treat this as a rendered-layout requirement, not just a word-count suggestion.
- If most core bullets still render as a single short line, the draft is underwritten even if the sentence length looks acceptable in Markdown.
- Do not crop content. If a one-page resume overflows, reduce content by selection and compression, or export a multi-page complete version. Never hide overflowing content or hard-cut the page.
- Do not make text tiny to fake a full page. Keep font size readable; fill space by adding relevant factual content and stronger bullets.
- The final PDF must match the preview. Verify page count and visual layout when producing designed output.
- For formal resume delivery, prefer producing both the editable Markdown source and a PDF export when local tooling is available, even if the user only explicitly asks for "简历" or "正式版".

## One-Page Contract

Use this contract unless the user explicitly asks for a complete multi-page resume:

- Deliver exactly one A4 page for compact resumes, not "about one page".
- A one-page resume must be visually full enough: no large blank lower third when factual content exists.
- A one-page resume must remain readable: do not use tiny fonts, cramped line height, or hidden overflow to force fit.
- If content is underfilled, expand with real facts first: methods, scope, user groups, data dimensions, collaboration process, outputs, relevant projects, campus experience, education details, and compact skills.
- If content overflows, compress by selection first: remove generic summary, weak skills, repeated bullets, low-signal projects, and secondary campus bullets before cutting core internships/work.
- If the user asks for PDF/HTML, export and verify actual page count. Do not claim one page without checking when tools are available.
- If PDF export tooling is available, do not stop at Markdown for a delivery-ready resume; export the PDF and verify the page count by tool.
- If exact one-page fit is impossible without losing important factual content, produce the best one-page compact version and clearly offer a complete multi-page version as a separate artifact.

### One-Page Balance Rule

Do not interpret one-page quality as "every bullet must be equally long."

For strong one-page Chinese resumes, optimize for this balance:

- The page should feel visually full, without a large empty lower area.
- The top 6-8 core bullets should read like evidence paragraphs, usually around 1.5-2 rendered lines each.
- Secondary bullets may be shorter, often around 1.1-1.6 rendered lines, if that helps preserve page balance.
- Education details, secondary projects, compact campus items, and grouped skills may help complete the page, but should not dilute the strongest core experiences.
- Avoid both extremes: too many clipped one-line bullets, and too few oversized bullets that leave the page visually sparse.

### Typography And Spacing Rule For A4

When producing an HTML/PDF Chinese one-page resume, choose typography deliberately instead of guessing.

Recommended starting ranges:

- Page padding: 9-11 mm vertical and 10.5-12 mm horizontal.
- Name: 30-34 px.
- Target/contact/meta: 10.5-11.2 px.
- Section title: 12-13 px.
- Entry title: 11-11.6 px.
- Date: 10.2-10.8 px.
- Experience bullet body: 10.2-10.8 px with 1.42-1.52 line-height.
- Skills/footer: 9.8-10.4 px with 1.35-1.45 line-height.

Use these adjustments in order:

1. First set content selection and bullet richness.
2. If the page has a visible empty lower area, increase bullet/body font size and line-height within the readable range.
3. Then increase entry title, section title, meta, and skill font sizes slightly.
4. Then adjust page padding by small increments.
5. Only after typography reaches the upper readable range should you add more content.

Do not shrink below the readable range to force one page. Do not keep tiny text with large blank space; use font size and line-height to let the resume breathe and fill the page.

## Experience Expansion Principle

Default Chinese resume bullets should read like compact evidence paragraphs, not clipped task labels:

- Target 1.5-2 rendered lines per core bullet in the actual final A4 layout, not just in source text.
- For Markdown-only drafting, target roughly 85-130 Chinese characters per core bullet and 70-110 Chinese characters for secondary bullets.
- A strong bullet should include at least three of these four parts: context/task, action/method, output/evidence, target-role meaning.
- If a bullet fits in one short line, expand it with factual method, scope, user group, data dimension, collaboration detail, deliverable, or evidence from the source.
- Do not pad with adjectives, self-evaluation, or invented metrics. Expansion must come from real facts or conservative interpretation.
- Only allow shorter one-line bullets for low-priority secondary items when the page is already dense or overflowing.
- Treat short core internship/work/entrepreneurship bullets as errors to fix. Treat short project/campus bullets as warnings unless the page is underfilled.

### Visual Interpretation Of "1.5-2 Lines"

Use this rule to avoid ambiguity:

- In the exported A4 PDF/HTML, a core bullet should usually break onto a second line naturally.
- A bullet that stays as one compact line across the page width is usually too short for a core experience, even if it contains a metric.
- Do not satisfy this rule by shrinking the content column, forcing narrow containers, or using decorative line breaks. The bullet should wrap naturally because it contains enough factual evidence.
- If one-page space becomes tight, reduce the number of experiences or bullets before reducing core bullet richness.
- When in doubt, prefer `fewer experiences + fuller bullets` over `more experiences + clipped bullets`.

### Selection Pressure For One-Page PM Resumes

For Chinese one-page product resumes, default to this priority order:

1. 2-3 strongest internships/work experiences, each with 3 substantial bullets.
2. 1-2 strongest projects, each with 2-3 substantial bullets.
3. 1 compact campus/entrepreneurship section only if it adds clear product, growth, leadership, or user-research evidence.
4. Skills only after the above are strong enough.

If the page is crowded, cut in this order:

1. Weak summary.
2. Redundant skills.
3. Lowest-signal campus items.
4. Lowest-signal projects.
5. Extra bullets from secondary experiences.

Do not respond to crowding by making every bullet short.

### Practical Balance Strategy

When trying to satisfy both "full page" and "full bullets":

1. First ensure the top 2 experiences each have 3 strong expanded bullets.
2. Then ensure the next 1-2 experiences or projects have 2-3 solid bullets, even if slightly shorter.
3. If the lower half still feels sparse, expand with factual education details, one useful campus/entrepreneurship item, stronger project outputs, or better-grouped skills.
4. Only add another whole experience when these lower-cost expansions are insufficient.
5. Do not force every section to have identical density. A good one-page resume can have thick primary sections and lighter secondary sections.

## Required Reference Loading

- For every resume writing, rewriting, polishing, or PDF/export task, read `references/output-format.md` before drafting or editing output.
- When writing or revising bullet content quality, read `references/examples-good.md` and `references/examples-bad.md`.
- When producing a Markdown resume file, run `scripts/validate_resume.py <resume.md>` when feasible and fix format errors before final delivery.
- When producing a PDF resume from Markdown, prefer using `scripts/export_resume_pdf.py <resume.md> <resume.pdf>` when available, then verify the exported page count.

## Operating Modes

### Complete Version

Use when the user has rich experience or asks not to lose content.

- Allow multiple A4 pages if needed.
- Preserve all strong relevant experience.
- Export all pages; do not force one page.
- This is the default when the user says content has been cut off or when the source material is dense.
- If the user did not explicitly ask for this mode, do not switch to it just because fitting is hard. First produce a one-page compact version.

### One-Page Compact Version

Use by default unless the user explicitly wants a complete multi-page version.

- Fit exactly one A4 page by selecting and compressing content.
- Fill the page intentionally; if the page is sparse, add relevant factual content before changing typography.
- Do not crop.
- Do not shrink fonts below professional readability.
- Keep education + strongest internships/projects first.
- Remove weaker bullets, low-signal projects, repeated claims, and fallback summary/skills before cutting core internships.
- Prefer visibly fuller core bullets over listing every possible experience.

### Editor/HTML Version

Use when the user wants a designed resume, PDF, or editable source.

- Produce HTML/CSS or DOCX/PDF-ready layout.
- Keep dates aligned right.
- Use compact sections and dense but readable bullets.
- Render/check before final delivery when possible.

### Default PDF Delivery

Use when the user asks for a resume that is intended to be submitted, forwarded, printed, or archived.

- By default, deliver an editable Markdown resume plus an A4 PDF export when local tooling is available.
- Verify the actual exported PDF page count instead of assuming the layout fits.
- If the compact version exceeds one page, revise content selection or typography first; only then fall back to a complete multi-page export when the user explicitly wants completeness.
- Keep the PDF filename professional and role-oriented, e.g. `姓名_产品经理简历.pdf`.

## Source Reading Workflow

1. Gather all source material:
   - Existing resume or PDF/DOCX.
   - Raw experience notes.
   - Project summaries.
   - Portfolio/GitHub/product links.
   - Target role name and JD if available.
   - User preferences: Chinese/English/bilingual, photo/no photo, one page/complete version.
2. Extract a factual brief:
   - Basic info: name, phone, email, links, location if provided.
   - Education: school, major, degree, dates, GPA/rank, scholarships, competitions, relevant courses, languages.
   - Experiences: organization, role, dates, category, tasks, actions, outputs, metrics, tools, collaborators, links.
   - Target: role title, JD keywords, industry language, core evaluation criteria.
3. Build an experience inventory before writing:
   - List all candidate experiences.
   - Classify each as education, internship/work, project, campus, entrepreneurship, portfolio, award, or skill.
   - Recommend a selection order.
   - If the user wants control, ask them to confirm which experiences to include before final writing.
4. Write the resume:
   - Translate raw facts into target-role evidence.
   - Prioritize internships/work.
   - Expand selected experiences using STAR.
   - Use keyword-led bullets for every experience bullet. For Chinese resumes, use `- **关键词：** 内容...`.
- Expand each core bullet to roughly 1.5-2 resume lines; avoid clipped one-line task bullets.
- Focus especially on the first 6-8 core bullets; lower-priority bullets may be somewhat shorter if needed to preserve overall one-page balance.
- Add projects/campus/entrepreneurship to fill and strengthen the one-page resume.
- Add skills/summary only when useful or necessary.
5. Verify layout:
   - Check page count.
   - Check whether the page is visually full enough.
   - Check no cropping.
   - Check dates, section order, bullet length, photo placement, and PDF/preview consistency.
   - Check whether core bullets visually render at roughly 1.5-2 lines in the exported layout; if not, revise content selection or typography.
   - Check typography against the A4 ranges; if the page is sparse but text is below the upper readable range, increase font/line-height before adding weak content.
- For Markdown resumes, run the bundled validator when feasible.
- The validator treats short core experience bullets as hard errors and short secondary experience bullets as warnings.
- For PDF resumes, export the actual file, verify page count with tooling, and do not describe the resume as "一页" unless the exported PDF is truly one A4 page.

## Experience Selection

Before generating a final resume from many raw materials, create a short recommendation like:

```markdown
建议写入：
1. Spatius / SpatialWalk - 数字人产品与海外增长实习
2. ZooNotFound - AI 陪伴机器人产品实习
3. 新浪微博 - 品牌运营实习
4. 跃历 Career Leap - AI 简历工具
5. 抖音黑客松 - AI 健身信息流卡
6. Funlish / 校园创业 - 如版面需要补充

建议弱化或不写：
- 与目标岗位无关且缺少产出的经历
```

If the user does not respond and the task should proceed, use the recommended set.

## Section Rules

### Output Language

Always determine the target output language before writing:

- `中文`
- `English`
- `中英双语`

If the user does not specify, ask when necessary or use the most reasonable default based on the source material and use case. If the user asks for bilingual output, generate both versions and keep formatting expectations consistent across them.

### Header

Use a compact header:

`姓名`

`电话 | 邮箱 | GitHub/作品集/LinkedIn`

Optional target line only when useful:

`求职方向：投资人实习生 / VC Analyst Intern`

### Photo

- Chinese resumes may include a photo if the user provides one.
- English/international resumes usually do not need a photo unless requested.
- Keep photo aspect ratio natural.
- Place it in the top-right header area.
- It must sit above the education section line and must not cover section borders, dates, or text.

### Education

Always include education near the top unless explicitly asked otherwise.

Preferred dense format:

`学校 | 专业/学位 | 时间`

`GPA/排名 | 奖项 | 竞赛 | 语言能力 | 相关课程`

Include factual awards such as scholarships, rankings, competitions, honors, and language scores.

### Internship / Work Experience

Use company/organization as the title anchor:

`公司 / 组织 — 岗位名称` on the left, `YYYY.MM - YYYY.MM` on the right.

Write 3-5 dense keyword-led bullets for important experiences. Each bullet should include:

- Context or task.
- Action/method.
- Output/evidence/metric.
- Target-role relevance.

### Projects

Use project name as the title anchor only when it is not a formal internship.

`项目名称 — 角色` on the left, `YYYY.MM - YYYY.MM` on the right.

If the project has GitHub, demo, portfolio, article, or prototype links, embed the link in the title or place it on the title line.

### Campus / Entrepreneurship

Include when it shows:

- Leadership.
- Growth/operations.
- Monetization.
- User research.
- Community building.
- Cross-cultural communication.
- Project execution.
- Business judgment.

Do not discard campus/entrepreneurial experience just because it is not a formal internship. Reframe it toward the target role.

### Skills

Skills should be compact and grouped. Avoid random keyword dumping.

Good format:

`研究分析：行业/竞品研究、公司基本面分析、财报/招股书阅读、用户访谈、双语资料检索`

`工具与表达：Excel/飞书多维表格、Markdown、SQL/Python（如真实）、PRD/调研报告/策略文档撰写`

Only include skills that are factual or clearly supported by experience.

### Summary

Use only when:

- The resume is still visually sparse.
- The target role benefits from a concise profile.
- The user asks for it.

Keep it to 2-3 lines and make it specific. Do not write generic self-praise.

## STAR Writing Pattern

Every major bullet should follow a compressed STAR pattern:

`Action/Method + Task/Scope + Result/Evidence + Role-fit takeaway`

For Chinese resumes, the visible bullet format is mandatory:

`- **关键词：** Action/Method + Task/Scope + Result/Evidence + Role-fit takeaway`

The bullet should be long enough to show reasoning and evidence. For core Chinese bullets, prefer:

`关键词 + 场景/任务 + 方法/动作 + 证据/结果 + 岗位相关性`

Avoid writing only:

`关键词 + 做了什么`

Chinese bullet shape:

`- **行业研究：** 围绕 AI 陪伴硬件赛道调研 20+ 款软硬件产品，拆解定位、人群、定价订阅、交互玩法与用户反馈，为赛道判断和商业模式分析提供证据。`

English bullet shape:

`Market Research: Analyzed 20+ AI companion hardware/software products across positioning, target users, pricing, interaction design, and user feedback, building evidence for market and business model assessment.`

Avoid:

- `负责很多工作`
- `提升综合能力`
- `显著提升体验` without proof
- Unsupported ownership claims
- Same rhythm in every bullet
- Copying raw notes too literally

## Target-Role Translation

Translate facts into the evaluation language of the target role.

### Product Manager / AI Product

Emphasize:

- User research.
- Requirement definition.
- PRD/prototype.
- AI workflow.
- Model testing.
- Cross-functional collaboration.
- Product metrics.

### Operations / Growth

Emphasize:

- Campaigns.
- Community.
- Funnel.
- Conversion.
- Retention.
- Content.
- SOP.
- Data review.

### Marketing / Brand

Emphasize:

- Positioning.
- Audience insight.
- Brand campaign.
- Channel strategy.
- Content strategy.
- KOL/resource leverage.
- Communication results.

### Consulting / Strategy

Emphasize:

- Structured analysis.
- Business diagnosis.
- Industry research.
- Competitor benchmarking.
- Stakeholder communication.
- Insight synthesis.
- Recommendation logic.

### Investor Intern / VC Analyst

Emphasize:

- Industry mapping and market sizing logic.
- Company/competitor research.
- Business model and monetization analysis.
- Financial statement, prospectus, annual report, or earnings report reading.
- Customer/market demand validation.
- Founder/startup resource research.
- Growth channel and GTM analysis.
- AI/consumer/content/education-tech trend sensitivity.
- Clear writing and memo-style output.

Good wording:

- `训练投资研究中的供给侧扫描、可比公司拆解和成本结构判断能力。`
- `沉淀自上而下行业机会与自下而上公司需求验证的方法。`
- `辅助判断增长故事、盈利质量和规模化潜力。`
- `体现对早期产品需求真实性、用户体验和迭代速度的判断。`

Avoid making the user sound like they already made investment decisions unless factual.

### Campus Recruiting

Emphasize:

- Learning agility.
- Structured thinking.
- Internship evidence.
- Campus leadership.
- Project ownership.
- Potential and transferability.

## Density Rules

For Chinese resumes:

- Core bullets should usually be 85-130 Chinese characters depending on layout, aiming for about 1.5-2 resume lines.
- Secondary bullets should usually be 70-110 Chinese characters unless the resume is overflowing.
- Important experiences: 3-5 keyword-led bullets.
- Secondary experiences: 2-3 keyword-led bullets.
- Section spacing should be tight but readable.
- Do not leave a large blank bottom area if factual content exists. If the user asks to fill the page, treat underfilled output as incomplete until factual expansion is attempted.
- If short, expand real methods, process, evidence, project/campus experiences, education details, and compact skills before enlarging fonts.
- If long, remove repeated claims before shrinking text; do not shorten every core bullet into one-line task labels.

For English resumes:

- Use one strong sentence per bullet.
- Avoid photos by default.
- Prefer concise, active verbs.

## Layout Rules

For A4 designed output:

- Use A4 dimensions and print CSS if producing HTML.
- Keep margins professional: roughly 9-13 mm depending on density.
- Header should not waste vertical space.
- Dates align right and use consistent font size.
- Section rules must not be covered by photos or floating elements.
- Bullets use consistent indentation.
- Bold leading keywords are required for Chinese experience bullets: `- **行业研究：** ...`, `- **用户洞察：** ...`, `- **增长验证：** ...`.
- Hyperlinks should survive PDF export when possible.
- Verify page count after export.

## One-Page Fit Strategy

Goal: one A4 page, visually full, readable, and uncropped.

If underfilled:

1. Expand core internship bullets to 1.5-2 lines with factual method/output/relevance.
2. Add additional real experiences from the source inventory.
3. Add awards, language scores, relevant courses under education.
4. Add compact skills.
5. Add a brief summary only as a last resort.
6. If producing HTML/PDF, adjust margins and section spacing only after factual content has been expanded.

If overflowing:

1. Remove generic summary first.
2. Remove weak skills.
3. Compress repeated bullets.
4. Reduce secondary projects to one bullet.
5. Keep strongest internships and education intact.
6. If still overflowing, produce the strongest one-page compact version and offer a complete multi-page version separately. Do not silently switch modes.

## Output Formats

### Text/Markdown

```markdown
# 姓名
电话 | 邮箱 | 作品链接

## 教育经历
学校 | 专业/学位 | 时间
GPA/排名 | 奖项 | 相关课程/语言能力

## 实习经历
公司 — 岗位 | 时间
- **关键词：** 内容...
- **关键词：** 内容...
- **关键词：** 内容...

## 项目经历
项目 — 角色 | 时间
- **关键词：** 内容...
- **关键词：** 内容...
```

### HTML/PDF

When asked for PDF:

1. Produce editable HTML/CSS source.
2. Export to PDF.
3. Confirm page count.
4. Confirm the page is visually full enough and not crowded.
5. Render or visually inspect the PDF if tools are available.
6. If photo is included, verify it sits above the education rule and does not distort.

## Quality Checklist

Before final delivery, verify:

- Basic info is correct.
- Education is present.
- Internships are not misclassified as projects.
- Major experiences have dates.
- Role keywords are reflected naturally.
- Bullets are fact-based and not generic.
- Every Chinese experience bullet starts with `- **关键词：**`.
- Important experiences have enough bullets to show context, method, evidence, and role-fit. A single vague bullet is not enough.
- Core experience bullets are not clipped to one short line; they are expanded to show method and evidence.
- Claims trace back to source material.
- Page is exactly one A4 page unless the user explicitly requested a complete multi-page version.
- Page is full enough but not crowded.
- PDF does not crop content.
- Preview and export match.
- If a photo is used, it is correctly placed and not stretched.

## Quick Variant Commands

When the user asks for quick changes, apply these without requiring a long prompt:

- `更像产品经理`: emphasize user research, requirements, prioritization, PRD, cross-functional collaboration, product metrics.
- `更像运营`: emphasize campaigns, communities, growth funnels, conversion, content, retention, execution.
- `更像市场`: emphasize positioning, audience insight, campaign planning, brand, channel strategy, data review.
- `更像咨询`: emphasize structured analysis, business diagnosis, competitor research, stakeholder communication, insight synthesis.
- `更像投资人实习生`: emphasize industry research, competitor/company analysis, business model, financial signals, growth channels, market demand validation, and memo-style output.
- `更数据化`: add real metrics, denominators, methods, dashboards, A/B tests, SQL/Python/Tableau only if factual.
- `更简洁`: compress wording while preserving facts, results, and role-fit takeaway.
- `更适合校招`: emphasize potential, learning agility, campus leadership, internships, projects, awards, and transferable skills.

## Missing Facts Protocol

If key facts are missing:

- Ask one concise question if the missing fact blocks the resume.
- Use conservative wording when ownership is unclear: `参与`, `协助`, `支持`.
- Use qualitative evidence when no metric exists: `输出调研报告`, `完成竞品拆解`, `搭建 SOP`.
- Mark placeholders only when necessary: `时间待补充`.
- Never invent a metric just because the bullet looks stronger with numbers.
