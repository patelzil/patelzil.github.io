#!/usr/bin/env python3
"""
Simple static site builder for markdown-based portfolio.
Converts markdown blog posts to HTML using Python's markdown library.

Usage:
    python build.py              # Build all markdown files
    python build.py --watch      # Watch for changes (future enhancement)
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Try to import markdown, provide helpful error if not installed
try:
    import markdown
except ImportError:
    print("Error: markdown library not installed.")
    print("Install it with: pip install markdown")
    exit(1)


# Configuration
CONTENT_DIR = Path("content/blog")
OUTPUT_DIR = Path("blog")
TEMPLATE_FILE = Path("blog_template.html")

# HTML template for blog posts
BLOG_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <script src="/nav.js" defer></script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{description}">
  <meta name="author" content="Zil Patel">
  <title>{title} - Zil Patel</title>
  <link rel="stylesheet" href="/style.css">
</head>
<body>
  <article>
    <header class="site-header">
      <h1>{title}</h1>
      <p class="text-muted text-small">{date}</p>
    </header>

    <main>
{content}

      <hr style="margin: 2rem 0; border: none; border-top: 1px solid var(--color-border);">

      <p class="text-muted text-small">
        <a href="/blog">← Back to blog</a>
      </p>
    </main>
  </article>

  <footer>
    <p>&copy; 2025 Zil Patel. Built with HTML, CSS, and zero frameworks.</p>
  </footer>
</body>
</html>
"""


def extract_metadata(content):
    """Extract title and date from markdown content."""
    lines = content.split('\n')
    title = None
    date = None
    
    # Look for first heading as title
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Look for date in bold or as standalone line
    date_pattern = r'\*\*([A-Za-z]+ \d{1,2}, \d{4})\*\*'
    match = re.search(date_pattern, content)
    if match:
        date = match.group(1)
    
    return title, date


def convert_markdown_to_html(md_file):
    """Convert a single markdown file to HTML."""
    print(f"Processing {md_file.name}...")
    
    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract metadata
    title, date = extract_metadata(md_content)
    
    if not title:
        print(f"  Warning: No title found in {md_file.name}, using filename")
        title = md_file.stem.replace('-', ' ').title()
    
    if not date:
        print(f"  Warning: No date found in {md_file.name}, using current date")
        date = datetime.now().strftime("%B %d, %Y")
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'fenced_code'])
    html_content = md.convert(md_content)
    
    # Remove the title from content (it's in the header)
    html_content = re.sub(r'<h1>.*?</h1>', '', html_content, count=1)
    # Remove the date line
    html_content = re.sub(r'<p><strong>[A-Za-z]+ \d{1,2}, \d{4}</strong></p>', '', html_content, count=1)
    
    # Create description from first paragraph
    description_match = re.search(r'<p>(.*?)</p>', html_content)
    description = description_match.group(1) if description_match else title
    # Strip HTML tags from description
    description = re.sub(r'<[^>]+>', '', description)[:160]
    
    # Generate output filename
    output_file = OUTPUT_DIR / f"{md_file.stem.replace('2025-12-13-', '')}.html"
    
    # Fill template
    html_output = BLOG_TEMPLATE.format(
        title=title,
        date=date,
        description=description,
        content=html_content
    )
    
    # Write output
    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"  ✓ Created {output_file}")
    
    return {
        'title': title,
        'date': date,
        'filename': output_file.name,
        'excerpt': description
    }


def build_blog_index(posts):
    """Update blog/index.html with list of all posts."""
    print("\nUpdating blog index...")
    
    # Sort posts by date (newest first)
    # This is a simple sort, you might want to parse dates properly
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate blog items HTML
    blog_items = []
    for post in posts:
        item = f"""      <li class="blog-item">
        <h2 class="blog-title">
          <a href="/blog/{post['filename']}">{post['title']}</a>
        </h2>
        <p class="blog-meta">{post['date']}</p>
        <p class="blog-excerpt">
          {post['excerpt']}
        </p>
      </li>"""
        blog_items.append(item)
    
    blog_items_html = '\n\n'.join(blog_items)
    
    # Read current blog/index.html
    blog_html_path = Path("blog/index.html")
    if blog_html_path.exists():
        with open(blog_html_path, 'r', encoding='utf-8') as f:
            blog_html = f.read()
        
        # Replace the blog list section
        # Find the <ul class="blog-list"> section and replace its contents
        pattern = r'(<ul class="blog-list">)(.*?)(</ul>)'
        replacement = f'\\1\n{blog_items_html}\n      \\3'
        blog_html = re.sub(pattern, replacement, blog_html, flags=re.DOTALL)
        
        # Write updated blog/index.html
        with open(blog_html_path, 'w', encoding='utf-8') as f:
            f.write(blog_html)
        
        print(f"  ✓ Updated {blog_html_path}")


def main():
    """Main build function."""
    print("Building static site...\n")
    
    # Check if content directory exists
    if not CONTENT_DIR.exists():
        print(f"Error: Content directory {CONTENT_DIR} does not exist")
        print("Creating it now...")
        CONTENT_DIR.mkdir(parents=True, exist_ok=True)
        print("Add markdown files to content/blog/ and run this script again.")
        return
    
    # Find all markdown files
    md_files = list(CONTENT_DIR.glob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {CONTENT_DIR}")
        print("Add some .md files and run this script again.")
        return
    
    print(f"Found {len(md_files)} markdown file(s)\n")
    
    # Convert all markdown files
    posts = []
    for md_file in md_files:
        post_info = convert_markdown_to_html(md_file)
        posts.append(post_info)
    
    # Update blog index
    build_blog_index(posts)
    
    print("\n✓ Build complete!")
    print(f"\nGenerated {len(posts)} blog post(s)")
    print("Open index.html in your browser to view the site.")


if __name__ == "__main__":
    main()
