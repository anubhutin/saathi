"""Shared page layout and HTML helpers for the SAATHI static site.

Every page module in tools/pages/ exposes PAGES: a list of dicts:
    {
      "path": "explore.html"            # output path relative to repo root
      "title": "Explore",               # <title> prefix (", SAATHI" is appended)
      "description": "...",             # meta description
      "active": "explore",              # nav key to highlight (or None)
      "body": "<section>...</section>", # inner HTML of <main>; may use {root}
      "scripts": ["assets/js/x.js"],    # optional extra scripts (root-relative)
    }

Inside "body", write internal links as  href="{root}explore.html"  and
assets as  src="{root}assets/img/x.svg". {root} becomes "" or "../" etc.
Use `esc()` for any text you interpolate. Never use other {braces} in body
strings, or escape them as {{ }} (body is passed through str.format).
"""

import html

esc = html.escape

SITE = {
    "name": "SAATHI",
    # Leave empty until a real, monitored inbox exists. Pages hide contact lines when empty.
    "contact_email": "",
}

NAV = [
    ("explore", "explore.html", "nav.explore", "Explore"),
    ("pathways", "pathways.html", "nav.pathways", "Age pathways"),
    ("support", "find-support.html", "nav.support", "Find support"),
    ("connect", "connect.html", "nav.connect", "Connect"),
    ("story", "our-story.html", "nav.story", "Our story"),
]

FOOTER_COLS = [
    ("footer.use", "Use SAATHI", [
        ("explore.html", "Explore resources"),
        ("pathways.html", "Age pathways"),
        ("find-support.html", "Find support"),
        ("connect.html", "Connect with a person"),
        ("languages.html", "Languages and accessibility"),
    ]),
    ("footer.about", "About", [
        ("our-story.html", "Our story"),
        ("approach.html", "Our approach"),
        ("roadmap.html", "Roadmap"),
        ("faqs.html", "Questions and answers"),
    ]),
    ("footer.work", "Work with us", [
        ("professionals.html", "For professionals"),
        ("partners.html", "For partners"),
        ("dashboard.html", "Professional workspace"),
        ("safety.html", "Safety and privacy"),
    ]),
]

# Checked against public sources (PIB, state police and ministry pages), November 2026. Re-check before launch:
# see docs/helplines.md.
HELPLINES = [
    {"number": "112", "tel": "112", "name": "Emergency Response Support System",
     "desc": "Police, fire and ambulance. Call if someone is in immediate danger."},
    {"number": "14416", "tel": "14416", "name": "Tele-MANAS",
     "desc": "Free national mental health support, 24 hours, in many Indian languages. Also 1-800-891-4416."},
    {"number": "181", "tel": "181", "name": "Women Helpline",
     "desc": "Support and referral for women facing violence, 24 hours."},
    {"number": "1098", "tel": "1098", "name": "Childline",
     "desc": "For children in need of care and protection, or adults worried about a child."},
    {"number": "14567", "tel": "14567", "name": "Elderline",
     "desc": "National helpline for senior citizens."},
]


def helplines_html(compact=False):
    """Helpline list. compact=True gives a short strip (112 + Tele-MANAS)."""
    items = HELPLINES[:2] if compact else HELPLINES
    lis = "".join(
        f'<li class="helpline"><a class="helpline__num" href="tel:{h["tel"]}">{esc(h["number"])}</a>'
        f'<span class="helpline__text"><strong>{esc(h["name"])}</strong> {esc(h["desc"])}</span></li>'
        for h in items
    )
    return f'<ul class="helplines{" helplines--compact" if compact else ""}">{lis}</ul>'


LOGO_SVG = (
    '<svg class="logo__mark" viewBox="0 0 40 40" aria-hidden="true">'
    '<path d="M8 30c6-2 9-8 12-14s7-9 12-8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
    '<path d="M20 16c-4-1-6-4-6-8 4 0 7 3 6 8z" fill="var(--sage)"/>'
    '<path d="M24 22c3-3 7-3 10-1-2 3-6 4-10 1z" fill="var(--terracotta)"/>'
    '<circle cx="8" cy="30" r="2.6" fill="currentColor"/></svg>'
)


def _header(root, active):
    links = "".join(
        f'<li><a href="{root}{href}" data-i18n="{key}"'
        f'{" aria-current=\"page\"" if k == active else ""}>{esc(label)}</a></li>'
        for k, href, key, label in NAV
    )
    return f"""
<a class="skip-link" href="#main" data-i18n="a11y.skip">Skip to content</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="logo" href="{root}index.html" aria-label="SAATHI home">{LOGO_SVG}<span class="logo__word">saathi</span><span class="logo__hi" lang="hi">साथी</span></a>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>{links}</ul>
    </nav>
    <div class="site-header__tools">
      <label class="lang-select"><span class="visually-hidden" data-i18n="lang.label">Language</span>
        <select data-lang-select aria-label="Language">
          <option value="en">English</option>
          <option value="hi" lang="hi">हिन्दी</option>
          <option value="bn" lang="bn">বাংলা</option>
          <option value="mai" lang="mai">मैथिली</option>
          <option value="bho" lang="bho">भोजपुरी</option>
        </select>
      </label>
      <a class="btn btn--help" href="{root}safety.html#urgent" data-i18n="nav.help_now">Get help now</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle>
        <span class="nav-toggle__bars" aria-hidden="true"></span><span data-i18n="nav.menu">Menu</span>
      </button>
    </div>
  </div>
  <div class="lang-banner" data-lang-banner hidden></div>
</header>"""


