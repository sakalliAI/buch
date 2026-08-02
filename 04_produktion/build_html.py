#!/usr/bin/env python3
"""Baut aus den Markdown-Quellen eine lesbare Web-Fassung des Buchs."""

import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "04_produktion" / "buch_lesefassung.html"

TEIL = {1: "Teil I · Das Muster", 2: "Teil I · Das Muster", 3: "Teil I · Das Muster",
        4: "Teil I · Das Muster",
        5: "Teil II · Die ehrliche Bilanz", 6: "Teil II · Die ehrliche Bilanz",
        7: "Teil II · Die ehrliche Bilanz", 8: "Teil II · Die ehrliche Bilanz",
        9: "Teil III · Vom Fürchten zum Vertrauen",
        10: "Teil III · Vom Fürchten zum Vertrauen",
        11: "Teil III · Vom Fürchten zum Vertrauen",
        12: "Teil III · Vom Fürchten zum Vertrauen"}


def inline(t):
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"\[(\d+)\]", r'<sup class="nref">\1</sup>', t)
    return t


def md2html(md):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(html.escape(lines[i])); i += 1
            out.append("<pre><code>" + "\n".join(block) + "</code></pre>")
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i]); i += 1
            i -= 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            cells = [c for c in cells if not all(re.fullmatch(r":?-{2,}:?", x or "-") for x in c)]
            if cells:
                head = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
                body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                               for r in cells[1:])
                out.append(f'<div class="tw"><table><thead><tr>{head}</tr></thead>'
                           f"<tbody>{body}</tbody></table></div>")
        elif re.match(r"^\s*[-*]\s+", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i].rstrip())); i += 1
            i -= 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
        elif ln.startswith("#### "):
            out.append(f"<h4>{inline(ln[5:])}</h4>")
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.startswith("## "):
            out.append(f"<h2>{inline(ln[3:])}</h2>")
        elif ln.startswith("# "):
            out.append(f"<h2>{inline(ln[2:])}</h2>")
        elif ln.startswith("> "):
            out.append(f"<blockquote>{inline(ln[2:])}</blockquote>")
        elif ln.strip() == "---":
            out.append("<hr>")
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
        i += 1
    return "\n".join(out)


def kapitel():
    docs = []
    for p in sorted((ROOT / "02_kapitel").glob("*.md")):
        num = int(p.name[:2])
        raw = p.read_text(encoding="utf-8")
        parts = re.split(r"^## Quellen zu .*$", raw, maxsplit=1, flags=re.M)
        body, notes = parts[0], (parts[1] if len(parts) > 1 else "")
        m = re.search(r"^#\s+(.+)$", body, re.M)
        voll = m.group(1).strip() if m else p.stem
        body = re.sub(r"^#\s+.+$", "", body, count=1, flags=re.M)

        if 1 <= num <= 12:
            eyebrow, ziffer = TEIL[num], str(num)
            titel = re.sub(r"^Kapitel\s+\d+\s*[—–-]\s*", "", voll)
        else:
            eyebrow = "Rahmen"
            ziffer = "" if num == 0 else "·"
            titel = re.sub(r"^(Einleitung|Schluss)\s*[—–-]\s*", "", voll)
            if num == 0:
                eyebrow, ziffer = "Auftakt", "0"
            else:
                eyebrow, ziffer = "Ausklang", "†"

        inner = md2html(body)
        if notes.strip():
            inner += ('<details class="notes"><summary>Quellen und Anmerkungen</summary>'
                      + md2html(notes) + "</details>")
        docs.append({"id": f"k{num:02d}", "num": ziffer, "eyebrow": eyebrow,
                     "titel": titel, "kurz": voll,
                     "woerter": len(body.split()), "html": inner})
    return docs


def beiwerk():
    quellen = [
        ("expose", "Exposé", "Verlagsunterlage", ROOT / "06_expose" / "EXPOSE.md"),
        ("kdp", "KDP-Paket", "Veröffentlichung", ROOT / "05_kdp" / "KDP_PAKET.md"),
        ("pruef", "Prüfliste", "Vor Drucklegung",
         ROOT / "03_pruefung" / "PRUEFLISTE_VOR_DRUCK.md"),
    ]
    docs = []
    for did, titel, eyebrow, pfad in quellen:
        if not pfad.exists():
            continue
        raw = pfad.read_text(encoding="utf-8")
        raw = re.sub(r"^#\s+.+$", "", raw, count=1, flags=re.M)
        docs.append({"id": did, "num": "", "eyebrow": eyebrow, "titel": titel,
                     "kurz": titel, "woerter": len(raw.split()),
                     "html": md2html(raw)})
    return docs


