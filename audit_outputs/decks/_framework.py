"""Slide framework HTML/CSS/JS — shared by all 3 decks."""

CSS = """
:root {
  --red:#DC0032; --ink:#1a1a1a; --bg:#0f0f10; --slide:#fff; --muted:#666;
  --border:#e5e5e5; --p0:#c00021; --p1:#d97706; --p2:#0891b2;
  --accent:#DC0032; --grey:#2e2e2f;
}
* { box-sizing: border-box; }
html, body { margin:0; padding:0; height:100%; background: var(--bg); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; color: var(--ink); overflow: hidden; }
#deck { width:100vw; height:100vh; display:flex; align-items:center; justify-content:center; }
.slide {
  display:none; width: min(1200px, 96vw); aspect-ratio: 16/9;
  background: var(--slide); border-radius: 8px; padding: 56px 72px;
  box-shadow: 0 20px 80px rgba(0,0,0,0.5);
  position: relative; overflow: hidden;
}
.slide.active { display: flex; flex-direction: column; }
.slide h1 { font-size: 44px; font-weight: 800; letter-spacing: -1px; margin: 0 0 8px; line-height: 1.05; }
.slide h2 { font-size: 32px; font-weight: 700; letter-spacing: -0.5px; margin: 0 0 24px; line-height: 1.1; color: var(--ink); }
.slide h2.bordered { padding-bottom: 12px; border-bottom: 3px solid var(--red); display: inline-block; padding-right: 32px; }
.slide h3 { font-size: 20px; font-weight: 700; margin: 0 0 12px; color: var(--ink); }
.slide p { font-size: 17px; line-height: 1.6; margin: 0.6em 0; color: #333; }
.slide ul { padding-left: 22px; }
.slide li { font-size: 17px; line-height: 1.7; margin: 4px 0; color: #333; }
.slide .eyebrow { display:inline-block; background: var(--red); color:#fff; padding:5px 14px; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; border-radius:2px; margin-bottom:18px; }
.slide .muted { color: var(--muted); font-size: 14px; }
.slide footer.bar {
  position:absolute; bottom: 18px; left: 72px; right: 72px;
  display:flex; justify-content: space-between; align-items: center;
  font-size: 12px; color: var(--muted); border-top: 1px solid var(--border);
  padding-top: 12px;
}
.slide footer.bar .left { display:flex; gap: 18px; align-items: center; }
.slide footer.bar .brand { color: var(--red); font-weight: 700; letter-spacing: 0.5px; }
/* Cover */
.slide.cover { background: linear-gradient(135deg, #1a1a1a 0%, #2e2e2f 100%); color: #fff; padding: 80px; justify-content: center; }
.slide.cover h1 { color: #fff; font-size: 64px; max-width: 900px; }
.slide.cover h2 { color: #fff; opacity: 0.7; font-size: 26px; font-weight: 400; }
.slide.cover p { color: rgba(255,255,255,0.55); font-size: 14px; }
.slide.cover footer.bar { border-color: rgba(255,255,255,0.1); color: rgba(255,255,255,0.5); }
/* Section divider */
.slide.section { background: linear-gradient(135deg, #DC0032 0%, #8b0020 100%); color:#fff; justify-content: center; padding: 80px; }
.slide.section h1 { color:#fff; font-size: 72px; line-height: 1; }
.slide.section h2 { color: rgba(255,255,255,0.7); font-size: 22px; font-weight: 400; }
.slide.section .num { font-size: 200px; font-weight: 900; opacity: 0.18; position: absolute; top: 40px; right: 80px; line-height: 1; }
.slide.section footer.bar { border-color: rgba(255,255,255,0.15); color: rgba(255,255,255,0.6); }
/* Layouts */
.layout-2col { display:grid; grid-template-columns: 1fr 1fr; gap: 40px; flex: 1; align-content: start; }
.layout-3col { display:grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; flex: 1; align-content: start; }
.layout-img-right { display:grid; grid-template-columns: 1.1fr 0.9fr; gap: 40px; flex: 1; align-items: center; }
.layout-img-right img { max-width:100%; max-height: 480px; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); border: 1px solid var(--border); }
.layout-img-full { flex:1; display:flex; align-items:center; justify-content:center; }
.layout-img-full img { max-width:100%; max-height: 100%; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); border: 1px solid var(--border); }
.card { background:#fafafa; border: 1px solid var(--border); border-radius: 8px; padding: 20px; }
.card.accent { border-left: 4px solid var(--red); }
.card h3 { color: var(--red); font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
.card p { font-size: 14px; margin: 0; }
.kpi { display:grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 20px 0; }
.kpi .item { background: #fafafa; border-radius: 8px; padding: 16px; text-align: center; }
.kpi .item .v { font-size: 32px; font-weight: 800; color: var(--red); line-height:1; }
.kpi .item .l { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 6px; }
table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 8px 0; }
th, td { padding: 8px 10px; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }
th { background: #f5f5f4; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 0.3px; color: #555; }
.badge { display:inline-block; padding: 2px 8px; border-radius:3px; font-size: 11px; font-weight:700; letter-spacing: 0.3px; }
.badge.p0 { background: #fee2e2; color: var(--p0); }
.badge.p1 { background: #fef3c7; color: var(--p1); }
.badge.p2 { background: #cffafe; color: var(--p2); }
.badge.bu { background: #f1f5f9; color: #475569; }
.tag { display: inline-block; background: #f1f5f9; color: #475569; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; margin: 2px; }
.flow { display:flex; gap: 8px; align-items: stretch; margin: 20px 0; }
.flow .step { flex: 1; background:#fafafa; border:1px solid var(--border); border-radius:6px; padding:12px; font-size: 12px; position: relative; }
.flow .step .num { background: var(--red); color: #fff; width: 22px; height: 22px; border-radius: 50%; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 6px; }
.flow .step h4 { margin: 0 0 4px; font-size: 13px; }
.flow .step p { font-size: 11px; margin: 0; color: #555; }
.arrow { display:flex; align-items: center; color: var(--red); font-weight: 700; }
/* Page indicator */
.page-indicator { position: fixed; top: 16px; right: 24px; color: rgba(255,255,255,0.5); font-size: 12px; font-family: monospace; z-index: 10; }
.nav-hint { position: fixed; bottom: 16px; left: 24px; color: rgba(255,255,255,0.35); font-size: 11px; z-index: 10; }
/* Print: each slide on its own page */
@media print {
  @page { size: A4 landscape; margin: 0; }
  html, body { overflow: visible; background: white; height: auto; }
  #deck { display: block; width: 100%; height: auto; }
  .slide { display: flex !important; flex-direction: column; page-break-after: always; box-shadow: none; border-radius: 0; aspect-ratio: auto; width: 100%; height: 100vh; min-height: 100vh; max-height: 100vh; }
  .slide.cover, .slide.section { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .page-indicator, .nav-hint { display: none; }
}
"""

