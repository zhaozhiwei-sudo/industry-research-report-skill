# Auditable Report Workflow

## Team Setup

Before Step 1, define who owns each part of the report:

- Chief analyst: final narrative and rating.
- Data expert: source ledger and reliability checks.
- Industry analyst: policy, demand, pricing, and technology route.
- Company analyst: listed-company evidence and announcement verification.
- Valuation and trading analyst: valuation dashboard and crowding interpretation.
- Visualization editor: HTML layout, navigation, and final consistency.

Minimum operating rule:

- No expert writes a final conclusion without citing the source rows that support it.
- No section is considered finished until another role can verify where its evidence came from.

## Step 1: Scope And Universe

Output:

- Industry definition and excluded adjacent sectors.
- Geographic and capital-market scope.
- Initial listed-company pool.
- Target report date and data collection time.

Verification:

- Company universe must match the industry value chain.
- Scope must be narrow enough for source collection.

Entry standard for next step:

- Industry boundary, company pool, and output format are explicit.
- Team role ownership is explicit.

## Step 2: Source Inventory

Output:

- A/B source table with grade, institution, title, date, market, purpose, and URL.
- Counts for total A/B sources, concrete research reports, broker reports.
- Rejected or missing-source companies if relevant.

Verification:

- Open representative links.
- Remove unknown institutions and media-only summaries.
- Prefer primary sources over reposts.
- Require the data expert to flag unsupported claims before other experts draft around them.

Entry standard:

- At least several A-level anchors and enough B-level reports to support consensus.
- The source ledger is shared across the full team.

## Step 3: Data Collection

Output:

- Market-data table: price, change, PE, PB, market cap, turnover, turnover rate, ownership/holding if available.
- Company-announcement table: latest quarterly/annual reports, important contracts, financing, risk notices.
- Missing fields and failed endpoint log.

Verification:

- Record collection timestamp.
- Cross-check suspicious outliers.
- Never invent missing PE/PB/holding percentiles.
- Require all analysts to use the same dated snapshot for comparable fields.

Entry standard:

- Core company pool has current market data or a documented missing-data reason.

## Step 4: Industry Analysis

Output:

- Executive conclusion and score/rating.
- Key facts with source attribution.
- Industry logic chain.
- Demand split, price/capacity tracking, technology roadmap, risk triggers.

Verification:

- Every important conclusion maps to source rows.
- Separate factual observation from interpretation.
- Resolve disagreements by evidence priority, not by writing confidence.

Entry standard:

- The report can explain both upside drivers and downside triggers.

## Step 5: Company And Valuation Analysis

Output:

- Company stratification by value-chain position and confidence.
- Financial/announcement evidence.
- Valuation and trading dashboard.
- Watchlist and downgrade conditions.

Verification:

- Avoid recommending high-valuation names without order/profit evidence.
- Flag stale, missing, or unreliable fields.
- Make the chief analyst explicitly approve any high-confidence conclusion on incomplete data.

Entry standard:

- Company conclusions are supported by announcements, data, or traceable reports.

## Step 6: HTML Report And Audit

Output:

- Professional HTML report with stable navigation.
- Source list at the end.
- If multi-industry: switchboard and coverage audit page updated.
- If requested: integrated single-file HTML suite.

Verification:

- Open locally in browser.
- Check section anchors, source rows, and counts.
- Confirm switchboard metadata matches report counts.
- Confirm that section text, source tables, and expert conclusions still agree after layout edits.

Entry standard:

- The report is readable, links work, and counts are consistent.