EMERGENCY = [
    ("112", "All emergencies"), ("100", "Police"), ("101", "Fire"), ("108", "Ambulance"),
    ("102", "Ambulance for pregnant women and young children"), ("181", "Women Helpline"),
    ("1098", "Childline"), ("14416", "Tele-MANAS, mental health"), ("14567", "Elderline, senior citizens"),
    ("1930", "Cyber crime"),
]


def _footer(root):
    sos = "".join(f'<li><a href="tel:{n}">{n}</a><span>{esc(t)}</span></li>' for n, t in EMERGENCY)
    cols = "".join(
        f'<div class="site-footer__col"><h2 class="site-footer__h" data-i18n="{key}">{esc(h)}</h2><ul>'
        + "".join(f'<li><a href="{root}{href}">{esc(t)}</a></li>' for href, t in links)
        + "</ul></div>"
        for key, h, links in FOOTER_COLS
    )
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="site-footer__top">
      <div class="site-footer__brand">
        <a class="logo logo--footer" href="{root}index.html">{LOGO_SVG}<span class="logo__word">saathi</span></a>
        <p data-i18n="footer.tagline">A space to feel heard. A pathway to feel supported.</p>
      </div>
      {cols}
    </div>
    <div class="site-footer__urgent">
      <h2 class="site-footer__h" data-i18n="footer.emergency">Emergency numbers in India, free from any phone</h2>
      <ul class="sos">{sos}</ul>
      <p class="small" data-i18n="footer.urgent2">SAATHI is not an emergency service and does not provide diagnosis or treatment.</p>
    </div>
    <div class="site-footer__base">
      <p>© 2026 SAATHI. <span data-i18n="footer.credit">Website by</span> <a class="credit-link" href="http://safalsolutions.co.in/" target="_blank" rel="noopener">Safal Solutions</a></p>
      <label class="lite-toggle"><input type="checkbox" data-lite-toggle> <span data-i18n="footer.lite">Light version for slow connections</span></label>
    </div>
  </div>
</footer>
<a class="quick-exit" href="https://www.google.com/search?q=weather+today" data-quick-exit>
  <span data-i18n="quick_exit">Leave quickly</span><span class="quick-exit__hint" data-i18n="quick_exit.hint">or press Esc twice</span>
</a>"""


def render_page(page, depth):
    root = "../" * depth
    body = page["body"].format(root=root)
    scripts = "".join(
        f'<script src="{root}{s}" defer></script>' for s in page.get("scripts", [])
    )
    title = page["title"]
    full_title = "SAATHI: a space to feel heard" if title == "Home" else f"{title}, SAATHI"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(page.get('description', ''))}">
<meta name="theme-color" content="#1E3A2B">
<meta name="referrer" content="no-referrer">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<script>
/* Light version skips web fonts. Runs before paint. */
(function(){{try{{var l=localStorage.getItem('saathi.lite')==='1';var g=localStorage.getItem('saathi.lang')||'en';
document.documentElement.lang=g;if(l){{document.documentElement.classList.add('lite');return;}}}}catch(e){{}}
var f=document.createElement('link');f.rel='stylesheet';
f.href='https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Tiro+Bangla&family=Mukta:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@400;600&display=swap';
document.head.appendChild(f);}})();
</script>
<link rel="stylesheet" href="{root}assets/css/saathi.css">
</head>
<body data-page="{esc(page.get('active') or '')}">
{_header(root, page.get('active'))}
<main id="main" tabindex="-1">
{body}
</main>
{_footer(root)}
<script src="{root}assets/js/i18n-strings.js" defer></script>
<script src="{root}assets/js/main.js" defer></script>
{scripts}
</body>
</html>
"""


# ---------- Reusable section helpers (use these for consistency) ----------

def page_head(title, lede, kicker=None, art=None):
    """Standard inner-page heading. kicker = short context line (sentence case)."""
    k = f'<p class="page-head__kicker">{esc(kicker)}</p>' if kicker else ""
    a = f'<div class="page-head__art" aria-hidden="true">{art}</div>' if art else ""
    return f"""<section class="page-head"><div class="wrap page-head__inner">
<div class="page-head__text">{k}<h1>{esc(title)}</h1><p class="lede">{esc(lede)}</p></div>{a}
</div></section>"""


def note(text, kind="info"):
    """kind: info | caution | demo. Use 'demo' for prototype/demo-data notices."""
    return f'<div class="note note--{kind}" role="note"><p>{text}</p></div>'


def ul(items, cls="list-leaf"):
    return f'<ul class="{cls}">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"
