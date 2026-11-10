"""Explore page and resource pages."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from layout import page_head, note, esc
from content_resources import RESOURCES, by_id
from content_pathways import PATHWAYS

ROOT_TOKEN = "@@ROOT@@"
CATEGORIES = ["Emotional wellbeing", "Stress and anxiety", "Self-worth", "Relationships",
              "Consent and safety", "Women's wellbeing", "Parenting", "Child wellbeing",
              "Violence and abuse", "Ageing and caregiving"]
FORMATS = ["Article", "Activity", "Audio", "Story", "Journal", "Guide"]
PATH_BY_SLUG = {p["slug"]: p for p in PATHWAYS}


def _finish(html_):
    """Escape braces for str.format, then restore {root}."""
    return html_.replace("{", "{{").replace("}", "}}").replace(ROOT_TOKEN, "{root}")


def _blocks(body):
    out = []
    for kind, val in body:
        if kind == "p":
            out.append(f"<p>{esc(val)}</p>")
        elif kind == "h":
            out.append(f"<h2>{esc(val)}</h2>")
        elif kind in ("ul", "ol"):
            cls = ' class="list-leaf"' if kind == "ul" else ""
            out.append(f"<{kind}{cls}>" + "".join(f"<li>{esc(i)}</li>" for i in val) + f"</{kind}>")
        elif kind == "tip":
            out.append(f'<div class="note note--info" role="note"><p>{esc(val)}</p></div>')
    return "\n".join(out)


def _opt(values, label_fn=lambda v: v):
    return "".join(f'<option value="{esc(v)}">{esc(label_fn(v))}</option>' for v in values)


def _card(r):
    ages = " ".join(r["ages"])
    search = " ".join([r["title"], r["summary"], r["category"], r["format"], r["for_whom"]]).lower()
    return (f'<li><a class="card resource-card" href="{ROOT_TOKEN}resources/{r["id"]}.html" '
            f'data-category="{esc(r["category"])}" data-format="{esc(r["format"])}" '
            f'data-ages="{ages}" data-search="{esc(search)}">'
            f'<span class="resource-card__format">{esc(r["format"])}, {r["minutes"]} min</span>'
            f'<h3>{esc(r["title"])}</h3><p>{esc(r["summary"])}</p>'
            f'<span class="tag tag--plain">{esc(r["category"])}</span></a></li>')


def explore_page():
    cards = "".join(_card(r) for r in RESOURCES)
    age_opts = "".join(f'<option value="{p["slug"]}">{esc(p["range"])} ({esc(p["name"].lower())})</option>' for p in PATHWAYS)
    body = page_head("Explore", "Short, gentle resources you can read, try or share. Search, or narrow by topic, kind and age.",
                     kicker="Resource library") + f"""
