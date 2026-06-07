---
name: industry-research-report
description: Build auditable industry and stock research reports with A/B source discipline, market-data collection, research-report inventory, expert-role workflow, valuation/trading analysis, and professional HTML output. Use when Codex is asked to analyze an industry, collect broker or institutional reports, verify source reliability, compare listed companies, generate an industry research report, create a visual HTML dashboard, update a multi-report switchboard, or document the report-production workflow.
---

# Industry Research Report

Use this skill to produce professional, evidence-backed industry reports. The expected output is usually an HTML report or a set of linked/integrated HTML reports with source lists, company dashboards, valuation/trading indicators, and a verification trail.

## Core Workflow

1. Define scope: industry boundary, regions/markets, listed-company universe, report date, and whether the output is a single report, multi-industry switchboard, audit page, or reusable workflow document.
2. Build the expert-team workflow:
   - Chief analyst: investment conclusion, rating, industry logic.
   - Data expert: source reliability, research-report inventory, market data and missing-data log.
   - Industry analyst: demand split, policy, price, capacity, technology path.
   - Company analyst: listed-company mapping, announcements, financials, order evidence.
   - Valuation and trading analyst: PE/PB, turnover, ownership, historical percentile when available.
   - Visualization editor: HTML structure, tables, charts, navigation, final QA.
3. Collect only A/B sources for conclusions:
   - A: official/government/regulator/exchange/company announcement/international original release.
   - B: traceable broker report, industry research institution, consulting/public research abstract.
   - Exclude unknown institutions, media-only summaries, forums, unsupported reposts, and untraceable report snippets from conclusions.
4. Inventory research reports before writing:
   - Record source grade, institution, title, date, market/coverage, use in report, and URL.
   - Count total A/B sources, specific research reports, broker reports, and companies with missing reports.
   - Keep rejected candidates in notes only when useful; do not cite them as evidence.
5. Gather market and company data:
   - For China A-shares, use the `a-stock-data` skill when available.
   - Record collection date/time and failed endpoints.
   - Separate observed values, calculated metrics, and interpretation.
6. Draft report in this order:
   - Executive conclusion and rating.
   - Key facts and evidence strength.
   - Industry logic chain.
   - Research-report consensus.
   - Demand split and price/capacity tracking.
   - Technology roadmap.
   - Company stratification.
   - Valuation/trading dashboard.
   - Announcement verification.
   - Risk triggers and source list.
7. Verify before delivery:
   - Every material conclusion maps to at least one A/B source.
   - Source list has institution, title, date, link, grade, and use.
   - Counts in report, audit page, and switchboard match.
   - HTML loads locally, industry switching works, and key sections are visible.

## Report Types

- Single industry report: build one self-contained HTML page.
- Multi-industry suite: build or update each report, then update the switchboard and audit page after every new report.
- Integrated single HTML: embed all reports plus audit page into one switchable file when the user asks for portability.
- Workflow document: summarize expert roles, step outputs, verification method, and entry criteria for each step.

## References

Read only the needed reference:

- `references/source-grading.md`: source levels, inclusion rules, and rejection rules.
- `references/report-workflow.md`: step-by-step production workflow and verification gates.
- `references/report-template.md`: recommended sections, tables, and HTML structure.
- `references/market-data.md`: market-data fields, A-share workflow, and missing-data handling.

## Scripts

Use `scripts/create_report_scaffold.py` when starting a new industry report from scratch and a deterministic HTML skeleton is useful:

```bash
python3 scripts/create_report_scaffold.py --industry "机器人" --slug robotics --output outputs/robotics-industry-report.html
```

The scaffold is only a starting point; fill it with verified data and sources before delivery.
