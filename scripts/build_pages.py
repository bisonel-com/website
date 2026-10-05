#!/usr/bin/env python3
"""Assemble static multipage HTML. Run from repo root: python3 scripts/build_pages.py"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "home": {
        "dir": "",
        "file": "index.html",
        "title": "Bisonel Limited | Software consulting, fractional CTO, and AI",
        "description": "Bisonel Limited provides software consulting, fractional CTO leadership, and AI architecture, product, and delivery. Registered in the United Kingdom and Nigeria.",
        "canonical": "https://bisonel-com.github.io/website/",
        "nav": "home",
        "depth": 0,
    },
    "services": {
        "dir": "services",
        "file": "index.html",
        "title": "Services | Bisonel Limited",
        "description": "Software consulting, fractional CTO, and AI architecture, product, and delivery from Bisonel Limited.",
        "canonical": "https://bisonel-com.github.io/website/services/",
        "nav": "services",
        "depth": 1,
    },
    "clients": {
        "dir": "clients",
        "file": "index.html",
        "title": "Clients | Bisonel Limited",
        "description": "Companies Bisonel works with across software development consulting, product advisory, and CTO leadership.",
        "canonical": "https://bisonel-com.github.io/website/clients/",
        "nav": "clients",
        "depth": 1,
    },
    "incubation": {
        "dir": "incubation",
        "file": "index.html",
        "title": "Incubation | Bisonel Limited",
        "description": "Products from the Bisonel lab: DiniPro, Prepleau, and Naixien.",
        "canonical": "https://bisonel-com.github.io/website/incubation/",
        "nav": "incubation",
        "depth": 1,
    },
    "about": {
        "dir": "about",
        "file": "index.html",
        "title": "About | Bisonel Limited",
        "description": "Bisonel Limited is an IT consultancy registered in the United Kingdom and Nigeria.",
        "canonical": "https://bisonel-com.github.io/website/about/",
        "nav": "about",
        "depth": 1,
    },
    "contact": {
        "dir": "contact",
        "file": "index.html",
        "title": "Contact | Bisonel Limited",
        "description": "Contact Bisonel Limited at hello@bisonel.com.",
        "canonical": "https://bisonel-com.github.io/website/contact/",
        "nav": "contact",
        "depth": 1,
    },
}


def prefix(depth: int) -> str:
    return "" if depth == 0 else "../" * depth


def nav_html(p: str, active: str) -> str:
    items = [
        ("services/", "Services", "services"),
        ("clients/", "Clients", "clients"),
        ("incubation/", "Incubation", "incubation"),
        ("about/", "About", "about"),
        ("contact/", "Contact", "contact"),
    ]
    links = []
    for href, label, key in items:
        current = ' aria-current="page"' if key == active else ""
        cls = ' class="nav-cta"' if key == "contact" else ""
        links.append(f'<a href="{p}{href}"{cls}{current}>{label}</a>')
    return "\n        ".join(links)


def header_footer(p: str, active: str) -> tuple[str, str]:
    header = f"""  <header class="site-header" data-header>
    <div class="shell header-inner">
      <a class="brand" href="{p}" aria-label="Bisonel Limited home">
        <img class="brand-logo" src="{p}assets/logo.png" width="200" height="37" alt="Bisonel">
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle>
        <span class="sr-only">Menu</span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </button>
      <nav id="site-nav" class="site-nav" data-nav aria-label="Primary">
        {nav_html(p, active)}
      </nav>
    </div>
  </header>"""

    footer = f"""  <footer class="site-footer">
    <div class="shell footer-inner">
      <p>Bisonel Limited · Company number 14557664 (UK) · Registered in the United Kingdom and Nigeria</p>
      <p class="footer-email"><a href="mailto:hello@bisonel.com">hello@bisonel.com</a></p>
    </div>
  </footer>"""
    return header, footer


def page_shell(meta: dict, body: str) -> str:
    p = prefix(meta["depth"])
    header, footer = header_footer(p, meta["nav"])
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["description"]}">
  <meta name="theme-color" content="#F7F9FC">
  <link rel="canonical" href="{meta["canonical"]}">
  <link rel="icon" href="{p}assets/favicon.png" type="image/png" sizes="any">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Syne:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}css/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

{header}

  <main id="main">
{body}
  </main>

{footer}

  <script src="{p}js/main.js" defer></script>
</body>
</html>
"""


