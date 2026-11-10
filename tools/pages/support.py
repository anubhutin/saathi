"""Support pages: find-support, connect, safety, languages, faqs, partners, professionals."""
from layout import esc, helplines_html, note, page_head, ul
from content_pathways import ESCALATION
from _hp_util import fin

HL = helplines_html()


def sec(inner, cls="", head=None, lede=None, sid=None):
    h = ""
    if head:
        h = f'<div class="section__head"><h2>{head}</h2>' + (f'<p class="lede">{lede}</p>' if lede else "") + "</div>"
    i = f' id="{sid}"' if sid else ""
    return f'<section class="section {cls}"{i}><div class="wrap">{h}{inner}</div></section>'


# ---------------------------------------------------------------- find-support
FEEL = [
    ("Calm or tired", ["a-quiet-evening", "difficult-days", "journaling-week"]),
    ("Worried", ["the-worry-jar", "breathing-for-hard-moments", "grounding-five-senses"]),
    ("Low, numb or overwhelmed", ["difficult-days", "understanding-feelings", "breathing-for-hard-moments"]),
    ("Angry or lonely", ["understanding-feelings", "everyday-connection", "journaling-week"]),
    ("Unsafe at home", ["recognising-coercive-control", "healthy-relationships", "staying-safe-online"]),
]
TITLES = {
    "a-quiet-evening": "A quiet evening", "difficult-days": "Getting through difficult days",
    "journaling-week": "A week of journaling", "the-worry-jar": "The worry jar",
    "breathing-for-hard-moments": "Breathing for hard moments", "grounding-five-senses": "Grounding with your five senses",
    "understanding-feelings": "Understanding feelings", "everyday-connection": "Everyday connection",
    "recognising-coercive-control": "Recognising coercive control", "healthy-relationships": "Healthy relationships",
    "staying-safe-online": "Staying safe online",
}
static_feel = "".join(
    f'<li><strong>{esc(n)}.</strong> ' + ", ".join(f'<a href="@R@resources/{r}.html">{esc(TITLES[r])}</a>' for r in rs) + "</li>"
    for n, rs in FEEL)

FIND = f"""
{page_head("Find support", "A short, optional check-in to point you towards things that may help. It is not a test, and you can skip it and go straight to the library or the helplines.", kicker="Three short questions, no sign-up")}
<section class="section"><div class="wrap" style="max-width:48rem">
  <div data-checkin data-root="@R@" class="sp-checkin">
    <div data-checkin-app hidden aria-live="polite"></div>
    <div data-checkin-static class="sp-static">
      <div class="note" role="note"><p>Here is the check-in as a simple guide.</p></div>
      <h2>First: is anyone in immediate danger?</h2>
      <p>If yes, call <a href="tel:112"><strong>112</strong></a>, stay with the person, and call Tele-MANAS on <a href="tel:14416"><strong>14416</strong></a>. Read <a href="@R@safety.html#urgent">what to do in the first minutes</a>.</p>
      <h2>If you are feeling</h2>
      <ul class="list-leaf">{static_feel}</ul>
      <h2>Unsafe at home</h2>
      <p>Call the Women Helpline on <a href="tel:181">181</a> or <a href="tel:112">112</a>. A One Stop Centre (Sakhi) offers a safe place, counselling, medical and legal help. Read the <a href="@R@safety.html#shared-phone">shared phone tips</a>.</p>
      <h2>If you are thinking of ending your life</h2>
      <p>Please call <a href="tel:14416">14416</a> or <a href="tel:112">112</a> now.</p>
      <h2>Who can you ask in India?</h2>
      <ul class="list-leaf">
        <li>For a young child: your anganwadi worker, an RBSK team or District Early Intervention Centre, and your PHC.</li>
        <li>For a school-age child or teenager: the school counsellor, an RKSK adolescent clinic, your PHC or CHC, and Childline 1098 if a child may be unsafe.</li>
        <li>For an adult woman: your PHC or CHC, your ASHA or anganwadi worker, the District Mental Health Programme, and a One Stop Centre if you face violence.</li>
        <li>For an older person: your PHC, CHC or district hospital, your ASHA worker, the District Mental Health Programme, and Elderline 14567.</li>
        <li>For anyone: Tele-MANAS, 14416, free and open 24 hours.</li>
      </ul>
      <h2>Choose by age</h2>
      <p><a href="@R@pathways.html">Browse the nine age pathways</a>, or <a href="@R@explore.html">explore the whole library</a>. To talk to a person, see <a href="@R@connect.html">how connecting will work</a>.</p>
    </div>
  </div>
  <div class="panel panel--warm" style="margin-top:2.5rem">
    <h2 style="font-size:var(--step-2)">Helplines, free to call</h2>
    {HL}
  </div>
</div></section>
"""

# ---------------------------------------------------------------- connect
STATES = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
          "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
          "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
          "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
          "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi",
          "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"]
