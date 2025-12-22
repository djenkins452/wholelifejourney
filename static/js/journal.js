// =====================================================
// Journal UI Logic (State-Persistent)
// =====================================================

let allExpanded = false;

/* ----------------------------------------
   Restore State on Load
---------------------------------------- */
document.addEventListener("DOMContentLoaded", () => {
  const savedState = localStorage.getItem("journal_expand_state");

  if (savedState === "expanded") {
    expandAllEntries();
  } else {
    collapseAllEntries();
  }
});

/* ----------------------------------------
   Expand / Collapse Individual Entry
---------------------------------------- */
function toggleEntry(id, btn) {
  const body = document.getElementById("entry-" + id);
  const preview = document.getElementById("preview-" + id);
  const icon = btn.querySelector("img");

  const expanded = body.style.display === "block";

  body.style.display = expanded ? "none" : "block";
  preview.style.display = expanded ? "-webkit-box" : "none";
  icon.src = expanded
    ? "/static/icons/arrow-right.svg"
    : "/static/icons/arrow-down.svg";
}

/* ----------------------------------------
   Expand / Collapse All
---------------------------------------- */
function toggleAll() {
  allExpanded = !allExpanded;

  if (allExpanded) {
    expandAllEntries();
    localStorage.setItem("journal_expand_state", "expanded");
  } else {
    collapseAllEntries();
    localStorage.setItem("journal_expand_state", "collapsed");
  }
}

/* ----------------------------------------
   Helpers
---------------------------------------- */
function expandAllEntries() {
  allExpanded = true;

  document.querySelectorAll(".entry-body").forEach(el => {
    el.style.display = "block";
  });

  document.querySelectorAll(".preview").forEach(el => {
    el.style.display = "none";
  });

  document.querySelectorAll(".entry-toggle img").forEach(icon => {
    icon.src = "/static/icons/arrow-down.svg";
  });

  const toggleIcon = document.getElementById("toggleAllIcon");
  const toggleText = document.getElementById("toggleAllText");

  if (toggleIcon) toggleIcon.src = "/static/icons/arrow-down.svg";
  if (toggleText) toggleText.textContent = "Collapse all";
}

function collapseAllEntries() {
  allExpanded = false;

  document.querySelectorAll(".entry-body").forEach(el => {
    el.style.display = "none";
  });

  document.querySelectorAll(".preview").forEach(el => {
    el.style.display = "-webkit-box";
  });

  document.querySelectorAll(".entry-toggle img").forEach(icon => {
    icon.src = "/static/icons/arrow-right.svg";
  });

  const toggleIcon = document.getElementById("toggleAllIcon");
  const toggleText = document.getElementById("toggleAllText");

  if (toggleIcon) toggleIcon.src = "/static/icons/arrow-right.svg";
  if (toggleText) toggleText.textContent = "Expand all";
}

/* ----------------------------------------
   Submit Edit / Hide / Delete
---------------------------------------- */
function submitDelete(action, entryId) {
  let message = "";

  if (action === "hide") {
    message = "Move this entry to Hidden?";
  } else if (action === "delete") {
    message = "Permanently delete this entry? This cannot be undone.";
  } else {
    console.error("Unknown delete action:", action);
    return;
  }

  if (!confirm(message)) return;

  const url =
    action === "hide"
      ? `/journal/delete/${entryId}/`
      : `/journal/delete-permanent/${entryId}/`;

  const form = document.createElement("form");
  form.method = "POST";
  form.action = url;

  const csrf = document.querySelector(
    "input[name='csrfmiddlewaretoken']"
  );

  if (!csrf) {
    console.error("CSRF token not found");
    return;
  }

  const csrfClone = csrf.cloneNode();
  form.appendChild(csrfClone);

  document.body.appendChild(form);
  form.submit();
}
