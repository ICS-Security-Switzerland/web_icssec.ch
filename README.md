[![pages-build-deploy-jekyll](https://github.com/ICS-Security-Switzerland/web_icssec.ch/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/ICS-Security-Switzerland/web_icssec.ch/actions/workflows/jekyll-gh-pages.yml)

# ICS Security Switzerland Website

Official website of [ICS Security Switzerland](https://www.icssec.ch/), built with Jekyll and hosted on GitHub Pages.

## Workflow Philosophy

This repository is content-first and CI-first:

- Edit content and templates locally.
- Let GitHub Actions validate and build on pull requests.
- Deploy only from `main`.

Local Ruby is optional for day-to-day content work.

## Preview

### With Docker (no local Ruby needed)

Builds with the exact same image GitHub Actions uses, so what you see is what
gets deployed:

```bash
docker run --rm --platform linux/amd64 -v "$PWD":/site -e GITHUB_WORKSPACE=/site -e INPUT_SOURCE=./ -e INPUT_DESTINATION=./_site ghcr.io/actions/jekyll-build-pages:latest
```

Then serve the result and open <http://localhost:4173>:

```bash
python3 -m http.server 4173 --directory _site
```

### With local Ruby (Codespaces / devcontainer)

Requires a Ruby that can install the `github-pages` gem plus the Bundler version
pinned in `Gemfile.lock`. The devcontainer provides this; macOS system Ruby does not.

```bash
npm run preview
```

Then open port `4000`.

## Scripts

```bash
npm run dev        # alias for preview
npm run preview    # bundle install (if needed) + jekyll serve --livereload on :4000
npm run check:full # install/check Ruby dependencies without serving
npm run clean      # remove _site, .jekyll-cache, vendor, .ruby-lsp
```

## CI/CD

Workflow file: `.github/workflows/jekyll-gh-pages.yml`

- Pull requests to `main`: build validation only (no deploy).
- Pushes to `main`: build and deploy to GitHub Pages.

Site URL: https://www.icssec.ch

## Notes

- Jekyll dependencies are declared through `github-pages` in `Gemfile` for Pages parity.
  The deploy workflow does **not** use this Gemfile — `actions/jekyll-build-pages` ships its
  own pinned bundle (currently Jekyll 3.10). The Gemfile only governs local previews.
- Ruby LSP is disabled by default in this workspace. Opt in by setting `rubyLsp.enabled` to `true` in `.vscode/settings.json` when needed.