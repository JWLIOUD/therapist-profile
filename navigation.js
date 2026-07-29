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
})();
