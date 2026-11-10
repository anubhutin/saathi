/* SAATHI request-contact form. Until a referral backend is configured, nothing is sent; the form is cleared and helplines are shown. */
(function () {
  "use strict";
  var form = document.querySelector("[data-connect-form]");
  if (!form) return;
  var submit = form.querySelector("[data-submit]");
  var consents = form.querySelectorAll("[data-consent]");
  var sharedYes = form.querySelector("#sp-shared-yes");
  var sharedBox = document.getElementById("sp-shared-advice");
  var age = form.querySelector("#sp-age");
  var minorConsent = document.getElementById("sp-minor-consent");
  var done = document.getElementById("sp-done");

  function update() {
    var ok = true;
    consents.forEach(function (c) {
      if (c.closest("[hidden]")) return;
      if (!c.checked) ok = false;
    });
    submit.disabled = !ok;
    submit.setAttribute("aria-disabled", String(!ok));
  }
  function showAdvice() { if (sharedBox) sharedBox.hidden = !(sharedYes && sharedYes.checked); }
  function showMinor() {
    var minor = ["0-5", "6-9", "10-13", "14-17"].indexOf(age.value) > -1;
    minorConsent.hidden = !minor;
    update();
  }
  form.addEventListener("change", function () { showAdvice(); showMinor(); update(); });
  form.addEventListener("reset", function () { setTimeout(function () { showAdvice(); showMinor(); update(); }, 0); });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (submit.disabled) return;
    form.reset();
    form.hidden = true;
    done.hidden = false;
    done.focus();
    done.scrollIntoView({ block: "start" });
  });
  var again = document.querySelector("[data-again]");
  if (again) again.addEventListener("click", function () {
    done.hidden = true; form.hidden = false; showAdvice(); showMinor(); update();
    form.querySelector("input,select").focus();
  });
  showAdvice(); showMinor(); update();
})();
