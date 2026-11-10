/* SAATHI shared behaviour: mobile nav, quick exit, language, light version. */
(function () {
  "use strict";

  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      if (val === null) localStorage.removeItem(key);
      else localStorage.setItem(key, val);
    } catch (e) { return null; }
  }

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Quick exit ----------
     Replaces this page in history so Back does not return here.
     It cannot erase browser history, network logs or device traces. */
  var exitLink = document.querySelector("[data-quick-exit]");
  function quickExit(e) {
    if (e) e.preventDefault();
    document.body.style.visibility = "hidden";
    document.title = "Weather";
    window.location.replace(exitLink ? exitLink.href : "https://www.google.com");
  }
  if (exitLink) exitLink.addEventListener("click", quickExit);
  var lastEsc = 0;
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var now = Date.now();
    if (now - lastEsc < 800) quickExit();
    lastEsc = now;
  });

  /* ---------- Language ----------
     Interface strings come from locales/*.json (built into i18n-strings.js).
     Missing keys fall back to the English text already in the page. */
  var STRINGS = window.SAATHI_STRINGS || {};
  var originals = new Map();

  function applyLang(lang) {
    var dict = STRINGS[lang] || {};
    var meta = dict._meta || {};
    document.documentElement.lang = lang;
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      if (!originals.has(el)) originals.set(el, el.textContent);
      var val = lang === "en" ? null : dict[key];
      el.textContent = val || originals.get(el);
    });
    document.querySelectorAll("[data-lang-select]").forEach(function (s) { s.value = lang; });
    var banner = document.querySelector("[data-lang-banner]");
    if (banner) {
      if (lang !== "en" && meta.banner) {
        banner.textContent = meta.banner;
        banner.hidden = false;
      } else {
        banner.hidden = true;
      }
    }
  }

  function setLang(lang) {
    store("saathi.lang", lang);
    applyLang(lang);
  }

  var current = store("saathi.lang") || "en";
  document.querySelectorAll("[data-lang-select]").forEach(function (s) {
    s.addEventListener("change", function () { setLang(s.value); });
  });
  document.querySelectorAll("[data-set-lang]").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.getAttribute("data-set-lang")); });
  });
  applyLang(current);
  window.SAATHI = { setLang: setLang, store: store };

  /* ---------- Light version ---------- */
  var lite = store("saathi.lite") === "1";
  document.querySelectorAll("[data-lite-toggle]").forEach(function (cb) {
    cb.checked = lite;
    cb.addEventListener("change", function () {
      store("saathi.lite", cb.checked ? "1" : null);
      window.location.reload();
    });
  });
})();