AGE_OPTS = [("0-5", "0 to 5 years"), ("6-9", "6 to 9 years"), ("10-13", "10 to 13 years"), ("14-17", "14 to 17 years"),
            ("18-24", "18 to 24 years"), ("25-39", "25 to 39 years"), ("40-59", "40 to 59 years"),
            ("60-74", "60 to 74 years"), ("75-plus", "75 years or more")]
state_opts = "".join(f'<option value="{esc(s)}">{esc(s)}</option>' for s in STATES)
age_opts = "".join(f'<option value="{v}">{esc(t)}</option>' for v, t in AGE_OPTS)
lang_opts = "".join(f"<option>{l}</option>" for l in ["English", "Hindi", "Bengali", "Maithili", "Bhojpuri", "Other"])
chan_opts = "".join(f"<option>{c}</option>" for c in ["WhatsApp", "Phone call", "SMS", "Email"])

CONNECT = f"""
{page_head("Connect with a person", "When you are ready to talk to someone, this is how human support will work. Reaching out is always your choice, and you decide how much to share.", kicker="Human support")}
<section class="section"><div class="wrap split">
  <div>
    <h2>How it will work</h2>
    <p class="muted">Nobody is pushed through these steps. You can stop after any one of them.</p>
  </div>
  <ol class="steps">
    <li><h3>You tell us how to reach you</h3><p>Just a contact method and a language. No account or password. A name, age band, state or anything else is optional.</p></li>
    <li><h3>A trained person looks at your request</h3><p>A person, not a program, reads it and decides who is best placed to help. SAATHI does not diagnose and does not use automated scoring to decide how urgent you are.</p></li>
    <li><h3>You are matched with a verified service</h3><p>This might be a counsellor, a school or college counsellor, a District Mental Health Programme team, a One Stop Centre, or an NGO that has passed our checks. You can ask for a woman counsellor.</p></li>
    <li><h3>They contact you the way you asked</h3><p>On WhatsApp, a call, SMS or email, at the times you said are safe. If you said others use your phone, they will keep messages discreet.</p></li>
    <li><h3>You decide what happens next</h3><p>You can pause, change who you talk to, or stop at any time.</p></li>
  </ol>
</div></section>

<section class="section section--deep"><div class="wrap grid grid--2">
  <div class="card"><h3>You can stay anonymous</h3>
    <p>You never need to tell us who you are. Use any name you like: Doraemon, Chhota Bheem, Silvermist, Spider-Man, or your favourite character. No real name, no account, no password.</p>
    <p>Reading and exploring SAATHI is completely private. Nothing you read, search or choose is stored.</p>
    <p>If you ask for someone to contact you, only the counsellor who helps you sees what you chose to share, and only to reach you. SAATHI never sells your details, never shows them to advertisers, and never tells your family, school or employer.</p>
    <p>You can ask us to delete your request at any time. See <a href="@R@safety.html#privacy">privacy</a>.</p></div>
  <div class="card" id="limits"><h3>The limits of confidentiality, in plain words</h3>
    <p>Counselling is private, but nobody can honestly promise secrecy about everything. A counsellor may need to involve other people if:</p>
    {ul(["you or someone else is in serious, immediate danger, for example, you are at risk of ending your life or of being seriously hurt;",
         "a child may be being abused or harmed. Under the POCSO Act 2012, anyone who knows of sexual abuse of a person under 18 must report it, and the counsellor will tell you if they have to;",
         "a court or the law requires information to be shared."])}
    <p>If this applies, they will tell you first where it is safe to do so, and share only what is needed.</p></div>
</div></section>

<section class="section"><div class="wrap" style="max-width:48rem">
  <h2>Ask for someone to contact you</h2>
  {note("<strong>Online requests are opening district by district.</strong> If they are not open where you live yet, your request will not be sent. You can reach a trained counsellor today on Tele-MANAS, <a href=\"tel:14416\">14416</a>.", "info")}
  <form data-connect-form novalidate onsubmit="return false" autocomplete="off" aria-label="Request contact">
    <p class="muted">Two short steps. No account, no password. Only the first step is needed; everything else is up to you.</p>
    <h3 class="sp-form-step">1. How should we reach you?</h3>
    <div class="grid grid--2">
      <div class="field"><label for="sp-channel">Contact me by</label><select id="sp-channel" name="channel">{chan_opts}</select></div>
      <div class="field"><label for="sp-lang">In this language</label><select id="sp-lang" name="lang">{lang_opts}</select></div>
    </div>
    <fieldset class="field"><legend>Do other people use this phone?</legend>
      <label class="choice"><input type="radio" name="shared" value="yes" id="sp-shared-yes"> <span>Yes</span></label>
      <label class="choice"><input type="radio" name="shared" value="no" checked> <span>No</span></label></fieldset>
    <div id="sp-shared-advice" hidden>{note("Because others use this phone, we will not leave messages or say \"SAATHI\" unless you tell us it is safe. Add safe times below, and see the <a href=\"@R@safety.html#shared-phone\">shared phone tips</a>.", "caution")}</div>

    <details class="sp-more">
      <summary>Add more details (optional)</summary>
      <div class="sp-more__body">
        <div class="field"><label for="sp-name">What should we call you?</label>
          <span class="hint">Any name is fine, even a favourite character like Doraemon or Silvermist. You do not need to give your real name.</span><input type="text" id="sp-name" name="name" autocomplete="off"></div>
        <div class="field"><label for="sp-age">Age band</label>
          <select id="sp-age" name="age"><option value="">Prefer not to say</option>{age_opts}</select></div>
        <div class="grid grid--2">
          <div class="field"><label for="sp-state">State or union territory</label>
            <select id="sp-state" name="state"><option value="">Choose</option>{state_opts}</select></div>
          <div class="field"><label for="sp-district">District</label>
            <input type="text" id="sp-district" name="district" autocomplete="off"></div>
        </div>
        <fieldset class="field"><legend>Would you prefer a woman counsellor?</legend>
          <label class="choice"><input type="radio" name="woman" value="yes"> <span>Yes, I would prefer a woman</span></label>
          <label class="choice"><input type="radio" name="woman" value="none" checked> <span>No preference</span></label></fieldset>
        <div class="field"><label for="sp-times">Safe times to contact you</label>
          <span class="hint">For example, weekday afternoons while the family is out, or after 9 pm.</span><input type="text" id="sp-times" name="times"></div>
        <fieldset class="field"><legend>Is it all right to leave a message?</legend>
          <label class="choice"><input type="radio" name="msg" value="yes"> <span>Yes</span></label>
          <label class="choice"><input type="radio" name="msg" value="no" checked> <span>No, please do not leave messages</span></label></fieldset>
        <fieldset class="field"><legend>Is it all right to say "SAATHI" when calling?</legend>
          <label class="choice"><input type="radio" name="say" value="yes"> <span>Yes</span></label>
          <label class="choice"><input type="radio" name="say" value="no" checked> <span>No, please use a plain greeting</span></label></fieldset>
        <div class="field"><label for="sp-need">What support would you like?</label>
          <span class="hint">Share only what you want to. You do not need to describe anything painful.</span>
          <textarea id="sp-need" name="need" rows="4"></textarea></div>
      </div>
    </details>

    <h3 class="sp-form-step">2. Before you send</h3>
    <fieldset class="field"><legend class="visually-hidden">Before you send</legend>
      <label class="choice"><input type="checkbox" data-consent> <span>I agree to share what I typed here with the person who reads my request and the service I am matched with, so they can contact me. I understand the <a href="#limits">limits of confidentiality</a>.</span></label>
      <label class="choice" id="sp-minor-consent" hidden><input type="checkbox" data-consent> <span>I am under 18, and I understand that a trusted adult may need to be involved to keep me safe.</span></label></fieldset>
    <div class="btn-row"><button type="submit" class="btn btn--primary" data-submit disabled aria-disabled="true">Send my request</button>
      <button type="reset" class="btn btn--secondary">Clear the form</button></div>
  </form>
  <div id="sp-done" class="panel panel--sage" tabindex="-1" hidden>
    <h2 style="font-size:var(--step-2)">Talk to someone today</h2>
    <p>Online requests are not open in your area yet, so your request was not sent. Your details have been cleared from this page.</p>
    <p>If you need to talk to someone today, these services are free and real:</p>
    {HL}
    <div class="btn-row"><button type="button" class="btn btn--secondary" data-again>Start again</button></div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- safety
SAFETY = f"""
{page_head("Safety and privacy", "What to do in an emergency, how SAATHI treats your information, what the law says in plain words, and how to stay private on a shared phone.", kicker="Please read this first if you are worried")}
<section class="section" id="urgent"><div class="wrap">
  <div class="panel panel--warm">
    <h2>If someone is in danger right now</h2>
    <p class="lede">Call <a href="tel:112"><strong>112</strong></a>. It is free and works across India.</p>
    <div class="grid grid--2">
      <div><h3>If someone may end their life soon</h3>
        <ul class="list-leaf"><li>Treat it as an emergency and get urgent, in-person emergency care. Call 112 or go to the nearest hospital.</li>
        <li>Do not leave the person alone.</li>
        <li>Calmly keep away anything they could use to hurt themselves.</li>
        <li>Listen without arguing or blaming. Asking directly, "are you thinking of ending your life?", does not put the idea in their mind.</li></ul>
        <p class="small">Under the Mental Healthcare Act 2017, a person who attempts suicide should receive care, not punishment.</p></div>
      <div><h3>If there is sudden confusion, severe intoxication or a medical emergency</h3>
        <ul class="list-leaf"><li>Sudden confusion, severe drowsiness, trouble breathing or a fast decline in health needs urgent medical care.</li>
        <li>Call 112 or go to the nearest hospital. Do not wait to see if it passes.</li>
        <li>Tell the doctors about any medicines, alcohol or other substances.</li></ul></div>
    </div>
    <h3 style="margin-top:1.5rem">Helplines, free to call</h3>
    {HL}
    <p style="margin-top:1rem">For online fraud, blackmail or abuse online, call <a href="tel:1930"><strong>1930</strong></a> or report at <a href="https://cybercrime.gov.in" rel="noopener">cybercrime.gov.in</a>.</p>
  </div>
