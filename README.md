# Industry Research Report Skill

An auditable Codex skill for building professional industry and stock research reports.

The skill is designed for workflows such as:

- collecting A/B-grade sources and broker research reports;
- validating source reliability and missing-data risk;
- mapping industry chains to listed companies;
- adding market data, PE/PB, turnover, ownership and announcement checks;
- generating HTML industry reports, multi-industry switchboards and audit pages.

## What It Produces

- Single industry research reports.
- Multi-industry report suites with switchable views.
- Research-report coverage audit pages.
- Expert-team workflow documents.
- Reusable HTML report scaffolds.

## Source Discipline

The skill separates evidence into:

- **A-level sources**: government, regulator, exchange, company announcement, official statistics, international original release.
- **B-level sources**: traceable broker reports, industry research institutions and public consulting/research abstracts.

Unknown institutions, media-only summaries, forums and unsupported reposts are excluded from final conclusions.

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
  scripts/
    create_report_scaffold.py
```

## Install

Copy the skill folder into your Codex skills directory:

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

The scaffold is only a starting point. Fill it with verified data, A/B sources and market evidence before delivery.
