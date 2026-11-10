from layout import esc, helplines_html, page_head, note, ul
from content_pathways import PATHWAYS
from _hp_util import fin, resource_title

WHO = {
    "child_small": [
        "Your anganwadi worker, who can see how a young child is growing and playing, and knows what the village or ward offers.",
        "Your ASHA, who can visit the home and help you reach the nearest health centre.",
        "A paediatrician, or the doctor at your PHC or CHC, for a developmental check.",
        "RBSK (Rashtriya Bal Swasthya Karyakram) and the District Early Intervention Centre at the district hospital, which screen young children and offer therapy. Ask for the nearest one.",
    ],
    "child": [
        "A school counsellor or a teacher you trust. Many schools have one person children can talk to.",
        "A Rashtriya Kishor Swasthya Karyakram (RKSK) adolescent clinic, also called an Adolescent Friendly Health Clinic, at a health centre or district hospital.",
        "Your family doctor or the doctor at the PHC, CHC or district hospital.",
        "Childline 1098, free, for any child who is unsafe or any adult worried about a child. The District Child Protection Unit and Child Welfare Committee act on cases of abuse.",
    ],
    "young": [
        "The campus counselling cell, or a warden, mentor or faculty member you trust, if you are in college or a hostel.",
        "Tele-MANAS on 14416, free and confidential, in many Indian languages, if you cannot go out or do not want to be overheard at home.",
        "The doctor at the PHC, CHC or district hospital, or a trusted family doctor.",
        "A friend, an older cousin or a sibling. One person who knows is often enough to begin.",
    ],
    "adult": [
        "Your nearest PHC or CHC, or the district hospital. Ask for the doctor, and for the mental health clinic if there is one.",
        "The District Mental Health Programme (DMHP), which runs mental health clinics at district level and sometimes in outreach camps.",
        "For violence at home or at work: the One Stop Centre (Sakhi) in your district, and Women Helpline 181. A Protection Officer under the Domestic Violence Act can help you apply for protection and a safe place.",
        "Tele-MANAS on 14416, free, if you cannot travel or need to talk first.",
        "Your ASHA or anganwadi worker, and women's groups such as the self-help group (SHG) in your area, for company and a first conversation.",
    ],
    "elder": [
        "The geriatric clinic at the district hospital, where doctors look at body and mind together.",
        "Elderline 14567, the national helpline for senior citizens.",
        "The doctor at your PHC or CHC, and your ASHA, who can arrange home visits where available.",
        "Tele-MANAS on 14416 for someone to talk to, in your own language.",
        "A temple, mosque, church, gurdwara or senior citizens' group in your area. Company matters too.",
    ],
}
WHO_FOR = {"0-5": "child_small", "6-9": "child", "10-13": "child", "14-17": "child", "18-24": "young",
           "25-39": "adult", "40-59": "adult", "60-74": "elder", "75-plus": "elder"}

age_cards = "".join(
    f'<a class="age-card" href="@R@pathways/{p["slug"]}.html"><span class="age-card__range">{esc(p["range"])}</span>'
    f'<span class="age-card__name">{esc(p["name"])}</span><span class="age-card__for">For {esc(p["audience"].lower())}</span></a>'
    for p in PATHWAYS)

INDEX = page_head("Age pathways",
    "Nine pathways, from early childhood to later life. Each one explains what a person might be going through, what shapes it in India, what can help and who to ask near you.",
    kicker="Understand") + f"""
<section class="section"><div class="wrap">
  {note("The pathways are for understanding, not for diagnosis. Only a trained professional, after talking with the person, can say what is happening. Every person and every family is different.", "caution")}
  <div class="section__head" style="margin-top:2rem"><h2>Choose an age group</h2>
  <p class="lede">Pick the age of the person you are thinking about, whether that is you, your child, your parent or a student you teach.</p></div>
  <div class="age-grid">{age_cards}</div>
</div></section>
<section class="section section--deep"><div class="wrap split">
  <div><h2>How each pathway is organised</h2>
  <p class="muted">The same order every time, so you always know where to look.</p></div>
  <ol class="steps">
    <li><h3>What someone might experience</h3><p>The common difficulties at this stage of life, in plain words.</p></li>
    <li><h3>Signs you might notice</h3><p>Things that show up in daily life. There is a card you can print and keep, or share with a family member.</p></li>
    <li><h3>What shapes this in India</h3><p>Family, school, money, distance, stigma and other realities that make things harder or easier.</p></li>
    <li><h3>What can help</h3><p>Kinds of support, from everyday care to professional help.</p></li>
    <li><h3>Important to know</h3><p>Cautions, so that a sign is never mistaken for a diagnosis.</p></li>
    <li><h3>If you're a parent, teacher or family member</h3><p>Practical things you can do and say.</p></li>
    <li><h3>Who to ask near you</h3><p>Real services in India, such as anganwadi workers, school counsellors, district hospitals and helplines.</p></li>
  </ol>
</div></section>
<section class="section"><div class="wrap"><div class="panel panel--sage">
  <h2 style="font-size:var(--step-2)">Not sure where to start?</h2>
  <p>You do not have to pick the right pathway. <a href="@R@explore.html">Browse the library</a> by feeling or topic, or <a href="@R@find-support.html">see who can help near you</a>.</p>
</div></div></section>
"""