</div></section>

<section class="section section--deep" id="privacy"><div class="wrap split">
  <div><h2>Privacy</h2><p class="muted">Short and honest.</p></div>
  <div class="prose">
    <h3>This website</h3>
    <ul class="list-leaf"><li>It collects nothing personal. Your check-in answers stay on your screen and are cleared when you leave.</li>
    <li>There are no analytics, no tracking and no cookies.</li>
    <li>The only things it remembers in your browser are your choices of language and light version.</li>
    <li>Fonts load from Google Fonts, so Google can see that your device asked for them. Turn on the light version (at the bottom of any page) to avoid this.</li></ul>
    <h3>What we collect when you ask for contact, and why</h3>
    <p>Only what is needed to contact you and match you with the right service: the details in the request form, and only if you choose to send them. We would keep them for as long as needed to help you, and you could ask us to correct or delete them.</p>
    <h3>The Digital Personal Data Protection Act 2023, in plain words</h3>
    <p>This law says an organisation must tell you what personal data it collects and why, collect only what it needs, ask for your consent, keep the data safe, and let you correct or erase it. For a child, the consent of a parent or lawful guardian must be properly verified. SAATHI is built to follow it. This is a summary, not legal advice.</p>
  </div>
</div></section>

<section class="section" id="indian-law"><div class="wrap">
  <div class="section__head"><h2>Indian law, in plain words</h2><p class="lede">Four laws matter most here. This is general information, not legal advice. A lawyer, legal services authority or One Stop Centre can help with your own situation.</p></div>
  <div class="grid grid--2">
    <div class="card"><h3>POCSO Act 2012</h3><p>Protects every child under 18 from sexual abuse and exploitation. Anyone who knows or suspects a child is being sexually abused must report it to the police or Childline. This applies to teachers, doctors, counsellors and family members alike. Not reporting is itself an offence. The child's identity is protected.</p></div>
    <div class="card"><h3>Protection of Women from Domestic Violence Act 2005</h3><p>Covers physical, sexual, verbal, emotional and economic abuse by a husband or partner or his relatives, including in-laws. A woman can approach a Protection Officer, a One Stop Centre or a court for a protection order, a residence order (the right to stay in the shared home) and monetary relief. Shelter and medical help are also available. You do not need to file a police complaint first.</p></div>
    <div class="card"><h3>Mental Healthcare Act 2017</h3><p>Gives every person the right to access mental health care and treatment from government services, to be treated with dignity, and to have their information kept confidential. Section 115 says a person who attempts suicide is presumed to be under severe stress and should receive care and rehabilitation, not punishment.</p></div>
    <div class="card"><h3>Digital Personal Data Protection Act 2023</h3><p>Sets rules for how organisations handle your personal data, including your right to know, correct and erase it. Data about children needs verifiable consent from a parent or guardian. See <a href="#privacy">privacy</a> above.</p></div>
  </div>
