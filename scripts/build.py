"""Generate the SEO-friendly static home page (index.html), sitemap.xml and robots.txt
from curriculum/curriculum.json.

Usage:
    python3 scripts/build.py           # write files
    python3 scripts/build.py --check   # exit 1 if the files are out of date (used by CI)
"""
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://espinovah.github.io/zero-french/"
REPO_URL = "https://github.com/espiNovah/zero-french"

TITLE = "Zéro French: Free Curriculum to Pass the TCF Canada"
DESCRIPTION = (
    "Learn French for free, from zero to TCF Canada success. "
    "Grammar, vocabulary, listening and speaking practice, with a real-world project every few lessons."
)
H1 = "Learn French, from zero to TCF Canada"
LEAD = (
    "Zéro French is a free, open-source curriculum for passing the TCF Canada. "
    "Written lessons, the best free resources on the internet, and a practice project "
    "every few lessons to build real fluency."
)

FAQ = [
    ("Is Zéro French really free?",
     "Yes. Every lesson is free, and every linked resource is free to use. The only optional cost is a few dollars for premium practice tools, but free alternatives exist for everything."),
    ("Do I need any French experience to start?",
     "No. The A1 Basics path starts from zero: the French alphabet, pronunciation, greetings and basic sentence structure. If you already have some French, use the placement guide to find your level."),
    ("How long does it take to finish?",
     "The full curriculum covers roughly 600 hours of study, about 10 to 14 months at 10 to 15 hours a week. Your pace will depend on your starting level and the NCLC score you need."),
    ("What is the TCF Canada?",
     "The Test de connaissance du français pour le Canada is an official French proficiency test accepted by IRCC for Canadian immigration (Express Entry, PNP, citizenship). It tests listening, reading, writing and speaking."),
    ("How is Zéro French different from a course or an app?",
     "It follows the method of The Odin Project: one ordered path, written lessons that link the best free material instead of recording new lectures, and a practice project every few lessons that builds real-world skills."),
]

WHO = [
    ("Express Entry applicants", "Need NCLC 7+ in French to maximise CRS points for permanent residency."),
    ("PNP candidates", "Many Provincial Nominee Programs award extra points or require a minimum French level."),
    ("Citizenship applicants", "Need to demonstrate adequate French (or English) proficiency for Canadian citizenship."),
    ("Complete beginners", "The A1 path starts from zero — no prior French knowledge required."),
]

e = html.escape


def lesson_count(path):
    lessons = [l for s in path["sections"] for l in s["lessons"]]
    return len(lessons), sum(1 for l in lessons if l.get("project"))


