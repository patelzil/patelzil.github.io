# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A minimalist static portfolio website built with pure HTML, CSS, and vanilla JavaScript. No frameworks, no build steps (build script is optional), zero dependencies for the site itself. Philosophy: content over complexity.

## Development Commands

### Local Development
```bash
# Start local server (required for clean URLs and fetch API)
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Build Script (Optional)
```bash
# Install markdown dependency (one-time)
pip install markdown

# Convert markdown blog posts to HTML
python3 build.py
```

The build script is **optional**—you can write HTML directly. It converts markdown files from `content/blog/` to HTML in `blog/` and wraps them with the site template.

## Architecture

### JSON-Driven Content System

The site uses a **JSON-based content management system** instead of manually editing HTML:

- **`projects.json`**: Single source of truth for all projects
- **`blog.json`**: Single source of truth for all blog posts
- JavaScript `fetch()` calls load JSON and dynamically render content
- This pattern is used on 3 pages: `index.html` (recent items), `projects/index.html` (all projects), `blog/index.html` (all posts)

**Key insight**: When adding content, you edit JSON files—not HTML. The HTML pages automatically reflect changes via client-side rendering.

### Content Workflow

#### Adding a Blog Post
1. Write HTML in `blog/your-post.html` (or use markdown + `build.py`)
2. Add entry to `blog.json` with: `id`, `title`, `date`, `excerpt`, `url`
3. Refresh—appears automatically on homepage (latest 2) and blog index

#### Adding a Project
1. Add entry to `projects.json` with: `id`, `title`, `date`, `description`, `keyLearnings`, `tags[]`, `links{}`
2. Refresh—appears automatically on homepage (latest 2) and projects page

### Directory Structure

```
portfolio/
├── index.html           # Homepage - loads recent projects/posts via JS
├── projects.json        # Project data (loaded by index.html and projects/index.html)
├── blog.json           # Blog post data (loaded by index.html and blog/index.html)
├── style.css           # Single CSS file with CSS variables for theming
├── build.py            # Optional: Markdown → HTML converter
├── projects/
│   └── index.html      # All projects page - dynamically renders from projects.json
├── blog/
│   ├── index.html      # Blog index - dynamically renders from blog.json
│   └── *.html          # Individual blog post pages
├── tools/
│   └── index.html      # Tools page (static HTML)
├── content/blog/       # Markdown source files (optional)
└── assets/            # Images, logos, etc.
```

### Clean URLs

The site uses directory-based URLs:
- Home: `/` (not `/index.html`)
- Projects: `/projects` (not `/projects.html`)
- Blog: `/blog` (not `/blog.html`)
- Tools: `/tools` (not `/tools.html`)

**Important**: This requires a local server (`python3 -m http.server`) during development. Opening `index.html` directly in a browser will break fetch calls and navigation.

### Styling System

All styles in `style.css` use CSS variables for easy customization:
```css
:root {
  --color-link: #0066cc;
  --color-accent: #0066cc;
  --max-width: 42rem;
  /* etc. */
}
```

- Dark mode via `@media (prefers-color-scheme: dark)`
- No CSS frameworks—pure CSS with semantic class names
- Mobile-first responsive design

**Design patterns**:
- **Timeline**: Vertical line (`.timeline::before`) with logo boxes that have `z-index: 1` to overlay the line
- **Section headers**: `h2` elements have bottom borders for visual separation
- **Social icons**: 32px circular buttons with hover effects (transform + color change)
- **Visual hierarchy**: Header is separated from main content with border-bottom

### JavaScript Architecture

Each page that loads JSON follows this pattern:
1. `async function loadContent()` - fetches JSON
2. `function renderContent(data)` - generates HTML from JSON
3. Auto-executes on page load

**Example** (from `index.html`):
```javascript
async function loadRecentProjects() {
  const response = await fetch('/projects.json');
  const data = await response.json();
  const recentProjects = data.projects.slice(0, 2); // Latest 2
  renderRecentProjects(recentProjects);
}
loadRecentProjects(); // Auto-run
```

### Build Script Details

`build.py` is a Python script that:
- Scans `content/blog/*.md` files
- Extracts title (first `# heading`) and date (from `**Month Day, Year**` format)
- Converts markdown to HTML using Python's `markdown` library with `extra`, `codehilite`, and `fenced_code` extensions
- Wraps content in `BLOG_TEMPLATE` (defined in script)
- Outputs to `blog/` with filename: `{original-name-minus-date-prefix}.html`
- Generates `<meta name="description">` from first paragraph

**Note**: The script updates `blog/index.html` automatically, but with the JSON system, you should manually update `blog.json` instead.

## Adding Shared Components to New Pages

The `nav.js` script automatically injects:
- **Favicon** (`/assets/favicon.svg`)
- **Navigation menu** (Home, Projects, Blog, Tools)
- **Theme toggle** button and functionality

**To add these to any new HTML page**, simply include this line in the `<head>`:
```html
<script src="/nav.js" defer></script>
```

That's it! The script will automatically:
1. Add the favicon link to `<head>`
2. Inject the navigation menu at the top of the page
3. Initialize theme toggle functionality

**Manual Setup (if not using nav.js)**

If you need to manually add components without using `nav.js`, copy-paste these blocks:

**1. Add to `<nav>` section (inside nav, after the `<ul>`)**:
```html
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
```

**2. Add before closing `</body>` tag**:
```html
<script>
    // Theme toggle - Copy this block to every page
    (function() {
        const toggle = document.getElementById('theme-toggle');
        const body = document.body;
        const saved = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (saved) body.classList.add(saved);
        else body.classList.add(prefersDark ? 'dark-mode' : 'light-mode');

        if (toggle) {
            toggle.addEventListener('click', () => {
                const isDark = body.classList.contains('dark-mode');
                body.classList.remove('dark-mode', 'light-mode');
                body.classList.add(isDark ? 'light-mode' : 'dark-mode');
                localStorage.setItem('theme', isDark ? 'light-mode' : 'dark-mode');
            });
        }
    })();
</script>
```

The CSS is already global in `style.css` and will work automatically.

## Key Patterns to Follow

### When Adding Features
- **Prefer editing JSON** over editing HTML (for projects/blog content)
- **No frameworks**: Use vanilla JS, plain CSS, standard HTML
- **Single CSS file**: Add styles to `style.css` using existing naming conventions
- **Inline JavaScript**: Small scripts inline in HTML (no separate JS files)
- **Theme toggle**: Copy-paste the two blocks above to every new HTML page

### When Modifying Content
- **Projects**: Edit `projects.json`
- **Blog posts**: Create HTML in `blog/`, add entry to `blog.json`
- **Styling**: Update CSS variables in `:root` or add new classes in `style.css`

### File Naming Conventions
- Blog posts: `lowercase-with-hyphens.html` in `blog/`
- Markdown files: `YYYY-MM-DD-title.md` in `content/blog/`
- JSON structure: camelCase for keys (`keyLearnings`, not `key_learnings`)

## Common Gotchas

1. **Relative paths**: All links use root-relative paths (`/blog`, `/style.css`), not relative (`./blog`, `../style.css`)
2. **Fetch requires server**: JSON loading only works with a local server, not `file://` protocol
3. **JSON order matters**: Top items in `projects.json` and `blog.json` arrays appear first (newest posts should be at top)
4. **Build script date parsing**: `build.py` looks for dates in format `**Month Day, Year**` in markdown
5. **No git repo**: This is not currently a git repository—commits won't work without `git init`