</div></section>

<section class="section section--deep" id="children"><div class="wrap split">
  <div><h2>Keeping children safe</h2><p class="muted">For parents, teachers and anyone who works with children.</p></div>
  <div class="prose">
    <ul class="list-leaf">
    <li><strong>Listen and stay calm.</strong> Believe the child. Say it was not their fault, and thank them for telling you.</li>
    <li><strong>Do not promise to keep it a secret.</strong> You may need to involve others to keep the child safe. Say so gently: "I will only tell people who can help keep you safe."</li>
    <li><strong>Do not ask leading questions</strong> or ask the child to repeat the story. Write down in their own words what they told you, with date and time.</li>
    <li><strong>Do not confront the person alleged to have harmed the child</strong> before the child is safe.</li>
    <li><strong>Report.</strong> Call Childline <a href="tel:1098">1098</a>, or 112 if the child is in danger now. A Child Welfare Committee (CWC) or District Child Protection Unit (DCPU) can arrange care and protection. Under POCSO, reporting is a legal duty.</li>
    <li>Take the child for a medical check if there has been harm. Look for a trained, child-friendly professional.</li></ul>
  </div>
</div></section>

<section class="section" id="warning-signs"><div class="wrap">
  <div class="section__head"><h2>Warning signs</h2><p class="lede">You do not need to be sure to ask for help. These are signs that a person may need support. The ones marked urgent need a response today.</p></div>
  <div class="grid grid--2">
    {"".join(f'<div class="card"><h3>{esc(e["concern"])}' + (' <span class="tag tag--warm">Urgent</span>' if e.get("urgent") else "") + f'</h3><p>{esc(e["look_for"])}</p></div>' for e in ESCALATION)}
  </div>
  <p style="margin-top:1.5rem">If you see these signs, speak to the person with kindness and ask directly. Then see <a href="@R@find-support.html">find support</a>, or call Tele-MANAS on <a href="tel:14416">14416</a>.</p>
</div></section>

