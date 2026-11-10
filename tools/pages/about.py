from layout import esc, page_head, note, ul
from _hp_util import fin

STORY = page_head("Our story",
    "SAATHI means companion. We are building a quiet place where women, girls and families in India can feel heard, and find a real person when they are ready.",
    kicker="Why SAATHI exists") + """
<section class="section"><div class="wrap split">
  <div><h2>Why we are building this</h2></div>
  <div class="prose">
    <p class="lede">In India, many people carry heavy feelings alone. Not because help does not matter, but because reaching it is hard.</p>
    <p>There is stigma. Someone who is low or anxious can be called "pagal", or told to be strong and pray. There is the fear of "log kya kahenge", and the worry that a daughter's or daughter-in-law's struggles will damage the family's name or a marriage.</p>
    <p>There are family expectations: to keep going, to look after everyone first, to not make a fuss. For a girl or woman there may be restricted mobility, with no permission to go out alone, nobody free to take her, or the clinic too far away.</p>
    <p>There is the practical side. A phone shared by the whole family, where every search can be seen. The cost of a visit and a day's lost wages. Very few counsellors and psychiatrists outside the big cities. And behind it all, the fear of being judged.</p>
  </div>
</div></section>

<section class="section section--deep"><div class="wrap split">
  <div><h2>Meeting people where they are</h2></div>
  <div class="prose">
    <p>Many people already live part of their life online, and most are on WhatsApp. So SAATHI begins on a phone, in your own time, with no sign-up. It is made to work on a simple phone and a slow connection, with a light version and, over time, audio and more languages.</p>
    <p>A website cannot replace a person. It can be the first, private step: somewhere to read, listen, understand a little more, and find who to ask near you. When you want to talk, we help you reach a real person, only with your consent.</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="panel panel--sage">
    <h2 style="font-size:var(--step-2)">What "saathi" means</h2>
    <p><span lang="hi">साथी</span> (saathi) means a companion: someone who walks beside you. Not someone who fixes you, judges you, or walks ahead. That is the kind of presence we want this site to be.</p>
  </div>
  <div class="section__head" style="margin-top:3rem"><h2>Our core promise</h2></div>
  <p class="lede">A space to feel heard. A pathway to feel supported.</p>
  <p>You can explore freely, understand safely and connect when you are ready. We will always tell you plainly what SAATHI is and is not. It is not an emergency service, and it does not diagnose or treat. If someone is in immediate danger, call 112.</p>
  <div class="btn-row"><a class="btn btn--primary" href="@R@approach.html">Read our approach</a><a class="btn btn--secondary" href="@R@roadmap.html">See the roadmap</a></div>
</div></section>
"""

PRINC = [("Explore freely", "Read, listen and look around without an account, a name or a label. Nothing you read or choose here is stored."),
         ("Understand safely", "Gentle, age-appropriate guidance in plain language, reviewed by people, with cautions where they matter."),
         ("Connect when ready", "Support from a real person is always your choice. Referrals need your clear consent, and we say who sees what.")]
pr = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in PRINC)

APPROACH = page_head("Our approach",
    "How we decide what to write, show and never do. These are commitments, so that you can hold us to them.",
    kicker="How SAATHI works") + f"""
<section class="section"><div class="wrap split">
  <div><h2>Three principles</h2></div>
  <ol class="steps">{pr}</ol>
</div></section>

<section class="section section--deep"><div class="wrap grid grid--2">
  <div class="card"><h3>Not a diagnosis</h3><p>Our pathways and check-ins help you notice and understand. They never say "you have" something. Only a trained professional, after talking with you, can do that.</p></div>
  <div class="card"><h3>People stay in charge</h3><p>Content is reviewed by qualified people before it is shown. Referrals and follow-up involve verified professionals and services, with clear safeguarding. Nothing important is left to automation.</p></div>
  <div class="card"><h3>Language with care</h3><p>We avoid words like "pagal" and "mad", we do not blame, and we never use fear to get attention. Sensitive content in each language is checked by speakers of that language, and by people who know the subject.</p></div>
  <div class="card"><h3>Faith and traditional care</h3><p>For many families, prayer, a dargah or temple, a trusted elder or a traditional healer is part of how they cope. We respect that. We also encourage a medical check alongside it, when something is affecting daily life.</p></div>
</div></section>

<section class="section"><div class="wrap split">
  <div><h2>Grounded in Indian law</h2><p class="muted">In plain words. This is information, not legal advice.</p></div>
  <div class="prose">
    <p><strong>Mental Healthcare Act 2017.</strong> Every person has a right to access mental health care. Under section 115, a person who attempts suicide is presumed to be under severe stress, and should be given care and support, not punishment.</p>
    <p><strong>POCSO Act 2012.</strong> Protects children from sexual abuse. Anyone who knows or suspects that a child is being sexually abused is required to report it. Our pages explain how, and point to Childline 1098.</p>
    <p><strong>Protection of Women from Domestic Violence Act 2005.</strong> Women facing violence at home can seek protection and support, including through a Protection Officer and a One Stop Centre (Sakhi).</p>
    <p><strong>Digital Personal Data Protection Act 2023.</strong> Personal data should be handled with care and consent. For children, this means verifiable consent from a parent or guardian. We collect as little as possible, and in this prototype, none.</p>
  </div>
</div></section>

<section class="section section--forest"><div class="wrap split">
  <div><h2>What we will never do</h2></div>
  {ul(["Diagnose, label or score you.",
       "Present a service or partner as real before it has been verified.",
       "Promise absolute confidentiality. We will tell you what is shared, with whom and why.",
       "Share your details without your consent, except where the law or your immediate safety requires it, and we will say so.",
       "Use frightening statistics, invented stories or fake testimonials.",
       "Share methods of self-harm, or talk about suicide without pointing to help.",
       "Pretend to be an emergency service."], "list-leaf")}
</div></section>
<section class="section"><div class="wrap">
  {note("SAATHI cannot erase your browsing history. The quick exit button helps you leave the page fast, but on a shared phone also clear your history. See <a href='@R@safety.html#shared-phone'>safety and privacy</a>.", "info")}
</div></section>
"""

