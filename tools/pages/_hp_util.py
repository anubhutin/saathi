"""Small helpers shared by home/pathways/about page modules (underscore: not built as a page)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

FALLBACK_IDS = ["breathing-for-hard-moments", "grounding-five-senses", "understanding-feelings", "difficult-days",
    "exam-pressure", "body-image", "healthy-relationships", "what-consent-means", "staying-safe-online",
    "recognising-coercive-control", "periods-and-mood", "after-the-baby", "everyday-connection",
    "body-safety-conversations", "menopause-changes", "caring-for-a-parent", "caregiver-wellbeing",
    "loneliness-later-life", "journaling-week", "the-worry-jar", "a-quiet-evening"]


def fin(raw):
    """Escape all literal braces for str.format, keeping the @R@ root token."""
    return raw.replace("{", "{{").replace("}", "}}").replace("@R@", "{root}")


def resource_title(rid):
    try:
        import content_resources as cr
        b = getattr(cr, "by_id", None)
        r = b(rid) if callable(b) else (b or {}).get(rid)
        if r is None:
            for item in getattr(cr, "RESOURCES", []):
                if item.get("id") == rid:
                    r = item
        if r:
            t = r.get("title") if isinstance(r, dict) else getattr(r, "title", None)
            if t:
                return t
    except Exception:
        pass
    return rid.replace("-", " ").capitalize()