<section class="section section--deep" id="shared-phone"><div class="wrap split">
  <div><h2>If you share a phone</h2><p class="muted">In many homes one phone is used by everyone. These steps can help. None of them is perfect, so choose what feels safe.</p></div>
  <div class="prose">
    <ul class="list-leaf">
    <li><strong>Clear your browser history</strong> after visiting. On most phones: browser menu, then History, then Clear. Or use a private or incognito window from the start.</li>
    <li><strong>Lock sensitive WhatsApp chats.</strong> In WhatsApp, open the chat info and choose Lock chat. Turn off notification previews.</li>
    <li><strong>Delete call log entries</strong> after calling a helpline, if it is safe to do so. Save the number under another name.</li>
    <li><strong>Agree a code word</strong> with a trusted friend, neighbour or relative that means "please call for help".</li>
    <li>Use the phone of a trusted friend, or a phone at a clinic or One Stop Centre, if yours is checked.</li>
    <li>Be careful with new apps. If you suspect someone is watching your phone, do not remove anything suddenly, as that may alert them. Ask a trusted person or the Women Helpline on <a href="tel:181">181</a> for advice.</li></ul>
  </div>
</div></section>

<section class="section" id="quick-exit"><div class="wrap split">
  <div><h2>Quick exit</h2></div>
  <div class="prose">
    <p>Every page has a "Leave quickly" button at the bottom right. Press it, or press the Esc key twice, and your screen moves to an ordinary weather search.</p>
    <p><strong>What it cannot do:</strong> it cannot erase your browser history or the back button. After leaving, clear your history as described under <a href="#shared-phone">shared phone</a>, or use a private window.</p>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- languages
LANG_CARDS = [("English", "en", "English"), ("हिन्दी", "hi", "Hindi"), ("বাংলা", "bn", "Bengali"),
              ("मैथिली", "mai", "Maithili"), ("भोजपुरी", "bho", "Bhojpuri")]
lang_cards = "".join(
    f'<li class="card"><p style="font-family:var(--font-head);font-size:var(--step-2);margin:0" lang="{c}">{n}</p>'
    f'<p class="muted small">{e}</p><button type="button" class="btn btn--secondary btn--small" data-set-lang="{c}">Use {e}</button></li>'
    for n, c, e in LANG_CARDS)

