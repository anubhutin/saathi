/* SAATHI guided check-in. Nothing is saved or sent: all answers live in memory on this page only. */
(function () {
  "use strict";
  var root = document.querySelector("[data-checkin]");
  if (!root) return;
  var staticGuide = root.querySelector("[data-checkin-static]");
  var app = root.querySelector("[data-checkin-app]");
  if (!app) return;
  if (staticGuide) staticGuide.hidden = true;
  app.hidden = false;

  var R = root.getAttribute("data-root") || "";
  function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

  var FEELINGS = [
    ["calm", "Calm"], ["tired", "Tired"], ["worried", "Worried"], ["low", "Low"],
    ["overwhelmed", "Overwhelmed"], ["angry", "Angry"], ["lonely", "Lonely"], ["numb", "Numb"],
    ["unsafe", "Unsafe at home"], ["unsure", "Not sure"]
  ];
  var WHO = [
    ["me", "Me"], ["child", "My child"], ["student", "A young person I teach"],
    ["elder", "An older family member"], ["other", "Someone else"]
  ];
  var AGES = [
    ["0-5", "0 to 5 years"], ["6-9", "6 to 9 years"], ["10-13", "10 to 13 years"], ["14-17", "14 to 17 years"],
    ["18-24", "18 to 24 years"], ["25-39", "25 to 39 years"], ["40-59", "40 to 59 years"],
    ["60-74", "60 to 74 years"], ["75-plus", "75 years or more"], ["", "Not sure or prefer not to say"]
  ];
  var COMFORT = [
    ["read", "Read something"], ["calm", "Try a calming activity"],
    ["understand", "Understand what might be going on"], ["talk", "Talk to a person"]
  ];
  var RES_TITLES = {
    "breathing-for-hard-moments": "Breathing for hard moments", "grounding-five-senses": "Grounding with your five senses",
    "understanding-feelings": "Understanding feelings", "difficult-days": "Getting through difficult days",
    "exam-pressure": "Exam pressure", "body-image": "Body image", "healthy-relationships": "Healthy relationships",
    "what-consent-means": "What consent means", "staying-safe-online": "Staying safe online",
    "recognising-coercive-control": "Recognising coercive control", "periods-and-mood": "Periods and mood",
    "after-the-baby": "After the baby", "everyday-connection": "Everyday connection",
    "body-safety-conversations": "Body safety conversations", "menopause-changes": "Menopause and changes",
    "caring-for-a-parent": "Caring for a parent", "caregiver-wellbeing": "Caregiver wellbeing",
    "loneliness-later-life": "Loneliness in later life", "journaling-week": "A week of journaling",
    "the-worry-jar": "The worry jar", "a-quiet-evening": "A quiet evening"
  };
  var BY_FEELING = {
    calm: ["a-quiet-evening", "journaling-week", "everyday-connection"],
    tired: ["difficult-days", "breathing-for-hard-moments", "a-quiet-evening"],
    worried: ["the-worry-jar", "breathing-for-hard-moments", "grounding-five-senses"],
    low: ["difficult-days", "understanding-feelings", "everyday-connection"],
    overwhelmed: ["breathing-for-hard-moments", "grounding-five-senses", "difficult-days"],
    angry: ["understanding-feelings", "breathing-for-hard-moments", "journaling-week"],
    lonely: ["everyday-connection", "journaling-week", "understanding-feelings"],
    numb: ["understanding-feelings", "grounding-five-senses", "difficult-days"],
    unsafe: ["recognising-coercive-control", "healthy-relationships", "staying-safe-online"],
    unsure: ["understanding-feelings", "journaling-week", "breathing-for-hard-moments"]
  };

  var state = { danger: "", feelings: [], who: "me", age: "", comfort: "" };
  var step = 0;
  var LAST = 2; /* Three short steps. Only the safety question needs an answer. */

  function label(list, key) { for (var i = 0; i < list.length; i++) if (list[i][0] === key) return list[i][1]; return key; }

  function radioGroup(name, list, selected) {
    return list.map(function (o) {
      return '<label class="choice"><input type="radio" name="' + name + '" value="' + esc(o[0]) + '"' +
        (selected === o[0] ? " checked" : "") + '> <span>' + esc(o[1]) + "</span></label>";
    }).join("");
  }

  function head(title, hint) {
    return '<h2 class="sp-step-title" tabindex="-1" id="sp-step-title">' + esc(title) + "</h2>" +
      (hint ? '<p class="muted">' + esc(hint) + "</p>" : "");
  }

  function view() {
    var h = "", prog = "Step " + (step + 1) + " of 3";
    if (step === 0) {
      h = head("Is anyone in immediate danger right now?", "This includes you. We ask first, always.") +
        '<fieldset class="field"><legend class="visually-hidden">Is anyone in immediate danger right now?</legend>' +
        radioGroup("danger", [["yes", "Yes"], ["no", "No"], ["unsure", "Not sure"]], state.danger) + "</fieldset>" +
        '<div id="sp-urgent" class="sp-urgent" hidden></div>';
    } else if (step === 1) {
      h = head("How have things been feeling lately?", "Choose any that fit, or none. There are no right answers.") +
        '<div class="chips" role="group" aria-label="Feelings">' + FEELINGS.map(function (f) {
          var on = state.feelings.indexOf(f[0]) > -1;
          return '<button type="button" class="chip" data-feeling="' + f[0] + '" aria-pressed="' + on + '">' + esc(f[1]) + "</button>";
        }).join("") + "</div>" +
        '<div class="field" style="margin-top:1.5rem"><label for="sp-who">Who is this about?</label>' +
        '<select id="sp-who">' + WHO.map(function (o) { return '<option value="' + o[0] + '"' + (state.who === o[0] ? " selected" : "") + ">" + esc(o[1]) + "</option>"; }).join("") + "</select></div>";
    } else if (step === 2) {
      h = head("What would feel comfortable right now?", "Pick one if you like, or go straight to your suggestions.") +
        '<fieldset class="field"><legend class="visually-hidden">What would feel comfortable right now?</legend>' +
        radioGroup("comfort", COMFORT, state.comfort) + "</fieldset>" +
        '<div class="field"><label for="sp-age-c">Age of the person this is about <span class="muted">(optional)</span></label>' +
        '<span class="hint">Only used to suggest the right age guide.</span><select id="sp-age-c">' +
        AGES.map(function (a) { return '<option value="' + a[0] + '"' + (state.age === a[0] ? " selected" : "") + ">" + esc(a[0] ? a[1] : "Skip this") + "</option>"; }).join("") + "</select></div>";
    }
    var back = step > 0 ? '<button type="button" class="btn btn--secondary" data-back>Go back</button>' : "";
    var nextLabel = step === LAST ? "See my suggestions" : (step === 0 ? "Continue" : "Next");
    app.innerHTML = '<div class="sp-card">' + (prog ? '<p class="sp-progress small muted">' + prog + "</p>" : "") + h +
      '<div class="btn-row">' + back + '<button type="button" class="btn btn--primary" data-next>' + nextLabel + "</button>" +
      '<button type="button" class="btn btn--secondary" data-restart>Start again</button></div>' +
      '<p class="small muted sp-note">Nothing you choose here is saved or sent. This is not a test or a diagnosis.</p></div>';
    var t = document.getElementById("sp-step-title");
    if (t && started) t.focus();
  }
  var started = false;

  function urgentPanel() {
    return '<h3>Please get help now</h3><ul class="list-leaf">' +
      '<li>Call <a href="tel:112"><strong>112</strong></a> for police, fire or ambulance.</li>' +
      "<li>Stay with the person. Do not leave them alone.</li>" +
      '<li>For support from a trained counsellor, call Tele-MANAS on <a href="tel:14416"><strong>14416</strong></a>.</li></ul>' +
      '<p><a href="' + R + 'safety.html#urgent">Read what to do in the first minutes</a></p>' +
      '<p class="small">You can carry on with the check-in afterwards, or now if you prefer.</p>';
  }

  function collect() {
    var f;
    if (step === 0) { f = app.querySelector('input[name="danger"]:checked'); state.danger = f ? f.value : ""; }
    if (step === 1) { f = app.querySelector("#sp-who"); state.who = f ? f.value : "me"; }
    if (step === 2) {
      f = app.querySelector('input[name="comfort"]:checked'); state.comfort = f ? f.value : "";
      f = app.querySelector("#sp-age-c"); state.age = f ? f.value : "";
    }
  }

  function needMsg(msg) {
    var p = app.querySelector(".sp-need");
    if (!p) { p = document.createElement("p"); p.className = "sp-need"; p.setAttribute("role", "alert"); app.querySelector(".btn-row").before(p); }
    p.textContent = msg;
  }

  function services() {
    var w = state.who, a = state.age, young = ["0-5", "6-9", "10-13", "14-17"].indexOf(a) > -1;
    var out = [];
    if (w === "child" || w === "student" || (w !== "elder" && young)) {
      if (a === "0-5") {
        out.push("Your anganwadi worker, who can check on your child's growth and development and refer onwards.");
        out.push("A Rashtriya Bal Swasthya Karyakram (RBSK) team or District Early Intervention Centre, if you are worried about speech, movement or development.");
      } else {
        out.push("Your child's or student's school counsellor or a trusted class teacher.");
        out.push("A Rashtriya Kishor Swasthya Karyakram (RKSK) adolescent clinic, where one is available, for ages 10 and above.");
      }
      out.push("Your nearest primary health centre (PHC) or community health centre (CHC), for a first check-up.");
      out.push("Childline 1098, if a child may be unsafe or in need of care and protection.");
    } else if (w === "elder" || a === "60-74" || a === "75-plus") {
      out.push("Your nearest primary health centre (PHC), community health centre (CHC) or district hospital, for a health check. Low mood and confusion can have physical causes.");
      out.push("Your ASHA worker, who can visit at home and help you reach the right clinic.");
      out.push("The District Mental Health Programme (DMHP) team, which runs clinics and outreach in every district.");
      out.push("Elderline 14567, the national helpline for senior citizens.");
    } else {
      out.push("Your nearest primary health centre (PHC) or community health centre (CHC), where a doctor can see you and refer you onwards.");
      out.push("Your ASHA or anganwadi worker, who knows local services and can go with you.");
      out.push("The District Mental Health Programme (DMHP) team, which runs free clinics at district hospitals and some CHCs.");
      if (w !== "other") out.push("A school or college counsellor, if you are a student.");
    }
    if (state.feelings.indexOf("unsafe") > -1 && (!young || w === "me" && a === "18-24")) {
      out.push("A One Stop Centre (Sakhi), which offers women facing violence a safe place, counselling, medical and legal help, all in one place.");
    }
    out.push("Tele-MANAS, 14416: free, 24 hours, in many languages. " + (w === "me" ? "You can call for yourself." : "You can call to ask how to help someone else."));
    return out;
  }

  function resources() {
    var ids = [], extra = [], w = state.who, a = state.age;
    if (w === "child" || w === "student") extra.push("body-safety-conversations");
    if ((a === "10-13" || a === "14-17" || a === "18-24") && state.feelings.indexOf("worried") > -1) extra.push("exam-pressure");
    if (w === "me" && (a === "18-24" || a === "25-39") && (state.feelings.indexOf("low") > -1 || state.feelings.indexOf("tired") > -1)) extra.push("after-the-baby");
    if (w === "elder" || a === "60-74" || a === "75-plus") extra.push(state.feelings.indexOf("lonely") > -1 ? "loneliness-later-life" : "caring-for-a-parent");
    var order = state.feelings.length ? state.feelings : ["unsure"];
    var pool = [];
    if (order.indexOf("unsafe") > -1) pool = pool.concat(BY_FEELING.unsafe);
    order.forEach(function (f) { pool = pool.concat(BY_FEELING[f] || []); });
    pool = extra.slice(0, 1).concat(pool);
    pool.forEach(function (id) { if (ids.indexOf(id) < 0 && ids.length < 3) ids.push(id); });
    return ids;
  }

  function listFeelings() {
    var n = state.feelings.map(function (k) { return label(FEELINGS, k).toLowerCase(); });
    if (!n.length) return "";
    if (n.length === 1) return n[0];
    return n.slice(0, -1).join(", ") + " and " + n[n.length - 1];
  }

  function result() {
    var w = state.who, a = state.age, fs = state.feelings, has = function (k) { return fs.indexOf(k) > -1; };
    var whoTxt = { me: "yourself", child: "your child", student: "a young person you teach", elder: "an older family member", other: "someone you care about" }[w] || "someone";
    var s = "You told us this is about " + whoTxt;
    if (a) s += ", in the " + label(AGES, a).toLowerCase() + " age band";
    s += fs.length ? ", and that " + (w === "me" ? "you are" : "they seem to be") + " feeling " + listFeelings() + "." : ".";
    var h = '<div class="sp-card sp-result" tabindex="-1" id="sp-result"><h2 id="sp-result-title">Here is a gentle summary</h2>' +
      "<p class=\"lede\">" + esc(s) + "</p>" +
      "<p>What you describe is a part of being human, and it deserves attention and care. This is not a label or a diagnosis. Only a trained professional who meets the person can say more.</p>";
    if (has("unsafe")) {
      h += '<div class="note note--caution" role="note"><p><strong>Feeling unsafe at home matters.</strong> If this phone is shared, or someone checks it, you can use the Leave quickly button at any time. ' +
        'The <a href="' + R + 'safety.html#shared-phone">shared phone tips</a> show how to stay private. ' +
        'You can call the Women Helpline on <a href="tel:181">181</a>, or <a href="tel:112">112</a> if you are in danger right now. A One Stop Centre (Sakhi) can give you a safe place and help. ' +
        'Read about <a href="' + R + 'resources/recognising-coercive-control.html">recognising coercive control</a>.</p></div>';
    }
    if (has("low") || has("numb") || has("overwhelmed")) {
      h += '<div class="note note--caution" role="note"><p>If you are thinking of ending your life, or someone else is, please call <a href="tel:14416"><strong>14416</strong></a> or <a href="tel:112"><strong>112</strong></a> now. You do not need to be sure. Calling is always allowed.</p></div>';
    }
    if (state.danger === "yes") {
      h += '<p><strong>You told us someone may be in danger. Please call <a href="tel:112">112</a> first.</strong></p>';
    }
    if (a) h += '<h3>A suggested pathway</h3><p><a href="' + R + "pathways/" + a + '.html">Read the guide for the ' + esc(label(AGES, a).toLowerCase()) + " age band</a>. It describes what is common at this stage, what helps, and when to ask for support.</p>";
    else h += '<h3>A suggested pathway</h3><p><a href="' + R + 'pathways.html">Browse the age pathways</a> and choose the band that fits.</p>';
    var ids = resources();
    h += "<h3>Things you might read or try</h3><ul class=\"list-leaf\">" + ids.map(function (id) {
      return '<li><a href="' + R + "resources/" + id + '.html">' + esc(RES_TITLES[id]) + "</a></li>";
    }).join("") + "</ul>";
    if (state.comfort === "read") h += '<p><a href="' + R + "explore.html" + (a ? "?age=" + a : "") + '">Browse more to read</a></p>';
    if (state.comfort === "calm") h += '<p>Start with <a href="' + R + 'resources/breathing-for-hard-moments.html">slow breathing</a>, then <a href="' + R + 'resources/grounding-five-senses.html">grounding</a>.</p>';
    h += "<h3>People and services you can ask</h3><ul class=\"list-leaf\">" + services().map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + "</ul>";
    if (state.comfort === "talk") {
      h += '<div class="panel panel--sage"><h3>You chose to talk to a person</h3><p>You can ask for someone to contact you, or call one of the free helplines below today.</p>' +
        '<p><a class="btn btn--primary" href="' + R + 'connect.html">See how to connect with a person</a></p></div>';
    }
    h += '<h3>Helplines, free to call</h3><ul class="helplines">' +
      '<li class="helpline"><a class="helpline__num" href="tel:112">112</a><span class="helpline__text"><strong>Emergency</strong> Police, fire and ambulance.</span></li>' +
      '<li class="helpline"><a class="helpline__num" href="tel:14416">14416</a><span class="helpline__text"><strong>Tele-MANAS</strong> Free mental health support, 24 hours. Also 1-800-891-4416.</span></li>' +
      '<li class="helpline"><a class="helpline__num" href="tel:181">181</a><span class="helpline__text"><strong>Women Helpline</strong> For women facing violence.</span></li>' +
      '<li class="helpline"><a class="helpline__num" href="tel:1098">1098</a><span class="helpline__text"><strong>Childline</strong> For children in need of care and protection.</span></li></ul>' +
      '<p class="small muted sp-note">Nothing you chose here was saved or sent. This is not a test or a diagnosis.</p>' +
      '<div class="btn-row"><button type="button" class="btn btn--secondary" data-back>Change my answers</button><button type="button" class="btn btn--secondary" data-restart>Start again</button></div></div>';
    app.innerHTML = h;
    var r = document.getElementById("sp-result");
    if (r) r.focus();
  }

  app.addEventListener("click", function (e) {
    var t = e.target.closest("button");
    if (!t) return;
    started = true;
    var c = t.getAttribute("data-feeling");
    if (c) {
      var i = state.feelings.indexOf(c);
      if (i > -1) state.feelings.splice(i, 1); else state.feelings.push(c);
      t.setAttribute("aria-pressed", String(i < 0));
      return;
    }
    if (t.hasAttribute("data-restart")) { state = { danger: "", feelings: [], who: "me", age: "", comfort: "" }; step = 0; view(); return; }
    if (t.hasAttribute("data-back")) { step = step > 0 ? (app.querySelector("#sp-result") ? LAST : step - 1) : 0; view(); return; }
    if (t.hasAttribute("data-next")) {
      collect();
      if (step === 0) {
        if (!state.danger) { needMsg("Please choose an answer to continue."); return; }
        if (state.danger === "yes" && !app.querySelector("#sp-urgent").dataset.shown) {
          var u = app.querySelector("#sp-urgent"); u.innerHTML = urgentPanel(); u.hidden = false; u.dataset.shown = "1";
          t.textContent = "Continue the check-in"; return;
        }
      }
      if (step === LAST) { result(); return; }
      step++; view();
    }
  });
  app.addEventListener("change", function (e) { var n = app.querySelector(".sp-need"); if (n) n.remove(); });

  view();
})();
