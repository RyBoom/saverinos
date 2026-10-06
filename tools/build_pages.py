#!/usr/bin/env python3
"""Generates site/index.html and site/menu.html from shared partials (header, footer, forms).

Run from anywhere:  python3 tools/build_pages.py
Edit the copy here, regenerate, and commit both the script and the two pages.
Set SITE_URL below to the deployed origin to switch on the link preview image.
"""
import json, os, random, re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site") + os.sep
ADDR = '314 West 11th Street, <span class="nw">Columbia, TN 38401</span>'
PHONE = "931-223-8335"
TEL = "tel:+19312238335"
MAPS = "https://www.google.com/maps/dir/?api=1&destination=314+West+11th+Street%2C+Columbia%2C+TN+38401"
MAP_EMBED = "https://www.google.com/maps?q=314+West+11th+Street,+Columbia,+TN+38401&output=embed"
IG = "https://www.instagram.com/savarinosmarket"
TT = "https://www.tiktok.com/@savarinosmarket"
SITE_URL = ""  # deployed origin with no trailing slash, set only at real launch on the public domain, never for a hidden preview address. It switches on og:image.

# The eight words, exactly as they sit on the sign. Order = two lines of the logo.
LINE1 = ["Catering", "Deli", "Pastas", "Sandwiches"]
LINE2 = ["Pastries", "Cookies", "Cakes", "Bread"]
MENU_ORDER = ["Sandwiches", "Deli", "Pastas", "Bread", "Pastries", "Cookies", "Cakes", "Catering"]
SLUG = {w: w.lower() for w in LINE1 + LINE2}

DN_LOG = []  # (key, text) collected for NOTES.md


def dn(key, text, inline=False):
    DN_LOG.append((key, text))
    cls = "dn dn--inline" if inline else "dn"
    tag = "span" if inline else "p"
    return f'<{tag} class="{cls}" data-dn="{key}"><b>CONFIRM WITH OWNER</b> {text}</{tag}>'


def words_list(words, cls, label, prefix="menu.html"):
    items = "".join(f'<li><a href="{prefix}#{SLUG[w]}">{w}</a></li>' for w in words)
    return f'<ul class="{cls}" aria-label="{label}">{items}</ul>'


