#!/usr/bin/env python3
"""Regenerate index.html from images found in each category folder."""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
IMAGES_DIR = REPO_ROOT / "images"
INDEX_HTML = REPO_ROOT / "index.html"

CATEGORIES = [
    ("fanart",  "Fan Art",  "/images/fanart/"),
    ("players", "Players",  "/images/players/"),
    ("events",  "Events",   "/images/events/"),
]

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


def get_images(folder: Path) -> list[str]:
    if not folder.exists():
        return []
    return sorted(
        f.name
        for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() in IMAGE_EXTS
    )


def render_category(slug: str, title: str, url_prefix: str) -> str:
    images = get_images(IMAGES_DIR / slug)
    lines = [
        f'  <h2>{title} \u2014 <code>{url_prefix}</code></h2>',
        f'  <div class="gallery" id="{slug}">',
    ]
    if images:
        for name in images:
            alt = Path(name).stem
            lines.append('    <div class="card">')
            lines.append(f'      <img src="images/{slug}/{name}" alt="{alt}" />')
            lines.append(f'      <a href="images/{slug}/{name}">{name}</a>')
            lines.append('    </div>')
    else:
        lines.append('    <p class="empty-message">No images yet.</p>')
    lines.append('  </div>')
    return "\n".join(lines)


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Evie SMP Art</title>
  <style>
    body {{ font-family: sans-serif; max-width: 900px; margin: 2rem auto; padding: 0 1rem; background: #1a1a2e; color: #eee; }}
    h1 {{ color: #a78bfa; }}
    h2 {{ color: #c4b5fd; border-bottom: 1px solid #4c1d95; padding-bottom: 0.25rem; margin-top: 2rem; }}
    .gallery {{ display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem; }}
    .gallery img {{ width: 180px; height: 180px; object-fit: cover; border-radius: 6px; border: 2px solid #4c1d95; }}
    .gallery a {{ color: #a78bfa; font-size: 0.8rem; display: block; text-align: center; margin-top: 0.25rem; word-break: break-all; }}
    .card {{ text-align: center; }}
    p {{ color: #ccc; }}
    code {{ background: #2d1b69; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.9rem; }}
    .empty-message {{ color: #888; font-style: italic; }}
  </style>
</head>
<body>
  <h1>🎨 Evie SMP Art Gallery</h1>
  <p>Static image host for the Evie SMP Minecraft mod. Images are served directly via GitHub Pages.</p>
  <p>Base URL: <code>https://captaincooky.github.io/evie-smp-art-test/</code></p>

{sections}
</body>
</html>
"""


def main() -> None:
    sections = "\n\n".join(
        render_category(slug, title, url_prefix)
        for slug, title, url_prefix in CATEGORIES
    )
    html = HTML_TEMPLATE.format(sections=sections)
    INDEX_HTML.write_text(html, encoding="utf-8")
    print(f"Written {INDEX_HTML}")


if __name__ == "__main__":
    main()
