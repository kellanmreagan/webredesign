document.addEventListener("DOMContentLoaded", function () {
  var header = document.querySelector(".site-header");
  if (header) {
    var setHeaderOffset = function () {
      document.documentElement.style.setProperty(
        "--header-offset",
        header.getBoundingClientRect().height + 16 + "px"
      );
    };
    setHeaderOffset();
    window.addEventListener("resize", setHeaderOffset);
    // Re-measure after the fonts load, since text reflow changes header height.
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(setHeaderOffset);
    }
  }

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Smooth-scroll only for same-page "#id" links (skip link, in-page CTAs).
  // Cross-page links that happen to carry a #hash (e.g. "rates.html#moose-lodge-rates")
  // are left alone so the browser jumps instantly on load, landing correctly thanks
  // to the scroll-margin-top set on anchor targets in style.css.
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      var id = link.getAttribute("href").slice(1);
      var target = id && document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      history.pushState(null, "", "#" + id);
    });
  });

  var lightbox = document.querySelector(".lightbox");
  if (lightbox) {
    var lbImg = lightbox.querySelector("img");
    var lbCaption = lightbox.querySelector("figcaption");
    var closeBtn = lightbox.querySelector(".lightbox-close");

    document.querySelectorAll(".gallery a").forEach(function (link) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        lbImg.src = link.getAttribute("href");
        lbImg.alt = link.dataset.caption || "";
        lbCaption.textContent = link.dataset.caption || "";
        lightbox.classList.add("open");
      });
    });

    function closeLightbox() {
      lightbox.classList.remove("open");
      lbImg.removeAttribute("src");
    }

    closeBtn.addEventListener("click", closeLightbox);
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeLightbox();
    });
  }
});