JS = """
<script>
let idx = 0;
const slides = document.querySelectorAll('.slide');
const ind = document.querySelector('.page-indicator');
function show(i) {
  i = Math.max(0, Math.min(slides.length - 1, i));
  idx = i;
  slides.forEach((s, k) => s.classList.toggle('active', k === i));
  if (ind) ind.textContent = (i + 1) + ' / ' + slides.length;
  window.location.hash = '#' + (i + 1);
}
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); show(idx + 1); }
  else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(idx - 1); }
  else if (e.key === 'Home') { show(0); }
  else if (e.key === 'End') { show(slides.length - 1); }
});
document.addEventListener('click', e => {
  if (e.target.closest('a')) return;
  const r = window.innerWidth;
  if (e.clientX > r * 0.5) show(idx + 1); else show(idx - 1);
});
const h = parseInt(window.location.hash.replace('#', ''), 10);
show((h && !isNaN(h)) ? h - 1 : 0);
</script>
"""

def slide(content, klass=""):
    return f'<section class="slide {klass}">{content}</section>'

def cover(eyebrow, title, subtitle, meta, page_n=1, page_total=10):
    return slide(f"""
        <span class="eyebrow">{eyebrow}</span>
        <h1>{title}</h1>
        <h2>{subtitle}</h2>
        <div style="margin-top: auto;">
          <p>{meta}</p>
        </div>
        <footer class="bar">
          <div class="left"><span class="brand">GEOPOST</span><span>Templates Revamp Project</span></div>
          <div>{page_n} / {page_total}</div>
        </footer>
    """, klass="cover")

def section_slide(num, title, subtitle="", page_n=1, page_total=10):
    return slide(f"""
        <div class="num">{num:02d}</div>
        <h2>Partie {num:02d}</h2>
        <h1>{title}</h1>
        {f'<h2 style="font-size:22px; font-weight:400; opacity:0.7;">{subtitle}</h2>' if subtitle else ''}
        <footer class="bar">
          <div class="left"><span class="brand" style="color:#fff;">GEOPOST</span><span>Templates Revamp</span></div>
          <div>{page_n} / {page_total}</div>
        </footer>
    """, klass="section")

def content_slide(eyebrow, title, body_html, page_n, page_total, deck_name):
    return slide(f"""
        <span class="eyebrow">{eyebrow}</span>
        <h2 class="bordered">{title}</h2>
        <div style="flex:1;">{body_html}</div>
        <footer class="bar">
          <div class="left"><span class="brand">GEOPOST</span><span>{deck_name}</span></div>
          <div>{page_n} / {page_total}</div>
        </footer>
    """)

def build_deck(title, slides_html, out_path):
    body = "\n".join(slides_html)
    full = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<div class="page-indicator">1 / {len(slides_html)}</div>
<div class="nav-hint">← → · clic · Ctrl+P pour PDF</div>
<div id="deck">
{body}
</div>
{JS}
</body>
</html>
"""
    with open(out_path, "w") as f:
        f.write(full)
    return out_path
