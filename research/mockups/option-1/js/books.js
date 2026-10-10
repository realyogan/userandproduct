/* Books pages: each 3D cover settles in when it scrolls into view (CSS does the motion, see .b3d in
   books.css). Without this script, or with reduced motion, the books simply stand at rest. */
(function () {
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var books = document.querySelectorAll(".b3d");
  books.forEach(function (b) { b.classList.add("is-pre"); });
  var io = new IntersectionObserver(function (entries) {
    var n = 0;
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.style.transitionDelay = (n++ * 90) + "ms";   // a slight stagger when several arrive together
      requestAnimationFrame(function () { e.target.classList.remove("is-pre"); });
      io.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -12% 0px" });
  books.forEach(function (b) { io.observe(b); });
})();
