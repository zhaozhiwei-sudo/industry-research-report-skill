# Market Data Workflow

## A-Share Data

When China A-share market data is needed, use the `a-stock-data` skill if available.

Collect:

- Stock code and name
- Segment/value-chain role
- Price and daily change
- PE and PB
- Market cap
- Turnover amount and turnover rate
- Northbound/ownership fields when available
- Announcement count and recent key announcement links

Always report:

- Collection date/time
- Failed endpoints
- Missing fields
- Whether values are observed, calculated, or interpreted

## Valuation And Trading Crowding

Useful fields:

- PE(TTM), PB, market cap
- Turnover amount and turnover rate
- Ownership/holding percentile if reliable historical holding data is available
- Historical PE/PB percentile only when there is a real historical series

Do not fabricate percentiles. If percentile data is unavailable, write:

- "缺历史序列，暂不计算分位"
- "仅以当前横截面热度判断"
- "需要后续接入历史行情/持仓数据"

## Company Announcements

Use company announcements to verify:

- Revenue/profit trend
- Orders/contracts
- Capacity expansion
- Financing
- Related-party transactions
- Regulatory inquiry or risk warning

Prefer official exchange/CNInfo/company filing links.

## Missing-Data Handling

Every report should include a concise note when fields are missing:

- Which field is missing
- Which endpoint/source failed
- Whether this affects the conclusion
- What should be collected next
