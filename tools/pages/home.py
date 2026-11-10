from layout import esc, helplines_html
from content_pathways import PATHWAYS
from _hp_util import fin, resource_title

HERO_ART = """<svg class="decor" viewBox="0 0 480 440" role="presentation" aria-hidden="true" focusable="false">
<circle cx="372" cy="92" r="46" fill="var(--terracotta-soft)"/>
<path d="M0 330 C70 270 150 290 220 320 S400 330 480 270 V440 H0Z" fill="var(--sage-soft)"/>
<path d="M0 380 C90 340 170 370 260 372 S420 350 480 340 V440 H0Z" fill="var(--sage)" opacity=".45"/>
<path d="M30 400 C90 392 150 410 210 400" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" opacity=".6"/>
<g fill="var(--sage)">
<path d="M70 300 C50 280 54 250 76 238 C92 258 90 284 70 300Z"/>
<path d="M70 300 C92 296 108 280 110 262 C88 262 74 278 70 300Z" fill="var(--terracotta)" opacity=".8"/>
<path d="M70 300 L74 246" stroke="var(--forest)" stroke-width="1.6" fill="none" stroke-linecap="round"/>
</g>
<g>
<path d="M414 330 C396 312 400 286 420 276 C434 294 432 318 414 330Z" fill="var(--terracotta)" opacity=".85"/>
<path d="M414 330 C434 326 448 312 450 296 C430 296 418 310 414 330Z" fill="var(--sage)"/>
<path d="M414 330 L418 282" stroke="var(--forest)" stroke-width="1.6" fill="none" stroke-linecap="round"/>
</g>
<path d="M250 200 C236 186 238 166 254 158 C264 172 264 190 250 200Z" fill="var(--sage)" opacity=".7"/>
<path d="M120 130 C106 118 108 100 122 94 C132 106 132 120 120 130Z" fill="var(--terracotta)" opacity=".5"/>
<g aria-hidden="true">
<g fill="var(--terracotta)" opacity=".55"><circle cx="60" cy="60" r="3"/><circle cx="76" cy="60" r="3"/><circle cx="92" cy="60" r="3"/><circle cx="68" cy="46" r="3"/><circle cx="84" cy="46" r="3"/><circle cx="68" cy="74" r="3"/><circle cx="84" cy="74" r="3"/><circle cx="76" cy="32" r="3"/><circle cx="76" cy="88" r="3"/></g>
<circle cx="76" cy="60" r="6" fill="none" stroke="var(--terracotta)" stroke-width="1.5" opacity=".7"/>
</g>
<g>
<path d="M300 408 L300 366 M300 384 L286 370 M300 378 L314 362" stroke="var(--forest)" stroke-width="3" fill="none" stroke-linecap="round"/>
<g fill="var(--sage)" opacity=".85"><circle cx="300" cy="346" r="20"/><circle cx="278" cy="360" r="14"/><circle cx="322" cy="358" r="15"/><circle cx="292" cy="332" r="13"/><circle cx="312" cy="334" r="12"/></g>
</g>
<g>
<rect x="356" y="372" width="58" height="34" fill="var(--paper)" stroke="var(--forest)" stroke-width="2.4"/>
<rect x="352" y="366" width="66" height="8" fill="var(--forest)"/>
<rect x="377" y="384" width="14" height="22" fill="var(--terracotta)" opacity=".85"/>
<rect x="397" y="382" width="10" height="10" fill="var(--terracotta-soft)" stroke="var(--forest)" stroke-width="1.5"/>
</g>
<path class="path-draw" d="M40 404 C120 384 205 404 190 332 S80 282 150 234 S330 252 320 172 S400 92 440 62" fill="none" stroke="var(--forest)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g class="path-stop" style="animation-delay:1.0s"><circle cx="190" cy="332" r="11" fill="var(--paper)" stroke="var(--forest)" stroke-width="3"/><circle cx="190" cy="332" r="4" fill="var(--terracotta)"/>
<text x="208" y="338" font-family="var(--font-head)" font-size="20" fill="var(--forest)">Explore</text></g>
<g class="path-stop" style="animation-delay:1.7s"><circle cx="320" cy="172" r="11" fill="var(--paper)" stroke="var(--forest)" stroke-width="3"/><circle cx="320" cy="172" r="4" fill="var(--terracotta)"/>
<text x="338" y="200" font-family="var(--font-head)" font-size="20" fill="var(--forest)">Understand</text></g>
<g class="path-stop" style="animation-delay:2.4s"><circle cx="440" cy="62" r="11" fill="var(--paper)" stroke="var(--forest)" stroke-width="3"/><circle cx="440" cy="62" r="4" fill="var(--terracotta)"/>
<text x="424" y="40" text-anchor="end" font-family="var(--font-head)" font-size="20" fill="var(--forest)">Connect</text></g>
<g class="path-stop" style="animation-delay:.6s"><circle cx="40" cy="404" r="5" fill="var(--forest)"/></g>
</svg>"""

