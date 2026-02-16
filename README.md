
[![pages-build-deploy-jekyll](https://github.com/ICS-Security-Switzerland/web_icssec.ch/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/ICS-Security-Switzerland/web_icssec.ch/actions/workflows/jekyll-gh-pages.yml)


# ICS Security Switzerland Website

Official website of **[ICS Security Switzerland](https://www.icssec.ch/)** — built with **Jekyll** and hosted on **GitHub Pages** - [www.icssec.ch](https://www.icssec.ch/)

This project supports both:
- 🧩 Local development on macOS / Linux / Windows  
- 💻 GitHub Codespaces (preconfigured container environment)

---

## 🚀 Quick Start (GitHub Codespaces)

1. **Open the repository** in GitHub Codespaces  
   → GitHub will automatically create a preconfigured environment with Ruby and Bundler installed.

2. Wait for initialization to complete  
   *(the `postCreateCommand` runs `bundle install` automatically)*

3. Start the local preview server:
   ```bash
   npm run dev
   ```
   or directly:
   ```bash
   bundle exec jekyll serve --host 0.0.0.0 --livereload --port 4000
   ```

4. Open the **forwarded port (4000)** in your browser preview:  
   ```
   http://localhost:4000
   ```

---

## 💻 Local Development (manual setup)

If you prefer to run the site locally without Codespaces:

### 1. Install Ruby and Bundler
You’ll need:
- Ruby ≥ 3.0
- Bundler ≥ 2.4

Example (macOS):
```bash
brew install ruby
gem install bundler
```

### 2. Install dependencies
```bash
bundle install
```

### 3. Run local Jekyll server
```bash
bundle exec jekyll serve --host 0.0.0.0 --livereload --port 4000
```

Your site is now available at:
```
http://localhost:4000
```

---

## 📁 Project Structure

```
.
├── _config.yml          # Site configuration (title, URL, plugins)
├── _layouts/            # Page templates (default, home, page)
├── _includes/           # Header, navigation, footer
├── assets/
│   ├── main.scss        # Complete custom stylesheet (CSS variables, responsive)
│   └── images/          # Logo and other images
├── index.md             # English homepage
├── about.md             # English about page
├── events.md            # English events page
├── members.md           # English membership page
├── contacts.md          # English contact page
├── de/                  # German translations
├── fr/                  # French translations
├── it/                  # Italian translations
├── Gemfile              # Ruby gem dependencies (GitHub Pages)
├── package.json         # NPM scripts for convenience
└── .devcontainer/       # GitHub Codespaces configuration
```

---

## 🔄 Deployment (GitHub Pages)

The site is automatically built and deployed via GitHub Actions:

- Triggered on every push to the `main` branch  
- Uses the official [jekyll-build-pages](https://github.com/actions/jekyll-build-pages) GitHub Action  
- Deployment result:  
  ```
  https://www.icssec.ch
  ```

To check build status:
1. Go to your repository → **Actions** tab  
2. Select workflow: `pages-build-deploy-jekyll`  
3. Verify that all steps are ✅ successful

---

## 🧠 Developer Tips

| Action | Command |
|--------|----------|
| Install dependencies | `bundle install` |
| Serve locally | `npm run dev` |
| Rebuild after `_config.yml` changes | Stop + restart server |
| Update RubyGems (optional) | `gem update --system` |
| Check Jekyll version | `bundle exec jekyll -v` |

---

## ⚙️ Environment Notes

- No need to install `jekyll` manually.  
  It’s already included via `github-pages` Gem (ensures version parity with GitHub Pages).
- `.gitignore` excludes `_site/` and `vendor/` folders to keep the repo clean.
- Codespaces automatically exposes port `4000` for preview.

---

## 👥 Contributions

Contributions and pull requests are welcome!