/* SAATHI professional workspace (sample cases). State lives in memory only. */
(function () {
  'use strict';

  var TODAY = new Date(2026, 10, 10); // 10/11/2026
  var STATUSES = ['New', 'Under review', 'Contacted', 'Appointment set', 'Referred on', 'Follow-up due', 'Closed'];
  var PRIORITIES = ['Not yet reviewed', 'Routine', 'Soon', 'Urgent'];
  var LANGS = { mai: 'Maithili', bho: 'Bhojpuri', hi: 'Hindi', bn: 'Bengali', en: 'English' };
  var PURPOSES = ['Contact you about this request', 'Share your request with a named professional', 'Keep a case record'];
  var CONSENT_V = 'v1.0';

  function seed() {
    function c(id, d, age, state, dist, lang, ch, sum, pr, who, st, extra) {
      var o = {
        id: id, received: d, age: age, state: state, district: dist, lang: lang, channel: ch, summary: sum,
        priority: pr, assigned: who, status: st, notes: [], pocso: false,
        consent: { version: CONSENT_V, at: d + ' 10:15 IST', purposes: PURPOSES.slice(0, 2 + (id.length % 2)) },
        timeline: [{ at: d, text: 'Request received by ' + ch }], followUp: null
      };
      for (var k in extra) o[k] = extra[k];
      return o;
    }
    return {
      cases: [
        c('SA-2026-0141', '09/11/2026', '14-17', 'Bihar', 'Darbhanga', 'mai', 'WhatsApp', 'Feels very anxious before board exams and cannot sleep.', 'Not yet reviewed', 'Unassigned', 'New', {}),
        c('SA-2026-0140', '09/11/2026', '25-39', 'Bihar', 'Madhubani', 'mai', 'WhatsApp', 'Low mood after the baby was born; family says it will pass.', 'Not yet reviewed', 'Unassigned', 'New', {}),
        c('SA-2026-0138', '08/11/2026', '18-24', 'Bihar', 'Patna', 'hi', 'Web form', 'Hostel student feeling very alone, wants someone to talk to.', 'Routine', 'Counsellor A (Hindi, Maithili)', 'Under review', {}),
        c('SA-2026-0135', '07/11/2026', '25-39', 'Uttar Pradesh', 'Varanasi', 'bho', 'WhatsApp', 'Pressure from in-laws; asks about safe options at home.', 'Urgent', 'Social worker B (Bhojpuri, Hindi)', 'Contacted', {}),
        c('SA-2026-0133', '06/11/2026', '10-13', 'West Bengal', 'Kolkata', 'bn', 'Phone call', 'Parent worried about a child who has stopped going to school.', 'Soon', 'Counsellor C (Bengali, English)', 'Appointment set', { under18: true }),
        c('SA-2026-0131', '05/11/2026', '14-17', 'West Bengal', 'Murshidabad', 'bn', 'WhatsApp', 'Teenager describes being touched by an adult relative.', 'Urgent', 'Counsellor C (Bengali, English)', 'Under review', {}),
        c('SA-2026-0127', '04/11/2026', '40-59', 'Uttar Pradesh', 'Gorakhpur', 'hi', 'WhatsApp', 'Constant tiredness and worry; looking after an ill parent.', 'Routine', 'Counsellor A (Hindi, Maithili)', 'Follow-up due', { followUp: { due: '10/11/2026', done: false, outcome: '' } }),
        c('SA-2026-0122', '02/11/2026', '18-24', 'Jharkhand', 'Ranchi', 'hi', 'Web form', 'Coaching-centre stress; wants coping ideas and a referral.', 'Routine', 'Counsellor D (Hindi, English)', 'Referred on', {}),
        c('SA-2026-0118', '31/10/2026', '60-74', 'Delhi', 'South Delhi', 'en', 'Web form', 'Feeling lonely since moving in with a son and his family.', 'Routine', 'Social worker E (English, Hindi)', 'Follow-up due', { followUp: { due: '12/11/2026', done: false, outcome: '' } }),
        c('SA-2026-0112', '29/10/2026', '14-17', 'Bihar', 'Patna', 'hi', 'WhatsApp', 'Being pressured online by someone she does not know.', 'Soon', 'Counsellor A (Hindi, Maithili)', 'Appointment set', {}),
        c('SA-2026-0104', '24/10/2026', '25-39', 'Delhi', 'North Delhi', 'hi', 'WhatsApp', 'Wants to talk about stress at work and at home.', 'Routine', 'Counsellor D (Hindi, English)', 'Closed', { followUp: { due: '03/11/2026', done: true, outcome: 'Felt better supported; has the Tele-MANAS number.' } }),
        c('SA-2026-0099', '20/10/2026', '6-9', 'Jharkhand', 'Ranchi', 'hi', 'Phone call', 'Teacher noticed a child is very quiet and not eating at school.', 'Soon', 'Counsellor D (Hindi, English)', 'Contacted', { under18: true })
      ],
      appts: [
        { when: '11/11/2026 11:00', who: 'SA-2026-0133', with: 'Counsellor C (Bengali, English)', mode: 'Video call' },
        { when: '13/11/2026 16:30', who: 'SA-2026-0112', with: 'Counsellor A (Hindi, Maithili)', mode: 'Phone call' },
        { when: '19/11/2026 10:00', who: 'SA-2026-0135', with: 'Social worker B (Bhojpuri, Hindi)', mode: 'In person' }
      ],
      audit: []
    };
  }

  var S;
  var tabs, panels, selected = null, filters = { q: '', status: '', priority: '', state: '' };

  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    for (var k in (attrs || {})) {
      if (k === 'text') e.textContent = attrs[k];
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] === true) e.setAttribute(k, '');
      else if (attrs[k] !== false && attrs[k] != null) e.setAttribute(k, attrs[k]);
    }
    (kids || []).forEach(function (n) { if (n != null) e.appendChild(typeof n === 'string' ? document.createTextNode(n) : n); });
    return e;
  }
  function field(label, control, id) {
    control.id = id;
    return h('div', { 'class': 'field' }, [h('label', { 'for': id, text: label }), control]);
  }
  function opt(sel, list, val) {
    list.forEach(function (o) { var x = h('option', { value: o, text: o }); if (o === val) x.selected = true; sel.appendChild(x); });
    return sel;
  }
  function parseD(s) { var p = s.split('/'); return new Date(+p[2], +p[1] - 1, +p[0]); }
  function days(a, b) { return Math.round((a - b) / 864e5); }
  function now() { return '10/11/2026 ' + new Date().toTimeString().slice(0, 5) + ' IST'; }
  function say(t) { var l = document.getElementById('db-live'); if (l) l.textContent = t; }
  function log(action, id) {
    S.audit.unshift({ at: now(), who: 'You', action: action, id: id || '' });
  }
  function byId(id) { return S.cases.filter(function (c) { return c.id === id; })[0]; }
  function empty(el) { while (el.firstChild) el.removeChild(el.firstChild); }

  function counts() {
    var n = { fresh: 0, review: 0, appts: 0, due: 0, pocso: 0 };
    S.cases.forEach(function (c) {
      if (c.status === 'New') n.fresh++;
      if (c.status === 'New' || c.status === 'Under review' || c.priority === 'Not yet reviewed') n.review++;
      if (c.pocso) n.pocso++;
      if (c.followUp && !c.followUp.done && days(parseD(c.followUp.due), TODAY) <= 7) n.due++;
    });
    S.appts.forEach(function (a) {
      var d = days(parseD(a.when.split(' ')[0]), TODAY);
      if (d >= 0 && d < 7) n.appts++;
    });
    return n;
  }

  /* ---------- Panels ---------- */
  function renderOverview(p) {
    var n = counts();
    var items = [
      ['New requests', n.fresh, 'Not yet opened by anyone'],
      ['Awaiting review', n.review, 'New, under review, or no priority set'],
      ['Appointments this week', n.appts, 'In the next 7 days'],
      ['Follow-ups due', n.due, 'Due within 7 days or overdue'],
      ['POCSO reports flagged', n.pocso, 'Marked by a reviewer in this session']
    ];
    var g = h('div', { 'class': 'db-stats' });
    items.forEach(function (i) {
      g.appendChild(h('div', { 'class': 'db-stat' }, [h('p', { 'class': 'db-stat__num', text: String(i[1]) }), h('h3', { text: i[0] }), h('p', { 'class': 'db-muted', text: i[2] })]));
    });
    p.appendChild(g);
    p.appendChild(h('p', { 'class': 'db-muted', text: 'Counts are worked out from the cases below. They describe workload only. They say nothing about how anyone is doing.' }));
  }

  function renderQueue(p) {
    if (selected) return renderDetail(p);
    var f = h('form', { 'class': 'db-filters', role: 'search', 'aria-label': 'Filter referrals', onsubmit: function (e) { e.preventDefault(); } });
    var q = h('input', { type: 'search', value: filters.q, oninput: function (e) { filters.q = e.target.value; redrawBody(); } });
    var st = opt(h('select', { onchange: function (e) { filters.status = e.target.value; redrawBody(); } }), [''].concat(STATUSES), filters.status);
    st.firstChild.textContent = 'All statuses';
    var pr = opt(h('select', { onchange: function (e) { filters.priority = e.target.value; redrawBody(); } }), [''].concat(PRIORITIES), filters.priority);
    pr.firstChild.textContent = 'All priorities';
    var states = []; S.cases.forEach(function (c) { if (states.indexOf(c.state) < 0) states.push(c.state); });
    var sx = opt(h('select', { onchange: function (e) { filters.state = e.target.value; redrawBody(); } }), [''].concat(states.sort()), filters.state);
    sx.firstChild.textContent = 'All states';
    f.appendChild(field('Search case ID or request', q, 'db-f-q'));
    f.appendChild(field('Status', st, 'db-f-status'));
    f.appendChild(field('Priority', pr, 'db-f-priority'));
    f.appendChild(field('State', sx, 'db-f-state'));
    p.appendChild(f);
    p.appendChild(h('p', { 'class': 'db-muted', text: 'Priority is set by a reviewer. SAATHI never assigns it automatically.' }));
    p.appendChild(h('div', { id: 'db-queue-body' }));
    redrawBody();
  }

  function redrawBody() {
    var box = document.getElementById('db-queue-body'); if (!box) return;
    empty(box);
    var q = filters.q.toLowerCase();
    var rows = S.cases.filter(function (c) {
      return (!filters.status || c.status === filters.status) && (!filters.priority || c.priority === filters.priority) &&
        (!filters.state || c.state === filters.state) && (!q || (c.id + ' ' + c.summary).toLowerCase().indexOf(q) >= 0);
    });
    if (!rows.length) { box.appendChild(h('p', { 'class': 'db-empty', text: 'No referrals match these filters.' })); return; }
    var head = ['Case ID', 'Received', 'Age band', 'Place', 'Language', 'Channel', 'Request (summary)', 'Priority', 'Assigned to', 'Status'];
    var tr = h('tr', {}, head.map(function (t) { return h('th', { scope: 'col', text: t }); }));
    var tb = h('tbody');
    rows.forEach(function (c) {
      var open = h('button', { type: 'button', 'class': 'db-link', text: c.id, 'aria-label': 'Open case ' + c.id, onclick: function () { selected = c.id; render('queue'); focusPanel('queue'); } });
      var pr = opt(h('select', { 'aria-label': 'Priority for ' + c.id, onchange: function (e) {
        log('Priority set to "' + e.target.value + '" (was "' + c.priority + '")', c.id); c.priority = e.target.value; say('Priority updated for ' + c.id + '.');
      } }), PRIORITIES, c.priority);
      var ss = opt(h('select', { 'aria-label': 'Status for ' + c.id, onchange: function (e) {
        log('Status changed to "' + e.target.value + '" (was "' + c.status + '")', c.id); c.timeline.push({ at: '10/11/2026', text: 'Status: ' + e.target.value }); c.status = e.target.value; say('Status updated for ' + c.id + '.');
      } }), STATUSES, c.status);
      tb.appendChild(h('tr', {}, [
        h('td', {}, [open]), h('td', { text: c.received }), h('td', { text: c.age }),
        h('td', { text: c.district + ', ' + c.state }), h('td', { text: LANGS[c.lang] }), h('td', { text: c.channel }),
        h('td', { text: c.summary }), h('td', {}, [pr]), h('td', { text: c.assigned }), h('td', {}, [ss])
      ]));
    });
    box.appendChild(h('div', { 'class': 'table-wrap' }, [h('table', {}, [
      h('caption', { 'class': 'visually-hidden', text: 'Referral queue, ' + rows.length + ' records' }), h('thead', {}, [tr]), tb])]));
    box.appendChild(h('p', { 'class': 'db-muted', text: 'Showing ' + rows.length + ' of ' + S.cases.length + ' referrals. Dates are DD/MM/YYYY, IST.' }));
  }

  function renderDetail(p) {
    var c = byId(selected);
    p.appendChild(h('button', { type: 'button', 'class': 'btn btn--secondary btn--small', text: 'Back to the queue', onclick: function () { selected = null; render('queue'); focusPanel('queue'); } }));
    p.appendChild(h('h2', { 'class': 'db-h', text: 'Case ' + c.id }));
    p.appendChild(h('p', { text: c.summary }));
    p.appendChild(h('p', { 'class': 'db-muted', text: c.age + ' years, ' + c.district + ', ' + c.state + '. ' + LANGS[c.lang] + ', via ' + c.channel + '. Status: ' + c.status + '. Priority: ' + c.priority + '.' }));
    var tl = h('ol', { 'class': 'db-timeline' });
    c.timeline.forEach(function (t) { tl.appendChild(h('li', {}, [h('strong', { text: t.at }), ' ' + t.text])); });
    var cons = h('ul', { 'class': 'list-leaf' }, [
      h('li', { text: 'Consent version: ' + c.consent.version }),
      h('li', { text: 'Recorded: ' + c.consent.at }),
      h('li', { text: 'Purposes agreed: ' + c.consent.purposes.join('; ') })
    ]);
    var notes = h('ul', { 'class': 'db-notes' });
    function drawNotes() {
      empty(notes);
      if (!c.notes.length) notes.appendChild(h('li', { 'class': 'db-muted', text: 'No notes yet.' }));
      c.notes.forEach(function (n) { notes.appendChild(h('li', { text: n })); });
    }
    drawNotes();
    var ta = h('textarea', { rows: '3' });
    var nf = h('form', { onsubmit: function (e) {
      e.preventDefault(); var v = ta.value.trim(); if (!v) return;
      c.notes.push('10/11/2026: ' + v); log('Note added', c.id); ta.value = ''; drawNotes(); say('Note added.');
    } }, [field('Add a note (kept in memory only; do not type real details)', ta, 'db-note'), h('button', { 'class': 'btn btn--primary btn--small', type: 'submit', text: 'Add note' })]);
    p.appendChild(h('div', { 'class': 'grid grid--2' }, [
      h('div', { 'class': 'card' }, [h('h3', { text: 'Timeline' }), tl]),
      h('div', { 'class': 'card' }, [h('h3', { text: 'Consent record' }), cons])
    ]));
    p.appendChild(h('div', { 'class': 'card db-gap' }, [h('h3', { text: 'Notes' }), notes, nf]));
    if (c.under18) {
      var box = h('div', { 'class': 'card db-gap' }, [h('h3', { text: 'Child protection' })]);
      var msg = h('p', { 'class': 'db-muted', text: 'Under 18. If a child may have been sexually abused, the POCSO Act 2012 requires it to be reported to the police or the Special Juvenile Police Unit. Your organisation\'s safeguarding lead decides how, using the escalation matrix.' });
      box.appendChild(msg);
      var btn = h('button', { type: 'button', 'class': 'btn btn--warm btn--small', 'aria-pressed': c.pocso ? 'true' : 'false', text: c.pocso ? 'Marked as mandatory report (POCSO)' : 'Mark as mandatory report (POCSO)', onclick: function () {
        if (c.pocso) return; c.pocso = true; c.priority = c.priority; log('Marked as mandatory report (POCSO). Safeguarding lead to be notified.', c.id);
        c.timeline.push({ at: '10/11/2026', text: 'Marked as mandatory report (POCSO)' }); say('Case marked as a mandatory report. An audit entry was added.'); render('queue');
      } });
      if (c.pocso) btn.disabled = true;
      box.appendChild(btn); p.appendChild(box);
    } else {
      p.appendChild(h('p', { 'class': 'db-muted db-gap', text: 'The mandatory report option appears for cases involving someone under 18.' }));
    }
  }

  function renderAppts(p) {
    p.appendChild(h('h2', { 'class': 'db-h', text: 'Appointments' }));
    var list = h('ul', { 'class': 'db-list' });
    S.appts.forEach(function (a) { list.appendChild(h('li', {}, [h('strong', { text: a.when }), ' with ' + a.with + ', ' + a.mode.toLowerCase() + ', case ' + a.who])); });
    p.appendChild(list);
    var date = h('input', { type: 'text', placeholder: 'DD/MM/YYYY', inputmode: 'numeric' });
    var time = h('input', { type: 'text', placeholder: 'HH:MM' });
    var cs = opt(h('select'), S.cases.map(function (c) { return c.id; }));
    var who = opt(h('select'), ['Counsellor A (Hindi, Maithili)', 'Social worker B (Bhojpuri, Hindi)', 'Counsellor C (Bengali, English)', 'Counsellor D (Hindi, English)']);
    var mode = opt(h('select'), ['Phone call', 'Video call', 'In person']);
    var err = h('p', { 'class': 'db-error', role: 'alert' });
    var form = h('form', { 'class': 'card db-gap', onsubmit: function (e) {
      e.preventDefault(); err.textContent = '';
      if (!/^\d{2}\/\d{2}\/\d{4}$/.test(date.value) || !/^\d{2}:\d{2}$/.test(time.value)) { err.textContent = 'Enter the date as DD/MM/YYYY and the time as HH:MM.'; return; }
      S.appts.push({ when: date.value + ' ' + time.value, who: cs.value, with: who.value, mode: mode.value });
      log('Appointment added for ' + date.value + ' ' + time.value, cs.value); say('Appointment added.'); render('appointments');
    } }, [h('h3', { text: 'Add an appointment' }),
      field('Date', date, 'db-a-date'), field('Time (IST)', time, 'db-a-time'), field('Case', cs, 'db-a-case'),
      field('Professional', who, 'db-a-who'), field('How', mode, 'db-a-mode'), err,
      h('button', { 'class': 'btn btn--primary', type: 'submit', text: 'Add appointment' })]);
    p.appendChild(form);
  }

  function renderFollow(p) {
    p.appendChild(h('h2', { 'class': 'db-h', text: 'Follow-ups' }));
    var due = S.cases.filter(function (c) { return c.followUp; });
    if (!due.length) { p.appendChild(h('p', { 'class': 'db-empty', text: 'No follow-ups are due.' })); return; }
    var ul = h('ul', { 'class': 'db-list' });
    due.forEach(function (c) {
      var li = h('li', {}, [h('strong', { text: c.id }), ' due ' + c.followUp.due + ', ' + c.assigned + '. ']);
      if (c.followUp.done) { li.appendChild(h('span', { text: 'Done. Outcome: ' + c.followUp.outcome })); }
      else {
        var out = h('input', { type: 'text' });
        var f = h('form', { 'class': 'db-inline', onsubmit: function (e) {
          e.preventDefault(); if (!out.value.trim()) { out.focus(); return; }
          c.followUp.done = true; c.followUp.outcome = out.value.trim(); if (c.status === 'Follow-up due') c.status = 'Closed';
          log('Follow-up marked done', c.id); say('Follow-up marked done.'); render('followups');
        } }, [field('Outcome (a few words, no personal details)', out, 'db-o-' + c.id), h('button', { 'class': 'btn btn--primary btn--small', type: 'submit', text: 'Mark done' })]);
        li.appendChild(f);
      }
      ul.appendChild(li);
    });
    p.appendChild(ul);
  }

  function renderDirectory(p) {
    p.appendChild(h('h2', { 'class': 'db-h', text: 'Service directory' }));
    p.appendChild(h('div', { 'class': 'db-empty' }, [h('strong', { text: 'No verified services yet' }), h('p', { text: 'SAATHI will not list a service until a person has checked it. Nothing here is a real listing.' })]));
    p.appendChild(h('h3', { text: 'How a service would be verified' }));
    var crit = ['A named person confirms the service exists, at this place, and is open to the people we refer.',
      'Staff qualifications and registration are checked where they apply, for example an RCI-registered psychologist.',
      'The service agrees to a written referral and consent process, and to child safeguarding including POCSO reporting.',
      'The service is free or its fees are stated clearly in rupees.',
      'Languages, accessibility and opening hours are confirmed directly, not copied from a website.',
      'Every listing shows when it was last checked and is re-checked at least every six months.'];
    p.appendChild(h('ul', { 'class': 'list-leaf' }, crit.map(function (t) { return h('li', { text: t }); })));
    p.appendChild(h('h3', { text: 'Types of partner we expect to verify' }));
    var types = ['District Mental Health Programme (DMHP) teams', 'One Stop Centres (Sakhi) for women facing violence', 'Child Welfare Committees and District Child Protection Units (DCPU)',
      'Primary and community health centres (PHC and CHC)', 'School counsellors', 'RCI-registered clinical and rehabilitation psychologists', 'Non-governmental organisations (NGOs) with safeguarding policies'];
    p.appendChild(h('ul', { 'class': 'list-leaf' }, types.map(function (t) { return h('li', { text: t }); })));
  }

  function tally(key, label) {
    var m = {}; S.cases.forEach(function (c) { var k = label ? label(c) : c[key]; m[k] = (m[k] || 0) + 1; });
    return Object.keys(m).sort(function (a, b) { return m[b] - m[a]; }).map(function (k) { return [k, m[k]]; });
  }
  function bars(title, rows) {
    var max = Math.max.apply(null, rows.map(function (r) { return r[1]; }));
    var ul = h('ul', { 'class': 'db-bars' });
    rows.forEach(function (r) {
      var fill = h('span', { 'class': 'db-bar__fill' }); fill.style.width = Math.round(r[1] / max * 100) + '%';
      ul.appendChild(h('li', { 'class': 'db-bar' }, [h('span', { 'class': 'db-bar__label', text: r[0] }), h('span', { 'class': 'db-bar__track', 'aria-hidden': 'true' }, [fill]), h('span', { 'class': 'db-bar__val', text: r[1] + (r[1] === 1 ? ' case' : ' cases') })]));
    });
    return h('div', { 'class': 'card' }, [h('h3', { text: title }), ul]);
  }
  function renderReports(p) {
    p.appendChild(h('h2', { 'class': 'db-h', text: 'Reports' }));
    p.appendChild(h('p', { 'class': 'db-muted', text: 'Counts of referrals only. These numbers describe who contacted the service. They do not measure outcomes or anyone\'s wellbeing.' }));
    p.appendChild(h('div', { 'class': 'grid grid--3' }, [
      bars('By age band', tally('age')), bars('By language', tally('lang', function (c) { return LANGS[c.lang]; })), bars('By state', tally('state'))]));
    p.appendChild(h('div', { 'class': 'db-gap' }, [bars('By channel', tally('channel'))]));
  }

  function renderAudit(p) {
    p.appendChild(h('h2', { 'class': 'db-h', text: 'Audit log' }));
    p.appendChild(h('p', { 'class': 'db-muted', text: 'Every action is recorded here: who did what, and when. Records for real cases are kept permanently.' }));
    if (!S.audit.length) { p.appendChild(h('p', { 'class': 'db-empty', text: 'No actions yet in this session.' })); return; }
    var tb = h('tbody');
    S.audit.forEach(function (a) { tb.appendChild(h('tr', {}, [h('td', { text: a.at }), h('td', { text: a.who }), h('td', { text: a.id }), h('td', { text: a.action })])); });
    p.appendChild(h('div', { 'class': 'table-wrap' }, [h('table', {}, [h('thead', {}, [h('tr', {}, ['When', 'Who', 'Case', 'Action'].map(function (t) { return h('th', { scope: 'col', text: t }); }))]), tb])]));
  }

  var RENDER = { overview: renderOverview, queue: renderQueue, appointments: renderAppts, followups: renderFollow, directory: renderDirectory, reports: renderReports, audit: renderAudit };

  function render(key) {
    var p = document.getElementById('db-panel-' + key);
    empty(p); RENDER[key](p);
  }
  function focusPanel(key) { var p = document.getElementById('db-panel-' + key); if (p) p.focus(); }

  function show(i, focus) {
    tabs.forEach(function (t, j) {
      var on = i === j;
      t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; panels[j].hidden = !on;
    });
    render(tabs[i].id.replace('db-tab-', ''));
    if (focus) tabs[i].focus();
  }

  function init() {
    var list = document.querySelector('.db-tabs'); if (!list) return;
    S = seed(); selected = null;
    tabs = [].slice.call(list.querySelectorAll('[role=tab]'));
    panels = [].slice.call(document.querySelectorAll('.db-panel'));
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { show(i); });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = (i + 1) % tabs.length;
        else if (e.key === 'ArrowLeft') n = (i - 1 + tabs.length) % tabs.length;
        else if (e.key === 'Home') n = 0; else if (e.key === 'End') n = tabs.length - 1;
        if (n !== null) { e.preventDefault(); show(n, true); }
      });
    });
    document.getElementById('db-reset').addEventListener('click', function () {
      S = seed(); selected = null; filters = { q: '', status: '', priority: '', state: '' };
      var cur = tabs.map(function (t) { return t.getAttribute('aria-selected'); }).indexOf('true');
      show(cur); say('Sample cases reset.');
    });
    show(0);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
