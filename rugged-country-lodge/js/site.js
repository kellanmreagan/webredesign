(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function (event) {
      event.preventDefault();
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".site-nav .has-sub > a").forEach(function (link) {
    link.addEventListener("click", function (event) {
      if (window.matchMedia("(max-width: 760px)").matches) {
        event.preventDefault();
        link.parentElement.classList.toggle("open");
      }
    });
  });

  var lightbox = document.createElement("div");
  lightbox.className = "lightbox";
  lightbox.innerHTML = '<button type="button" aria-label="Close">Close</button><img alt="">';
  document.body.appendChild(lightbox);
  var lbImg = lightbox.querySelector("img");
  var lbBtn = lightbox.querySelector("button");

  function closeLb() {
    lightbox.classList.remove("open");
    lbImg.removeAttribute("src");
  }

  lbBtn.addEventListener("click", closeLb);
  lightbox.addEventListener("click", function (event) {
    if (event.target === lightbox) closeLb();
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeLb();
  });

  document.querySelectorAll("[data-lightbox]").forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      lbImg.src = link.getAttribute("href");
      lbImg.alt = (link.querySelector("img") && link.querySelector("img").alt) || "";
      lightbox.classList.add("open");
    });
  });

  document.querySelectorAll("form[data-mail]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var to = form.getAttribute("data-mail") || "info@ruggedcountrylodge.com";
      var subject = form.getAttribute("data-subject") || "Rugged Country Lodge";
      var parts = [];
      form.querySelectorAll("input, textarea").forEach(function (field) {
        if (!field.name || field.type === "submit") return;
        parts.push((field.name) + ": " + (field.value || ""));
      });
      var href =
        "mailto:" +
        encodeURIComponent(to) +
        "?subject=" +
        encodeURIComponent(subject) +
        "&body=" +
        encodeURIComponent(parts.join("\n"));
      window.location.href = href;
    });
  });
})();