LANGS = [
    ("English", "en", "Available now"),
    ("हिन्दी", "hi", "Menus and buttons now, full content coming soon"),
    ("বাংলা", "bn", "Menus and buttons now, full content coming soon"),
    ("मैथिली", "mai", "Coming soon"),
    ("भोजपुरी", "bho", "Coming soon"),
]

age_cards = "".join(
    f'<a class="age-card" href="@R@pathways/{p["slug"]}.html"><span class="age-card__range">{esc(p["range"])}</span>'
    f'<span class="age-card__name">{esc(p["name"])}</span><span class="age-card__for">For {esc(p["audience"].lower())}</span></a>'
    for p in PATHWAYS)

NOW = [("breathing-for-hard-moments", "A few slow breaths for when things feel too much."),
       ("grounding-five-senses", "A one-minute way to come back to the room you are in."),
       ("a-quiet-evening", "Something gentle to settle into at the end of the day.")]
now_cards = "".join(
    f'<a class="card resource-card" href="@R@resources/{rid}.html"><h3>{esc(resource_title(rid))}</h3><p>{esc(d)}</p></a>'
    for rid, d in NOW)

langs = "".join(
    f'<li class="card" style="background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.18);color:#EEF1E8">'
    f'<p style="font-family:var(--font-head);font-size:var(--step-2);margin:0 0 .25rem;color:#FBF6EC" lang="{c}">{n}</p>'
    f'<p class="small" style="margin:0">{esc(s)}</p></li>' for n, c, s in LANGS)

ICONS = {
    "leaf": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M10 38C10 20 22 10 40 9c0 18-11 29-28 29" fill="var(--sage)"/><path d="M10 38c8-9 15-15 24-21" fill="none" stroke="var(--forest)" stroke-width="2" stroke-linecap="round"/></svg>',
    "diya": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6c5 7 6 11 0 17-6-6-5-10 0-17z" fill="var(--haldi)"/><path d="M6 27h36c-2 9-9 13-18 13S8 36 6 27z" fill="var(--terracotta)"/><path d="M6 27h36" stroke="var(--forest)" stroke-width="2" stroke-linecap="round"/></svg>',
    "hands": '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="17" cy="16" r="6" fill="var(--sage)"/><circle cx="31" cy="16" r="6" fill="var(--terracotta)"/><path d="M6 40c1-9 6-14 11-14s8 3 9 6M42 40c-1-9-6-14-11-14s-8 3-9 6" fill="none" stroke="var(--forest)" stroke-width="2.2" stroke-linecap="round"/></svg>',
}

DOORS = [
    ("leaf", "I need a moment for myself",
     "Gentle audio, grounding exercises and small pauses for a busy day.",
     "explore.html?category=Stress+and+anxiety", "Find a little calm"),
    ("diya", "I want to understand how I feel",
     "Simple, judgement-free resources about emotions, stress and self-worth.",
     "explore.html?category=Emotional+wellbeing", "Explore feelings"),
    ("hands", "I think I want to talk to someone",
     "Learn about support options and decide what feels comfortable for you.",
     "find-support.html", "See support options"),
]
door_cards = "".join(
    f'<li class="card hp-door"><span class="hp-door__icon">{ICONS[i]}</span>'
    f'<h3>{esc(t)}</h3><p>{esc(d)}</p>'
    f'<a class="hp-door__link" href="@R@{href}">{esc(cta)}</a></li>'
    for i, t, d, href, cta in DOORS)

COLLECTION = [
    ("breathing-for-hard-moments", "A 2-minute breathing pause", "Activity, 2 minutes"),
    ("journaling-week", "A gentle journal prompt", "Journal, a few minutes a day"),
    ("difficult-days", "Understanding stress", "Article, 4 minutes"),
]
collection = "".join(
    f'<li><a href="@R@resources/{rid}.html">{esc(t)}</a><span class="muted small">{esc(m)}</span></li>'
    for rid, t, m in COLLECTION)

