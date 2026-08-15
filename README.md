# 跃历 Resume Writer

一个面向 AI Agent 的事实优先简历写作 Skill。

它把零散经历、旧简历、作品集与目标 JD 整理成可信、匹配岗位、可以直接投递的一页 A4 简历。核心不是把人“写得更厉害”，而是守住真实事实，再把经历翻译成目标岗位能理解的语言。

## 它能做什么

- 从旧简历、原始笔记、作品集和 JD 中提取事实
- 按目标岗位筛选、排序并重组经历
- 使用 STAR 方法写出有证据的经历要点
- 默认控制为一页 A4，不裁切、不靠小字硬塞
- 输出可编辑 Markdown，并在环境允许时导出 PDF
- 校验中文经历要点格式、长度和信息密度

## 安装

```bash
npx skills add wangranm-a11y/yueli-resume-writer
```

也可以手动复制到 Codex Skills 目录：

```bash
git clone https://github.com/wangranm-a11y/yueli-resume-writer.git
cp -R yueli-resume-writer ~/.codex/skills/yueli-resume-writer
```

重新开始一个 Codex 任务后即可使用。

## 使用示例

```text
用 $yueli-resume-writer 把我的旧简历和目标产品经理 JD，重写成一页中文简历。
```

```text
用 $yueli-resume-writer 根据这些项目笔记生成一份英文 AI Product Intern 简历，不要编造数据。
```

## 工作方法

```text
事实提取 → 岗位翻译 → 经历筛选 → STAR 重写 → 一页排版 → 导出验证
```

三条核心原则：

1. **事实优先**：不编造公司、岗位、时间、奖项、数据、技能或职责。
2. **经历优先**：用教育、实习、项目和创业经历证明能力，不用空泛自我评价凑版面。
3. **可投递优先**：默认交付真正的一页 A4，并检查页面密度、可读性和导出结果。

## 目录

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── examples-good.md
│   ├── examples-bad.md
│   └── output-format.md
└── scripts/
    ├── validate_resume.py
    └── export_resume_pdf.py
```

## 依赖

Skill 的写作流程本身不要求 API Key。

PDF 导出脚本使用 Python，并依赖 `reportlab`、`Pillow` 与系统中的 `pdfinfo`。如果环境没有这些依赖，Agent 仍可正常输出和校验 Markdown 简历。

## License

MIT
