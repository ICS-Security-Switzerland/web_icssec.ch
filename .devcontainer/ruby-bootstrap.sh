#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-install}"

bundler_version="$(awk '/^BUNDLED WITH$/{getline; gsub(/^[[:space:]]+|[[:space:]]+$/, "", $0); print; exit}' Gemfile.lock 2>/dev/null || true)"

if [[ -n "${bundler_version}" ]]; then
  if ! gem list -i bundler -v "${bundler_version}" >/dev/null 2>&1; then
    gem install bundler -v "${bundler_version}" --no-document
  fi
  bundle_cmd=(bundle "_${bundler_version}_")
else
  bundle_cmd=(bundle)
fi

case "${MODE}" in
  install)
    "${bundle_cmd[@]}" check || "${bundle_cmd[@]}" install
    ;;
  serve)
    "${bundle_cmd[@]}" check || "${bundle_cmd[@]}" install
    # Kill any stale Jekyll/LiveReload processes before starting fresh
    pkill -f "jekyll serve" 2>/dev/null || true
    sleep 1
    exec "${bundle_cmd[@]}" exec jekyll serve --livereload --host 0.0.0.0 --port 4000
    ;;
  *)
    echo "Usage: $0 [install|serve]" >&2
    exit 1
    ;;
esac