LANGUAGES = f"""
{page_head("Languages and accessibility", "SAATHI should be usable in the language you think in, and by people with different needs. Here is where we honestly are.", kicker="Be understood")}
<section class="section"><div class="wrap">
  <h2>Choose a language</h2>
  <ul class="grid grid--3 list-plain" style="margin-top:1.25rem">{lang_cards}</ul>
  <h2 style="margin-top:3rem">Where each language stands</h2>
  <div class="table-wrap" style="margin-top:1rem"><table>
    <thead><tr><th>Language</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>English</td><td>Full interface and content.</td></tr>
      <tr><td>Hindi</td><td>Menus and buttons in Hindi. Full content coming soon.</td></tr>
      <tr><td>Bengali</td><td>Menus and buttons in Bengali. Full content coming soon.</td></tr>
      <tr><td>Maithili</td><td>Coming soon. Shows English for now.</td></tr>
      <tr><td>Bhojpuri</td><td>Coming soon. Shows English for now.</td></tr>
    </tbody></table></div>
  {note("Anything about suicide, violence, consent, abuse, child safety or health is translated by a person and checked by someone who knows the subject. Until that is done, it stays in English.", "caution")}
</div></section>

<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>Accessibility</h2></div>
  <div class="grid grid--2">
    <div class="card"><h3>Light version</h3><p>Uses no web fonts and loads faster on a slow connection or a small data plan.</p>
      <label class="lite-toggle"><input type="checkbox" data-lite-toggle> <span>Use the light version</span></label></div>
    <div class="card"><h3>Text size</h3><p>The text resizes with your browser. On most phones, change the font size in Settings, then Display. In a browser on a computer, press Ctrl and plus, or Command and plus on a Mac.</p></div>
    <div class="card"><h3>Screen readers</h3><p>Pages use headings, labelled forms and landmarks, and work with the keyboard alone. If something does not work well with your reader, tell us once there is a way to do so.</p></div>
    <div class="card"><h3>Captions and transcripts</h3><p>Every video will have captions, and every audio piece will have a written transcript, in the same language.</p></div>
    <div class="card"><h3>If reading is hard</h3><p>Many people are not confident readers, and many women have had less schooling than their brothers. We plan audio-first versions, short spoken guides that can be played on a basic smartphone, and picture-led pages. These are planned, not yet built.</p></div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- faqs
FAQ_GROUPS = [
    ("People using SAATHI", [
        ("Will my family find out?", "Not from SAATHI. Browsing SAATHI stores nothing about you. Your family could still learn that you visited if they see your browser history or look at your phone. See the <a href=\"@R@safety.html#shared-phone\">shared phone tips</a>, or use a private window."),
        ("What if my in-laws or husband check my phone?", "Use a private window, clear your history after each visit, and use the Leave quickly button if someone comes in. Lock sensitive WhatsApp chats and delete call log entries. If checking your phone is part of control in your home, read about <a href=\"@R@resources/recognising-coercive-control.html\">coercive control</a>. You can call the Women Helpline on <a href=\"tel:181\">181</a> to talk about your safety."),
        ("Is it shameful to see a counsellor?", "No. People worry about \"log kya kahenge\", and that fear is real. But asking for help is what a sensible person does with a sore tooth or a fever, and it is the same with a sore mind. A counsellor is for anyone who is carrying too much, not only for people who are \"pagal\". Many people in your own street have done it quietly and felt better for it."),
        ("Can I come here if I also go to a temple, dargah, gurudwara or church, or see a traditional healer?", "Yes. Faith and community are a real source of strength, and we respect them. Prayer, a visit to a place of worship, or a conversation with someone you trust can sit alongside other support. We encourage you to also get a medical check, because low mood, anxiety and confusion can have physical causes and can often be treated."),
        ("Do I need an account?", "No. There is no sign-up and nothing to log in to."),
        ("Do I have to give my real name?", "No. Call yourself anything you like, even Doraemon, Chhota Bheem, Silvermist or Spider-Man. We only need a way to reach you if you ask for contact."),
        ("Is it free?", "Yes. Everything on this site is free, and SAATHI never asks for payment. If a service we connect you with charges a fee, we will tell you in advance if any of them charge, and we will favour free and government services."),
        ("Is SAATHI a diagnosis?", "No. SAATHI never diagnoses. The check-in and the pathways help you understand what might be going on and where to look for help. Only a trained professional who has met you can say more."),
        ("Is this an emergency service?", "No. If someone is in immediate danger, call <a href=\"tel:112\">112</a>. For emotional support at any hour, call Tele-MANAS on <a href=\"tel:14416\">14416</a>."),
    ]),
    ("Families and caregivers", [
        ("How can I support my child without frightening them?", "Listen more than you speak, and keep ordinary routines going. Say what you notice, kindly, for example: \"You have seemed quiet lately. I am here if you want to talk.\" The <a href=\"@R@pathways.html\">age pathways</a> have guidance for each stage."),
        ("My child's exams are close and they are very stressed. What can I do?", "Board exams, NEET and JEE put huge weight on young shoulders. Ask how they are, not only how much they studied. Protect their sleep, meals and a little time to play. Read <a href=\"@R@resources/exam-pressure.html\">exam pressure</a> together."),
        ("I am caring for an elderly parent and feel exhausted. Is that normal?", "Yes, very. Caring in a joint family often falls on one person, usually a woman, with little rest. Read <a href=\"@R@resources/caregiver-wellbeing.html\">caregiver wellbeing</a>, and ask your ASHA worker or PHC about support. Elderline <a href=\"tel:14567\">14567</a> can help with the person you care for."),
        ("What should I do if I think a child is being harmed?", "Stay calm, listen, do not promise secrecy, and call Childline <a href=\"tel:1098\">1098</a>. If the child is in danger now, call <a href=\"tel:112\">112</a>. Read <a href=\"@R@safety.html#children\">keeping children safe</a>."),
    ]),
    ("Young people", [
        ("What if I am under 18?", "You are welcome here. When you ask for contact, you will be asked to agree that a trusted adult may need to be involved to keep you safe. If someone is hurting you, you can call Childline <a href=\"tel:1098\">1098</a> yourself, free, any time."),
        ("Will you tell my parents?", "A counsellor will keep your conversation private, but if you are in serious danger or someone is harming you, they may have to involve other adults. They will tell you first where possible."),
        ("My friend says things that worry me. What do I do?", "You do not have to fix it alone. Stay with your friend, listen, and tell a trusted adult such as a teacher, a school counsellor or a relative. If they might hurt themselves, call <a href=\"tel:112\">112</a> or Tele-MANAS on <a href=\"tel:14416\">14416</a> together."),
        ("Why do I feel so low before my exams, or about how I look?", "Many young people do. You are not weak. See <a href=\"@R@resources/exam-pressure.html\">exam pressure</a> and <a href=\"@R@resources/body-image.html\">body image</a>, and talk to someone you trust."),
    ]),
    ("Professionals and partners", [
        ("Who can join as a professional?", "Mental health professionals with valid registration, for example, psychologists registered with the Rehabilitation Council of India (RCI) and psychiatrists registered with the National Medical Commission (NMC) or a state medical council. See <a href=\"@R@professionals.html\">for professionals</a>."),
        ("How are partners checked?", "Every partner goes through the same steps: a registration and credential check, a review of their safeguarding policy, a check of their service area, a data-sharing agreement, and regular reviews. See <a href=\"@R@partners.html\">for partners</a>."),
        ("How do I know a partner is genuine?", "Organisations appear on SAATHI only after they have been verified. If an organisation is not listed, it has not been checked by us."),
        ("Will a computer decide how serious my situation is?", "No. A person reviews every request. There is no automated diagnosis."),
        ("Which child-protection duties apply to professionals?", "Under POCSO, anyone who learns of sexual abuse of a child must report it. Professionals working with SAATHI will be expected to follow this and local child-protection procedures."),
    ]),
    ("About SAATHI", [
        ("Is this run by the government?", "No. SAATHI is not run by, or affiliated with, any government body. We list government helplines, such as 112, Tele-MANAS and 181, because they are free and trusted."),
        ("Is this medical advice?", "No. SAATHI shares general information and points you to people who can help. Only a doctor or counsellor who meets you can give advice about your situation."),
        ("Why are some pages only in English?", "Translations on sensitive topics are done carefully by people, so they take time. See <a href=\"@R@languages.html\">languages and accessibility</a>."),
        ("What does SAATHI mean?", "Saathi (साथी) means companion, someone who walks with you."),
    ]),
]
faq_html = ""
for g, qs in FAQ_GROUPS:
    faq_html += f'<h2 style="margin-top:2.5rem">{esc(g)}</h2>' + "".join(
        f'<details class="qa"><summary>{esc(q)}</summary><div class="prose"><p>{a}</p></div></details>' for q, a in qs)

FAQS = f"""
{page_head("Questions and answers", "Honest answers to the things people ask us most, including the ones that are hard to ask out loud.", kicker="Frequently asked questions")}
<section class="section"><div class="wrap" style="max-width:50rem">{faq_html}
  <div class="panel panel--warm" style="margin-top:3rem"><h2 style="font-size:var(--step-2)">Still worried? Talk to someone now.</h2>{helplines_html(compact=True)}</div>