# ---------------------------------------------------------------- shared partials
def head(title, desc, page):
    ld = ""
    if page == "home":
        data = {
            "@context": "https://schema.org",
            "@type": "Bakery",
            "name": "Savarino's Market",
            "description": "Sicilian family bakery, deli and market in Columbia, Tennessee.",
            "telephone": "+1-931-223-8335",
            "address": {"@type": "PostalAddress", "streetAddress": "314 West 11th Street", "addressLocality": "Columbia",
                        "addressRegion": "TN", "postalCode": "38401", "addressCountry": "US"},
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.7", "reviewCount": "156"},
            "openingHoursSpecification": [
                {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "15:00"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday"], "opens": "10:00", "closes": "16:00"},
                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Wednesday", "Thursday", "Friday", "Saturday"], "opens": "10:00", "closes": "17:00"},
            ],
            "sameAs": [IG, TT],
        }
        ld = f'<script type="application/ld+json">{json.dumps(data)}</script>'
    og_title = "Savarino’s Market, Columbia, Tennessee" if page == "home" else "Menu | Savarino’s Market"
    og_img = (f'<meta property="og:image" content="{SITE_URL}/assets/img/og.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="Savarino’s Market, since 2002">\n<meta name="twitter:card" content="summary_large_image">\n' if SITE_URL else "")
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#001C41">
<meta name="robots" content="noindex, nofollow, noarchive, noimageindex">
<meta name="referrer" content="no-referrer">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Savarino’s Market">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
{og_img}<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<script>document.documentElement.className=document.documentElement.className.replace("no-js","js")</script>
<link rel="preload" href="assets/fonts/abril-fatface-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
{ld}
</head>"""


def header(page):
    home = page == "home"
    prefix = "" if home else "index.html"
    cur = ' aria-current="page"'
    nav = [
        ("Menu", "menu.html", cur if page == "menu" else ""),
        ("Catering and Cakes", f"{prefix}#catering-cakes", ""),
        ("Wholesale", f"{prefix}#wholesale", ""),
        ("Visit", f"{prefix}#visit", ""),
    ]
    lis = "".join(f'<li><a href="{h}"{c}>{t}</a></li>' for t, h, c in nav)
    mobile = "".join(f'<a href="{h}"{c}>{t}</a>' for t, h, c in nav)
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="concept-bar" role="region" aria-label="Concept notice"><div class="wrap">
<p><b>Concept</b> for Carmelo Savarino<span class="long">. Designer notes mark what to confirm.</span></p>
<button type="button" data-notes-toggle>Hide designer notes</button>
</div></div>
<header class="site-header">
<div class="wrap hdr">
<div class="hdr-id">
<a class="hdr-logo" href="{'#top' if home else 'index.html'}" aria-label="Savarino's Market, home"><img src="assets/img/logo.webp" alt="Savarino's Market, since 2002" width="1535" height="630"></a>
<span class="hdr-place caps" aria-hidden="true">Sicilian bakery and deli</span>
</div>
<nav class="hdr-nav" aria-label="Primary"><ul>{lis}</ul></nav>
<a class="btn btn-teal hdr-call" href="{TEL}">Call {PHONE}</a>
<button class="hdr-toggle" type="button" aria-expanded="false" aria-controls="hdr-panel" aria-label="Site navigation"><span></span></button>
</div>
<nav class="hdr-panel" id="hdr-panel" aria-label="Primary, mobile">{mobile}<a href="{TEL}">Call {PHONE}</a></nav>
</header>"""


def dock(page):
    cur = ' aria-current="page"' if page == "menu" else ""
    return f"""<nav class="dock" aria-label="Quick actions">
<a href="{TEL}">Call</a>
<a href="{MAPS}" rel="noopener">Directions</a>
<a href="menu.html"{cur}>Menu</a>
</nav>"""


def footer():
    words = "".join(f'<li><a href="menu.html#{SLUG[w]}">{w}</a></li>' for w in LINE1 + LINE2)
    hours = [("Sunday", "10am to 3pm"), ("Monday", "10am to 4pm"), ("Tuesday", "10am to 4pm"),
             ("Wednesday", "10am to 5pm"), ("Thursday", "10am to 5pm"), ("Friday", "10am to 5pm"), ("Saturday", "10am to 5pm")]
    hrs = "".join(f'<div><dt>{d}</dt><span class="lead" aria-hidden="true"></span><dd>{t}</dd></div>' for d, t in hours)
    return f"""<footer class="site-footer" id="footer">
<div class="wrap foot">
<div class="foot-top">
<a class="foot-plate" href="index.html" aria-label="Savarino's Market, home"><img src="assets/img/logo.webp" alt="Savarino's Market, since 2002" width="1535" height="630" loading="lazy"></a>
</div>
<div class="foot-rule"><ul class="words words--foot" aria-label="Everything on the sign">{words}</ul></div>
<div class="foot-cols">
<div class="foot-visit">
<h3>Visit</h3>
<address>{ADDR}</address>
<a class="foot-phone" href="{TEL}">{PHONE}</a>
<p class="foot-since" style="margin-top:16px">Since 2002</p>
<p style="margin-top:12px;font-size:.9375rem;color:var(--ivory-on-navy)">Free street parking and a gravel lot across the street. Outdoor seating only.</p>
<div class="btn-row" style="margin-top:20px"><a class="btn btn-saffron" href="{MAPS}" rel="noopener">Get Directions</a></div>
</div>
<div>
<h3>Hours</h3>
<dl class="foot-hours" style="margin:0">{hrs}</dl>
</div>
<div>
<h3>Follow</h3>
<ul class="foot-social">
<li><a href="{IG}" rel="noopener">Instagram</a></li>
<li><a href="{TT}" rel="noopener">TikTok</a></li>
</ul>
<p class="foot-handle">@savarinosmarket on both.</p>
{dn("social", "Instagram and TikTok links are built from the handle @savarinosmarket. Check they land on the right accounts.")}
</div>
<div>
<h3>Map</h3>
<div class="foot-map">
<div class="foot-map-fallback" aria-hidden="true"><p style="margin:0;max-width:none">{ADDR}</p></div>
<iframe title="Map to Savarino's Market, 314 West 11th Street, Columbia, Tennessee" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer"></iframe>
</div>
<a class="btn btn-line-light foot-map-link" href="{MAPS}" rel="noopener">Open in Maps</a>
</div>
</div>
</div>
<div class="tile-band" role="presentation"></div>
<div class="legal"><div class="wrap"><p>Concept draft for Carmelo Savarino. Forms do not send yet. Photos are placeholders.</p></div></div>
</footer>"""


def form_catering(p):
    return f"""<form class="form" data-form="catering" novalidate aria-label="Cake, tray and catering inquiry">
<div class="f"><label for="{p}-name">Name</label><input id="{p}-name" name="name" autocomplete="name" required data-error="Tell us your name."><span class="err" aria-live="polite"></span></div>
<div class="f"><label for="{p}-phone">Phone</label><input id="{p}-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="931-555-0123" required data-error="We need a number to call you back."><span class="err" aria-live="polite"></span></div>
<div class="f-row">
<div class="f"><label for="{p}-date">Date needed (optional)</label><input id="{p}-date" name="date" type="date"><span class="err" aria-live="polite"></span></div>
<div class="f"><label for="{p}-count">Headcount (optional)</label><input id="{p}-count" name="headcount" type="number" min="1" inputmode="numeric" placeholder="12"><span class="err" aria-live="polite"></span></div>
</div>
<div class="f"><label for="{p}-need">What you need</label><textarea id="{p}-need" name="need" rows="4" placeholder="A birthday cake, two cookie trays, lunch for the office" required data-error="Tell us what you are after."></textarea><span class="err" aria-live="polite"></span></div>
<button class="btn btn-teal" type="submit">Send my request</button>
<p class="form-note">Or call <a href="{TEL}">{PHONE}</a>.</p>
<div class="form-ok" hidden><h3>Nothing sent yet.</h3><p>This is a concept form. When the site goes live, your request goes to the family. For now, call <a href="{TEL}">{PHONE}</a>.</p></div>
</form>"""


def muffuletta_photo(cls=""):
    return ('<figure class="photo %s"><img src="assets/img/muffuletta.webp" alt="A muffuletta cut in half and held in two hands: layers of sliced meat and cheese, roasted red peppers and green relish on seeded bread, with the other half in a takeout box" width="1200" height="1600" loading="lazy"></figure>') % cls


def framed(inner, cls=""):
    return f'<div class="framed {cls}"><i class="cn tl"></i><i class="cn tr"></i><i class="cn bl"></i><i class="cn br"></i>{inner}</div>'


GO = '<svg class="go" viewBox="0 0 34 16" width="34" height="16" aria-hidden="true" focusable="false"><path d="M1 8h30M25 2l6 6-6 6" fill="none" stroke="#001C41" stroke-width="2"/></svg>'


def star(i, frac):
    d = "M12 1.8l2.9 6.2 6.7.8-4.9 4.6 1.3 6.7L12 16.7 6 20.1l1.3-6.7L2.4 8.8l6.7-.8z"
    out = f'<svg viewBox="0 0 24 22" aria-hidden="true" focusable="false"><path d="{d}" fill="none" stroke="#001C41" stroke-width="1.4" stroke-linejoin="round"/>'
    if frac >= 1:
        out += f'<path d="{d}" fill="#F1B21C" stroke="#001C41" stroke-width="1.4" stroke-linejoin="round"/>'
    elif frac > 0:
        out += f'<clipPath id="sc{i}"><rect x="0" y="0" width="{24*frac:.1f}" height="22"/></clipPath><path d="{d}" fill="#F1B21C" clip-path="url(#sc{i})"/><path d="{d}" fill="none" stroke="#001C41" stroke-width="1.4" stroke-linejoin="round"/>'
    return out + "</svg>"


def parking_svg():
    """Sketch of the block, north up: West 11th Street runs east to South High Street, Parker Street
    meets it from the north, the shop sits east of Parker, the gravel lot and the CAB building are
    across the street. Placement follows a satellite view; sizes are exaggerated so labels read."""
    rnd = random.Random(7)
    dots = ""
    for _ in range(70):
        x = rnd.uniform(14, 166); y = rnd.uniform(174, 232)
        dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.choice([1,1.2,1.6]):.1f}"/>'
    bays_n = "".join(f'<rect x="{112+21*i}" y="114" width="19" height="12"/>' for i in range(5))
    bays_s = "".join(f'<rect x="{112+21*i}" y="144" width="19" height="12"/>' for i in range(5))
    f = 'font-family="Montserrat, sans-serif" font-weight="700" fill="#FDFEF8"'
    return f"""<svg viewBox="0 0 360 250" role="img" aria-labelledby="pk-t pk-d" focusable="false">
<title id="pk-t">Where to park</title>
<desc id="pk-d">Sketch, north up. Savarino's, with its porch, is on the north side of West 11th Street just east of Parker Street. Free street parking runs along the curbs. A gravel lot is across the street to the southwest, and the CAB building is across the street to the southeast. West 11th Street ends at South High Street.</desc>
<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#FDFEF8" stroke-opacity=".28" stroke-width="1.4"/></pattern></defs>
<g fill="none" stroke="#FDFEF8" stroke-width="2">
<path d="M0 112H72M102 112H316M0 158H316M72 0V112M102 0V112M316 0V250M350 0V250"/>
</g>
<path d="M232 135H306M12 135H12" stroke="#069DA3" stroke-width="2.5" stroke-dasharray="10 8" fill="none"/>
<g fill="none" stroke="#FDFEF8" stroke-opacity=".4" stroke-width="1.5"><rect x="180" y="78" width="16" height="34"/><rect x="200" y="78" width="16" height="34"/><rect x="232" y="58" width="68" height="54"/><rect x="266" y="168" width="36" height="40"/></g>
<rect x="108" y="56" width="64" height="56" fill="url(#hatch)" stroke="#FDFEF8" stroke-width="2"/>
<rect x="120" y="100" width="40" height="12" fill="#001C41" stroke="#F1B21C" stroke-width="2"/>
<circle cx="140" cy="72" r="7" fill="#F1B21C" stroke="#001C41" stroke-width="2"/>
<text x="140" y="92" text-anchor="middle" font-family="Abril Fatface, Georgia, serif" font-size="12" fill="#FDFEF8">Savarino's</text>
<g fill="none" stroke="#FDFEF8" stroke-opacity=".75" stroke-width="1.5">{bays_n}{bays_s}</g>
<rect x="190" y="168" width="66" height="58" fill="url(#hatch)" stroke="#FDFEF8" stroke-width="2"/>
<text x="223" y="192" text-anchor="middle" font-family="Abril Fatface, Georgia, serif" font-size="17" fill="#FDFEF8">CAB</text>
<text x="223" y="207" text-anchor="middle" {f} font-size="9" letter-spacing="1.2">BUILDING</text>
<rect x="8" y="168" width="164" height="70" fill="none" stroke="#069DA3" stroke-width="2.5" stroke-dasharray="7 5"/>
<g fill="#FDFEF8" fill-opacity=".6">{dots}</g>
<rect x="46" y="196" width="88" height="24" fill="#001C41"/>
<text x="90" y="212" text-anchor="middle" {f} font-size="12" letter-spacing="1.5">GRAVEL LOT</text>
<path d="M128 168C128 150 140 142 140 118" fill="none" stroke="#F1B21C" stroke-width="3" stroke-dasharray="3 6" stroke-linecap="round"/>
<path d="M133 124l7-9 7 9" fill="none" stroke="#F1B21C" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<text x="10" y="138.5" {f} font-size="10" letter-spacing="1.4" fill-opacity=".9">WEST 11TH STREET</text>
<text transform="translate(91 104) rotate(-90)" {f} font-size="10" letter-spacing="1.6">PARKER ST</text>
<text transform="translate(337 108) rotate(-90)" {f} font-size="10" letter-spacing="1.6">S HIGH ST</text>
</svg>"""


