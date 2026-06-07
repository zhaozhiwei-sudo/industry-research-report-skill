---
name: industry-research-report
description: Build auditable industry and stock research reports with A/B source discipline, market-data collection, research-report inventory, expert-role workflow, valuation/trading analysis, and professional HTML output. Use when Codex is asked to analyze an industry, collect broker or institutional reports, verify source reliability, compare listed companies, generate an industry research report, create a visual HTML dashboard, update a multi-report switchboard, or document the report-production workflow.
---

# Industry Research Report

Use this skill to produce professional, evidence-backed industry reports. The expected output is usually an HTML report or a set of linked/integrated HTML reports with source lists, company dashboards, valuation/trading indicators, and a verification trail.

## Multi-Expert Team

Treat this skill as a multi-expert workflow, not a single linear writing task. Build a team with explicit ownership before drafting:

- Chief analyst: own scope, rating, final investment conclusion, and conflict resolution.
- Data expert: own source grading, research-report inventory, missing-data log, and reliability review.
- Industry analyst: own policy, demand split, price/capacity tracking, and technology route.
- Company analyst: own listed-company mapping, announcements, financial evidence, and order/capacity verification.
- Valuation and trading analyst: own PE/PB, turnover, ownership/holding, percentile logic when available, and crowding interpretation.
- Visualization editor: own HTML structure, tables, navigation, consistency checks, and final presentation QA.

Scale the team to the task:

- Small report: chief analyst + data expert + one combined industry/company analyst.
- Standard industry report: use all roles above.
- Multi-industry suite: keep one shared data expert and one shared visualization editor across all reports for consistency.

## Collaboration Rules

Run the team with explicit handoffs:

1. The chief analyst defines scope and the initial company universe.
2. The data expert opens the source ledger first and blocks unsupported claims before drafting starts.
3. The industry, company, and valuation analysts work in parallel but must write against the same source ledger and timestamped data snapshot.
4. The chief analyst merges conclusions only after role outputs are complete enough to compare.
5. The visualization editor formats only after conclusion text, source counts, and tables are stable.

Use these handoff contracts:

- Every expert output must state: what was observed, what was inferred, what source supports it, and what remains missing.
- If two experts disagree, resolve in this order: A-level source, company announcement/financial filing, B-level consensus, then analyst interpretation.
- If a number cannot be verified, keep the field blank or mark it as missing; do not smooth over uncertainty.
- If a conclusion depends on a missing datapoint, downgrade the confidence rather than hiding the gap.

## Core Workflow

1. Define scope: industry boundary, regions/markets, listed-company universe, report date, and whether the output is a single report, multi-industry switchboard, audit page, or reusable workflow document.
2. Build the expert team before writing:
   - Assign roles and decide whether any role is shared across multiple reports.
   - Open one shared source ledger and one shared missing-data log.
   - Define the merge owner, usually the chief analyst.
   - Define the presentation owner, usually the visualization editor.
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

- `references/team-collaboration.md`: team setup, role boundaries, handoff templates, and conflict-resolution rules.
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