PAGES = [{"path": "pathways.html", "title": "Age pathways", "active": "pathways",
          "description": "Nine age pathways from early childhood to later life: what people may experience, signs to notice, what shapes it in India, what helps and who to ask.",
          "body": fin(INDEX)}]


def pathway_body(i, p):
    prev = PATHWAYS[i - 1] if i > 0 else None
    nxt = PATHWAYS[i + 1] if i < len(PATHWAYS) - 1 else None
    signs = "".join(f"<li>{esc(s)}</li>" for s in p["signs"])
    cards = "".join(
        f'<a class="card resource-card" href="@R@resources/{r}.html"><h3>{esc(resource_title(r))}</h3></a>'
        for r in p["resources"])
    pn = ""
    pn += (f'<a href="@R@pathways/{prev["slug"]}.html">Previous: {esc(prev["range"])}, {esc(prev["name"])}</a>' if prev else "<span></span>")
    pn += (f'<a href="@R@pathways/{nxt["slug"]}.html">Next: {esc(nxt["range"])}, {esc(nxt["name"])}</a>' if nxt else "<span></span>")
    caution = " ".join(esc(c) for c in p["considerations"])
    return page_head(p["name"], p["intro"], kicker=p["range"]) + f"""
<section class="section" style="padding-bottom:0"><div class="wrap"><p class="small"><strong>Written for:</strong> {esc(p["audience"])}. <a href="@R@pathways.html">All age pathways</a></p></div></section>

<section class="section"><div class="wrap split">
  <div><h2>What someone might experience</h2>
  <p class="muted">These are common, not certain. Many people go through some of them and are fine.</p></div>
  {ul(p["experiences"])}
</div></section>

<section class="section"><div class="wrap">
  <div class="signs-board">
    <h2>Signs you might notice</h2>
    <p class="muted">A card to keep or share. These are signs to notice and talk about, not a diagnosis. {esc(p["name"])}, {esc(p["range"])}.</p>
    <ul class="signs">{signs}</ul>
    <p class="muted" style="margin-top:1.25rem">If several of these are present, or they are getting worse, speak to a doctor, counsellor or one of the services below. If someone may be in danger, call 112.</p>
    <div class="btn-row no-print"><button class="btn btn--secondary" type="button" data-print>Print this card</button></div>
  </div>
</div></section>

<section class="section section--deep"><div class="wrap split">
  <div><h2>What shapes this in India</h2>
  <p class="muted">Not everything is about the person. Their surroundings matter a great deal.</p></div>
  {ul(p["context"])}
</div></section>

<section class="section"><div class="wrap split">
  <div><h2>What can help</h2></div>
  {ul(p["support"])}
</div></section>

<section class="section"><div class="wrap">
  <h2 style="font-size:var(--step-2)">Important to know</h2>
  {note(caution, "caution")}
  <p style="margin-top:1rem">SAATHI cannot diagnose. Faith, prayer and traditional healers are part of many families' lives, and can sit alongside care. If something is affecting daily life, please also see a doctor or counsellor.</p>
</div></section>

<section class="section section--deep"><div class="wrap split">
  <div><h2>If you're a parent, teacher or family member</h2></div>
  {ul(p["trusted"])}
</div></section>

<section class="section"><div class="wrap">
  <div class="section__head"><h2>Who to ask near you</h2>
  <p class="lede">You do not have to work this out alone. These are real services in India. Availability varies by district, so a call or a visit is the best way to check.</p></div>
  {ul(WHO[WHO_FOR[p["slug"]]])}
  <div class="panel panel--warm" style="margin-top:2rem"><h3>Helplines, free in India</h3>{helplines_html()}</div>
  <div class="btn-row">
    <a class="btn btn--primary" href="@R@connect.html">Connect with a person</a>
    <a class="btn btn--secondary" href="@R@find-support.html">Find support near you</a>
  </div>
</div></section>

<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>Read and listen</h2></div>
  <div class="grid grid--3">{cards}</div>
  <div class="btn-row"><a class="btn btn--secondary" href="@R@explore.html?age={p["slug"]}">See everything for this age</a></div>
  <nav class="pathway-nav" aria-label="Other age pathways">{pn}</nav>
</div></section>
"""

for i, p in enumerate(PATHWAYS):
    PAGES.append({"path": f"pathways/{p['slug']}.html", "title": f"{p['name']}, {p['range']}",
                  "active": "pathways",
                  "description": f"{p['name']} ({p['range']}): what to notice, what shapes it in India, what can help and who to ask.",
                  "body": fin(pathway_body(i, p)), "scripts": ["assets/js/pathway.js"]})