# ---------------------------------------------------------------- HOME
def home():
    blocks = {
        "Catering": "Trays and family meals for the table or the whole crowd.",
        "Deli": "Cured meats and cheeses from the case, olives, imported olive oil.",
        "Pastas": "Lasagna, stuffed shells and dinners to take home, with house sauce.",
        "Sandwiches": "Huge ones, named for regulars.",
        "Pastries": "Cannoli filled to order, sfogliatelle, bomboloni.",
        "Cookies": "Pignoli, rainbow cookies and biscotti, trays by order.",
        "Cakes": "Tiramisu, cheesecake and custom cakes by order.",
        "Bread": "Baked in house, with focaccia on Fridays.",
    }
    star_set = [4, 4, 4, 4, 4]

    K = {"Catering": 1.1, "Deli": 1.5, "Pastas": 1.3, "Sandwiches": 1.0, "Pastries": 1.1, "Cookies": 1.15, "Cakes": 1.5, "Bread": 1.5}

    def block(w, star=False):
        cls = "block block--star" if star else "block"
        return (f'<li class="{cls}" style="--k:{K[w]}"><a href="menu.html#{SLUG[w]}"><h4>{w}</h4><p>{blocks[w]}</p>'
                f'{GO}<span class="sr-only">See {w} on the menu</span></a></li>')

    row1 = "".join(block(w, w == "Sandwiches") for w in LINE1)
    row2 = "".join(block(w, w == "Pastries") for w in LINE2)

    hrs = [(0, "Sunday", "10am to 3pm"), (1, "Monday", "10am to 4pm"), (2, "Tuesday", "10am to 4pm"),
           (3, "Wednesday", "10am to 5pm"), (4, "Thursday", "10am to 5pm"), (5, "Friday", "10am to 5pm"), (6, "Saturday", "10am to 5pm")]
    hours_rows = "".join(
        f'<tr data-day="{d}"><th scope="row">{n}</th><td class="lead" aria-hidden="true"></td><td>{t}</td></tr>' for d, n, t in hrs)

    stars = "".join(star(i, 1 if i < 4 else 0.7) for i in range(5))

    return head("Savarino's Market | Sicilian bakery and deli, Columbia, Tennessee",
                "Sicilian family bakery, deli and market since 2002. Sandwiches, pastas, bread, pastries, cakes and catering at 314 West 11th Street, Columbia, Tennessee. Open today.",
                "home") + f"""
<body class="home" id="top">
{header("home")}
<main id="main">

<section class="hero field-ivory" aria-label="Savarino's Market">
<div class="wrap">
{words_list(LINE1, "words words--top", "On the sign, line one")}
<h1 class="hero-logo" data-hero-logo><img src="assets/img/logo.webp" alt="Savarino's Market, since 2002" width="1535" height="630" fetchpriority="high"></h1>
{words_list(LINE2, "words words--bottom", "On the sign, line two")}
<div class="hero-info">
<p class="hero-line"><span>The red brick building on West 11th.</span><span data-open-only hidden>Yes, we're open.</span></p>
<div class="hero-where-block">
<p class="status" data-status data-open="false" aria-live="polite"><span class="status-dot" aria-hidden="true"></span><span data-status-text>Open every day. Hours below.</span></p>
<address class="hero-where"><strong>{ADDR}</strong></address>
<a class="hero-phone" href="{TEL}" aria-label="Call {PHONE}">{PHONE}</a>
</div>
<div class="hero-cta">
<div class="btn-row"><a class="btn btn-teal" href="{MAPS}" rel="noopener">Get Directions</a><a class="btn btn-line" href="menu.html">See the Menu</a></div>
</div>
<div class="hero-note">
<p class="hero-since"><b>Since 2002,</b> first in Nashville. Now on the corner of West 11th and Parker, in the Columbia Arts District.</p>
{dn("headline", "Hero headline and the voice of every line on this page. Approve or rewrite.")}
</div>
</div>
</div>
</section>

<div class="tile-band tile-band--slim" role="presentation"></div>
<section class="sec field-navy" id="visit" aria-labelledby="visit-h">
<div class="wrap">
<div class="rf">
<div class="rail"><h2 id="visit-h">Know before you go</h2></div>
<div class="field">
<div class="know">
<div class="know-hours">
<h3>Hours, Central time</h3>
<table class="hours" data-hours><caption class="sr-only">Hours, Central time</caption><tbody>{hours_rows}</tbody></table>
</div>
<div class="know-points">
<h3>Good to know</h3>
<ul class="points">
<li><h4>Look for</h4><p>The two story red brick building with the front porch, at West 11th and Parker. It can look closed from the street. If the hours say we're open, we are.</p></li>
<li><h4>Parking</h4><p>Free street parking, and a gravel lot across the street.</p></li>
<li><h4>Seating</h4><p>Outdoor seating only. We're small and built for carry out.</p></li>
<li><h4>Saturdays</h4><p>Saturdays are busy. Come early, or call ahead.</p></li>
<li><h4>Late in the day</h4><p>Hot food can run out before we close. Call ahead to check.</p></li>
</ul>
{dn("know", "Holiday and seasonal hours (the hours shown are the ones supplied). Accessibility: porch steps or ramp, door width, restroom, how many outdoor tables. Daily specials: how to show what is in the case today and when hot food runs out.")}
</div>
<div class="know-diagram">
<figure>{parking_svg()}<figcaption>Sketch, north up, not to scale. The bays are free street parking. The gold line walks you from the lot to the porch.</figcaption></figure>
{dn("parking", "Where the gravel lot sits, any time limits or signage, and whether customers may use it. This diagram is a sketch from the facts supplied, not a survey.")}
</div>
<div class="know-photo"><div class="ph" style="aspect-ratio:16/10"><span>PHOTO: the brick storefront with the porch, shot from across the street</span></div></div>
</div>
</div>
</div>
</div>
</section>

<section class="sec field-ivory" id="sign" aria-labelledby="sign-h">
<div class="wrap">
<div class="rf">
<div class="rail"><h2 id="sign-h">Everything on the sign</h2></div>
<div class="field">
<div class="sign-row"><h3 class="row-label">From the kitchen</h3><ul class="blocks">{row1}</ul></div>
<div class="sign-row"><h3 class="row-label">From the bakery</h3><ul class="blocks">{row2}</ul></div>
</div>
</div>
</div>
</section>

<section class="sec field-ivory" id="favorites" aria-labelledby="fav-h" style="padding-top:0">
<div class="wrap">
<div class="divider" aria-hidden="true"><img src="assets/img/fleuron.svg" alt="" width="72" height="24"></div>
<h2 class="fav-head" id="fav-h" style="margin-top:clamp(40px,6vw,104px)"><span>Come hungry.</span> <span>The muffuletta feeds two.</span></h2>
<div class="favs">
<article class="fav fav--muff">
{muffuletta_photo()}
<h3>The muffuletta</h3>
<p>Big enough to share. Bring someone, or take half home.</p>
</article>
<article class="fav fav--cannoli">
{framed('''<div class="stage" data-stage>
<div class="stage-copy"><h3>Cannoli, filled to order</h3><p>We fill each one when you order it.<span class="js-only"> Tap the shell and watch.</span></p></div>
<div class="cannoli" aria-hidden="true">
<img class="c-full" src="assets/img/cannoli-full.webp" alt="" width="1168" height="434" loading="lazy">
<img class="c-empty" src="assets/img/cannoli-empty.webp" alt="" width="1168" height="434" loading="lazy">
<img class="c-fill l" src="assets/img/cannoli-fill-left.webp" alt="" width="1168" height="434" loading="lazy">
<img class="c-fill r" src="assets/img/cannoli-fill-right.webp" alt="" width="1168" height="434" loading="lazy">
</div>
<p class="stage-status" data-stage-status aria-live="polite"></p>
<button class="btn btn-teal" type="button" data-fill>Fill it</button>
<a class="stage-next" href="menu.html#pastries">See Pastries</a>
</div>''')}
</article>
<article class="fav fav--foc">
<h3>Focaccia on Fridays</h3>
<p>Baked in house.</p>
</article>
<article class="fav fav--shells">
<h3>Family-size stuffed shells</h3>
<p>Dinner for the whole table, ready to take home.</p>
</article>
</div>
{dn("favorites", "Friday timing for the focaccia and whether it sells out. Pan sizes and how many each family-size tray feeds.")}
</div>
</section>

<section class="sec field-ivory-2" id="catering-cakes" aria-labelledby="cat-h">
<div class="wrap">
<h2 class="cat-head" id="cat-h">Catering and cakes, made fresh for you.</h2>
<div class="cat-grid">
<div>
<p class="lede">Tell us what you need and when. We'll take it from there.</p>
<ul class="offer">
<li><h3>Custom cakes</h3><p>Birthday, wedding and sheet cakes, made to order.</p></li>
<li><h3>Cookie trays</h3><p>Pignoli, rainbow cookies, biscotti and Italian wedding cookies, by order.</p></li>
<li><h3>Catering</h3><p>Food for a crowd.</p></li>
<li><h3>The family meal</h3><p>Entree, pasta, salad and a loaf.</p></li>
</ul>
<div class="cat-call"><p>Rather talk it through?</p><a class="btn btn-line" href="{TEL}">Call {PHONE}</a></div>
</div>
<div>{framed(form_catering("h"), "framed--form")}</div>
</div>
{dn("lead-times", "Notice needed for cakes, cookie trays, the family meal and catering. Catering minimums, pickup or delivery, and deposits.")}
{dn("form-routing", "Where form requests go (email, text or phone) and how fast the family can promise to answer.")}
</div>
</section>

<div class="tile-band tile-band--slim" role="presentation"></div>
<section class="sec wholesale field-navy" id="wholesale" aria-labelledby="ws-h">
<div class="wrap">
<div class="ws-main">
<h2 id="ws-h">Bread for your kitchen.</h2>
<p class="lede">We still bake wholesale for Nashville area restaurants. Bread, rolls and pastry, baked to order.</p>
</div>
<div class="ws-side">
<p class="ws-call">Prefer to talk? <a href="{TEL}">Call {PHONE}</a>.</p>
</div>
<details id="wholesale-form">
<summary><span class="btn btn-saffron">Ask about wholesale</span></summary>
<div class="ws-form">
<form class="form" data-form="wholesale" novalidate aria-label="Wholesale inquiry">
<div class="f"><label for="w-biz">Restaurant or shop</label><input id="w-biz" name="business" autocomplete="organization" required data-error="Tell us the name of your place."><span class="err" aria-live="polite"></span></div>
<div class="f-row">
<div class="f"><label for="w-name">Your name</label><input id="w-name" name="name" autocomplete="name" required data-error="Tell us who to ask for."><span class="err" aria-live="polite"></span></div>
<div class="f"><label for="w-contact">Phone or email</label><input id="w-contact" name="contact" autocomplete="tel" required data-error="We need a way to reach you."><span class="err" aria-live="polite"></span></div>
</div>
<div class="f"><label for="w-need">What you need, and how often</label><textarea id="w-need" name="need" rows="4" placeholder="Hoagie rolls, twice a week" required data-error="Tell us what you are after."></textarea><span class="err" aria-live="polite"></span></div>
<button class="btn btn-saffron" type="submit">Send wholesale inquiry</button>
<div class="form-ok" hidden><h3>Nothing sent yet.</h3><p>This is a concept form. For now, call <a href="{TEL}">{PHONE}</a>.</p></div>
</form>
</div>
</details>
<div>{dn("wholesale", "Wholesale delivery area, delivery days, minimums, lead times and a wholesale email or direct line.")}</div>
</div>
</section>

<section class="sec field-ivory" id="proof" aria-labelledby="proof-h">
<div class="wrap">
<div class="rf">
<div class="rail"><h2 id="proof-h">What people say</h2></div>
<div class="field">
<div class="proof-top">
<div>
<div class="stars" aria-hidden="true">{stars}</div>
<p class="rating">4.7 on Google<small>across 156 reviews</small></p>
</div>
<div class="honor">
<p><strong>Nashville Scene, Best of Nashville 2023:</strong> “Best Reason to Go to Columbia.”</p>
<p class="ddd">Savarino's Cucina, the family's Nashville restaurant in Hillsboro Village, was featured on Diners, <span class="nw">Drive-Ins</span> and Dives.</p>
</div>
</div>
<div class="slots">
<blockquote class="slot"><b>PASTE GOOGLE REVIEW</b><p>Theme: tastes like New York.</p><cite>Reviewer name and city</cite></blockquote>
<blockquote class="slot"><b>PASTE GOOGLE REVIEW</b><p>Theme: worth the drive.</p><cite>Reviewer name and city</cite></blockquote>
<blockquote class="slot"><b>PASTE GOOGLE REVIEW</b><p>Theme: the wedding cake.</p><cite>Reviewer name and city</cite></blockquote>
</div>
{dn("press", "Exact Nashville Scene wording and permission to use it, and the episode details for the Diners, Drive-Ins and Dives feature.")}
{dn("reviews", "Pick three real Google reviews to paste in, with the reviewers’ names as they appear.")}
</div>
</div>
</div>
</section>

<section class="sec field-ivory" id="family" aria-labelledby="fam-h" style="padding-top:0">
<div class="wrap">
<div class="rf">
<div class="rail"><h2 id="fam-h">The family</h2></div>
<div class="field">
<p class="route"><span>Sicily</span><i></i><span>Brooklyn</span><i></i><span>Nashville</span><i></i><span>Columbia</span></p>
<div class="family-grid">
<div class="family-copy">
<p>Corrado Savarino&nbsp;Sr. was born in Sicily, raised in Brooklyn and trained at Veniero's in Manhattan.</p>
<p>He opened the family's first bakery in Nashville in 2002, and the family ran Savarino's Cucina in Hillsboro Village from 2006 to 2017.</p>
<p>The Columbia bakery started baking wholesale in 2019 and opened to the public in 2023.</p>
<p>Today his son Carmelo runs the market, with Carmelo's younger brother Corrado&nbsp;Jr. right beside him.</p>
</div>
<div class="ph ph--tall" style="max-width:420px"><span>PHOTO: Carmelo and Corrado Jr. behind the case</span></div>
</div>
{dn("photos", "The muffuletta photo on both pages was supplied for this concept: a half sandwich held in two hands. Confirm it is the shop's own sandwich, that it may be used, and that the person holding it agrees. Every other photo is still a placeholder that names its shot.")}
</div>
</div>
</div>
</section>

</main>
{footer()}
{dock("home")}
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------- MENU
def item(name, desc="", price=True, cls=""):
    d = f'<p class="item-desc">{desc}</p>' if desc else ""
    return (f'<li class="item {cls}"><div class="item-top"><span class="item-name">{name}</span>'
            f'<span class="item-lead" aria-hidden="true"></span><span class="item-price">$00</span></div>{d}</li>')


def board(w, intro="", items_html="", two=True, extra="", ph=""):
    cols = "items items--2" if two else "items"
    return f"""<section class="board field-ivory" id="{SLUG[w]}" aria-labelledby="{SLUG[w]}-h">