CSS = """
:root{
  --paper:#F2F4F1; --raise:#FBFCFA; --ink:#17211F; --ink-2:#3D4B47;
  --muted:#6A7773; --rule:#D8DED8;
  --patina:#2E6B5D; --copper:#A9673C; --copper-soft:#C89A78;
  --shadow:0 1px 2px rgba(23,33,31,.05), 0 8px 24px -12px rgba(23,33,31,.18);
}
@media (prefers-color-scheme:dark){
  :root{
    --paper:#121816; --raise:#19211E; --ink:#E7ECE8; --ink-2:#B4C0BA;
    --muted:#87958E; --rule:#2A3531;
    --patina:#5FB39D; --copper:#D2955F; --copper-soft:#8A6244;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 30px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --paper:#121816; --raise:#19211E; --ink:#E7ECE8; --ink-2:#B4C0BA;
  --muted:#87958E; --rule:#2A3531;
  --patina:#5FB39D; --copper:#D2955F; --copper-soft:#8A6244;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 30px -14px rgba(0,0,0,.7);
}
:root[data-theme="light"]{
  --paper:#F2F4F1; --raise:#FBFCFA; --ink:#17211F; --ink-2:#3D4B47;
  --muted:#6A7773; --rule:#D8DED8;
  --patina:#2E6B5D; --copper:#A9673C; --copper-soft:#C89A78;
  --shadow:0 1px 2px rgba(23,33,31,.05), 0 8px 24px -12px rgba(23,33,31,.18);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font:400 1.0625rem/1.72 Georgia,"Iowan Old Style","Times New Roman",serif;
  -webkit-font-smoothing:antialiased}
.ui{font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}

/* ---- Gerüst ---- */
.shell{display:grid;grid-template-columns:280px minmax(0,1fr);min-height:100vh}
.rail{border-right:1px solid var(--rule);background:var(--raise);
  position:sticky;top:0;height:100vh;overflow-y:auto;padding:26px 0 40px}
.brand{padding:0 22px 20px;border-bottom:1px solid var(--rule);margin-bottom:14px}
.brand .kicker{font:600 .625rem/1.4 ui-sans-serif,-apple-system,sans-serif;
  letter-spacing:.16em;text-transform:uppercase;color:var(--copper);margin:0 0 9px}
.brand h1{margin:0;font-size:1.0625rem;line-height:1.3;font-weight:700;letter-spacing:-.01em}
.brand .by{margin:8px 0 0;font-size:.8125rem;color:var(--muted)}
.grp{font:600 .625rem/1.4 ui-sans-serif,-apple-system,sans-serif;letter-spacing:.15em;
  text-transform:uppercase;color:var(--muted);padding:18px 22px 7px}
.nav a{display:flex;gap:11px;align-items:baseline;padding:7px 22px;text-decoration:none;
  color:var(--ink-2);font-size:.9375rem;line-height:1.4;border-left:2px solid transparent}
.nav a:hover{background:color-mix(in srgb,var(--patina) 8%,transparent);color:var(--ink)}
.nav a.on{border-left-color:var(--copper);color:var(--ink);font-weight:600;
  background:color-mix(in srgb,var(--copper) 9%,transparent)}
.nav a .n{font:600 .75rem/1.6 ui-sans-serif,-apple-system,sans-serif;color:var(--copper);
  min-width:1.1em;font-variant-numeric:tabular-nums}
.nav a.on .n{color:var(--copper)}

/* ---- Lesefläche ---- */
main{padding:0 0 100px}
.bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 88%,transparent);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--rule);
  display:flex;align-items:center;gap:14px;padding:11px 34px}
.bar .where{font:600 .6875rem/1 ui-sans-serif,-apple-system,sans-serif;letter-spacing:.13em;
  text-transform:uppercase;color:var(--muted);flex:1;min-width:0;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.btn{font:600 .75rem/1 ui-sans-serif,-apple-system,sans-serif;letter-spacing:.04em;
  background:none;border:1px solid var(--rule);color:var(--ink-2);border-radius:2px;
  padding:7px 11px;cursor:pointer}
.btn:hover{border-color:var(--patina);color:var(--patina)}
.btn:focus-visible,.nav a:focus-visible{outline:2px solid var(--patina);outline-offset:2px}
.prog{position:absolute;left:0;bottom:-1px;height:2px;background:var(--copper);width:0}
#menu{display:none}

article{max-width:41rem;margin:0 auto;padding:64px 34px 0}
.open{margin-bottom:44px;position:relative}
.open .eye{font:600 .6875rem/1 ui-sans-serif,-apple-system,sans-serif;letter-spacing:.15em;
  text-transform:uppercase;color:var(--patina);margin:0 0 18px}
.open h2{margin:0;font-size:2.35rem;line-height:1.12;font-weight:700;letter-spacing:-.022em;
  text-wrap:balance}
.open .big{position:absolute;right:calc(100% + 26px);top:-14px;
  font:700 5.5rem/1 Georgia,serif;color:var(--copper);opacity:.22;
  font-variant-numeric:lining-nums;user-select:none}
.meta{margin:20px 0 0;font:400 .8125rem/1 ui-sans-serif,-apple-system,sans-serif;
  color:var(--muted);border-top:1px solid var(--rule);padding-top:16px}

article p{margin:0 0 1.15em}
article h2:not(.open h2){font-size:1.3rem;line-height:1.35;font-weight:700;
  margin:2.4em 0 .7em;letter-spacing:-.012em;text-wrap:balance}
article h3{font-size:1.0625rem;margin:2em 0 .5em;font-weight:700}
article h4{font-size:.9375rem;margin:1.7em 0 .4em;font-weight:700;color:var(--ink-2)}
article strong{font-weight:700}
blockquote{margin:1.6em 0;padding:2px 0 2px 20px;border-left:2px solid var(--copper);
  color:var(--ink-2);font-style:italic}
hr{border:0;height:1px;background:var(--rule);margin:2.6em 0}
ul{margin:0 0 1.15em;padding-left:1.15em}
li{margin:.3em 0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em;
  background:color-mix(in srgb,var(--patina) 11%,transparent);padding:.12em .35em;border-radius:2px}
pre{background:var(--raise);border:1px solid var(--rule);border-radius:3px;padding:16px;
  overflow-x:auto;font-size:.84rem;line-height:1.6}
pre code{background:none;padding:0}
.nref{color:var(--copper);font-weight:600;font-size:.68em;padding-left:1px}
.tw{overflow-x:auto;margin:1.6em 0;border:1px solid var(--rule);border-radius:3px}
table{border-collapse:collapse;width:100%;font-size:.875rem;line-height:1.5}
th,td{text-align:left;padding:10px 13px;border-bottom:1px solid var(--rule);vertical-align:top}
th{font:600 .6875rem/1.3 ui-sans-serif,-apple-system,sans-serif;letter-spacing:.09em;
  text-transform:uppercase;color:var(--muted);background:var(--raise)}
tbody tr:last-child td{border-bottom:0}
.notes{margin:56px 0 0;border-top:1px solid var(--rule);padding-top:8px}
.notes summary{cursor:pointer;font:600 .6875rem/1 ui-sans-serif,-apple-system,sans-serif;
  letter-spacing:.14em;text-transform:uppercase;color:var(--patina);padding:14px 0}
.notes[open] summary{margin-bottom:10px}
.notes p{font-size:.875rem;line-height:1.6;color:var(--ink-2);margin:0 0 .8em}
.foot{max-width:41rem;margin:70px auto 0;padding:26px 34px 0;border-top:1px solid var(--rule);
  display:flex;gap:12px;justify-content:space-between}
.foot button{flex:1;text-align:left;padding:14px 16px;background:var(--raise)}
.foot button:last-child{text-align:right}
.foot .lbl{display:block;font-size:.625rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin-bottom:5px}
.foot .ttl{display:block;font-size:.875rem;color:var(--ink);font-weight:600}
.foot button[disabled]{opacity:.32;cursor:default}

@media (max-width:900px){
  .shell{grid-template-columns:1fr}
  .rail{position:fixed;z-index:40;width:280px;transform:translateX(-100%);
    transition:transform .22s ease;box-shadow:var(--shadow)}
  .rail.show{transform:none}
  #menu{display:inline-block}
  .open .big{position:static;display:block;font-size:3.2rem;margin-bottom:2px}
  article{padding:40px 22px 0}
  .bar{padding:10px 18px}
  .foot{padding:26px 22px 0}
  .open h2{font-size:1.85rem}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

JS = """
const D = window.__DOCS__;
const rail=document.getElementById('rail'), nav=document.getElementById('nav'),
      body=document.getElementById('body'), where=document.getElementById('where'),
      prog=document.getElementById('prog'), prev=document.getElementById('prev'),
      next=document.getElementById('next');
