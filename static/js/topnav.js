// =====================================================
// Top Navigation Overlay (Phase N2)
// =====================================================

document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.querySelector("[data-hamburger]");
  const overlay = document.querySelector("[data-nav-overlay]");
  const backdrop = document.querySelector("[data-overlay-backdrop]");

  if (!hamburger || !overlay || !backdrop) return;

  function openOverlay() {
    overlay.classList.add("open");
    backdrop.classList.add("open");
  }

  function closeOverlay() {
    overlay.classList.remove("open");
    backdrop.classList.remove("open");
  }

  hamburger.addEventListener("click", openOverlay);
  backdrop.addEventListener("click", closeOverlay);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeOverlay();
    }
  });
});