<section class="section"><div class="wrap">
<div class="panel panel--sage rl-calm"><div>
<h2>A minute of calm</h2>
<p>If things feel like too much right now, start with one minute of slow breathing.</p></div>
<a class="btn btn--primary" href="{ROOT_TOKEN}resources/breathing-for-hard-moments.html">Start a breathing exercise</a></div>
<form class="filters rl-filters" role="search" aria-label="Find resources" data-explore-form>
<div class="field"><label for="rl-q">Search resources</label>
<input type="search" id="rl-q" name="q" autocomplete="off" placeholder="For example: exam, sleep, baby"></div>
<div class="rl-selects">
<div class="field"><label for="rl-cat">Topic</label><select id="rl-cat" name="category"><option value="">All topics</option>{_opt(CATEGORIES)}</select></div>
<div class="field"><label for="rl-fmt">Kind</label><select id="rl-fmt" name="format"><option value="">All kinds</option>{_opt(FORMATS)}</select></div>
<div class="field"><label for="rl-age">Age</label><select id="rl-age" name="age"><option value="">All ages</option>{age_opts}</select></div>
</div>
<p><button type="button" class="btn btn--secondary btn--small" data-explore-reset>Clear filters</button></p>
</form>
<p class="rl-count" data-explore-count role="status" aria-live="polite">Showing all {len(RESOURCES)} resources</p>
<ul class="grid grid--3 list-plain rl-grid" data-explore-grid>{cards}</ul>
<div class="empty-state" data-explore-empty hidden><h2>No resources match yet</h2>
<p>Try fewer words, or clear the filters. If you need to talk to someone, see <a href="{ROOT_TOKEN}find-support.html">Find support</a>.</p></div>
{note("These resources share general information and ideas for self-care. They are not a substitute for care from a doctor or counsellor.", "caution")}
</div></section>"""
    return {"path": "explore.html", "title": "Explore resources",
            "description": "Short, gentle wellbeing resources for children, young people, women and families in India.",
            "active": "explore", "body": _finish(body), "scripts": ["assets/js/explore.js"]}


PACER = f"""<div class="rl-pacer" data-breath-pacer>
<div class="rl-pacer__stage"><div class="rl-pacer__circle" data-pacer-circle aria-hidden="true"></div></div>
<p class="rl-pacer__cue" data-pacer-cue role="status" aria-live="polite">Press start when you are ready.</p>
<button type="button" class="btn btn--primary" data-pacer-toggle aria-pressed="false">Start breathing</button>
<p class="small muted">Breathe in as the circle grows (4 seconds), pause (2), then breathe out slowly as it shrinks (6). Stop whenever you like.</p>
</div>"""


def resource_page(r):
    tags = (f'<span class="tag">{esc(r["format"])}</span> <span class="tag tag--plain">{r["minutes"]} minutes</span> '
            f'<span class="tag tag--plain">{esc(r["category"])}</span> <span class="tag tag--plain">English</span> '
            '')
    audio = ""
    if r["format"] == "Audio":
        audio = note("The audio version is coming soon. You can read the full transcript below.", "demo")
    pacer = PACER if r["id"] == "breathing-for-hard-moments" else ""
    related = [x for x in RESOURCES if x["category"] == r["category"] and x["id"] != r["id"]][:3]
    if len(related) < 3:
        related += [x for x in RESOURCES if x["id"] != r["id"] and x not in related and set(x["ages"]) & set(r["ages"])][:3 - len(related)]
    rel = "".join(f'<li><a class="card resource-card" href="{ROOT_TOKEN}resources/{x["id"]}.html"><span class="resource-card__format">{esc(x["format"])}, {x["minutes"]} min</span><h3>{esc(x["title"])}</h3><p>{esc(x["summary"])}</p></a></li>' for x in related)
    slugs = [p["slug"] for p in PATHWAYS if r["id"] in p["resources"]]
    for s in r["ages"]:
        if s not in slugs and len(slugs) < 3:
            slugs.append(s)
    paths = "".join(f'<li><a href="{ROOT_TOKEN}pathways/{s}.html">Age pathway: {esc(PATH_BY_SLUG[s]["range"])}, {esc(PATH_BY_SLUG[s]["name"].lower())}</a></li>' for s in slugs if s in PATH_BY_SLUG)
    body = page_head(r["title"], r["summary"], kicker=r["category"]) + f"""
<section class="section"><div class="wrap rl-article">
<p class="rl-tags">{tags}</p>
<p><strong>Who it is for:</strong> {esc(r["for_whom"])}</p>
<p class="muted"><strong>Format:</strong> {esc(r["access"])}</p>
{audio}{pacer}
<div class="prose rl-body">{_blocks(r["body"])}</div>
{note("This is general information. It is not a substitute for care from a doctor or counsellor. If someone is in immediate danger, call 112.", "caution")}
<h2>Related resources</h2><ul class="grid grid--3 list-plain">{rel}</ul>
<h2>Find this in an age pathway</h2><ul class="list-leaf">{paths}</ul>
<p><a class="btn btn--secondary" href="{ROOT_TOKEN}explore.html">Back to Explore</a></p>
</div></section>"""
    return {"path": f"resources/{r['id']}.html", "title": r["title"], "description": r["summary"],
            "active": "explore", "body": _finish(body),
            "scripts": ["assets/js/explore.js"] if pacer else []}


PAGES = [explore_page()] + [resource_page(r) for r in RESOURCES]