HOME_BODY = """    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-atmosphere" aria-hidden="true">
        <div class="hero-grid"></div>
        <div class="hero-glow"></div>
      </div>
      <div class="shell hero-layout">
        <div class="hero-copy">
          <p class="hero-brand-label">Bisonel Limited</p>
          <h1 id="hero-title" class="hero-title">Technical leadership for companies that need clarity, not headcount.</h1>
          <p class="hero-lede">Software consulting, fractional CTO, and AI architecture, product, and delivery for founders and operators who want experienced judgment without a full-time hire.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="contact/">Start a conversation</a>
            <a class="btn btn-ghost" href="services/">Explore services</a>
          </div>
        </div>
        <div class="hero-visual" aria-hidden="true">
          <svg class="system-map" viewBox="0 0 520 520" role="img" focusable="false">
            <defs>
              <linearGradient id="nodeFill" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#2B8FD0"/>
                <stop offset="100%" stop-color="#0870A8"/>
              </linearGradient>
              <linearGradient id="ringStroke" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0870A8" stop-opacity="0.12"/>
                <stop offset="50%" stop-color="#0870A8" stop-opacity="0.45"/>
                <stop offset="100%" stop-color="#0870A8" stop-opacity="0.12"/>
              </linearGradient>
            </defs>
            <circle class="orbit orbit-a" cx="260" cy="260" r="196" fill="none" stroke="url(#ringStroke)" stroke-width="1.25"/>
            <circle class="orbit orbit-b" cx="260" cy="260" r="138" fill="none" stroke="rgba(8,112,168,0.2)" stroke-width="1" stroke-dasharray="4 10"/>
            <circle class="orbit orbit-c" cx="260" cy="260" r="78" fill="none" stroke="rgba(8,112,168,0.28)" stroke-width="1"/>
            <g class="links" stroke="rgba(8,112,168,0.32)" stroke-width="1.25">
              <line x1="260" y1="260" x2="260" y2="64"/>
              <line x1="260" y1="260" x2="430" y2="162"/>
              <line x1="260" y1="260" x2="430" y2="358"/>
              <line x1="260" y1="260" x2="260" y2="456"/>
              <line x1="260" y1="260" x2="90" y2="358"/>
              <line x1="260" y1="260" x2="90" y2="162"/>
            </g>
            <circle class="core" cx="260" cy="260" r="28" fill="url(#nodeFill)"/>
            <g class="nodes" fill="#F7F9FC" stroke="#0870A8" stroke-width="1.5">
              <circle cx="260" cy="64" r="10"/>
              <circle cx="430" cy="162" r="10"/>
              <circle cx="430" cy="358" r="10"/>
              <circle cx="260" cy="456" r="10"/>
              <circle cx="90" cy="358" r="10"/>
              <circle cx="90" cy="162" r="10"/>
            </g>
            <g class="labels" fill="#3A4D63" font-family="Source Sans 3, sans-serif" font-size="13" text-anchor="middle">
              <text x="260" y="42">Architecture</text>
              <text x="468" y="166">Delivery</text>
              <text x="468" y="362">Product</text>
              <text x="260" y="488">AI systems</text>
              <text x="52" y="362">Advisory</text>
              <text x="52" y="166">CTO</text>
            </g>
          </svg>
        </div>
      </div>
    </section>

    <section class="section section-home-preview" aria-labelledby="home-promise-title">
      <div class="shell">
        <div class="section-intro">
          <p class="eyebrow">What we do</p>
          <h2 id="home-promise-title">Consulting, fractional CTO, and AI in one practice</h2>
          <p class="section-lede">One clear engagement model for founders and operators who need technical leadership across architecture, delivery, and AI.</p>
        </div>
        <ul class="preview-list">
          <li>
            <a class="preview-link" href="services/">
              <span class="preview-name">Services</span>
              <span class="preview-copy">Software consulting, fractional CTO, and AI architecture, product, and delivery.</span>
              <span class="preview-arrow" aria-hidden="true">→</span>
            </a>
          </li>
          <li>
            <a class="preview-link" href="clients/">
              <span class="preview-name">Clients</span>
              <span class="preview-copy">Named partnerships across software development consulting and CTO work.</span>
              <span class="preview-arrow" aria-hidden="true">→</span>
            </a>
          </li>
          <li>
            <a class="preview-link" href="incubation/">
              <span class="preview-name">Incubation</span>
              <span class="preview-copy">Products from the Bisonel lab, including DiniPro, Prepleau, and Naixien.</span>
              <span class="preview-arrow" aria-hidden="true">→</span>
            </a>
          </li>
        </ul>
      </div>
    </section>
"""

SERVICES_BODY = """    <section class="page-hero">
      <div class="shell">
        <p class="eyebrow">Services</p>
        <h1>Three ways we lead technical work</h1>
        <p class="page-lede">Outcome-led engagement for teams that need clear judgment across architecture, delivery, and AI.</p>
      </div>
    </section>

    <section class="section section-services">
      <div class="shell">
        <div class="service-list">
          <article class="service-block">
            <p class="service-index">01</p>
            <h2>Software consulting</h2>
            <p>Architecture, delivery, and product advisory for teams building or modernising software. We help you choose the right shape of system, sequence the work, and keep delivery honest.</p>
          </article>
          <article class="service-block">
            <p class="service-index">02</p>
            <h2>Fractional CTO</h2>
            <p>Part-time technical leadership for growing companies. Strategy, hiring signals, roadmap pressure-testing, and calm ownership of the technology agenda without a full-time executive hire.</p>
          </article>
          <article class="service-block">
            <p class="service-index">03</p>
            <h2>AI</h2>
            <p>AI as a first-class part of consulting and CTO work: systems architecture, product decisions, and delivery that turn models and tooling into reliable capability inside your organisation.</p>
          </article>
        </div>
        <p class="section-cta"><a class="btn btn-primary" href="../contact/">Talk about an engagement</a></p>
      </div>
    </section>
"""

