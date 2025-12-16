/**
 * Shared Navigation Component
 * Injects navigation HTML, favicon, and theme toggle functionality into any page
 * Usage: Include <script src="/nav.js"></script> in the <head> with defer attribute
 */

(function () {
  // Inject favicon into <head> if not already present
  if (!document.querySelector('link[rel="icon"]')) {
    const favicon = document.createElement("link");
    favicon.rel = "icon";
    favicon.type = "image/svg+xml";
    favicon.href = "/assets/favicon.svg";
    document.head.appendChild(favicon);
  }

  // Navigation HTML template
  const navHTML = `
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/projects">Projects</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/tools">Tools</a></li>
      </ul>
      <button id="theme-toggle" aria-label="Toggle dark mode">
        <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"/>
          <line x1="12" y1="1" x2="12" y2="3"/>
          <line x1="12" y1="21" x2="12" y2="23"/>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
          <line x1="1" y1="12" x2="3" y2="12"/>
          <line x1="21" y1="12" x2="23" y2="12"/>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>
        <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
        </svg>
      </button>
    </nav>
  `;

  // Wait for DOM to be ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  function init() {
    // Insert navigation at the beginning of body
    const existingNav = document.querySelector("nav");
    if (existingNav) {
      // Replace existing nav with the shared one
      existingNav.outerHTML = navHTML;
    } else {
      // Insert at the beginning of body if no nav exists
      document.body.insertAdjacentHTML("afterbegin", navHTML);
    }

    // Initialize theme toggle
    initThemeToggle();
  }

  function initThemeToggle() {
    const toggle = document.getElementById("theme-toggle");
    const body = document.body;
    const saved = localStorage.getItem("theme");
    const prefersDark = window.matchMedia(
      "(prefers-color-scheme: dark)"
    ).matches;

    // Apply saved theme or system preference
    if (saved) {
      body.classList.add(saved);
    } else {
      body.classList.add(prefersDark ? "dark-mode" : "light-mode");
    }

    // Toggle theme on button click
    if (toggle) {
      toggle.addEventListener("click", () => {
        const isDark = body.classList.contains("dark-mode");
        body.classList.remove("dark-mode", "light-mode");
        body.classList.add(isDark ? "light-mode" : "dark-mode");
        localStorage.setItem("theme", isDark ? "light-mode" : "dark-mode");
      });
    }
  }
})();