def json_ld(manifest):
    provider = {"@type": "Organization", "name": "Zéro French", "url": SITE_URL, "sameAs": [REPO_URL]}
    graph = [
        {"@type": "WebSite", "@id": SITE_URL + "#website", "url": SITE_URL, "name": "Zéro French",
         "description": DESCRIPTION, "inLanguage": "en"},
        {"@type": "Course", "@id": SITE_URL + "#course", "name": "Zéro French", "url": SITE_URL,
         "description": LEAD, "provider": provider, "isAccessibleForFree": True,
         "inLanguage": "en", "educationalLevel": "Beginner",
         "teaches": ["French grammar", "French vocabulary", "TCF Canada preparation",
                     "Listening comprehension", "Reading comprehension",
                     "Written expression", "Oral expression", "Québec French"],
         "hasPart": [{"@type": "Course", "name": p["title"], "description": p["description"],
                      "provider": provider, "isAccessibleForFree": True} for p in manifest["paths"]]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def render_index(manifest):
    path_items = []
    for i, p in enumerate(manifest["paths"], start=1):
        total, projects = lesson_count(p)
        tag = ' <span class="tag optional">Elective</span>' if p.get("optional") else ""
        path_items.append(f"""        <li><a class="path-card" href="#/paths/{p['id']}" data-path="{p['id']}">
          <span class="num">{i:02d}</span>
          <div><h3>{e(p['title'])}{tag}</h3><p>{e(p['description'])}</p></div>
          <div class="meta"><span>{total} lessons · {projects} projects</span><div class="progress"><i></i></div></div>
        </a></li>""")
    who = "\n".join(f'        <li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in WHO)
    faq = "\n".join(f'        <details class="faq-item"><summary><h3>{e(q)}</h3></summary><p>{e(a)}</p></details>' for q, a in FAQ)
    first = manifest["paths"][0]
    total_lessons = sum(lesson_count(p)[0] for p in manifest["paths"])
    total_projects = sum(lesson_count(p)[1] for p in manifest["paths"])

    return f"""<!doctype html>
<!-- Generated by scripts/build.py from curriculum/curriculum.json. Edit the script, not this file. -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(TITLE)}</title>
  <meta name="description" content="{e(DESCRIPTION)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{SITE_URL}">
  <meta name="theme-color" content="#3056D3">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Zéro French">
  <meta property="og:title" content="{e(TITLE)}">
  <meta property="og:description" content="{e(DESCRIPTION)}">
  <meta property="og:url" content="{SITE_URL}">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{e(TITLE)}">
  <meta name="twitter:description" content="{e(DESCRIPTION)}">
  <script type="application/ld+json">
{json_ld(manifest)}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..900&family=JetBrains+Mono:wght@400;700&family=Public+Sans:ital,wght@0,400..800;1,400..800&display=swap">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css" media="(prefers-color-scheme: light)">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css" media="(prefers-color-scheme: dark)">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="topbar">
    <div class="container topbar-inner">
      <a class="brand" href="#/">Zéro French</a>
      <nav class="topnav" aria-label="Main">
        <a href="#/about" data-nav="about">About</a>
        <a href="#/tcf" data-nav="tcf">TCF Guide</a>
        <a href="{REPO_URL}" target="_blank" rel="noopener">GitHub</a>
      </nav>
    </div>
  </header>

  <main id="main" class="container" tabindex="-1">
    <div id="home">
      <section class="hero">
        <div class="eyebrow">Free · Open source · Project-based</div>
        <h1>{e(H1)}</h1>
        <p class="lead">{e(LEAD)}</p>
        <div class="actions">
          <a class="btn" href="#/paths/{first['id']}">Start with {e(first['title'])}</a>
          <a class="btn secondary" href="#/about">How it works</a>
        </div>
        <p class="hero-stats">{len(manifest['paths'])} paths · {total_lessons} lessons · {total_projects} practice projects</p>
      </section>

      <section aria-labelledby="paths-title">
        <h2 class="section-title" id="paths-title">The curriculum</h2>
        <ol class="paths">
{chr(10).join(path_items)}
        </ol>
      </section>

      <section class="home-block" aria-labelledby="who-title">
        <h2 class="section-title" id="who-title">Who it's for</h2>
        <ul class="who">
{who}
        </ul>
      </section>

      <section class="home-block home-faq" aria-labelledby="faq-title">
        <h2 class="section-title" id="faq-title">Frequently asked questions</h2>
        <div class="faq">
{faq}
        </div>
      </section>
    </div>
  </main>

  <footer class="footer">
    <div class="container">
      Zéro French is free and open source, inspired by <a href="https://www.theodinproject.com/" target="_blank" rel="noopener">The Odin Project</a> (not affiliated).
      Found a broken link or a better resource? <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">Contribute on GitHub</a>.
    </div>
  </footer>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.1.6/purify.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" defer></script>
  <script src="assets/js/app.js" defer></script>
</body>
</html>
"""


def render_sitemap():
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{SITE_URL}</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
</urlset>
"""


def render_robots():
    return f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n"


def main():
    manifest = json.loads((ROOT / "curriculum" / "curriculum.json").read_text(encoding="utf-8"))
    outputs = {
        ROOT / "index.html": render_index(manifest),
        ROOT / "sitemap.xml": render_sitemap(),
        ROOT / "robots.txt": render_robots(),
    }
    if "--check" in sys.argv:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            print("Out of date (run python3 scripts/build.py):", ", ".join(stale))
            sys.exit(1)
        print("Generated files are up to date.")
        return
    for p, text in outputs.items():
        p.write_text(text, encoding="utf-8")
        print("wrote", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
