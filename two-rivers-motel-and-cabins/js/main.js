(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.main-nav li.has-sub > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 760) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });
})();