</div></section>
"""

# ---------------------------------------------------------------- partners
PARTNER_TYPES = [
    ("Schools", "CBSE, ICSE and state board schools, for counsellors, teachers and parent groups."),
    ("Colleges and hostels", "Student welfare cells and counsellors."),
    ("Anganwadis and ASHA networks", "Frontline workers who meet mothers and young children at home."),
    ("PHCs and CHCs", "Primary and community health centres."),
    ("District Mental Health Programme teams", "Clinics and outreach in every district."),
    ("One Stop Centres (Sakhi)", "Integrated support for women facing violence."),
    ("Child Welfare Committees and DCPUs", "Statutory bodies for children in need of care and protection."),
    ("NGOs", "Non-profits doing community mental health and protection work."),
    ("Self-help groups and panchayats", "Women's collectives and village bodies."),
    ("Resident welfare associations", "Neighbourhood groups in towns and cities."),
    ("Psychologists", "With RCI registration."),
    ("Psychiatrists", "With NMC or state medical council registration."),
]
ptypes = "".join(f'<li class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for t, d in PARTNER_TYPES)

PARTNERS = f"""
{page_head("For partners", "Wellbeing grows in communities. We hope to work with the organisations people already trust, after checking each one carefully.", kicker="Work with us")}
{sec(note("Organisations appear here only after verification. Partner listings open district by district.", "info") + f'<h3 style="margin-top:2rem">Who we hope to work with</h3><ul class="grid grid--3 list-plain" style="margin-top:1rem">{ptypes}</ul>')}
<section class="section section--deep"><div class="wrap split">
  <div><h2>What partnership involves</h2></div>
  <div class="prose">{ul(["Receiving referrals from SAATHI and replying to the person in the way they asked.",
      "Telling us honestly about your capacity, languages and service area.",
      "Following child-protection and confidentiality rules, including POCSO reporting duties.",
      "Keeping people's information safe under the Digital Personal Data Protection Act 2023.",
      "Taking part in reviews, and telling us when something goes wrong."])}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section__head"><h2>How we verify a partner</h2><p class="lede">We will not list or refer to anyone who has not completed every step.</p></div>
  <ol class="steps" style="max-width:46rem">
    <li><h3>Registration and credentials</h3><p>We check the organisation's registration, and individual credentials, for example, RCI for psychologists and NMC for psychiatrists.</p></li>
    <li><h3>Safeguarding policy</h3><p>A written policy for protecting children and vulnerable adults, with named people responsible.</p></li>
    <li><h3>Service area and eligibility</h3><p>Where you work, who you serve, in which languages, and at what cost.</p></li>
    <li><h3>Data-sharing agreement</h3><p>A written agreement on how information is shared and protected, in line with the DPDP Act 2023.</p></li>
    <li><h3>Periodic review</h3><p>Regular check-ins, and listening to feedback from the people referred.</p></li>
  </ol>
</div></section>
<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>Community activities we would like to support</h2></div>
  <div class="grid grid--2">
    <div class="card"><h3>Wellbeing melas</h3><p>Open community days with stalls, music, games and a quiet corner to talk.</p></div>
    <div class="card"><h3>School sessions</h3><p>Talks and activities for students, teachers and parents on stress, exams and safety.</p></div>
    <div class="card"><h3>Parent meetings</h3><p>Evening conversations about talking with children and teenagers.</p></div>
    <div class="card"><h3>Self-help group conversations</h3><p>Short wellbeing talks held during regular SHG meetings.</p></div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- professionals
