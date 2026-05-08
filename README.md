[![pages-build-deploy-jekyll](https://github.com/ICS-Security-Switzerland/web_icssec.ch/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/ICS-Security-Switzerland/web_icssec.ch/actions/workflows/jekyll-gh-pages.yml)

# ICS Security Switzerland Website

Official website of [ICS Security Switzerland](https://www.icssec.ch/), built with Jekyll and hosted on GitHub Pages.

## Workflow Philosophy

This repository is content-first and CI-first:

- Edit content and templates locally.
- Let GitHub Actions validate and build on pull requests.
- Deploy only from `main`.

Local Ruby is optional for day-to-day content work.

## Quick Start (Codespaces)

Fast preview (no Ruby/Jekyll processing):

```bash
npm run preview:fast
```

Then open forwarded port `4173`.

Full Jekyll preview (only when needed):

```bash
npm run preview:full
```

Then open forwarded port `4000`.

## Scripts

```bash
npm run preview:fast   # static preview for quick editing
npm run preview:full   # full Jekyll preview (installs matching Bundler when needed)
npm run check:full     # installs/checks full Ruby dependencies without serving
npm run clean          # cleanup generated/cached artifacts
```

## CI/CD

Workflow file: `.github/workflows/jekyll-gh-pages.yml`

- Pull requests to `main`: build validation only (no deploy).
- Pushes to `main`: build and deploy to GitHub Pages.

Site URL: https://www.icssec.ch

## Notes

- Jekyll dependencies are managed through `github-pages` in `Gemfile` for Pages parity.
- If you only edit markdown/content, `preview:fast` is usually enough.
- Use `preview:full` for layout/liquid/plugin-sensitive checks.
- Ruby LSP is disabled by default in this workspace. Opt in by setting `rubyLsp.enabled` to `true` in `.vscode/settings.json` when needed.