<div class="board-head"><h2 id="{SLUG[w]}-h">{w}</h2></div>
{intro}
<ul class="{cols}">{items_html}</ul>
{extra}
{ph}
</section>"""


def menu():
    ORDER_LINE = '<p class="order-line"><a href="#order">Order ahead. Tell us the date.</a></p>'
    cat_links = "".join(f'<li><a href="#{SLUG[w]}">{w}</a></li>' for w in MENU_ORDER)

    sandwiches = "".join([
        item("The Savarino", "Eggplant."),
        item("The Ed Pontieri", "Mortadella, soppressata, capicola, provolone and bomba calabrese."),
        item("The Palermo", "Grilled chicken, marinara, mozzarella, prosciutto and roasted peppers."),
        item("Country Fire", "Chicken cutlet, marinara, mozzarella and hot cherry peppers."),
        item("The Sicilian"),
        item("The Corrado"),
        item("Muffuletta", "Feeds two."),
        item("Caprese"),
        item("Meatball"),
        item("Chicken parm"),
        item("Sausage and peppers"),
    ])
    deli = "".join([
        item("Cured meats and cheeses", "From the case."),
        item("Olives"),
        item("Imported olive oil"),
        item("Espresso"),
        item("Ladyfingers"),
        item("Italian sodas"),
    ])
    pastas = "".join([
        item("Lasagna"),
        item("Stuffed shells", "Family-size too."),
        item("Manicotti"),
        item("Chicken parm"),
        item("Eggplant rollatini"),
        item("Chicken francese"),
        item("Sausage and peppers"),
        item("Meatballs"),
        item("Fresh pasta"),
        item("House sauces and pesto"),
    ])
    meal = '<ul class="items"><li class="item item--meal"><div class="item-top"><span class="item-name">The family meal</span><span class="item-lead" aria-hidden="true"></span><span class="item-price">$00</span></div><p class="item-desc">Entree, pasta, salad and a loaf.</p></li></ul>'
    bread = "".join([
        item("Italian loaves"),
        item("Hoagie rolls"),
        item("Olive bread"),
        item("Focaccia", "Fridays."),
        item("Sicilian pizza twists"),
    ])
    pastries = "".join([
        item("Cannoli", "Filled to order."),
        item("Sfogliatelle"),
        item("Bomboloni"),
        item("Baba rum"),
        item("Éclairs"),
    ])
    cookies = "".join([
        item("Pignoli"),
        item("Rainbow cookies"),
        item("Biscotti"),
        item("Italian wedding cookies"),
        item("Cookie trays", "By order."),
    ])
    cakes = "".join([
        item("Tiramisu"),
        item("Italian cheesecake"),
        item("New York cheesecake"),
        item("Custom cakes", "Birthday, wedding and sheet cakes, by order."),
    ])

    ph = lambda t, cls="ph--wide": f'<div class="ph {cls}"><span>{t}</span></div>'

    body = ""
    body += board("Sandwiches",
                  intro='<p class="board-intro">At the Cucina, the family’s Nashville restaurant, sandwiches were named for regulars. Several names live on here.</p>',
                  items_html=sandwiches,
                  extra=dn("sandwiches", "What goes on The Savarino, The Sicilian, The Corrado and the classics, which names are still on the board, and who each one was named for."),
                  ph=muffuletta_photo("photo--wide"))
    body += board("Deli", items_html=deli, two=True)
    body += board("Pastas", items_html=pastas, extra=meal, ph="")
    body += board("Bread", intro='<p class="board-intro">Baked in house.</p>', items_html=bread,
                  ph=ph("PHOTO: focaccia on a Friday tray, fresh from the oven"))
    body += board("Pastries", items_html=pastries, ph=ph("PHOTO: Carmelo filling a cannoli"))
    body += board("Cookies", intro='<p class="wink">Biscotti. Not biscuits.</p>', items_html=cookies, extra=ORDER_LINE)
    body += board("Cakes", items_html=cakes,
                  extra=ORDER_LINE + dn("cake-leads", "Notice needed for custom cakes, sizes, and flavors."),
                  ph=ph("PHOTO: custom birthday cake on the counter"))
    cat = f"""<section class="board catering-board field-ivory" id="catering" aria-labelledby="catering-h">
