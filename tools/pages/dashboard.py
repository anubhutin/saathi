from layout import esc, page_head, note

TABS = [
    ("overview", "Overview"),
    ("queue", "Referral queue"),
    ("appointments", "Appointments"),
    ("followups", "Follow-ups"),
    ("directory", "Directory"),
    ("reports", "Reports"),
    ("audit", "Audit log"),
]

_tabs = "".join(
    f'<button class="db-tab" role="tab" id="db-tab-{k}" aria-controls="db-panel-{k}" '
    f'aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}" type="button">{esc(label)}</button>'
    for i, (k, label) in enumerate(TABS)
)
_panels = "".join(
    f'<div class="db-panel" role="tabpanel" id="db-panel-{k}" aria-labelledby="db-tab-{k}" tabindex="0"{"" if i == 0 else " hidden"}></div>'
    for i, (k, label) in enumerate(TABS)
)

DEMO = note(
    "<strong>You are viewing sample cases.</strong> Every case here is fictional, so you can see how "
    "the workspace works. Real cases appear only after a verified professional signs in, and they "
    "are stored securely in India with every action recorded.",
    "info",
)

DASHBOARD_BODY = (
    page_head(
        "Professional workspace",
        "How counsellors, social workers and case coordinators manage referrals, "
        "appointments and follow-ups, with people making every decision.",
        kicker="For professionals",
    )
    + f"""
<section class="section"><div class="wrap">
{DEMO}
<div class="db-toolbar">
  <p class="db-toolbar__text">Sample cases, dated <strong>10/11/2026</strong> (IST). Changes stay in this browser tab.</p>
  <button type="button" class="btn btn--secondary btn--small" id="db-reset">Reset sample cases</button>
</div>
<div class="db-tabs" role="tablist" aria-label="Workspace sections">{_tabs}</div>
{_panels}
<p class="db-live" id="db-live" role="status" aria-live="polite"></p>
<noscript><p class="note note--caution">The workspace needs JavaScript to run.</p></noscript>
</div></section>
"""
)

NOT_FOUND_BODY = (
    page_head(
        "We could not find that page",
        "The link may be old or mistyped. Nothing is wrong with you or your device. Here are a few places to start.",
        kicker="Page not found",
    )
    + """
<section class="section"><div class="wrap">
<div class="grid grid--3">
  <div class="card"><h2>Go to the home page</h2><p>Start again from the beginning.</p>
  <div class="btn-row"><a class="btn btn--primary" href="{root}index.html">Open the home page</a></div></div>
  <div class="card"><h2>Explore resources</h2><p>Browse gentle guides and activities by age and topic.</p>
  <div class="btn-row"><a class="btn btn--secondary" href="{root}explore.html">Explore resources</a></div></div>
  <div class="card"><h2>Safety and help</h2><p>If you are worried about your safety, or someone else's, look here first.</p>
  <div class="btn-row"><a class="btn btn--secondary" href="{root}safety.html">Read about safety</a></div></div>
</div>
</div></section>
"""
)

PAGES = [
    {
        "path": "dashboard.html",
        "title": "Professional workspace",
        "description": "The referral and case workspace for counsellors, social workers and case coordinators.",
        "active": None,
        "body": DASHBOARD_BODY,
        "scripts": ["assets/js/dashboard.js"],
    },
    {
        "path": "404.html",
        "title": "Page not found",
        "description": "This page could not be found.",
        "active": None,
        "body": NOT_FOUND_BODY,
    },
]
