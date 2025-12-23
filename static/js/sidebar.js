// =====================================================
// Sidebar Group Expand / Collapse (Phase C.1)
// - Persisted state
// - Auto-expand active group
// =====================================================

document.addEventListener("DOMContentLoaded", () => {
  const groups = document.querySelectorAll(".nav-group");

  groups.forEach(group => {
    const key = group.dataset.group;
    const title = group.querySelector(".nav-group-title");
    const items = group.querySelector(".nav-group-items");

    if (!key || !title || !items) return;

    const storageKey = `sidebar_group_${key}`;
    const savedState = localStorage.getItem(storageKey);

    // Check if this group contains the active link
    const hasActiveLink = items.querySelector("a.active") !== null;

    // Determine initial state
    if (hasActiveLink) {
      // Always expand the group that contains the active page
      items.style.display = "";
      group.classList.remove("collapsed");
      localStorage.setItem(storageKey, "expanded");
    } else if (savedState === "collapsed") {
      items.style.display = "none";
      group.classList.add("collapsed");
    }

    // Toggle on title click
    title.addEventListener("click", () => {
      const isCollapsed = items.style.display === "none";

      if (isCollapsed) {
        items.style.display = "";
        group.classList.remove("collapsed");
        localStorage.setItem(storageKey, "expanded");
      } else {
        items.style.display = "none";
        group.classList.add("collapsed");
        localStorage.setItem(storageKey, "collapsed");
      }
    });
  });
});
