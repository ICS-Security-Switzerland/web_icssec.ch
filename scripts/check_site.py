#!/usr/bin/env python3
"""Checks the built site for broken internal links and anchors.

    python3 scripts/check_site.py _site

Every href/src that stays on this site must resolve to a file in the build,
and every #fragment must match an id on the target page. Also checks that no
past event still offers a way to join (a stale meeting link). Standard
library only, so CI needs nothing installed. Exit code 1 on any finding.
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote

SITE_HOSTS = {"www.icssec.ch", "icssec.ch"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()
        self.past_depth = 0      # inside <article class="event event--past ...">
        self.past_join = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        cls = (a.get("class") or "").split()
        if tag == "article" and "event--past" in cls:
            self.past_depth = 1
        elif tag == "article" and self.past_depth:
            self.past_depth += 1
        if self.past_depth and "event-link--join" in cls:
            self.past_join += 1
        for key in ("href", "src"):
            if a.get(key) and not (tag == "link" and a.get("rel") in ("alternate", "canonical")):
                self.links.append(a[key])

    def handle_endtag(self, tag):
        if tag == "article" and self.past_depth:
            self.past_depth -= 1


def target_file(root, path):
    p = root / unquote(path).lstrip("/")
    for cand in (p, p / "index.html", p.with_suffix(".html")):
        if cand.is_file():
            return cand
    return None


def main(root):
    root = Path(root)
    pages = {f: f.read_text(encoding="utf-8", errors="replace") for f in root.rglob("*.html")}
    parsed = {}
    for f, text in pages.items():
        pg = Page(); pg.feed(text); parsed[f] = pg
    problems = []
    for f, pg in parsed.items():
        url = "/" + f.relative_to(root).as_posix()
        if pg.past_join:
            problems.append(f"{url}: past event offers a join link")
        for link in pg.links:
            if link.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            parts = urlsplit(urljoin("https://www.icssec.ch" + url, link))
            if parts.netloc not in SITE_HOSTS:
                continue
            target = target_file(root, parts.path)
            if target is None:
                problems.append(f"{url}: broken link {link}")
                continue
            if parts.fragment and target.suffix == ".html":
                if parts.fragment not in parsed[target].ids:
                    problems.append(f"{url}: missing anchor {link}")
    for p in sorted(set(problems)):
        print(p)
    print(f"checked {len(parsed)} pages, {len(set(problems))} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "_site"))