<div class="board-head"><h2 id="catering-h">Catering</h2></div>
<p class="lede">Trays, the family meal and food for a crowd. Tell us what you need and when.</p>
<div class="btn-row"><a class="btn btn-line" href="{TEL}">Call {PHONE}</a></div>
{dn("catering-menu", "Catering menu, minimums, pickup or delivery, and lead times.")}
<div class="form-wrap" id="order">{framed(form_catering("m"), "framed--form")}</div>
</section>"""

    return head("Menu | Savarino's Market, Columbia, Tennessee",
                "The Savarino's menu: sandwiches, deli, pastas, bread, pastries, cookies, cakes and catering. The case changes daily, so call to check on a favorite.",
                "menu") + f"""
<body class="menu-page">
{header("menu")}
<main id="main">
<section class="menu-hero field-ivory" aria-labelledby="menu-h">
<div class="wrap">
<div class="menu-hero-grid">
<div></div>
<div>
<h1 id="menu-h">The Menu</h1>
<p class="lede">The case changes daily. Call to check on a favorite.</p>
<div class="btn-row"><a class="btn btn-teal" href="{TEL}">Call {PHONE}</a><a class="btn btn-line" href="{MAPS}" rel="noopener">Get Directions</a></div>
<div class="menu-legend">{dn("prices", "Every price on this page. $00 is a placeholder, nothing here is final.")}</div>
</div>
</div>
</div>
</section>
<div class="wrap menu-grid">
<nav class="cat-nav" aria-label="Menu sections"><ul>{cat_links}</ul></nav>
<div>
{body}
{cat}
</div>
</div>
</main>
{footer()}
{dock("menu")}
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def curly(h):
    parts = re.split(r'(<script.*?</script>)', h, flags=re.S)
    return "".join(p if p.startswith("<script") else re.sub(r"(?<=\w)'(?=\w)", "\u2019", p) for p in parts)


if __name__ == "__main__":
    open(OUT + "index.html", "w").write(curly(home()))
    open(OUT + "menu.html", "w").write(curly(menu()))
    print("written; designer notes:", len(DN_LOG))