CLIENTS_BODY = """    <section class="page-hero page-hero-dark">
      <div class="shell">
        <p class="eyebrow">Clients</p>
        <h1>Companies we work with</h1>
        <p class="page-lede">Named engagements across software development consulting, product advisory, and CTO leadership.</p>
      </div>
    </section>

    <section class="section section-clients">
      <div class="shell">
        <ul class="client-list">
          <li>
            <a class="client-link" href="https://afrimash.com" target="_blank" rel="noopener noreferrer">
              <span class="client-name">Afrimash</span>
              <span class="client-role">Software development consulting</span>
            </a>
          </li>
          <li>
            <a class="client-link" href="https://ichota.co" target="_blank" rel="noopener noreferrer">
              <span class="client-name">Ichota</span>
              <span class="client-role">Software and product advisory</span>
            </a>
          </li>
          <li>
            <a class="client-link" href="https://kodobe.com" target="_blank" rel="noopener noreferrer">
              <span class="client-name">Kodobe</span>
              <span class="client-role">Software advisory</span>
            </a>
          </li>
          <li>
            <a class="client-link" href="https://asosconsulting.com" target="_blank" rel="noopener noreferrer">
              <span class="client-name">ASOS Consulting</span>
              <span class="client-role">CTO and software development consulting</span>
            </a>
          </li>
        </ul>
      </div>
    </section>
"""

INCUBATION_BODY = """    <section class="page-hero">
      <div class="shell">
        <p class="eyebrow">Incubation</p>
        <h1>Products from the Bisonel lab</h1>
        <p class="page-lede">Ventures incubated under Bisonel, spanning professional tools and opportunity networks.</p>
      </div>
    </section>

    <section class="section section-incubation">
      <div class="shell">
        <ul class="incubate-list">
          <li>
            <a class="incubate-link" href="https://dinipro.com/" target="_blank" rel="noopener noreferrer">
              <span class="incubate-name">DiniPro</span>
              <span class="incubate-arrow" aria-hidden="true">→</span>
            </a>
          </li>
          <li>
            <a class="incubate-link" href="https://prepleau.com/" target="_blank" rel="noopener noreferrer">
              <span class="incubate-name">Prepleau</span>
              <span class="incubate-arrow" aria-hidden="true">→</span>
            </a>
          </li>
          <li>
            <a class="incubate-link" href="https://naixien.com" target="_blank" rel="noopener noreferrer">
              <span class="incubate-name">Naixien</span>
              <span class="incubate-note">The African Business Opportunity Network</span>
              <span class="incubate-arrow" aria-hidden="true">→</span>
            </a>
          </li>
        </ul>
      </div>
    </section>
"""

ABOUT_BODY = """    <section class="page-hero">
      <div class="shell">
        <p class="eyebrow">About</p>
        <h1>A consultancy built for clear technical judgment</h1>
      </div>
    </section>

    <section class="section section-about">
      <div class="shell about-layout">
        <div class="about-copy">
          <p>Bisonel Limited is an IT consultancy (SIC 62020) focused on software consulting, fractional CTO leadership, and AI systems work. We partner with founders and operators who need clear technical direction, disciplined delivery, and practical AI capability.</p>
          <p>We keep engagements lean. The goal is better decisions and stronger systems, not process theatre.</p>
          <p>Bisonel is registered in the United Kingdom and Nigeria. The UK company number is 14557664.</p>
          <dl class="about-meta">
            <div>
              <dt>Company</dt>
              <dd>Bisonel Limited</dd>
            </div>
            <div>
              <dt>UK company number</dt>
              <dd>14557664</dd>
            </div>
            <div>
              <dt>Registered in</dt>
              <dd>United Kingdom and Nigeria</dd>
            </div>
          </dl>
        </div>
      </div>
    </section>
"""

CONTACT_BODY = """    <section class="page-hero">
      <div class="shell">
        <p class="eyebrow">Contact</p>
        <h1>Tell us what you are building</h1>
        <p class="page-lede">Share the context, constraints, and what good looks like. We will respond with a clear next step.</p>
      </div>
    </section>

    <section class="section section-contact">
      <div class="shell">
        <div class="contact-panel">
          <a class="contact-email" href="mailto:hello@bisonel.com">hello@bisonel.com</a>
          <p class="contact-note">Prefer email. No forms, portals, or queues.</p>
        </div>
      </div>
    </section>
"""

BODIES = {
    "home": HOME_BODY,
    "services": SERVICES_BODY,
    "clients": CLIENTS_BODY,
    "incubation": INCUBATION_BODY,
    "about": ABOUT_BODY,
    "contact": CONTACT_BODY,
}


def main() -> None:
    for key, meta in PAGES.items():
        out_dir = ROOT / meta["dir"] if meta["dir"] else ROOT
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / meta["file"]
        html = page_shell(meta, BODIES[key])
        path.write_text(html, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
