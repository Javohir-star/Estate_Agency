from pathlib import Path
import re

root = Path("c:/Users/User/Estate_Agency/templates")
html_files = list(root.rglob("*.html"))
print("Files:", len(html_files))

for path in html_files:
    text = path.read_text(encoding="utf-8")
    updated = text
    if "{% load static %}" not in updated:
        updated = re.sub(
            r"<html[^>]*>",
            lambda m: m.group(0) + "\n{% load static %}",
            updated,
            count=1,
        )
    updated = re.sub(
        r"\{\%\s*static\s*\"([^\"]*)\"\s*\%\}", r"{% static '\1' %}", updated
    )
    updated = re.sub(
        r"\{\%\s*static\s*'([^']*)'\s*\%\}",
        lambda m: "{% static '%s' %}" % m.group(1),
        updated,
    )
    updated = re.sub(
        r"\{\%\s*static\s*'(https?://[^']+)'\s*\%\}", lambda m: m.group(1), updated
    )
    updated = re.sub(
        r'\{\%\s*static\s*"(https?://[^"]+)"\s*\%\}', lambda m: m.group(1), updated
    )

    def rep_link(m):
        p = m.group(1)
        mapping = {
            "index.html": "/",
            "about.html": "/about/",
            "property-grid.html": "/property/",
            "blog-grid.html": "/blog/",
            "contact.html": "/contact/",
            "property-single.html": "/property/1/",
            "blog-single.html": "/blog/1/",
            "agents-grid.html": "/agents/",
            "agent-single.html": "/agent/1/",
        }
        return mapping.get(p, p)

    updated = re.sub(r"\{\%\s*static\s*'([^']+\.html)'\s*\%\}", rep_link, updated)
    updated = re.sub(r"\{\%\s*static\s*\"([^\"]+\.html)\"\s*\%\}", rep_link, updated)

    if updated != text:
        path.write_text(updated, encoding="utf-8")
        print("Updated", path)

print("Done")