rows = "".join(
    f'<tr><th scope="row">{esc(e["concern"])}' + (' <span class="tag tag--warm">Urgent</span>' if e.get("urgent") else "") +
    f'</th><td>{esc(e["look_for"])}</td><td>{esc(e["response"])}</td><td>{esc(e["escalation"])}</td></tr>'
    for e in ESCALATION)

PROFESSIONALS = f"""
{page_head("For professionals", "SAATHI is designed to help trained people receive requests that are made with consent, and to respond with care. It is not designed to replace their judgement.", kicker="Clinicians, counsellors and teams")}
<section class="section"><div class="wrap split">
  <div><h2>Who the workspace is for</h2></div>
  <div class="prose">{ul(["Psychologists and counsellors with valid registration.", "Psychiatrists and doctors.", "School and college counsellors.", "District Mental Health Programme, One Stop Centre and child-protection teams.", "Trained community workers supervised by a registered professional."])}
  </div>
</div></section>
<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>How a referral flows</h2></div>
  <ol class="steps" style="max-width:46rem">
    <li><h3>A person asks for support</h3><p>With their consent, through the request form.</p></li>
    <li><h3>A trained person triages the request</h3><p>A human reviews it and sets priority. Nothing is ranked or diagnosed by a program.</p></li>
    <li><h3>It is matched to a verified service</h3><p>By state, language, age band, preferences and capacity.</p></li>
    <li><h3>The professional makes contact</h3><p>Using the person's preferred channel and safe times.</p></li>
    <li><h3>Follow-up is recorded</h3><p>The outcome is logged, so nobody falls through the gaps.</p></li>
  </ol>
</div></section>
<section class="section"><div class="wrap">
  <div class="section__head"><h2>Principles</h2></div>
  <div class="grid grid--3">
    <div class="card"><h3>Human-reviewed priority</h3><p>People decide who needs help first.</p></div>
    <div class="card"><h3>No automated diagnosis</h3><p>SAATHI does not label anyone.</p></div>
    <div class="card"><h3>An audit trail</h3><p>Who saw or changed a record is logged.</p></div>
    <div class="card"><h3>Role-based access</h3><p>People see only what their role needs.</p></div>
    <div class="card"><h3>POCSO reporting duties</h3><p>Professionals must report child sexual abuse, and the platform does not override this.</p></div>
    <div class="card"><h3>Consent and dignity</h3><p>Care that respects autonomy, culture and faith.</p></div>
  </div>
</div></section>
<section class="section section--deep"><div class="wrap">
  <div class="section__head"><h2>Concerns, responses and escalation</h2><p class="lede">A guide to common concerns, what to do, and when to escalate. It supports, and does not replace, clinical judgement.</p></div>
  <div class="table-wrap"><table><thead><tr><th scope="col">Concern</th><th scope="col">What to look for</th><th scope="col">Suggested response</th><th scope="col">Escalation</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>
<section class="section"><div class="wrap split">
  <div><h2>To join</h2></div>
  <div class="prose">{ul(["Valid registration, for example, RCI for clinical and rehabilitation psychologists, or NMC or a state medical council for doctors and psychiatrists.", "Agreement to follow the safeguarding, confidentiality and data-protection rules.", "A credential check and an interview.", "Willingness to be reviewed regularly."])}
    <p>Applications open district by district. See <a href="@R@partners.html">for partners</a>.</p>
    <p><a class="btn btn--secondary" href="@R@dashboard.html">See the professional workspace</a></p>
  </div>
</div></section>
"""

PAGES = [
    {"path": "find-support.html", "title": "Find support", "active": "support", "scripts": ["assets/js/checkin.js"],
     "description": "A short, optional, non-diagnostic check-in that points you to resources and Indian services that may help.", "body": fin(FIND)},
    {"path": "connect.html", "title": "Connect with a person", "active": "connect", "scripts": ["assets/js/connect.js"],
     "description": "How human support works, who can see your information, and how to ask for someone to contact you.", "body": fin(CONNECT)},
    {"path": "safety.html", "title": "Safety and privacy", "active": None,
     "description": "Emergency help, privacy, Indian law in plain words, child safety, warning signs and tips for shared phones.", "body": fin(SAFETY)},
    {"path": "languages.html", "title": "Languages and accessibility", "active": None,
     "description": "Which languages SAATHI supports now, what is coming, and accessibility options.", "body": fin(LANGUAGES)},
    {"path": "faqs.html", "title": "Questions and answers", "active": None,
     "description": "Honest answers about privacy, family, stigma, faith, cost, age and how SAATHI works.", "body": fin(FAQS)},
    {"path": "partners.html", "title": "For partners", "active": None,
     "description": "The kinds of organisations SAATHI hopes to work with and how each will be verified.", "body": fin(PARTNERS)},
    {"path": "professionals.html", "title": "For professionals", "active": None,
     "description": "Who the SAATHI workspace is for, how referrals flow, principles and the escalation guide.", "body": fin(PROFESSIONALS)},
]
