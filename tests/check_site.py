#!/usr/bin/env python3
"""Dependency-free checks for the built SAATHI site. Run: python3 tests/check_site.py"""
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXTERNAL = re.compile(r"^(https?:|tel:|mailto:|//|data:|javascript:)", re.I)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()
        self.title = False
        self.title_text = ""
        self.lang = None
        self.h1 = 0
        self.quick_exit = False
        self.imgs_no_alt = 0
        self.controls = []  # (tag, attrs)
        self.labels_for, self.in_label, self.label_wrapped = set(), 0, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self.title = True
        elif tag == "h1":
            self.h1 += 1
        elif tag == "img" and a.get("alt") is None:
            self.imgs_no_alt += 1
        elif tag == "label":
            self.in_label += 1
            if a.get("for"):
                self.labels_for.add(a["for"])
        elif tag in ("input", "select", "textarea"):
            if tag == "input" and (a.get("type") or "text").lower() in ("hidden", "submit", "button", "reset", "image"):
                pass
            else:
                self.controls.append((a, self.in_label > 0))
        if tag == "a" and ("data-quick-exit" in a or "quick-exit" in (a.get("class") or "")):
            self.quick_exit = True
        for k in ("href", "src"):
            if k in a and a[k] is not None and tag != "base":
                self.links.append(a[k])

    def handle_endtag(self, tag):
        if tag == "title":
            self.title = False
        elif tag == "label" and self.in_label:
            self.in_label -= 1

    def handle_data(self, data):
        if self.title:
            self.title_text += data


def main():
    files = sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)
    parsed, errors = {}, []
    for f in files:
        text = f.read_text(encoding="utf-8")
        p = Page()
        p.feed(text)
        parsed[f] = (p, text)
    for f, (p, text) in parsed.items():
        rel = f.relative_to(ROOT)

        def bad(msg):
            errors.append(f"{rel}: {msg}")

        if not p.title_text.strip():
            bad("missing <title>")
        if not p.lang:
            bad("missing html lang")
        if p.h1 != 1:
            bad(f"expected exactly one h1, found {p.h1}")
        if not p.quick_exit:
            bad("no quick-exit link")
        if "{root}" in text or "{{" in text:
            bad("unformatted {root} or {{ in output")
        if p.imgs_no_alt:
            bad(f"{p.imgs_no_alt} <img> without alt")
        for a, wrapped in p.controls:
            if not (wrapped or a.get("aria-label") or a.get("aria-labelledby") or (a.get("id") and a["id"] in p.labels_for)):
                bad(f"unlabelled form control ({a.get('name') or a.get('id') or a.get('type') or 'field'})")
        for ref in p.links:
            ref = ref.strip()
            if not ref or EXTERNAL.match(ref) or ref == "#" or ref.startswith("{"):
                continue
            path, _, frag = ref.partition("#")
            path = unquote(path.split("?")[0])
            if not path:
                target = f
            else:
                target = (f.parent / path).resolve()
                if path.startswith("/"):
                    target = (ROOT / path.lstrip("/")).resolve()
                if target.is_dir():
                    target = target / "index.html"
            if not target.exists():
                bad(f"broken link {ref}")
                continue
            if frag and target.suffix == ".html":
                tp = parsed.get(target)
                if tp is None:
                    q = Page()
                    q.feed(target.read_text(encoding="utf-8"))
                    tp = (q, "")
                if frag not in tp[0].ids:
                    bad(f"missing anchor in {ref}")
    print(f"Checked {len(files)} HTML pages.")
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