BODY = f"""
<section class="hero"><div class="wrap hero__inner">
  <div class="hero__text">
    <p class="hp-hero-kicker" data-i18n="hero.kicker">You look after everyone. This space is for you, too.</p>
    <h1><span data-i18n="hero.title1">A space to feel heard.</span> <span class="line2" data-i18n="hero.title2">A pathway to feel supported.</span></h1>
    <p class="lede" data-i18n="hero.lede">Explore at your own pace, understand what you're going through, and reach a person when you're ready. No sign-up needed to start.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="@R@explore.html" data-i18n="cta.explore">Start exploring</a>
      <a class="btn btn--secondary" href="@R@find-support.html" data-i18n="cta.support">See support options</a>
    </div>
  </div>
  <div class="hero__art">{HERO_ART}</div>
</div></section>

<section class="section hp-start" aria-labelledby="start-anywhere"><div class="wrap">
  <div class="section__head">
    <p class="page-head__kicker" data-i18n="start.kicker">Start anywhere</p>
    <h2 id="start-anywhere" data-i18n="start.title">There is no right way to arrive here.</h2>
    <p class="lede" data-i18n="start.lede">Maybe you want a quiet moment. Maybe something has been on your mind. You can explore without creating an account or telling us your story.</p>
  </div>
  <ul class="hp-doors list-plain">{door_cards}</ul>
  <div class="hp-collection">
    <h3 data-i18n="start.collection">A small collection for you</h3>
    <ul class="list-plain">{collection}</ul>
    <p class="muted" data-i18n="start.close">Take what feels useful and leave the rest. You can come back whenever you need a moment for yourself.</p>
  </div>
</div></section>

<section class="section section--deep"><div class="wrap split">
  <div>
    <h2>You don't need to be in crisis to be here</h2>
    <p class="muted">Needing help is not a weakness, and it is not "pagal". It is human.</p>
  </div>
  <div class="prose">
    <p class="lede">Many of us wait until things are unbearable before we ask for anything. SAATHI does not ask you to prove that you are struggling.</p>
    <p>In many homes, the first worry is not "what is wrong with me?" but "log kya kahenge?" What will the neighbours say, what will the relatives think, will it spoil a rishta. So we stay quiet, and carry it alone.</p>
    <p>We know the other things that get in the way. One phone shared by the whole family. Needing permission to leave the house, or no one to go with. The cost of a clinic visit and a day's wages lost. Hours of travel, because there may be no counsellor within reach outside a city.</p>
    <p>So come for a story, a few minutes of calm, an answer to a question, or a way to find help. Nobody asks for your name, a label or a form. Nothing you type here is sent or stored, and the <a href="@R@safety.html#shared-phone">shared phone tips</a> show how to keep your reading private. You stay in charge, and if you want to talk to someone, we will help you find a real person, only with your consent.</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section__head"><h2>Three steps, at your own pace</h2>
  <p class="lede">Explore freely. Understand safely. Connect when ready. You can stop at any step, or move back and forth.</p></div>
  <ol class="steps" style="max-width:46rem">
    <li><h3 data-i18n="pillar.explore">Explore</h3>
      <p data-i18n="pillar.explore.desc">Stories, audio, guided activities and practical resources for everyday wellbeing. No pressure and no account.</p>
      <a href="@R@explore.html">Browse the library</a></li>
    <li><h3 data-i18n="pillar.understand">Understand</h3>
      <p data-i18n="pillar.understand.desc">Gentle guidance to help you recognise what you are going through and what kind of support might help. We do not diagnose.</p>
      <a href="@R@pathways.html">See the age pathways</a></li>
    <li><h3 data-i18n="pillar.connect">Connect</h3>
      <p data-i18n="pillar.connect.desc">When you are ready, find a trusted person or ask for a conversation with a verified service, with your consent.</p>
      <a href="@R@connect.html">See how to reach a person</a></li>
  </ol>
</div></section>

<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>Guidance for every stage of life</h2>
  <p class="lede">From a toddler's first words to dignity in later life: nine pathways, written for the person and for the people who care for them. They are for understanding, not for diagnosis.</p></div>
  <div class="age-grid">{age_cards}</div>
  <div class="btn-row"><a class="btn btn--secondary" href="@R@pathways.html">How the pathways work</a></div>
</div></section>


<section class="section section--forest"><div class="wrap">
  <div class="section__head"><h2>In the language you think in</h2>
  <p>Wellbeing is easier to talk about in the words we use at home. SAATHI is growing into five languages, starting with English, Hindi and Bengali. Every sensitive topic is translated and checked by people who speak the language.</p></div>
  <ul class="grid grid--3 list-plain">{langs}</ul>
  <p style="margin-top:1.5rem"><a href="@R@languages.html">Languages and accessibility</a></p>
</div></section>

<section class="section"><div class="wrap">
  <div class="panel panel--warm">
    <h2 style="font-size:var(--step-2)">If you or someone near you is in danger</h2>
    {helplines_html(compact=True)}
    <p style="margin-top:1rem">SAATHI is not an emergency service. For more numbers and what to do in the first minutes, read <a href="@R@safety.html#urgent">safety and privacy</a>.</p>
  </div>
</div></section>

<section class="section section--deep"><div class="wrap grid grid--2">
  <div class="card"><h3>For partners</h3>
    <p>Schools, colleges, NGOs, health services and community groups can help SAATHI reach people and connect them to real support. Partners are verified before they are shown to anyone.</p>
    <a href="@R@partners.html">Work with us as a partner</a></div>
  <div class="card"><h3>For professionals</h3>
    <p>Psychologists, counsellors, doctors and social workers can review content and take part in referral and follow-up, with consent and clear safeguarding.</p>
    <a href="@R@professionals.html">Find out about professional involvement</a></div>
</div></section>
"""

PAGES = [{
    "path": "index.html", "title": "Home", "active": None,
    "description": "SAATHI is a space to feel heard and a pathway to feel supported: wellbeing resources, age pathways and human support for women, girls and children in India.",
    "body": fin(BODY),
}]
