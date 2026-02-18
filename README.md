
# ICS Security Switzerland Website

Official website of **[ICS Security Switzerland](https://www.icssec.ch/)** — built with **Jekyll** and hosted on **Cloudflare Pages** - [www.icssec.ch](https://www.icssec.ch/)

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
├── _includes/           # Header, navigation, footer, membership form
├── assets/
│   ├── main.scss        # Complete custom stylesheet (CSS variables, responsive)
│   └── images/          # Logo and other images
├── functions/
│   └── api/
│       └── register.js  # Cloudflare Pages Function (membership → Webling)
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

## 🔄 Deployment (Cloudflare Pages)

The site is hosted on **Cloudflare Pages** with a built-in serverless function for the membership registration form.

### Initial Setup

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. Select the `ICS-Security-Switzerland/web_icssec.ch` repository
3. Configure the build:
   - **Build command:** `bundle exec jekyll build`
   - **Build output directory:** `_site`
   - **Root directory:** `/`
4. Under **Environment variables**, add:
   - `WEBLING_API_KEY` — Your API key from icssec.webling.ch → Administration → API keys
   - `WEBLING_GROUP_ID` — Numeric ID of the "Interessenten" membergroup.
     Find it via: `curl -H "apikey: YOUR_KEY" https://icssec.webling.ch/api/1/membergroup`
5. Deploy

### Custom Domain

After the first deployment, go to your Pages project → **Custom domains** → add `www.icssec.ch`.
Update your DNS to point to Cloudflare (CNAME record → `<project>.pages.dev`).

### How it works

- On every push to `main`, Cloudflare builds Jekyll and deploys the static site
- The `functions/api/register.js` file is automatically deployed as a serverless endpoint at `/api/register`
- The membership form on `/members/` submits directly to `/api/register` — no CORS, same domain

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