let cur=0;

function render(i){
  cur=Math.max(0,Math.min(D.length-1,i));
  const d=D[cur];
  body.innerHTML =
    '<div class="open">'+(d.num?'<div class="big">'+d.num+'</div>':'')+
    '<p class="eye">'+d.eyebrow+'</p><h2>'+d.titel+'</h2>'+
    '<p class="meta">'+d.woerter.toLocaleString('de-DE')+' Wörter</p></div>'+d.html;
  where.textContent=d.eyebrow+' — '+d.titel;
  [...nav.querySelectorAll('a')].forEach((a,n)=>a.classList.toggle('on',n===cur));
  const p=D[cur-1], n=D[cur+1];
  prev.disabled=!p; next.disabled=!n;
  prev.querySelector('.ttl').textContent=p?p.titel:'—';
  next.querySelector('.ttl').textContent=n?n.titel:'—';
  window.scrollTo({top:0,behavior:'instant'});
  rail.classList.remove('show');
  try{localStorage.setItem('buchpos',String(cur));}catch(e){}
}

nav.addEventListener('click',e=>{
  const a=e.target.closest('a'); if(!a) return;
  e.preventDefault(); render(+a.dataset.i);
});
prev.onclick=()=>render(cur-1);
next.onclick=()=>render(cur+1);
document.getElementById('menu').onclick=()=>rail.classList.toggle('show');
document.addEventListener('keydown',e=>{
  if(e.target.matches('input,textarea')) return;
  if(e.key==='ArrowLeft'&&cur>0) render(cur-1);
  if(e.key==='ArrowRight'&&cur<D.length-1) render(cur+1);
});
addEventListener('scroll',()=>{
  const h=document.documentElement.scrollHeight-innerHeight;
  prog.style.width=(h>0?(scrollY/h)*100:0)+'%';
},{passive:true});

