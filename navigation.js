(() => {
  const body = document.body;
  const hamburger = document.querySelector(".hamburger");
  const mobileMenu = document.querySelector("#mobileMenu");

  if (!hamburger || !mobileMenu) return;

  const closeMenu = ({ restoreFocus = false } = {}) => {
    body.classList.remove("menu-open");
    hamburger.setAttribute("aria-expanded", "false");
    hamburger.setAttribute("aria-label", "開啟選單");
    if (restoreFocus) hamburger.focus();
  };

  hamburger.addEventListener("click", () => {
    const isOpen = body.classList.toggle("menu-open");
    hamburger.setAttribute("aria-expanded", String(isOpen));
    hamburger.setAttribute("aria-label", isOpen ? "關閉選單" : "開啟選單");
  });

  mobileMenu.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => closeMenu());
  });

  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && body.classList.contains("menu-open")) {
      closeMenu({ restoreFocus: true });
    }
  });

  window.addEventListener("resize", () => {
    if (getComputedStyle(hamburger).display === "none") closeMenu();
  });

  document.querySelectorAll(".desktop-nav .nav-dropdown").forEach(dropdown => {
    const trigger = dropdown.querySelector(":scope > a");
    const submenu = dropdown.querySelector(".nav-submenu");
    if (!trigger || !submenu) return;
    trigger.setAttribute("aria-expanded", "false");
    let focusRequest = 0;

    const open = () => {
      dropdown.classList.remove("nav-dismissed");
      trigger.setAttribute("aria-expanded", "true");
    };
    const dismiss = ({ restoreFocus = false } = {}) => {
      focusRequest += 1;
      dropdown.classList.add("nav-dismissed");
      trigger.setAttribute("aria-expanded", "false");
      if (restoreFocus) trigger.focus();
    };
    const focusFirstItem = () => {
      const firstItem = submenu.querySelector("a");
      if (!firstItem) return;
      const request = ++focusRequest;
      let attempts = 0;
      const tryFocus = () => {
        if (request !== focusRequest || trigger.getAttribute("aria-expanded") !== "true" ||
            document.activeElement !== trigger || getComputedStyle(hamburger).display !== "none") return;
        firstItem.focus();
        if (document.activeElement !== firstItem && ++attempts < 30) requestAnimationFrame(tryFocus);
      };
      // visibility transitions can make an immediately focused item unfocusable.
      requestAnimationFrame(tryFocus);
    };

    dropdown.addEventListener("mouseenter", open);
    dropdown.addEventListener("mouseleave", () => {
      if (!dropdown.contains(document.activeElement)) dismiss();
    });
    dropdown.addEventListener("focusin", event => {
      if (!dropdown.classList.contains("nav-dismissed") || !dropdown.contains(event.relatedTarget)) open();
    });
    dropdown.addEventListener("focusout", event => {
      if (!dropdown.contains(event.relatedTarget)) dismiss();
    });
    dropdown.addEventListener("keydown", event => {
      if (event.key === "Escape" && trigger.getAttribute("aria-expanded") === "true") {
        event.preventDefault();
        event.stopPropagation();
        dismiss({ restoreFocus: true });
      } else if (event.target === trigger && (event.key === "ArrowDown" || event.key === " ")) {
        event.preventDefault();
        if (event.key === " " && trigger.getAttribute("aria-expanded") === "true") {
          dismiss();
        } else {
          open();
          focusFirstItem();
        }
      }
    });
    window.addEventListener("resize", () => {
      if (getComputedStyle(hamburger).display !== "none") dismiss();
    });
  });
})();
