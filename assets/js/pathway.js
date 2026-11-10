/* Print button for the signs card on pathway pages. No data is sent anywhere. */
(function () {
  document.querySelectorAll('[data-print]').forEach(function (b) {
    b.addEventListener('click', function () { window.print(); });
  });
})();
