#!/usr/bin/env python3
"""Build single-file HTML audit deliverable with base64-embedded images."""
import base64
import os
import re
import markdown

ROOT = "/home/user/Geopost/audit_outputs"
MD = f"{ROOT}/AUDIT_DPD_FR_v1.md"
OUT = f"{ROOT}/AUDIT_DPD_FR_v1.html"

with open(MD) as f:
    md = f.read()

# Inline images as base64 data URIs
def inline_img(match):
    alt, src = match.group(1), match.group(2)
    path = os.path.join(ROOT, src)
    if not os.path.exists(path):
        return match.group(0)
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'![{alt}](data:image/png;base64,{data})'

md = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', inline_img, md)

# Strip leading H1 + H2 (already in the hero header)
md = re.sub(r'^#\s+AUDIT.*\n+##\s+Email POC.*\n+', '', md, count=1)

html_body = markdown.markdown(md, extensions=["tables", "fenced_code", "toc", "attr_list"])

CSS = """
:root {
  --red:#DC0032; --bg:#fafafa; --ink:#1a1a1a; --muted:#6b6b6b;
  --card:#fff; --border:#e5e5e5; --p0:#c00021; --p1:#d97706; --p2:#0891b2;
  --code-bg:#f5f5f4;
}
* { box-sizing:border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: var(--ink); background: var(--bg); margin:0; padding:0; line-height:1.6;
}
.wrap { max-width: 980px; margin: 0 auto; padding: 48px 32px 80px; }
header.hero {
  background: linear-gradient(135deg, #1a1a1a 0%, #2e2e2f 100%);
  color: white; padding: 56px 32px; margin-bottom: 0;
}
header.hero .inner { max-width: 980px; margin: 0 auto; }
header.hero .eyebrow {
  display:inline-block; background: var(--red); color:white; padding:4px 12px;
  font-size: 11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase;
  border-radius: 2px; margin-bottom: 16px;
}
header.hero h1 { font-size: 36px; margin: 0 0 8px; font-weight: 800; letter-spacing:-0.5px; color: #fff; }
header.hero p.sub { color:#bbb; margin: 4px 0; font-size: 14px; }
h1, h2, h3, h4 { color: var(--ink); margin-top: 2.4em; margin-bottom: 0.6em; font-weight: 700; letter-spacing:-0.2px; }
h2 {
  font-size: 26px; padding-bottom: 8px; border-bottom: 3px solid var(--red);
  display: inline-block; padding-right: 24px;
}
h3 { font-size: 19px; color: #2e2e2f; }
h4 { font-size: 16px; }
p { margin: 0.8em 0; }
a { color: var(--red); text-decoration: none; border-bottom: 1px solid rgba(220,0,50,0.3); }
a:hover { border-color: var(--red); }
img {
  max-width:100%; height:auto; display:block; margin: 20px auto; border-radius:6px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08); border: 1px solid var(--border);
}
table {
  width: 100%; border-collapse: collapse; margin: 20px 0; background: var(--card);
  font-size: 13px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); border-radius: 6px; overflow: hidden;
}
th, td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }
th { background: #f5f5f4; font-weight: 700; color: #44403c; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
tr:last-child td { border-bottom: none; }
tr:hover { background: #fafafa; }
code {
  background: var(--code-bg); padding: 2px 6px; border-radius: 3px;
  font-family: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, monospace;
  font-size: 0.88em; color: #b91c1c;
}
pre {
  background: #1a1a1a; color: #e5e5e5; padding: 20px; border-radius: 8px;
  overflow-x: auto; font-size: 12.5px; line-height: 1.55;
}
pre code { background: transparent; color: inherit; padding: 0; }
blockquote {
  border-left: 4px solid var(--red); padding: 8px 20px; color: var(--muted);
  background: #fff; margin: 16px 0; font-size: 14px;
}
ul, ol { padding-left: 1.4em; }
li { margin: 0.4em 0; }
hr { border: 0; border-top: 1px solid var(--border); margin: 48px 0; }
/* Severity badges in tables */
td:nth-child(n) { font-size: 13px; }
/* Highlight P0/P1/P2 in any cell */
td { position: relative; }
strong { color: #1a1a1a; }
/* TOC */
.toc { background: white; padding: 20px 28px; border-radius: 8px; border: 1px solid var(--border); margin: 24px 0 40px; }
.toc ul { list-style: none; padding-left: 0; }
.toc ul ul { padding-left: 1.4em; }
.toc li { margin: 4px 0; font-size: 14px; }
.toc a { border: none; }
.toc a:hover { color: var(--red); }
/* Print */
@media print {
  body { background: white; }
  .wrap { max-width: none; padding: 0; }
  header.hero { padding: 24px; }
  img { page-break-inside: avoid; }
  h2 { page-break-after: avoid; }
  pre { white-space: pre-wrap; }
}
.badge-p0, .badge-p1, .badge-p2 {
  display:inline-block; padding: 2px 8px; border-radius:3px; font-size: 11px; font-weight:700;
  letter-spacing: 0.5px;
}
.badge-p0 { background: #fee2e2; color: var(--p0); }
.badge-p1 { background: #fef3c7; color: var(--p1); }
.badge-p2 { background: #cffafe; color: var(--p2); }
.meta { color: var(--muted); font-size: 13px; }
"""

# Severity highlight in tables (post-process)
def highlight_sev(html):
    html = re.sub(r'>\s*P0\s*<', '><span class="badge-p0">P0</span><', html)
    html = re.sub(r'>\s*P1\s*<', '><span class="badge-p1">P1</span><', html)
    html = re.sub(r'>\s*P2\s*<', '><span class="badge-p2">P2</span><', html)
    return html

html_body = highlight_sev(html_body)

FULL = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Audit Email CRM — Geopost / DPD France</title>
<style>{CSS}</style>
</head>
<body>
<header class="hero">
  <div class="inner">
    <span class="eyebrow">Audit CRM · Geopost</span>
    <h1>DPD France — Enquête satisfaction</h1>
    <p class="sub">Email POC #1 · Templates Revamp Project</p>
    <p class="sub">11 mai 2026 · Geopost Lead CRM V1 + Audit Agent V1</p>
  </div>
</header>
<div class="wrap">
{html_body}
</div>
</body>
</html>
"""

with open(OUT, "w") as f:
    f.write(FULL)

size_kb = os.path.getsize(OUT) // 1024
print(f"OK {OUT} ({size_kb} KB)")