PH = [("Phase 1: product foundation", "Finalise the user research, service model, age pathways, content standards, design system and first languages."),
      ("Phase 2: functional digital experience", "Build the responsive website, content library, guided journeys, multilingual navigation, accessibility and privacy-conscious browsing."),
      ("Phase 3: human support pilot", "Verify referral partners, set up professional workflows, and build consent-based referrals, appointments, follow-ups and safeguarding procedures."),
      ("Phase 4: pilot evaluation", "Test with a small, diverse group of users and measure accessibility, usefulness, referral completion, trust and safety."),
      ("Phase 5: responsible expansion", "Add languages, locations, content partners and service networks, and improve accessibility, based on what the pilot shows.")]
steps = "".join(
    f'<li><h3>{esc(t)}{" (where we are now)" if i == 1 else ""}</h3><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(PH))
M = [("Reach", "Unique visitors, age-group reach, language use"),
     ("Engagement", "Resource completion, repeat visits, activity participation"),
     ("Accessibility", "Low-bandwidth performance, audio usage, accessibility test results"),
     ("Help-seeking", "Voluntary support requests and completed referrals"),
     ("Continuity", "Appointments attended, follow-ups completed"),
     ("Trust", "User-reported comfort, understanding and perceived safety"),
     ("Quality", "Content review completion, partner verification"),
     ("Outcomes", "Appropriate, ethically collected user-reported changes over time")]
rows = "".join(f"<tr><th scope='row'>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in M)

ROADMAP = page_head("Roadmap",
    "From a website to a trusted service across India, in five phases. We will not skip the steps that keep people safe.",
    kicker="Where we are going") + f"""
<section class="section"><div class="wrap split">
  <div><h2>Five phases</h2>
  <div class="panel panel--warm" style="margin-top:1rem"><p><strong>Where we are now: Phase 2.</strong> The website, library, age pathways and check-in are open to everyone. Human support through SAATHI is being set up with verified partners, starting with pilot districts.</p></div></div>
  <ol class="steps">{steps}</ol>
</div></section>

<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>How we will know whether SAATHI is working</h2>
  <p class="lede">Not by page views alone. We will look at whether people felt safe, understood and able to reach help.</p></div>
  <div class="table-wrap"><table>
    <thead><tr><th scope="col">Area</th><th scope="col">Example indicators</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <p style="margin-top:1rem">We will use aggregated, privacy-preserving reporting. We will not make clinical outcome claims from simple engagement data.</p>
</div></section>
"""

PAGES = [
    {"path": "our-story.html", "title": "Our story", "active": "story",
     "description": "Why SAATHI exists: barriers to mental health support in India, and a quiet place to feel heard.", "body": fin(STORY)},
    {"path": "approach.html", "title": "Our approach", "active": "story",
     "description": "Principles, safeguards and the Indian laws behind SAATHI, and what we will never do.", "body": fin(APPROACH)},
    {"path": "roadmap.html", "title": "Roadmap", "active": "story",
     "description": "SAATHI's five-phase roadmap and how we will measure whether it is working.", "body": fin(ROADMAP)},
]
