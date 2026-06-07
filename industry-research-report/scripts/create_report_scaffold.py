#!/usr/bin/env python3
"""Create a compact HTML scaffold for an auditable industry report."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from string import Template


HTML_TEMPLATE = Template("""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>${industry}行业专业投研报告</title>
  <style>
    :root { --ink:#17202e; --muted:#667085; --line:#d9e2ec; --paper:#fff; --soft:#f5f8fb; --navy:#12343b; --teal:#0f766e; --blue:#2457c5; --green:#027a48; --red:#b42318; --shadow:0 18px 42px rgba(20,31,48,.12); }
    *{box-sizing:border-box} body{margin:0;color:var(--ink);font-family:Inter,"PingFang SC","Microsoft YaHei",Arial,sans-serif;background:#edf2f7} a{color:var(--teal);text-decoration:none} h1,h2,h3,p{margin:0}
    .page{max-width:1360px;margin:0 auto;padding:28px}.hero{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:18px;margin-bottom:18px}.hero-main{min-height:310px;padding:30px;border-radius:8px;color:#fff;background:var(--navy);box-shadow:var(--shadow);display:flex;flex-direction:column;justify-content:space-between}.eyebrow{color:#bdf4eb;font-size:13px;font-weight:900}h1{font-size:clamp(36px,5vw,60px);line-height:1.04;letter-spacing:0}.lead{max-width:920px;margin-top:18px;color:#d7e1eb;font-size:15px;line-height:1.8}.score-panel,.card,.metric{border:1px solid var(--line);border-radius:8px;background:var(--paper)}.score-panel{padding:22px;box-shadow:var(--shadow)}.score{margin:12px 0 8px;font-size:72px;line-height:1;font-weight:950}.rating{display:inline-flex;padding:6px 12px;border-radius:999px;color:#fff;background:var(--teal);font-size:13px;font-weight:900}.metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:18px}.metric{min-height:120px;padding:16px}.metric span{color:var(--muted);display:block;font-size:12px;font-weight:900}.metric strong{display:block;margin-top:9px;font-size:24px}.metric small{display:block;margin-top:7px;color:#475467;font-size:12px;line-height:1.55}.shell{display:grid;grid-template-columns:230px minmax(0,1fr);gap:18px;align-items:start}.toc{position:sticky;top:18px;padding:16px}.toc h2{margin-bottom:10px;font-size:14px}.toc a{display:block;padding:8px 0;border-bottom:1px solid #edf0f5;color:#475467;font-size:12px;font-weight:800}.layout{display:grid;gap:18px}.section-title{padding:14px 16px;border-bottom:1px solid #e7ecf2;background:#fbfcfe;display:flex;align-items:center;justify-content:space-between;gap:12px}.section-title h2{font-size:17px}.pill{display:inline-flex;padding:3px 8px;border-radius:999px;color:var(--teal);border:1px solid #bcd7d4;background:#effaf8;font-size:12px;font-weight:900}.body{padding:16px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.box{padding:15px;border:1px solid #d9e1ec;border-radius:8px;background:#fbfcfe}.box h3{margin-bottom:9px;font-size:15px}.box p,td,th,.note{color:#475467;font-size:13px;line-height:1.65}.table-wrap{overflow-x:auto}table{width:100%;min-width:960px;border-collapse:collapse}th,td{padding:11px 10px;border-bottom:1px solid #edf0f5;text-align:left;vertical-align:top}th{color:#344054;background:#fbfcfe;font-size:12px;font-weight:950}td strong{display:block;color:var(--ink);margin-bottom:3px}.note{padding:14px 16px;background:#fff}
    @media(max-width:1000px){.hero,.shell{grid-template-columns:1fr}.toc{position:static}.metrics,.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:680px){.page{padding:16px}.metrics,.grid{grid-template-columns:1fr}h1{font-size:36px}}
  </style>
</head>
<body>
  <main class="page">
    <section class="hero">
      <div class="hero-main">
        <div>
          <div class="eyebrow">${industry} Industry Research / A-B Source Discipline / ${today}</div>
          <h1>${industry}行业专业投研报告</h1>
          <p class="lead">请在此处写入行业边界、核心主题和报告摘要。结论只采用 A/B 来源，并在文末列出来源与报告名称清单。</p>
        </div>
      </div>
      <aside class="score-panel">
        <span>结论级别</span>
        <div class="score">--</div>
        <span class="rating">待核验</span>
      </aside>
    </section>

    <section class="metrics">
      <div class="metric"><span>政策节点</span><strong>待填</strong><small>写入 A 级政策或监管依据。</small></div>
      <div class="metric"><span>需求变化</span><strong>待填</strong><small>写入需求来源和验证方式。</small></div>
      <div class="metric"><span>研报入库</span><strong>待填</strong><small>写入 A/B 来源数量。</small></div>
      <div class="metric"><span>估值交易</span><strong>待填</strong><small>写入 PE/PB、成交额、拥挤度口径。</small></div>
    </section>

    <section class="shell">
      <nav class="toc card">
        <h2>报告目录</h2>
        <a href="#summary">1. 投研结论</a>
        <a href="#facts">2. 关键事实</a>
        <a href="#consensus">3. 研报共识</a>
        <a href="#companies">4. 公司分层</a>
        <a href="#valuation">5. 估值交易</a>
        <a href="#sources">6. 来源清单</a>
      </nav>
      <section class="layout">
        <article id="summary" class="card"><div class="section-title"><h2>一、投研结论</h2><span class="pill">结论</span></div><div class="body grid"><div class="box"><h3>配置结论</h3><p>待填。</p></div><div class="box"><h3>核心股票池</h3><p>待填。</p></div><div class="box"><h3>反证条件</h3><p>待填。</p></div></div></article>
        <article id="facts" class="card"><div class="section-title"><h2>二、关键事实</h2><span class="pill">A/B 来源</span></div><div class="body grid"><div class="box"><h3>A 级事实</h3><p>待填。</p></div><div class="box"><h3>B 级共识</h3><p>待填。</p></div><div class="box"><h3>数据缺口</h3><p>待填。</p></div></div></article>
        <article id="consensus" class="card"><div class="section-title"><h2>三、研报共识与证据链</h2><span class="pill">本轮入库</span></div><div class="table-wrap"><table><thead><tr><th>主题</th><th>主要来源</th><th>一致结论</th><th>投资判断方式</th></tr></thead><tbody><tr><td>待填</td><td>待填</td><td>待填</td><td>待填</td></tr></tbody></table></div></article>
        <article id="companies" class="card"><div class="section-title"><h2>四、公司分层</h2><span class="pill">股票池</span></div><div class="table-wrap"><table><thead><tr><th>公司</th><th>分层</th><th>定位</th><th>核心看点</th><th>主要风险</th></tr></thead><tbody><tr><td>待填</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td></tr></tbody></table></div></article>
        <article id="valuation" class="card"><div class="section-title"><h2>五、估值与交易</h2><span class="pill">行情快照</span></div><div class="table-wrap"><table><thead><tr><th>公司</th><th>PE</th><th>PB</th><th>市值</th><th>成交额</th><th>拥挤度/分位</th><th>结论</th></tr></thead><tbody><tr><td>待填</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td></tr></tbody></table></div></article>
        <article id="sources" class="card"><div class="section-title"><h2>六、来源与报告名称清单</h2><span class="pill">可追溯</span></div><p class="note">A 级为官方、交易所、上市公司公告和国际机构；B 级为可追溯券商研报、产业机构和咨询研究。C 类不进入主结论。</p><div class="table-wrap"><table><thead><tr><th>等级</th><th>来源/机构</th><th>报告或资料名称</th><th>时间</th><th>覆盖市场</th><th>用途</th><th>URL</th></tr></thead><tbody><tr><td>A/B</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td><td>待填</td></tr></tbody></table></div></article>
      </section>
    </section>
  </main>
</body>
</html>
""")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an industry research HTML scaffold.")
    parser.add_argument("--industry", required=True, help="Industry name in Chinese or English.")
    parser.add_argument("--slug", required=True, help="URL/file slug, e.g. robotics.")
    parser.add_argument("--output", required=True, help="Output HTML path.")
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    html = HTML_TEMPLATE.substitute(industry=args.industry, slug=args.slug, today=date.today().isoformat())
    output.write_text(html, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
