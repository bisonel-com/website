(() => {
  const header = document.querySelector("[data-header]");
  const nav = document.querySelector("[data-nav]");
  const toggle = document.querySelector("[data-nav-toggle]");
  const navLinks = nav ? Array.from(nav.querySelectorAll("a[href^='#']")) : [];
  const sections = ["services", "clients", "incubation", "about", "contact"]
    .map((id) => document.getElementById(id))
    .filter(Boolean);

  const setScrolled = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  const closeNav = () => {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  };

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", () => closeNav());
  });

  const updateCurrent = () => {
    const marker = window.scrollY + 120;
    let current = null;

    sections.forEach((section) => {
      if (section.offsetTop <= marker) {
        current = section.id;
      }
    });

    navLinks.forEach((link) => {
      const href = link.getAttribute("href") || "";
      const id = href.slice(1);
      if (id && id === current) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  const revealTargets = document.querySelectorAll(
    ".section-intro, .service-block, .client-link, .incubate-link, .about-copy, .contact-panel"
  );

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.16, rootMargin: "0px 0px -8% 0px" }
    );

    revealTargets.forEach((el) => {
      el.classList.add("reveal");
      observer.observe(el);
    });
  } else {
    revealTargets.forEach((el) => el.classList.add("is-visible"));
  }

  setScrolled();
  updateCurrent();
  window.addEventListener("scroll", () => {
    setScrolled();
    updateCurrent();
  }, { passive: true });
})();
