# evie-smp-art-test

Static image host for the **Evie SMP** Minecraft mod, served via GitHub Pages.

---

## 🌐 Live URL

```
https://captaincooky.github.io/evie-smp-art-test/
```

---

## 📁 Folder Structure

```
evie-smp-art-test/
├── index.html              ← Gallery page (required to enable GitHub Pages)
└── images/
    ├── fanart/             ← Fan-submitted art
    ├── players/            ← Player portraits / skins
    └── events/             ← Event / season artwork
```

---

## 🖼️ How to Add an Image

1. Place your PNG or JPG file in the appropriate folder, e.g.:
   ```
   images/fanart/my-artwork-01.png
   ```

2. Commit and push to the `main` branch.

3. Your image will be live at:
   ```
   https://captaincooky.github.io/evie-smp-art-test/images/fanart/my-artwork-01.png
   ```

4. *(Optional)* Add a `<div class="card">` entry in `index.html` so it appears in the gallery.

---

## 📝 File Naming Conventions

| ✅ Good | ❌ Avoid |
|---|---|
| `test-art-01.png` | `Test Art 01.png` |
| `player-steve.jpg` | `PlayerSteve.jpg` |
| `event-season-2.png` | `Event Season 2.PNG` |

- Use **lowercase** letters only
- Use **hyphens** (`-`) instead of spaces or underscores
- Use `.png` or `.jpg` extensions (lowercase)
- Keep filenames short to stay within Minecraft URL character limits

---

## ⚠️ Constraints

| Constraint | Detail |
|---|---|
| **File size** | Keep images under **1 MB** each (GitHub Pages has a 1 GB total soft limit) |
| **Formats** | `.png` and `.jpg` only (mod requirement) |
| **Caching** | GitHub Pages caches aggressively — use a new filename when replacing an image |
| **Repo size** | Keep total repo size under **1 GB** |
| **URL length** | Keep filenames short; Minecraft chat has a 256-character limit |
| **Branch** | Always push images to the `main` branch |

---

## ⚙️ GitHub Pages Setup

GitHub Pages must be configured to deploy from:
- **Branch:** `main`
- **Folder:** `/ (root)`

This is set in **Settings → Pages** of this repository.