let start=0;
try{const s=localStorage.getItem('buchpos'); if(s!==null) start=+s;}catch(e){}
render(start);
"""


def main():
    docs = kapitel() + beiwerk()
    buch = [d for d in docs if d["id"].startswith("k")]
    rest = [d for d in docs if not d["id"].startswith("k")]

    nav, idx = [], 0
    nav.append('<div class="grp">Das Buch</div><div class="nav">')
    for d in buch:
        nav.append(f'<a href="#" data-i="{idx}"><span class="n">{d["num"]}</span>'
                   f'<span>{html.escape(d["titel"])}</span></a>')
        idx += 1
    nav.append("</div>")
    if rest:
        nav.append('<div class="grp">Unterlagen</div><div class="nav">')
        for d in rest:
            nav.append(f'<a href="#" data-i="{idx}"><span class="n">·</span>'
                       f'<span>{html.escape(d["titel"])}</span></a>')
            idx += 1
        nav.append("</div>")

    gesamt = f"{sum(d['woerter'] for d in buch):,}".replace(",", ".")
    page = f"""<title>Erst kam die Angst, dann kam der Alltag</title>
<style>{CSS}</style>
<div class="shell">
  <aside class="rail ui" id="rail">
    <div class="brand">
      <p class="kicker">Manuskript · Lesefassung</p>
      <h1>Erst kam die Angst,<br>dann kam der Alltag</h1>
      <p class="by">Emre Sakalli · {gesamt} Wörter</p>
    </div>
    <div id="nav">{''.join(nav)}</div>
  </aside>
  <main>
    <div class="bar ui">
      <button class="btn" id="menu">Inhalt</button>
      <div class="where" id="where"></div>
      <div class="prog" id="prog"></div>
    </div>
    <article id="body"></article>
    <div class="foot ui">
      <button class="btn" id="prev"><span class="lbl">Zurück</span><span class="ttl"></span></button>
      <button class="btn" id="next"><span class="lbl">Weiter</span><span class="ttl"></span></button>
    </div>
  </main>
</div>
<script>window.__DOCS__={json.dumps(docs, ensure_ascii=False)};</script>
<script>{JS}</script>
"""
    OUT.write_text(page, encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    print(f"Geschrieben: {OUT}  ({kb:.0f} KB, {len(docs)} Dokumente, {gesamt} Woerter)")


if __name__ == "__main__":
    main()
