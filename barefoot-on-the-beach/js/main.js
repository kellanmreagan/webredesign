document.addEventListener("DOMContentLoaded", function () {
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

  var lightbox = document.querySelector(".lightbox");
  var galleryLinks = Array.from(document.querySelectorAll(".gallery-grid a"));
  if (lightbox && galleryLinks.length) {
    var lbImg = lightbox.querySelector("img");
    var lbCaption = lightbox.querySelector("figcaption");
    var closeBtn = lightbox.querySelector(".lightbox-close");
    var prevBtn = lightbox.querySelector(".lightbox-prev");
    var nextBtn = lightbox.querySelector(".lightbox-next");
    var currentIndex = 0;

    function show(index) {
      currentIndex = (index + galleryLinks.length) % galleryLinks.length;
      var link = galleryLinks[currentIndex];
      lbImg.src = link.getAttribute("href");
      lbImg.alt = link.dataset.caption || "";
      lbCaption.textContent = link.dataset.caption || "";
    }

    galleryLinks.forEach(function (link, index) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        show(index);
        lightbox.classList.add("open");
      });
    });

    function closeLightbox() {
      lightbox.classList.remove("open");
      lbImg.src = "";
    }

    closeBtn.addEventListener("click", closeLightbox);
    if (prevBtn) prevBtn.addEventListener("click", function () { show(currentIndex - 1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { show(currentIndex + 1); });
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", function (e) {
      if (!lightbox.classList.contains("open")) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowRight") show(currentIndex + 1);
      if (e.key === "ArrowLeft") show(currentIndex - 1);
    });
  }
});
