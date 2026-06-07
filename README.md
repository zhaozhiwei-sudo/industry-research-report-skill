# Industry Research Report Skill

Codex skill for building auditable industry and stock research reports with traceable sources, market data, company mapping, valuation analysis, and professional HTML output.

[中文说明](#中文说明)

## Overview

This repository packages a reusable Codex skill for workflows such as:

- researching an industry with A/B-grade source discipline;
- collecting broker reports and institutional research;
- validating source reliability and missing-data risk;
- assembling a multi-expert team and coordinating role handoffs;
- mapping the industry chain to listed companies;
- adding PE/PB, turnover, ownership, announcements, and trading-crowding views;
- generating HTML reports, switchboards, and audit pages.

## What The Skill Produces

- Single industry research reports
- Multi-industry report suites with switchable views
- Research-report coverage audit pages
- Expert-team workflow documents
- Reusable HTML report scaffolds

## Multi-Expert Collaboration

The skill explicitly emphasizes how to build and run a research team:

- how to assemble a chief analyst, data expert, industry analyst, company analyst, valuation/trading analyst, and visualization editor;
- how to split ownership across roles;
- how to hand off source ledgers, missing-data logs, and draft findings;
- how to resolve conflicts by evidence priority instead of writing confidence.

## Source Discipline

The skill separates evidence into:

- A-level sources: government, regulator, exchange, company announcement, official statistics, international original release
- B-level sources: traceable broker reports, industry research institutions, public consulting/research abstracts

Unknown institutions, media-only summaries, forums, and unsupported reposts are excluded from final conclusions.

## Repository Layout

```text
industry-research-report/
  SKILL.md
  agents/openai.yaml
  references/
    source-grading.md
    report-workflow.md
    report-template.md
    market-data.md
    team-collaboration.md
  scripts/
    create_report_scaffold.py
examples/
  robotics-demo-report.html
  multi-industry-switchboard-demo.html
```

## Install

```bash
mkdir -p ~/.codex/skills
cp -R industry-research-report ~/.codex/skills/
```

## Example Prompt

```text
Use $industry-research-report to analyze the robotics industry, collect A/B sources,
verify broker reports, and generate a professional HTML report with a source audit.
```

## Scaffold Example

```bash
python3 industry-research-report/scripts/create_report_scaffold.py \
  --industry "机器人" \
  --slug robotics \
  --output outputs/robotics-industry-report.html
```

The scaffold is only a starting point. Fill it with verified data, A/B sources, and market evidence before delivery.

## Example Output

Open these examples in a browser:

- [examples/robotics-demo-report.html](./examples/robotics-demo-report.html): single industry report demo
- [examples/multi-industry-switchboard-demo.html](./examples/multi-industry-switchboard-demo.html): multi-industry switchboard demo

## Chinese

## 中文说明

这是一个可复用的 Codex skill，用来生成“可核查”的行业研究报告。它沉淀了我们这套实际用过的工作流，适合以下任务：

- 按 A/B 级来源调研一个行业
- 收集券商研报、产业研究和官方资料
- 核验来源可靠性和缺失数据
- 搭建多专家团队并组织角色协作
- 把产业链映射到上市公司
- 补充 PE/PB、成交额、持仓、公告与交易拥挤度分析
- 生成专业的 HTML 行业报告、总览切换页和审计页

### 核心特点

- 只允许 A/B 级来源进入主结论
- 报告结论、来源清单、市场数据、公司分层、估值交易分析可以一一对应
- 明确强调首席分析师、数据专家、行业分析师、公司分析师、估值交易分析师和可视化编辑之间的交接方式
- 适合单行业、多行业切换台、审计页、工作流文档等多种输出
- 自带 HTML 报告骨架脚本，方便快速起稿

### 产出内容

- 单行业行业报告
- 多行业切换页
- 研报覆盖审计页
- 专家团队工作流文档
- HTML 报告模板骨架

### 示例

可以直接打开下面两个 demo：

- [examples/robotics-demo-report.html](./examples/robotics-demo-report.html)：单行业报告示例
- [examples/multi-industry-switchboard-demo.html](./examples/multi-industry-switchboard-demo.html)：多行业切换台示例
