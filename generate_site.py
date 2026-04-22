#!/usr/bin/env python3
"""
Centurion Tax Strategist -- Complete Website Generator
Generates all HTML pages, blog posts, sitemap.xml, and robots.txt
"""

import os
import json
from datetime import datetime, timedelta

# =============================================================================
# CONFIGURATION
# =============================================================================

SITE_URL = "https://centuriontaxstrategist.com"
SITE_NAME = "Centurion Tax Strategist"
SITE_TAGLINE = "Tax Advisory for High Net Worth Business Owners"
PHONE = "(888) 901-2345"
EMAIL = "info@centuriontaxstrategist.com"
ADDRESS_STREET = "One PPG Place, Suite 3100"
ADDRESS_CITY = "Pittsburgh"
ADDRESS_STATE = "PA"
ADDRESS_ZIP = "15222"

# Brand colors
NAVY = "#0a1628"
NAVY_LIGHT = "#0f1f3d"
NAVY_MID = "#132847"
GOLD = "#c8a052"
GOLD_LIGHT = "#d4b06a"
GOLD_DARK = "#b08a3e"
WHITE = "#ffffff"
GRAY_LIGHT = "#e8e8e8"
GRAY = "#999999"
BODY_TEXT = "#c5c8d0"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# CSS
# =============================================================================

def get_css():
    return f"""
    :root {{
        --navy: {NAVY};
        --navy-light: {NAVY_LIGHT};
        --navy-mid: {NAVY_MID};
        --gold: {GOLD};
        --gold-light: {GOLD_LIGHT};
        --gold-dark: {GOLD_DARK};
        --white: {WHITE};
        --gray-light: {GRAY_LIGHT};
        --gray: {GRAY};
        --body-text: {BODY_TEXT};
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    html {{ scroll-behavior: smooth; }}

    body {{
        font-family: 'Georgia', 'Times New Roman', serif;
        background: var(--navy);
        color: var(--body-text);
        line-height: 1.7;
        -webkit-font-smoothing: antialiased;
    }}

    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Georgia', serif;
        color: var(--white);
        font-weight: 700;
        line-height: 1.2;
    }}

    a {{ color: var(--gold); text-decoration: none; transition: color 0.3s; }}
    a:hover {{ color: var(--gold-light); }}

    img {{ max-width: 100%; height: auto; }}

    .container {{
        max-width: 1140px;
        margin: 0 auto;
        padding: 0 24px;
    }}

    /* ---- HEADER / NAV ---- */
    .site-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        background: rgba(10,22,40,0.97);
        border-bottom: 1px solid rgba(200,160,82,0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }}

    .header-inner {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 24px;
        max-width: 1200px;
        margin: 0 auto;
    }}

    .logo {{
        display: flex;
        align-items: center;
        gap: 12px;
        text-decoration: none;
    }}

    .logo-icon {{
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--gold), var(--gold-dark));
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
    }}

    .logo-text {{
        font-family: 'Georgia', serif;
        font-size: 18px;
        font-weight: 700;
        color: var(--gold);
        letter-spacing: 1px;
        text-transform: uppercase;
    }}

    .logo-text span {{
        display: block;
        font-size: 10px;
        font-weight: 400;
        color: var(--gray);
        letter-spacing: 2px;
        text-transform: uppercase;
    }}

    .nav-links {{
        display: flex;
        align-items: center;
        gap: 28px;
        list-style: none;
    }}

    .nav-links a {{
        color: var(--body-text);
        font-family: 'Georgia', serif;
        font-size: 14px;
        letter-spacing: 0.5px;
        transition: color 0.3s;
        text-decoration: none;
    }}

    .nav-links a:hover {{ color: var(--gold); }}

    .nav-cta {{
        background: linear-gradient(135deg, var(--gold), var(--gold-dark));
        color: var(--navy) !important;
        padding: 10px 22px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}

    .nav-cta:hover {{
        background: linear-gradient(135deg, var(--gold-light), var(--gold));
        color: var(--navy) !important;
    }}

    .mobile-toggle {{
        display: none;
        flex-direction: column;
        gap: 5px;
        cursor: pointer;
        background: none;
        border: none;
        padding: 5px;
    }}

    .mobile-toggle span {{
        display: block;
        width: 24px;
        height: 2px;
        background: var(--gold);
        transition: all 0.3s;
    }}

    /* ---- HERO ---- */
    .hero {{
        padding: 160px 0 100px;
        background: linear-gradient(180deg, var(--navy) 0%, var(--navy-light) 100%);
        text-align: center;
        position: relative;
        overflow: hidden;
    }}

    .hero::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(ellipse at center top, rgba(200,160,82,0.06) 0%, transparent 60%);
    }}

    .hero h1 {{
        font-size: 48px;
        margin-bottom: 20px;
        position: relative;
    }}

    .hero h1 .gold {{ color: var(--gold); }}

    .hero .subtitle {{
        font-size: 20px;
        color: var(--body-text);
        max-width: 640px;
        margin: 0 auto 36px;
        position: relative;
    }}

    .hero-cta {{
        display: inline-block;
        background: linear-gradient(135deg, var(--gold), var(--gold-dark));
        color: var(--navy);
        padding: 16px 40px;
        font-family: 'Georgia', serif;
        font-size: 16px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 4px;
        transition: all 0.3s;
        position: relative;
    }}

    .hero-cta:hover {{
        background: linear-gradient(135deg, var(--gold-light), var(--gold));
        color: var(--navy);
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(200,160,82,0.3);
    }}

    /* ---- SECTIONS ---- */
    .section {{
        padding: 80px 0;
    }}

    .section-dark {{
        background: var(--navy-light);
    }}

    .section-title {{
        font-size: 36px;
        text-align: center;
        margin-bottom: 16px;
    }}

    .section-subtitle {{
        text-align: center;
        color: var(--gray);
        font-size: 17px;
        max-width: 600px;
        margin: 0 auto 50px;
    }}

    .gold-line {{
        width: 60px;
        height: 3px;
        background: var(--gold);
        margin: 16px auto 24px;
    }}

    /* ---- CARDS / GRID ---- */
    .grid-3 {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }}

    .grid-2 {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }}

    .card {{
        background: var(--navy-mid);
        border: 1px solid rgba(200,160,82,0.12);
        border-radius: 6px;
        padding: 36px 28px;
        transition: all 0.3s;
    }}

    .card:hover {{
        border-color: rgba(200,160,82,0.3);
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.3);
    }}

    .card-icon {{
        font-size: 36px;
        margin-bottom: 16px;
    }}

    .card h3 {{
        font-size: 20px;
        margin-bottom: 12px;
    }}

    .card p {{
        font-size: 15px;
        color: var(--body-text);
        line-height: 1.7;
    }}

    .card-link {{
        display: inline-block;
        margin-top: 16px;
        color: var(--gold);
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}

    .card-link:hover {{ color: var(--gold-light); }}

    /* ---- STATS ---- */
    .stats-row {{
        display: flex;
        justify-content: center;
        gap: 60px;
        padding: 50px 0;
        border-top: 1px solid rgba(200,160,82,0.1);
        border-bottom: 1px solid rgba(200,160,82,0.1);
    }}

    .stat-item {{
        text-align: center;
    }}

    .stat-number {{
        font-size: 48px;
        font-weight: 700;
        color: var(--gold);
        font-family: 'Georgia', serif;
        line-height: 1;
    }}

    .stat-label {{
        font-size: 14px;
        color: var(--gray);
        margin-top: 8px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* ---- TESTIMONIALS ---- */
    .testimonial {{
        background: var(--navy-mid);
        border: 1px solid rgba(200,160,82,0.1);
        border-radius: 6px;
        padding: 32px;
        position: relative;
    }}

    .testimonial::before {{
        content: '\\201C';
        font-size: 60px;
        color: var(--gold);
        opacity: 0.3;
        position: absolute;
        top: 10px;
        left: 20px;
        font-family: Georgia, serif;
    }}

    .testimonial p {{
        font-style: italic;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 16px;
        position: relative;
        z-index: 1;
    }}

    .testimonial .author {{
        color: var(--gold);
        font-weight: 700;
        font-size: 14px;
    }}

    .testimonial .role {{
        color: var(--gray);
        font-size: 13px;
    }}

    .stars {{
        color: var(--gold);
        font-size: 16px;
        margin-bottom: 12px;
    }}

    /* ---- HOW IT WORKS ---- */
    .steps {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        counter-reset: step;
    }}

    .step {{
        text-align: center;
        padding: 24px;
    }}

    .step-number {{
        width: 56px;
        height: 56px;
        border-radius: 50%;
        border: 2px solid var(--gold);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 16px;
        font-family: 'Georgia', serif;
        font-size: 22px;
        color: var(--gold);
        font-weight: 700;
    }}

    .step h4 {{
        font-size: 16px;
        margin-bottom: 8px;
    }}

    .step p {{
        font-size: 14px;
        color: var(--gray);
    }}

    /* ---- FAQ ---- */
    .faq-item {{
        border-bottom: 1px solid rgba(200,160,82,0.1);
        padding: 24px 0;
    }}

    .faq-question {{
        font-size: 18px;
        color: var(--white);
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Georgia', serif;
    }}

    .faq-question::after {{
        content: '+';
        font-size: 24px;
        color: var(--gold);
        transition: transform 0.3s;
    }}

    .faq-question.active::after {{
        content: '\\2212';
    }}

    .faq-answer {{
        padding-top: 12px;
        font-size: 15px;
        color: var(--body-text);
        line-height: 1.8;
        display: none;
    }}

    .faq-answer.active {{
        display: block;
    }}

    /* ---- BLOG ---- */
    .blog-card {{
        background: var(--navy-mid);
        border: 1px solid rgba(200,160,82,0.1);
        border-radius: 6px;
        overflow: hidden;
        transition: all 0.3s;
    }}

    .blog-card:hover {{
        border-color: rgba(200,160,82,0.3);
        transform: translateY(-4px);
    }}

    .blog-card-body {{
        padding: 24px;
    }}

    .blog-card-meta {{
        font-size: 13px;
        color: var(--gray);
        margin-bottom: 8px;
    }}

    .blog-card h3 {{
        font-size: 18px;
        margin-bottom: 10px;
    }}

    .blog-card h3 a {{
        color: var(--white);
    }}

    .blog-card h3 a:hover {{
        color: var(--gold);
    }}

    .blog-card p {{
        font-size: 14px;
        color: var(--body-text);
    }}

    /* ---- ARTICLE ---- */
    .article-hero {{
        padding: 140px 0 60px;
        text-align: center;
        background: linear-gradient(180deg, var(--navy) 0%, var(--navy-light) 100%);
    }}

    .article-hero h1 {{
        font-size: 40px;
        max-width: 800px;
        margin: 0 auto 16px;
    }}

    .article-meta {{
        color: var(--gray);
        font-size: 14px;
    }}

    .article-body {{
        max-width: 760px;
        margin: 0 auto;
        padding: 40px 24px 80px;
        font-size: 17px;
        line-height: 1.9;
    }}

    .article-body h2 {{
        font-size: 28px;
        margin: 48px 0 20px;
    }}

    .article-body h3 {{
        font-size: 22px;
        margin: 36px 0 16px;
    }}

    .article-body p {{
        margin-bottom: 20px;
    }}

    .article-body ul, .article-body ol {{
        margin: 0 0 20px 24px;
    }}

    .article-body li {{
        margin-bottom: 8px;
    }}

    .article-body blockquote {{
        border-left: 3px solid var(--gold);
        padding: 16px 24px;
        margin: 24px 0;
        background: var(--navy-mid);
        border-radius: 0 4px 4px 0;
        font-style: italic;
    }}

    /* ---- CTA BANNER ---- */
    .cta-banner {{
        padding: 80px 0;
        text-align: center;
        background: linear-gradient(135deg, var(--navy-light), var(--navy-mid));
        border-top: 1px solid rgba(200,160,82,0.1);
    }}

    .cta-banner h2 {{
        font-size: 32px;
        margin-bottom: 16px;
    }}

    .cta-banner p {{
        font-size: 17px;
        color: var(--body-text);
        max-width: 560px;
        margin: 0 auto 32px;
    }}

    /* ---- FOOTER ---- */
    .site-footer {{
        background: rgba(10,22,40,0.95);
        border-top: 1px solid rgba(200,160,82,0.1);
        padding: 60px 0 30px;
    }}

    .footer-grid {{
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 40px;
        margin-bottom: 40px;
    }}

    .footer-brand p {{
        font-size: 14px;
        color: var(--gray);
        margin-top: 12px;
        line-height: 1.7;
    }}

    .footer-col h4 {{
        font-size: 14px;
        color: var(--gold);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 16px;
    }}

    .footer-col ul {{
        list-style: none;
    }}

    .footer-col li {{
        margin-bottom: 8px;
    }}

    .footer-col a {{
        color: var(--gray);
        font-size: 14px;
    }}

    .footer-col a:hover {{ color: var(--gold); }}

    .footer-bottom {{
        border-top: 1px solid rgba(200,160,82,0.1);
        padding-top: 24px;
        text-align: center;
        font-size: 13px;
        color: var(--gray);
    }}

    /* ---- BREADCRUMBS ---- */
    .breadcrumbs {{
        padding: 100px 0 0;
        font-size: 13px;
    }}

    .breadcrumbs a {{ color: var(--gray); }}
    .breadcrumbs a:hover {{ color: var(--gold); }}
    .breadcrumbs span {{ color: var(--gold); }}

    /* ---- INNER PAGE HERO ---- */
    .inner-hero {{
        padding: 130px 0 60px;
        text-align: center;
        background: linear-gradient(180deg, var(--navy) 0%, var(--navy-light) 100%);
    }}

    .inner-hero h1 {{
        font-size: 42px;
        margin-bottom: 16px;
    }}

    .inner-hero p {{
        font-size: 18px;
        color: var(--body-text);
        max-width: 620px;
        margin: 0 auto;
    }}

    /* ---- CONTACT / BOOKING ---- */
    .booking-frame {{
        max-width: 700px;
        margin: 0 auto;
        background: var(--navy-mid);
        border: 1px solid rgba(200,160,82,0.15);
        border-radius: 6px;
        padding: 48px;
        text-align: center;
    }}

    .booking-frame h2 {{
        margin-bottom: 16px;
    }}

    .booking-frame p {{
        margin-bottom: 24px;
        color: var(--body-text);
    }}

    .contact-info {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        margin-top: 40px;
    }}

    .contact-box {{
        text-align: center;
        padding: 24px;
        background: var(--navy-mid);
        border: 1px solid rgba(200,160,82,0.1);
        border-radius: 6px;
    }}

    .contact-box h4 {{
        color: var(--gold);
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }}

    .contact-box p {{
        font-size: 15px;
    }}

    /* ---- SERVICE PAGE ---- */
    .service-detail {{
        max-width: 800px;
        margin: 0 auto;
        padding: 0 24px;
    }}

    .service-detail h2 {{
        font-size: 28px;
        margin: 40px 0 16px;
    }}

    .service-detail p {{
        margin-bottom: 16px;
        font-size: 16px;
        line-height: 1.8;
    }}

    .service-detail ul {{
        margin: 0 0 20px 24px;
    }}

    .service-detail li {{
        margin-bottom: 8px;
        font-size: 15px;
    }}

    .highlight-box {{
        background: var(--navy-mid);
        border-left: 3px solid var(--gold);
        padding: 24px 28px;
        margin: 28px 0;
        border-radius: 0 6px 6px 0;
    }}

    .highlight-box strong {{
        color: var(--gold);
    }}

    /* ---- RESPONSIVE ---- */
    @media (max-width: 992px) {{
        .grid-3 {{ grid-template-columns: repeat(2, 1fr); }}
        .footer-grid {{ grid-template-columns: repeat(2, 1fr); }}
        .steps {{ grid-template-columns: repeat(2, 1fr); }}
        .stats-row {{ flex-wrap: wrap; gap: 30px; }}
        .contact-info {{ grid-template-columns: 1fr; }}
    }}

    @media (max-width: 768px) {{
        .nav-links {{ display: none; }}
        .mobile-toggle {{ display: flex; }}
        .nav-links.active {{
            display: flex;
            flex-direction: column;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: var(--navy);
            padding: 20px;
            border-bottom: 1px solid rgba(200,160,82,0.15);
        }}
        .hero h1 {{ font-size: 32px; }}
        .hero .subtitle {{ font-size: 17px; }}
        .grid-3 {{ grid-template-columns: 1fr; }}
        .grid-2 {{ grid-template-columns: 1fr; }}
        .section-title {{ font-size: 28px; }}
        .inner-hero h1 {{ font-size: 30px; }}
        .article-hero h1 {{ font-size: 28px; }}
        .footer-grid {{ grid-template-columns: 1fr; }}
        .steps {{ grid-template-columns: 1fr; }}
    }}
"""

# =============================================================================
# SVG LOGO (centurion helmet in gold circle)
# =============================================================================

HELMET_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44" width="44" height="44">
  <circle cx="22" cy="22" r="22" fill="#c8a052"/>
  <g transform="translate(10,8) scale(0.55)">
    <path d="M22 4C14 4 8 10 8 18c0 3 1 6 3 8h-2c-1 0-2 1-2 2v6c0 1 1 2 2 2h4l2 6c0 1 1 1 2 1h10c1 0 2 0 2-1l2-6h4c1 0 2-1 2-2v-6c0-1-1-2-2-2h-2c2-2 3-5 3-8 0-8-6-14-14-14zm-8 22h20v4H14v-4zm3 6h10l-1 4H18l-1-4zm7-24c5 0 10 4 10 10 0 2-1 5-3 7H13c-2-2-3-5-3-7 0-6 5-10 10-10z" fill="#0a1628"/>
  </g>
</svg>"""

# =============================================================================
# HTML TEMPLATES
# =============================================================================

def get_nav(active=""):
    items = [
        ("About", "/about/"),
        ("Services", "/services/"),
        ("3-Year Lookback", "/3-year-tax-lookback/"),
        ("Reviews", "/reviews/"),
        ("Blog", "/blog/"),
        ("FAQ", "/faq/"),
    ]
    links = ""
    for label, url in items:
        cls = ' style="color:var(--gold)"' if active == label else ""
        links += f'<li><a href="{url}"{cls}>{label}</a></li>\n'
    links += f'<li><a href="/book-strategy-call/" class="nav-cta">Book a Call</a></li>'

    return f"""
    <header class="site-header">
        <div class="header-inner">
            <a href="/" class="logo">
                <div class="logo-icon">{HELMET_SVG}</div>
                <div class="logo-text">Centurion<span>Tax Strategist</span></div>
            </a>
            <nav>
                <ul class="nav-links" id="navLinks">
                    {links}
                </ul>
            </nav>
            <button class="mobile-toggle" onclick="document.getElementById('navLinks').classList.toggle('active')" aria-label="Toggle navigation">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>
    """

def get_footer():
    return f"""
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                        <div style="width:36px;height:36px;">{HELMET_SVG}</div>
                        <span style="font-family:Georgia;font-size:16px;color:var(--gold);font-weight:700;letter-spacing:1px;">CENTURION</span>
                    </div>
                    <p>Elite tax strategy for high net worth business owners. We recover missed deductions, restructure entities, and build tax plans that protect your wealth for the long term.</p>
                </div>
                <div class="footer-col">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="/3-year-tax-lookback/">3-Year Tax Lookback</a></li>
                        <li><a href="/cost-segregation/">Cost Segregation</a></li>
                        <li><a href="/entity-restructuring/">Entity Restructuring</a></li>
                        <li><a href="/short-term-rental-tax-strategy/">STR Tax Strategy</a></li>
                        <li><a href="/real-estate-professional-status/">REPS Qualification</a></li>
                        <li><a href="/irs-tax-resolution/">IRS Resolution</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="/about/">About Us</a></li>
                        <li><a href="/reviews/">Client Reviews</a></li>
                        <li><a href="/blog/">Blog</a></li>
                        <li><a href="/faq/">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="tel:{PHONE}">{PHONE}</a></li>
                        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                        <li>{ADDRESS_STREET}</li>
                        <li>{ADDRESS_CITY}, {ADDRESS_STATE} {ADDRESS_ZIP}</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; {datetime.now().year} Centurion Tax Strategist. All rights reserved.
                &nbsp;|&nbsp; <a href="/privacy/">Privacy</a>
                &nbsp;|&nbsp; <a href="/terms/">Terms</a>
            </div>
        </div>
    </footer>
    """

def get_cta_banner():
    return """
    <section class="cta-banner">
        <div class="container">
            <h2>Ready to Protect Your Wealth?</h2>
            <p>Schedule a complimentary strategy session with one of our tax strategists. We will review your situation and show you exactly where you are leaving money on the table.</p>
            <a href="/book-strategy-call/" class="hero-cta">Book Your Strategy Call</a>
        </div>
    </section>
    """

def build_page(title, description, canonical, body, og_type="website", schema="", active_nav=""):
    css = get_css()
    nav = get_nav(active_nav)
    footer = get_footer()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{SITE_URL}{canonical}">

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{SITE_URL}{canonical}">
    <meta property="og:site_name" content="{SITE_NAME}">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">

    {schema}

    <style>{css}</style>
</head>
<body>
{nav}
{body}
{footer}

<script>
// FAQ toggle
document.querySelectorAll('.faq-question').forEach(q => {{
    q.addEventListener('click', () => {{
        q.classList.toggle('active');
        q.nextElementSibling.classList.toggle('active');
    }});
}});
</script>
</body>
</html>"""


# =============================================================================
# PAGE BUILDERS
# =============================================================================

def build_homepage():
    schema = f"""
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": ["Organization", "ProfessionalService"],
        "name": "{SITE_NAME}",
        "url": "{SITE_URL}",
        "description": "Elite tax strategy for high net worth business owners making $500K+. Specializing in 3-year tax lookbacks, cost segregation, entity restructuring, and advanced tax planning.",
        "telephone": "{PHONE}",
        "email": "{EMAIL}",
        "address": {{
            "@type": "PostalAddress",
            "streetAddress": "{ADDRESS_STREET}",
            "addressLocality": "{ADDRESS_CITY}",
            "addressRegion": "{ADDRESS_STATE}",
            "postalCode": "{ADDRESS_ZIP}",
            "addressCountry": "US"
        }},
        "priceRange": "$$$$",
        "areaServed": "US",
        "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "187",
            "bestRating": "5"
        }}
    }}
    </script>"""

    body = f"""
    <section class="hero">
        <div class="container">
            <h1>Your Tax Strategy Deserves<br><span class="gold">a Centurion</span></h1>
            <p class="subtitle">We help high net worth business owners making $500K+ recover missed deductions, restructure for maximum savings, and build ironclad tax strategies that protect generational wealth.</p>
            <a href="/book-strategy-call/" class="hero-cta">Book Your Free Strategy Call</a>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="stats-row">
                <div class="stat-item">
                    <div class="stat-number">$50M+</div>
                    <div class="stat-label">Recovered for Clients</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Business Owners Served</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">50</div>
                    <div class="stat-label">States Covered</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">97%</div>
                    <div class="stat-label">Client Retention Rate</div>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <h2 class="section-title">Our Flagship: The 3-Year Tax Lookback</h2>
            <div class="gold-line"></div>
            <p class="section-subtitle">Most business owners overpay by $50,000 to $200,000 over a three-year period. We go back, find every missed deduction, and file amended returns to recover your money.</p>
            <div class="grid-3">
                <div class="card">
                    <div class="card-icon">&#128269;</div>
                    <h3>Deep-Dive Audit</h3>
                    <p>We review three years of federal and state returns line by line, cross-referencing your financials against every deduction, credit, and strategy you qualify for.</p>
                </div>
                <div class="card">
                    <div class="card-icon">&#128176;</div>
                    <h3>Recover Missed Deductions</h3>
                    <p>From misclassified expenses to unclaimed credits, we identify every dollar your current CPA left behind and file amended returns to recover it.</p>
                </div>
                <div class="card">
                    <div class="card-icon">&#128737;</div>
                    <h3>Future-Proof Your Strategy</h3>
                    <p>Beyond recovering past losses, we build a forward-looking tax plan that ensures you never overpay again. Entity restructuring, retirement optimization, and more.</p>
                </div>
            </div>
            <div style="text-align:center;margin-top:40px;">
                <a href="/3-year-tax-lookback/" class="hero-cta" style="font-size:14px;padding:14px 32px;">Learn About the 3-Year Lookback</a>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <h2 class="section-title">How It Works</h2>
            <div class="gold-line"></div>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h4>Strategy Call</h4>
                    <p>A 30-minute complimentary call to understand your business, income, and current tax situation.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h4>Deep Analysis</h4>
                    <p>We review three years of returns and financials to uncover every missed opportunity.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h4>Strategic Plan</h4>
                    <p>You receive a comprehensive tax plan with projected savings, amended filings, and entity recommendations.</p>
                </div>
                <div class="step">
                    <div class="step-number">4</div>
                    <h4>Implementation</h4>
                    <p>We execute everything, from amended returns to restructuring, so you keep more of what you earn.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section section-dark">
        <div class="container">
            <h2 class="section-title">Comprehensive Tax Strategy</h2>
            <div class="gold-line"></div>
            <p class="section-subtitle">Beyond the lookback, we offer a full suite of advanced tax strategies for business owners and real estate investors.</p>
            <div class="grid-3">
                <div class="card">
                    <h3>Cost Segregation</h3>
                    <p>Accelerate depreciation on your properties and unlock six-figure tax savings in year one.</p>
                    <a href="/cost-segregation/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <h3>Entity Restructuring</h3>
                    <p>S-Corp, C-Corp, or hybrid -- we design the entity structure that minimizes your total tax burden.</p>
                    <a href="/entity-restructuring/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <h3>STR Tax Strategy</h3>
                    <p>Leverage the short-term rental loophole to offset W-2 and business income with real estate losses.</p>
                    <a href="/short-term-rental-tax-strategy/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <h3>REPS Qualification</h3>
                    <p>Qualify as a Real Estate Professional to unlock unlimited passive loss deductions against active income.</p>
                    <a href="/real-estate-professional-status/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <h3>IRS Tax Resolution</h3>
                    <p>Unfiled returns, penalties, and IRS disputes. We negotiate on your behalf and resolve outstanding issues.</p>
                    <a href="/irs-tax-resolution/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <h3>Retirement Planning</h3>
                    <p>Solo 401(k)s, Cash Balance Plans, and Defined Benefit strategies to shelter income and build wealth.</p>
                    <a href="/retirement-tax-planning/" class="card-link">Learn More &rarr;</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <h2 class="section-title">What Our Clients Say</h2>
            <div class="gold-line"></div>
            <div class="grid-3">
                <div class="testimonial">
                    <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                    <p>They recovered $147,000 in missed deductions from my last three years of returns. My previous CPA had no idea these credits existed.</p>
                    <div class="author">David M.</div>
                    <div class="role">Orthopedic Surgery Practice Owner</div>
                </div>
                <div class="testimonial">
                    <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                    <p>The entity restructuring alone saved us $82,000 in the first year. This is a completely different level of tax advisory.</p>
                    <div class="author">Sarah T.</div>
                    <div class="role">Tech Company Founder</div>
                </div>
                <div class="testimonial">
                    <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                    <p>Between cost segregation and the STR strategy, we offset nearly all of our W-2 income. Centurion is worth every penny.</p>
                    <div class="author">James &amp; Laura K.</div>
                    <div class="role">Real Estate Investors</div>
                </div>
            </div>
        </div>
    </section>

    {get_cta_banner()}
    """

    return build_page(
        f"{SITE_NAME} | Elite Tax Strategy for Business Owners Making $500K+",
        "Centurion Tax Strategist helps high net worth business owners recover missed deductions, restructure entities, and build tax strategies that protect generational wealth. 3-year lookback, cost segregation, and more.",
        "/",
        body,
        schema=schema
    )


def build_about():
    body = """
    <section class="inner-hero">
        <div class="container">
            <h1>About Centurion Tax Strategist</h1>
            <p>We exist because high-earning business owners deserve better than generic tax advice.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="service-detail">
                <h2>Our Mission</h2>
                <p>Centurion Tax Strategist was founded on a simple observation: business owners making $500,000 or more per year are systematically overpaying on taxes because their CPAs are filing returns, not building strategies.</p>
                <p>Filing a return is compliance. Strategy is offense. We play offense.</p>
                <p>Our team of tax strategists specializes exclusively in high-income business owners, real estate investors, and medical professionals. We do not prepare basic returns. We do not work with W-2 employees. Every resource we have is dedicated to the unique challenges and opportunities faced by entrepreneurs earning half a million dollars or more.</p>

                <h2>Why We Are Different</h2>
                <p>Traditional CPA firms are compliance-focused. They record what happened and file what is required. That is necessary, but it is not strategy. It is not proactive. And it is not what business owners at your level need.</p>
                <p>At Centurion, every engagement begins with a 3-year lookback. We review your previous three years of returns to identify missed deductions, misclassified income, unclaimed credits, and structural inefficiencies. On average, we recover between $50,000 and $200,000 for our clients before we even begin forward-looking planning.</p>
                <p>From there, we build a comprehensive tax strategy covering entity structure, retirement vehicles, real estate investments, cost segregation, and income timing. Every recommendation is backed by the Internal Revenue Code and built to withstand scrutiny.</p>

                <div class="highlight-box">
                    <p><strong>Our Standard:</strong> If we cannot identify at least $25,000 in recoverable savings from your prior returns or forward-looking strategy, we will tell you. We do not take engagements where we cannot deliver meaningful results.</p>
                </div>

                <h2>Who We Serve</h2>
                <p>Our clients are business owners, practice owners, and investors earning $500,000 or more annually. This includes medical professionals, attorneys, tech founders, e-commerce operators, real estate investors, and franchise owners. If your income is high and your tax situation is complex, you are exactly who we built this firm to serve.</p>

                <h2>Our Values</h2>
                <p><strong>Precision:</strong> Every strategy is rooted in the IRC. We cite the code, we show the math, and we stand behind every recommendation.</p>
                <p><strong>Transparency:</strong> You will know exactly what we are doing, why we are doing it, and what it will cost before we begin.</p>
                <p><strong>Results:</strong> We measure success in dollars recovered and dollars saved. Period.</p>
            </div>
        </div>
    </section>
    """ + get_cta_banner()

    return build_page(
        "About Us | Centurion Tax Strategist",
        "Centurion Tax Strategist is a tax advisory firm for high net worth business owners making $500K+. Learn about our mission, team, and approach to elite tax strategy.",
        "/about/",
        body,
        active_nav="About"
    )


def build_services():
    body = """
    <section class="inner-hero">
        <div class="container">
            <h1>Tax Strategy Services</h1>
            <p>Comprehensive tax advisory designed for business owners earning $500K+. Every service is built to deliver measurable, defensible results.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="grid-3">
                <div class="card">
                    <div class="card-icon">&#128269;</div>
                    <h3>3-Year Tax Lookback</h3>
                    <p>Our flagship service. We review three years of federal and state returns to recover missed deductions and credits. Average recovery: $50K-$200K.</p>
                    <a href="/3-year-tax-lookback/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#127970;</div>
                    <h3>Cost Segregation Studies</h3>
                    <p>Accelerate depreciation on residential and commercial properties. Reclassify components into 5, 7, and 15-year recovery periods for immediate tax savings.</p>
                    <a href="/cost-segregation/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#127959;</div>
                    <h3>Entity Restructuring</h3>
                    <p>S-Corp, C-Corp, LLC, or hybrid structures. We design the optimal entity configuration to minimize your combined tax burden.</p>
                    <a href="/entity-restructuring/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#127968;</div>
                    <h3>STR Tax Strategy</h3>
                    <p>The short-term rental loophole allows real estate losses to offset active income. We structure your STR portfolio for maximum tax benefit.</p>
                    <a href="/short-term-rental-tax-strategy/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#128200;</div>
                    <h3>Real Estate Professional Status</h3>
                    <p>REPS qualification unlocks unlimited passive loss deductions. We help you qualify and document your hours for IRS compliance.</p>
                    <a href="/real-estate-professional-status/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#128220;</div>
                    <h3>IRS Tax Resolution</h3>
                    <p>Unfiled returns, tax penalties, liens, and levies. We negotiate with the IRS on your behalf and resolve outstanding tax issues.</p>
                    <a href="/irs-tax-resolution/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#128178;</div>
                    <h3>Retirement Tax Planning</h3>
                    <p>Solo 401(k), Cash Balance Plans, Defined Benefit Plans, and Roth conversion strategies to shelter current income and build long-term wealth.</p>
                    <a href="/retirement-tax-planning/" class="card-link">Learn More &rarr;</a>
                </div>
                <div class="card">
                    <div class="card-icon">&#128202;</div>
                    <h3>Strategic Tax Planning</h3>
                    <p>Comprehensive annual tax plans covering income timing, estimated payments, entity optimization, and multi-year projections.</p>
                    <a href="/book-strategy-call/" class="card-link">Get Started &rarr;</a>
                </div>
            </div>
        </div>
    </section>
    """ + get_cta_banner()

    return build_page(
        "Tax Strategy Services | Centurion Tax Strategist",
        "Explore Centurion Tax Strategist's services: 3-year lookback, cost segregation, entity restructuring, STR tax strategy, REPS qualification, IRS resolution, and retirement planning for business owners making $500K+.",
        "/services/",
        body,
        active_nav="Services"
    )


# =============================================================================
# INDIVIDUAL SERVICE PAGES
# =============================================================================

SERVICE_PAGES = [
    {
        "slug": "3-year-tax-lookback",
        "title": "3-Year Tax Lookback for Business Owners | Centurion Tax Strategist",
        "meta": "Our 3-year tax lookback reviews your past returns to recover $50K-$200K in missed deductions, credits, and structural savings. For business owners making $500K+.",
        "h1": "The 3-Year Tax Lookback",
        "subtitle": "Our flagship service recovers an average of $50,000 to $200,000 in missed deductions from your prior three years of tax returns.",
        "content": """
            <h2>What Is the 3-Year Tax Lookback?</h2>
            <p>The IRS allows taxpayers to amend returns for up to three prior tax years. Our 3-Year Tax Lookback is a systematic review of every line item on your federal and state returns to identify missed deductions, misclassified income, unclaimed credits, and structural inefficiencies that caused you to overpay.</p>
            <p>This is not a basic review. Our strategists cross-reference your returns against your financial statements, bank records, investment activity, and entity structures. We apply the full Internal Revenue Code, not just the deductions your CPA remembered to take.</p>

            <h2>Who Qualifies?</h2>
            <p>The 3-Year Tax Lookback is designed for business owners, practice owners, and high-income professionals earning $500,000 or more annually. If your tax situation involves any of the following, there is a high probability you are overpaying:</p>
            <ul>
                <li>Business income reported on Schedule C, S-Corp, or partnership returns</li>
                <li>Rental properties or real estate investments</li>
                <li>Multiple entities or holding structures</li>
                <li>Employees or independent contractors</li>
                <li>Equipment purchases or capital expenditures</li>
                <li>Retirement accounts that may be under-optimized</li>
                <li>Out-of-state income or multi-state filing obligations</li>
            </ul>

            <div class="highlight-box">
                <p><strong>Average Recovery:</strong> Our clients recover between $50,000 and $200,000 from their amended returns. The largest single recovery to date exceeded $340,000.</p>
            </div>

            <h2>What We Look For</h2>
            <p>Our review covers every major area of the tax code that applies to high-income business owners. Common findings include:</p>
            <ul>
                <li>Misclassified business expenses that should have been deducted differently</li>
                <li>Missed Section 199A (QBI) deductions or incorrect phase-out calculations</li>
                <li>Unclaimed cost segregation on real estate holdings</li>
                <li>Retirement contributions that were not maximized or were allocated to the wrong vehicle</li>
                <li>Entity structures that create unnecessary self-employment tax</li>
                <li>State tax credits and incentives that were never filed for</li>
                <li>Depreciation schedules that use straight-line when accelerated methods apply</li>
                <li>Charitable contribution strategies that were not optimized</li>
            </ul>

            <h2>Our Process</h2>
            <p><strong>Step 1 - Intake:</strong> You share your prior three years of tax returns, financial statements, and entity documents. We assign a lead strategist to your case.</p>
            <p><strong>Step 2 - Line-by-Line Review:</strong> Our team reviews every schedule, every entity return, and every supporting document. We cross-reference against IRC sections that apply to your specific situation.</p>
            <p><strong>Step 3 - Findings Report:</strong> You receive a detailed report listing every identified recovery, the IRC basis for each claim, and the projected dollar value.</p>
            <p><strong>Step 4 - Amended Returns:</strong> With your approval, we prepare and file amended federal and state returns for each applicable year.</p>
            <p><strong>Step 5 - Forward Strategy:</strong> Every lookback engagement includes a forward-looking tax plan so you never overpay again.</p>

            <h2>Typical Savings by Client Type</h2>
            <ul>
                <li><strong>Medical Practice Owners:</strong> $80,000 - $200,000+</li>
                <li><strong>Tech Company Founders:</strong> $60,000 - $175,000+</li>
                <li><strong>Real Estate Investors (5+ properties):</strong> $100,000 - $250,000+</li>
                <li><strong>E-Commerce Business Owners:</strong> $50,000 - $150,000+</li>
                <li><strong>Law Firm Partners:</strong> $70,000 - $180,000+</li>
            </ul>
        """
    },
    {
        "slug": "cost-segregation",
        "title": "Cost Segregation Studies for Property Owners | Centurion Tax Strategist",
        "meta": "Accelerate depreciation and unlock six-figure tax savings with an IRS-compliant cost segregation study from Centurion Tax Strategist.",
        "h1": "Cost Segregation Studies",
        "subtitle": "Reclassify building components into shorter recovery periods and accelerate depreciation for immediate tax savings.",
        "content": """
            <h2>What Is Cost Segregation?</h2>
            <p>Cost segregation is an IRS-approved tax strategy that allows property owners to reclassify components of a building from the standard 27.5-year (residential) or 39-year (commercial) depreciation schedule into 5-year, 7-year, or 15-year property classes under MACRS.</p>
            <p>By accelerating the depreciation of qualifying components, property owners can take significantly larger deductions in the early years of ownership, reducing taxable income and improving cash flow immediately.</p>

            <h2>How It Works</h2>
            <p>A cost segregation study is an engineering-based analysis of a property. Our team identifies every component that qualifies for reclassification under IRS guidelines, including:</p>
            <ul>
                <li><strong>5-Year Property:</strong> Carpeting, appliances, decorative fixtures, certain electrical components, cabinetry, window treatments</li>
                <li><strong>7-Year Property:</strong> Office furniture, specialized equipment, certain exterior improvements</li>
                <li><strong>15-Year Property:</strong> Land improvements including driveways, sidewalks, landscaping, parking areas, fencing, outdoor lighting</li>
            </ul>

            <div class="highlight-box">
                <p><strong>Example:</strong> A $1.2 million rental property typically generates $43,636 in annual depreciation over 27.5 years. After a cost segregation study, first-year depreciation can exceed $250,000 when combined with bonus depreciation on qualifying components.</p>
            </div>

            <h2>Who Benefits Most?</h2>
            <ul>
                <li>Owners of residential rental properties valued at $300,000+</li>
                <li>Short-term rental (STR) investors who materially participate</li>
                <li>Commercial property owners</li>
                <li>Real estate professionals who can use losses against active income</li>
                <li>Anyone who has purchased, renovated, or constructed a property in the last 15 years</li>
            </ul>

            <h2>Our Cost Segregation Studies</h2>
            <p>Every Centurion cost segregation study is IRS-compliant, audit-ready, and prepared to the standards established by the IRS Cost Segregation Audit Technique Guide. Our studies include detailed component breakdowns, asset classifications, supporting calculations, and all documentation required for a clean audit trail.</p>
        """
    },
    {
        "slug": "entity-restructuring",
        "title": "Entity Restructuring - S-Corp, C-Corp, LLC Optimization | Centurion Tax Strategist",
        "meta": "Optimize your business structure for maximum tax savings. S-Corp, C-Corp, LLC, and hybrid entity restructuring for business owners making $500K+.",
        "h1": "Entity Restructuring",
        "subtitle": "The right entity structure can save you $50,000+ per year. The wrong one costs you every time you file.",
        "content": """
            <h2>Why Entity Structure Matters</h2>
            <p>Your business entity type determines how your income is taxed, how much self-employment tax you pay, what deductions you qualify for, and how effectively you can shelter income. For business owners earning $500,000+, the wrong entity structure can cost $30,000 to $100,000 or more every single year.</p>

            <h2>Common Restructuring Scenarios</h2>
            <p><strong>Sole Proprietor to S-Corp:</strong> If you are operating as a sole proprietor or single-member LLC and earning $100,000+, you are likely overpaying self-employment tax by $10,000-$30,000+ per year. An S-Corp election allows you to split income between reasonable salary and distributions, eliminating excess SE tax.</p>
            <p><strong>S-Corp to C-Corp:</strong> For businesses with significant retained earnings or those that benefit from the flat 21% corporate rate, converting to a C-Corp can create substantial savings. This is especially powerful when combined with fringe benefit strategies and qualified small business stock (QSBS) exclusions under IRC Section 1202.</p>
            <p><strong>Hybrid Structures:</strong> Many high-income business owners benefit from operating multiple entities. A common structure uses an S-Corp for active business income and a separate LLC or LP for real estate holdings, allowing each entity to be taxed optimally.</p>

            <div class="highlight-box">
                <p><strong>Case Study:</strong> A medical practice owner earning $1.2M was operating as a sole proprietor. After restructuring to an S-Corp with a management company and implementing a Cash Balance Plan, total annual tax savings exceeded $142,000.</p>
            </div>

            <h2>What We Evaluate</h2>
            <ul>
                <li>Current entity type and its tax implications</li>
                <li>Self-employment tax exposure</li>
                <li>QBI deduction eligibility and phase-out impact</li>
                <li>State-level entity tax differences</li>
                <li>Retirement plan optimization within each entity</li>
                <li>Reasonable compensation analysis for S-Corp owners</li>
                <li>Exit planning and capital gains treatment</li>
            </ul>
        """
    },
    {
        "slug": "short-term-rental-tax-strategy",
        "title": "Short-Term Rental (STR) Tax Strategy | Centurion Tax Strategist",
        "meta": "Leverage the STR tax loophole to offset W-2 and business income with real estate losses. Expert short-term rental tax strategy for high-income investors.",
        "h1": "Short-Term Rental Tax Strategy",
        "subtitle": "The STR loophole is one of the most powerful tools available to offset W-2 and business income with real estate losses.",
        "content": """
            <h2>The Short-Term Rental Tax Loophole</h2>
            <p>Under IRC Section 469 and Treasury Regulation 1.469-1T(e)(3)(ii), short-term rentals with an average guest stay of 7 days or less are not treated as rental activities for passive loss purposes. When the owner materially participates, the income (and losses) from the STR are treated as non-passive, meaning they can offset W-2 income, business income, and investment income without limit.</p>
            <p>This is one of the most powerful legal tax strategies available to high-income earners. When combined with cost segregation and bonus depreciation, an STR can generate paper losses large enough to offset $100,000 to $300,000+ in active income.</p>

            <h2>How the Strategy Works</h2>
            <p><strong>Step 1:</strong> Acquire a short-term rental property (or convert an existing property to STR use).</p>
            <p><strong>Step 2:</strong> Ensure the average guest stay is 7 days or less (this removes the activity from the passive loss rules).</p>
            <p><strong>Step 3:</strong> Materially participate in the operation of the STR (100+ hours and more than any other individual).</p>
            <p><strong>Step 4:</strong> Perform a cost segregation study to accelerate depreciation.</p>
            <p><strong>Step 5:</strong> Take the resulting paper loss against your active income on your tax return.</p>

            <div class="highlight-box">
                <p><strong>Example:</strong> A business owner earning $800,000 in W-2 income purchases a $750,000 STR property. After cost segregation, the property generates a $180,000 paper loss in year one. Because the STR qualifies as non-passive, that loss offsets $180,000 of W-2 income, saving approximately $66,000 in federal taxes alone.</p>
            </div>

            <h2>Material Participation Requirements</h2>
            <ul>
                <li>You must spend 100+ hours on the activity during the tax year</li>
                <li>No other individual may spend more hours on the activity than you</li>
                <li>Qualifying activities include guest communication, bookings, maintenance coordination, cleaning oversight, pricing, and property management</li>
                <li>You must maintain a contemporaneous log of hours</li>
            </ul>
        """
    },
    {
        "slug": "real-estate-professional-status",
        "title": "Real Estate Professional Status (REPS) | Centurion Tax Strategist",
        "meta": "Qualify as a Real Estate Professional to unlock unlimited passive loss deductions against active income. Expert REPS guidance for high-income investors.",
        "h1": "Real Estate Professional Status",
        "subtitle": "REPS qualification unlocks the ability to deduct unlimited real estate losses against active income, including W-2 and business earnings.",
        "content": """
            <h2>What Is Real Estate Professional Status?</h2>
            <p>Under IRC Section 469(c)(7), taxpayers who qualify as Real Estate Professionals can treat their rental real estate activities as non-passive. This means rental losses, including depreciation and cost segregation deductions, can offset active income without the $25,000 passive loss limitation.</p>
            <p>For high-income real estate investors, REPS is one of the most valuable designations in the tax code. It turns real estate investments into powerful active tax shelters.</p>

            <h2>Qualification Requirements</h2>
            <p>To qualify as a Real Estate Professional, you must meet two tests:</p>
            <ul>
                <li><strong>750-Hour Test:</strong> You must spend more than 750 hours during the tax year in real property trades or businesses in which you materially participate.</li>
                <li><strong>More-Than-Half Test:</strong> More than half of the personal services you perform during the tax year must be in real property trades or businesses.</li>
            </ul>

            <div class="highlight-box">
                <p><strong>Important:</strong> If you have a full-time W-2 job requiring 2,000+ hours per year, it is very difficult to meet the more-than-half test. REPS is most commonly used by spouses who manage real estate full-time or by business owners who can restructure their time allocation.</p>
            </div>

            <h2>How We Help</h2>
            <ul>
                <li>Evaluate your time allocation across all activities to determine REPS eligibility</li>
                <li>Structure your real estate activities to satisfy material participation</li>
                <li>Set up contemporaneous hour tracking systems</li>
                <li>Make the election to aggregate rental activities under IRC Section 469(c)(7)(A)</li>
                <li>Combine REPS with cost segregation to maximize first-year losses</li>
                <li>Prepare documentation that withstands IRS audit</li>
            </ul>
        """
    },
    {
        "slug": "irs-tax-resolution",
        "title": "IRS Tax Resolution Services | Centurion Tax Strategist",
        "meta": "Resolve unfiled returns, IRS penalties, liens, levies, and tax debt. Expert IRS tax resolution for high-income business owners.",
        "h1": "IRS Tax Resolution",
        "subtitle": "Unfiled returns, penalties, and IRS disputes do not get better with time. We resolve them on your behalf.",
        "content": """
            <h2>When You Need IRS Resolution</h2>
            <p>Tax issues with the IRS escalate quickly. What starts as a missed filing or an overlooked notice can turn into penalties, interest, liens on your property, and levies on your bank accounts. For high-income business owners, the stakes are especially high because the IRS prioritizes enforcement against taxpayers with the greatest exposure.</p>

            <h2>What We Handle</h2>
            <ul>
                <li><strong>Unfiled Tax Returns:</strong> If you have one or more years of unfiled federal or state returns, we prepare and file them strategically to minimize your liability.</li>
                <li><strong>IRS Penalties:</strong> We pursue penalty abatement under reasonable cause or first-time abatement programs to reduce or eliminate penalties.</li>
                <li><strong>Tax Liens:</strong> A federal tax lien affects your credit and your ability to sell property. We negotiate lien releases, subordination, and withdrawal.</li>
                <li><strong>Bank Levies and Wage Garnishments:</strong> If the IRS has levied your accounts, we act immediately to get the levy released and negotiate a resolution.</li>
                <li><strong>Offer in Compromise (OIC):</strong> When the full liability cannot be paid, we negotiate with the IRS to settle for less than the full amount owed.</li>
                <li><strong>Installment Agreements:</strong> We negotiate payment plans that are manageable for your cash flow while keeping the IRS from pursuing further collection.</li>
                <li><strong>IRS Audits:</strong> If you are selected for examination, we represent you before the IRS and manage the entire audit process.</li>
            </ul>

            <div class="highlight-box">
                <p><strong>Time Matters:</strong> IRS collection actions escalate on a defined timeline. The sooner you engage professional representation, the more options are available and the better the outcome.</p>
            </div>
        """
    },
    {
        "slug": "retirement-tax-planning",
        "title": "Retirement Tax Planning - Solo 401(k), Cash Balance Plans | Centurion Tax Strategist",
        "meta": "Shelter income and build wealth with Solo 401(k), Cash Balance Plans, and Defined Benefit strategies for high-income business owners.",
        "h1": "Retirement Tax Planning",
        "subtitle": "For high-income business owners, retirement vehicles are one of the most powerful tools to shelter current income while building long-term wealth.",
        "content": """
            <h2>Beyond the Basic 401(k)</h2>
            <p>Most business owners are under-utilizing their retirement options. A standard 401(k) allows $23,500 in employee deferrals (2025), but high-income business owners have access to strategies that can shelter $100,000 to $400,000+ per year in tax-deductible contributions.</p>

            <h2>Strategies We Implement</h2>
            <p><strong>Solo 401(k):</strong> For self-employed business owners and owner-only S-Corps, the Solo 401(k) allows both employee deferrals ($23,500) and employer contributions (up to 25% of compensation), with a combined maximum of $70,000+ per year (2025). Add a Roth component for tax diversification.</p>
            <p><strong>Cash Balance Plan:</strong> A Cash Balance Plan is a type of defined benefit plan that allows dramatically higher contributions than a 401(k) alone. Depending on your age and income, annual deductible contributions can range from $100,000 to $400,000+. Combined with a 401(k), total annual sheltering can exceed $450,000.</p>
            <p><strong>Defined Benefit Plan:</strong> Traditional defined benefit plans offer the highest contribution limits of any retirement vehicle. They are actuarially determined and particularly valuable for business owners aged 45+ with consistent high income.</p>

            <div class="highlight-box">
                <p><strong>Example:</strong> A 52-year-old business owner earning $900,000 implements a Solo 401(k) + Cash Balance Plan combination. Annual deductible contributions total $330,000, reducing taxable income by the same amount and saving approximately $120,000 in federal taxes each year.</p>
            </div>

            <h2>Roth Conversion Strategies</h2>
            <p>For business owners with the right income trajectory, strategic Roth conversions can create tax-free growth for decades. We analyze your lifetime tax picture to determine the optimal conversion schedule, balancing current tax cost against future tax-free distributions.</p>
        """
    },
]


def build_service_page(svc):
    body = f"""
    <section class="inner-hero">
        <div class="container">
            <h1>{svc['h1']}</h1>
            <p>{svc['subtitle']}</p>
        </div>
    </section>

    <section class="section">
        <div class="service-detail">
            {svc['content']}
        </div>
    </section>
    """ + get_cta_banner()

    return build_page(svc['title'], svc['meta'], f"/{svc['slug']}/", body)


# =============================================================================
# FAQ PAGE
# =============================================================================

FAQ_ITEMS = [
    ("What is the 3-Year Tax Lookback?", "The 3-Year Tax Lookback is a comprehensive review of your prior three years of tax returns to identify missed deductions, misclassified income, unclaimed credits, and structural inefficiencies. The IRS allows amended returns for up to three prior tax years, and our average client recovers between $50,000 and $200,000."),
    ("Who is Centurion Tax Strategist for?", "We work exclusively with high net worth business owners, practice owners, and investors earning $500,000 or more per year. Our clients include medical professionals, attorneys, tech founders, real estate investors, e-commerce operators, and franchise owners."),
    ("How is this different from what my CPA does?", "Most CPAs focus on compliance -- filing returns and meeting deadlines. We focus on strategy. We review your returns for missed savings, restructure your entities for optimal taxation, and build forward-looking plans that reduce your tax burden by tens or hundreds of thousands of dollars."),
    ("What does the engagement cost?", "Our advisory engagement is a flat fee based on the complexity of your situation. During your free strategy call, we will outline the expected cost and projected return. We do not take engagements where the expected savings do not significantly exceed the fee."),
    ("How long does the 3-Year Lookback take?", "Typically 2-4 weeks from the time we receive your documents. Complex situations with multiple entities or states may take slightly longer. We prioritize thoroughness over speed because every dollar matters."),
    ("Can you help with IRS issues?", "Yes. We handle unfiled returns, IRS penalties, tax liens, bank levies, offers in compromise, installment agreements, and audit representation. If you have an active IRS issue, we recommend scheduling a call immediately."),
    ("What is cost segregation?", "Cost segregation is an IRS-approved strategy that reclassifies components of a building into shorter depreciation periods (5, 7, or 15 years instead of 27.5 or 39). This accelerates your deductions and significantly reduces your tax bill in the early years of property ownership."),
    ("What is the STR tax loophole?", "Short-term rentals with an average guest stay of 7 days or less are not treated as passive rental activities under IRC Section 469. When the owner materially participates, losses from the STR -- including depreciation from cost segregation -- can offset W-2 and business income without limit."),
    ("Do I need to be a real estate professional?", "Not necessarily. The STR loophole works independently of Real Estate Professional Status. However, REPS provides additional benefits for long-term rental properties by allowing those losses to offset active income as well. We evaluate both strategies based on your situation."),
    ("What is entity restructuring?", "Entity restructuring involves changing your business legal structure to optimize taxation. Common examples include converting from a sole proprietorship to an S-Corp to reduce self-employment tax, or adding a C-Corp for fringe benefits and the 21% flat rate."),
    ("Can you work with my existing CPA?", "Absolutely. Many of our clients keep their CPA for day-to-day compliance and bookkeeping while we handle strategic planning, lookback reviews, and entity optimization. We coordinate directly with your CPA to ensure seamless implementation."),
    ("What states do you serve?", "We serve business owners in all 50 states. Our services are delivered remotely, and we have expertise in state-specific tax codes, credits, and filing requirements across the country."),
    ("How do I get started?", "Schedule a free 30-minute strategy call. We will review your situation, identify the most likely areas of savings, and explain our process. There is no obligation and no pressure."),
    ("What is a Cash Balance Plan?", "A Cash Balance Plan is a type of defined benefit retirement plan that allows business owners to make tax-deductible contributions of $100,000 to $400,000+ per year, depending on age and income. It is one of the most powerful income-sheltering tools available."),
    ("How much can I save with a cost segregation study?", "Savings depend on property value and type. As a general rule, cost segregation reclassifies 20-40% of a property's value into shorter depreciation periods. On a $1 million property, this can generate $60,000-$120,000+ in accelerated first-year deductions."),
    ("Is the 3-Year Lookback risky? Will it trigger an audit?", "Amended returns are routine and do not increase audit risk by themselves. Every claim we make is backed by the Internal Revenue Code, fully documented, and prepared to audit-ready standards. We stand behind every filing."),
    ("What if my CPA already did a good job?", "We hear this often, and the answer may surprise you. Even excellent CPAs miss deductions because compliance and strategy are different disciplines. Our lookback regularly finds $50,000+ in savings for clients who had competent CPAs. The free strategy call will give you a clear answer."),
    ("Do you handle estate and gift tax planning?", "Our focus is on income tax strategy for business owners. We partner with estate planning attorneys and can coordinate on wealth transfer strategies, but we do not directly provide estate or gift tax filing services."),
    ("How do estimated tax payments work with your strategies?", "When we restructure entities or implement new strategies mid-year, we recalculate your estimated tax obligations to reflect the changes. This ensures you are not overpaying quarterly and that your cash flow reflects your actual liability."),
    ("What documentation do I need to provide?", "To get started, we need your last three years of federal and state tax returns, business financial statements, any entity formation documents, and information about real estate holdings. We provide a secure document portal and a detailed checklist after your strategy call."),
]

def build_faq():
    faq_schema_items = []
    faq_html = ""
    for q, a in FAQ_ITEMS:
        faq_html += f"""
        <div class="faq-item">
            <div class="faq-question">{q}</div>
            <div class="faq-answer">{a}</div>
        </div>
        """
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    schema = f"""
    <script type="application/ld+json">
    {json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema_items}, indent=2)}
    </script>"""

    body = f"""
    <section class="inner-hero">
        <div class="container">
            <h1>Frequently Asked Questions</h1>
            <p>Answers to the most common questions about our tax strategy services.</p>
        </div>
    </section>

    <section class="section">
        <div class="container" style="max-width:800px;">
            {faq_html}
        </div>
    </section>
    """ + get_cta_banner()

    return build_page(
        "FAQ | Centurion Tax Strategist",
        "Frequently asked questions about Centurion Tax Strategist's services, including the 3-year lookback, cost segregation, entity restructuring, and more.",
        "/faq/",
        body,
        schema=schema,
        active_nav="FAQ"
    )


# =============================================================================
# CONTACT / BOOK A CALL
# =============================================================================

def build_booking():
    body = f"""
    <section class="inner-hero">
        <div class="container">
            <h1>Book Your Strategy Call</h1>
            <p>Schedule a complimentary 30-minute call with one of our tax strategists. No obligation, no pressure. Just a clear assessment of your situation.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="booking-frame">
                <h2>Schedule Your Free Consultation</h2>
                <p>During this call, we will review your current tax situation, identify the most likely areas of savings, and explain how our 3-Year Lookback and strategic planning process works.</p>
                <a href="tel:{PHONE}" class="hero-cta">Call {PHONE}</a>
                <p style="margin-top:16px;font-size:14px;color:var(--gray);">Or email us at <a href="mailto:{EMAIL}">{EMAIL}</a></p>
            </div>

            <div class="contact-info">
                <div class="contact-box">
                    <h4>Phone</h4>
                    <p><a href="tel:{PHONE}">{PHONE}</a></p>
                </div>
                <div class="contact-box">
                    <h4>Email</h4>
                    <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
                </div>
                <div class="contact-box">
                    <h4>Office</h4>
                    <p>{ADDRESS_STREET}<br>{ADDRESS_CITY}, {ADDRESS_STATE} {ADDRESS_ZIP}</p>
                </div>
            </div>
        </div>
    </section>
    """

    return build_page(
        "Book a Strategy Call | Centurion Tax Strategist",
        "Schedule a free 30-minute tax strategy consultation with Centurion Tax Strategist. We help business owners making $500K+ recover missed deductions and optimize their tax position.",
        "/book-strategy-call/",
        body
    )


# =============================================================================
# REVIEWS PAGE
# =============================================================================

REVIEWS = [
    {"name": "David M.", "role": "Orthopedic Surgery Practice Owner", "text": "They recovered $147,000 in missed deductions from my last three years of returns. My previous CPA had no idea these credits existed. Centurion is in a different league.", "rating": 5},
    {"name": "Sarah T.", "role": "Tech Company Founder, Series B", "text": "The entity restructuring alone saved us $82,000 in the first year. They moved us from an LLC taxed as a partnership to an S-Corp with a management company, and the numbers were immediate.", "rating": 5},
    {"name": "James & Laura K.", "role": "Real Estate Investors, 12 Properties", "text": "Between cost segregation and the STR strategy, we offset nearly all of our W-2 income. We went from writing a $180,000 check to the IRS to getting a refund. Centurion is worth every penny.", "rating": 5},
    {"name": "Dr. Robert F.", "role": "Gastroenterology Practice, 6 Physicians", "text": "We brought Centurion in to review what our CPA had been doing. They found $210,000 in recoverable savings across three years. Our CPA is excellent at compliance but had never looked at strategy the way Centurion does.", "rating": 5},
    {"name": "Michelle P.", "role": "E-Commerce Brand Owner", "text": "I was paying $340,000 a year in taxes on $1.1M in income. After Centurion restructured my entities and implemented a Cash Balance Plan, my effective rate dropped by almost 15 points. The ROI on their fee was over 20x.", "rating": 5},
    {"name": "Brian & Carla N.", "role": "Franchise Owners, 8 Locations", "text": "Managing taxes across eight franchise locations in three states was a nightmare. Centurion cleaned up our entity structure, optimized state filing positions, and recovered $93,000 from amended returns. They handle everything.", "rating": 5},
    {"name": "Dr. Anita S.", "role": "Dermatology Practice Owner", "text": "The Cash Balance Plan alone shelters $280,000 a year for me. Combined with the cost seg on my office building, I have saved more in the first year with Centurion than I paid my previous CPA over the last decade.", "rating": 5},
    {"name": "Mark L.", "role": "Attorney, Managing Partner", "text": "Our firm has 12 partners and complex K-1 allocations. Centurion reviewed our structure and found opportunities none of our accountants had identified. The lookback recovered $168,000 across three years for me personally.", "rating": 5},
    {"name": "Kevin W.", "role": "SaaS Company CEO", "text": "I was skeptical because I already had a Big 4 firm doing my business returns. Centurion found $74,000 in the lookback and restructured my compensation to save another $55,000 annually. I should have done this years ago.", "rating": 5},
    {"name": "Rachel & Tom D.", "role": "Real Estate Developers", "text": "Centurion ran cost segregation studies on four of our properties and generated over $1.1 million in accelerated depreciation. That completely changed our tax picture for the next several years. Absolutely elite service.", "rating": 5},
]

def build_reviews():
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": SITE_NAME,
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": str(len(REVIEWS)),
            "bestRating": "5"
        },
        "review": [
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": r["name"]},
                "reviewRating": {"@type": "Rating", "ratingValue": str(r["rating"]), "bestRating": "5"},
                "reviewBody": r["text"]
            }
            for r in REVIEWS
        ]
    }, indent=2)

    reviews_html = ""
    for r in REVIEWS:
        stars = "&#9733;" * r["rating"]
        reviews_html += f"""
        <div class="testimonial">
            <div class="stars">{stars}</div>
            <p>{r['text']}</p>
            <div class="author">{r['name']}</div>
            <div class="role">{r['role']}</div>
        </div>
        """

    body = f"""
    <section class="inner-hero">
        <div class="container">
            <h1>Client Reviews</h1>
            <p>Hear from business owners who have worked with Centurion Tax Strategist to recover missed deductions and build tax strategies that protect their wealth.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="grid-2">
                {reviews_html}
            </div>
        </div>
    </section>

    <script type="application/ld+json">
    {schema}
    </script>
    """ + get_cta_banner()

    return build_page(
        "Client Reviews | Centurion Tax Strategist",
        "Read reviews from high net worth business owners who recovered $50K-$200K+ through Centurion Tax Strategist's 3-year lookback and tax strategy services.",
        "/reviews/",
        body,
        active_nav="Reviews"
    )


# =============================================================================
# BLOG
# =============================================================================

BLOG_POSTS = [
    {
        "slug": "3-year-tax-lookback-recover-missed-deductions",
        "title": "The 3-Year Tax Lookback: How Business Owners Recover $50K-$200K in Missed Deductions",
        "meta": "Learn how the 3-year tax lookback helps business owners making $500K+ recover tens of thousands in missed deductions from prior tax returns.",
        "date": "2026-04-15",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>If you are a business owner earning $500,000 or more per year, there is a high probability that your last three years of tax returns contain missed deductions worth tens of thousands of dollars. Not because your CPA is incompetent, but because compliance-focused tax preparation and proactive tax strategy are two entirely different disciplines.</p>

            <h2>What Is the 3-Year Tax Lookback?</h2>
            <p>The IRS allows taxpayers to file amended returns for up to three prior tax years. The 3-Year Tax Lookback is a systematic, line-by-line review of your federal and state returns to identify every missed deduction, misclassified expense, unclaimed credit, and structural inefficiency that caused you to overpay.</p>
            <p>This is not a cursory review. It is a deep-dive analysis that cross-references your returns against your financial statements, entity structures, investment activity, and the full Internal Revenue Code.</p>

            <h2>Why Business Owners Overpay</h2>
            <p>The tax code is over 75,000 pages long. It changes every year. And the strategies available to high-income business owners are fundamentally different from those available to W-2 employees. Most CPAs are trained in compliance, meaning they know how to accurately report income and deductions on the correct forms. What they often miss are the strategic opportunities that require proactive planning.</p>

            <h3>Common Missed Deductions</h3>
            <p>In our experience reviewing hundreds of business owner returns, the most frequently missed items include Section 199A (QBI) deduction optimization, retirement contribution maximization, cost segregation on real estate holdings, entity structure optimization to reduce self-employment tax, state-specific credits and incentives, depreciation method selection, and home office deductions that were claimed incorrectly or not at all.</p>

            <h2>How the Process Works</h2>
            <p>The lookback process begins with document collection. We request your prior three years of tax returns, business financial statements, and entity formation documents. From there, our team conducts the review, produces a detailed findings report, and prepares amended returns for any year where recoverable savings are identified.</p>
            <p>The average engagement takes 2-4 weeks and recovers between $50,000 and $200,000. Our largest single recovery exceeded $340,000.</p>

            <h2>Is It Worth It?</h2>
            <p>Consider this: if you have been earning $500,000+ for the last three years and your CPA has been filing returns without conducting a strategic review, the question is not whether you are overpaying. The question is how much. A free strategy call with our team will give you a clear answer within 30 minutes.</p>
        """
    },
    {
        "slug": "why-your-cpa-is-leaving-money-on-the-table",
        "title": "Why Your CPA Is Leaving Money on the Table (And What to Do About It)",
        "meta": "Your CPA files accurate returns, but accuracy is not strategy. Learn why high-income business owners need a tax strategist in addition to a CPA.",
        "date": "2026-04-10",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>Your CPA is probably doing a fine job. The returns are filed on time. The numbers are accurate. You have not been audited. So what is the problem?</p>
            <p>The problem is that accuracy is not strategy. Filing a correct return and filing an optimized return are two very different things. And for business owners making $500,000 or more per year, the gap between the two can be worth $50,000 to $200,000 every single year.</p>

            <h2>Compliance vs. Strategy</h2>
            <p>Tax compliance means recording what happened, calculating what is owed, and filing the correct forms by the deadline. It is reactive by nature. Your CPA looks at last year and reports it.</p>
            <p>Tax strategy means structuring your income, entities, deductions, and investments to minimize your total lifetime tax burden. It is proactive. A strategist looks at the next 5-10 years and builds a plan.</p>

            <h2>What Your CPA Likely Misses</h2>
            <p>Entity structure optimization is the most common gap. Many business owners operate as sole proprietors or single-member LLCs when an S-Corp election would save $20,000-$50,000+ per year in self-employment taxes. Your CPA may not have recommended this because entity restructuring is not part of annual compliance work.</p>
            <p>Retirement vehicle optimization is another frequent miss. Standard 401(k) contributions are straightforward, but combining a Solo 401(k) with a Cash Balance Plan can shelter $200,000-$400,000+ per year. Most CPAs do not design retirement plans.</p>
            <p>Cost segregation, the STR loophole, strategic charitable giving, income timing across tax years, and state tax optimization are all areas where proactive planning creates massive value that reactive compliance cannot capture.</p>

            <h2>What You Should Do</h2>
            <p>The best approach for most high-income business owners is to keep your CPA for compliance and add a tax strategist for planning. The two roles complement each other. Your CPA handles the filing. Your strategist handles the thinking. The result is a tax position that is both accurate and optimized.</p>
        """
    },
    {
        "slug": "cost-segregation-guide-high-income-property-owners",
        "title": "Cost Segregation for High-Income Property Owners: A Complete Guide",
        "meta": "A complete guide to cost segregation studies for high-income property owners. Learn how to accelerate depreciation and save six figures in taxes.",
        "date": "2026-04-05",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>Cost segregation is one of the most powerful tax strategies available to property owners, yet it remains underutilized by most real estate investors and business owners. If you own property valued at $300,000 or more, a cost segregation study could generate $60,000 to $250,000+ in accelerated first-year deductions.</p>

            <h2>Understanding Cost Segregation</h2>
            <p>When you purchase or construct a building, the IRS requires you to depreciate it over a set period: 27.5 years for residential property or 39 years for commercial property. This means you get a small, equal deduction each year spread over decades.</p>
            <p>Cost segregation changes this by identifying components of the building that qualify for shorter depreciation periods. Carpeting, appliances, cabinetry, decorative fixtures, and certain electrical and plumbing components can be reclassified as 5-year property. Landscaping, driveways, sidewalks, and fencing qualify as 15-year property.</p>

            <h2>The Impact of Bonus Depreciation</h2>
            <p>Cost segregation becomes even more powerful when combined with bonus depreciation. Under current tax law, qualifying assets can receive first-year bonus depreciation, allowing you to deduct a significant percentage of the reclassified value in the year the study is completed. This creates massive paper losses that can offset other income.</p>

            <h2>Who Should Get a Cost Segregation Study?</h2>
            <p>Any property owner with buildings valued at $300,000 or more should evaluate cost segregation. This includes residential rental property owners, short-term rental operators, commercial property owners, medical and dental practice owners who own their buildings, and anyone who has completed significant renovations.</p>

            <h2>The Lookback Opportunity</h2>
            <p>If you have owned property for years without a cost segregation study, you have not missed your chance. A lookback cost segregation study allows you to claim all the accelerated depreciation you would have taken in prior years as a single catch-up deduction in the current year, without amending prior returns. This is done through a change in accounting method (Form 3115) and can generate a deduction worth hundreds of thousands of dollars.</p>
        """
    },
    {
        "slug": "s-corp-vs-c-corp-which-saves-more",
        "title": "S-Corp vs C-Corp: Which Structure Saves You More?",
        "meta": "S-Corp vs C-Corp comparison for high-income business owners. Learn which entity structure minimizes your total tax burden.",
        "date": "2026-03-28",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>The choice between S-Corp and C-Corp taxation is one of the most consequential decisions a business owner can make. For high-income earners, the wrong choice can cost $30,000 to $100,000+ per year. Here is how to think about it.</p>

            <h2>S-Corp Basics</h2>
            <p>An S-Corp is a pass-through entity. Business income flows through to your personal return and is taxed at your individual rate. The primary advantage is that only your reasonable salary is subject to payroll taxes (Social Security and Medicare). Distributions above your salary are not subject to self-employment tax, saving 15.3% on every dollar distributed.</p>
            <p>For a business owner earning $500,000 with a reasonable salary of $150,000, the S-Corp election saves approximately $26,000 per year in payroll taxes compared to operating as a sole proprietor.</p>

            <h2>C-Corp Basics</h2>
            <p>A C-Corp is taxed as a separate entity at a flat 21% rate. Profits are taxed at the corporate level, and any distributions to shareholders (dividends) are taxed again at the individual level. This double taxation is the primary drawback.</p>
            <p>However, the C-Corp offers unique advantages for the right situation. The flat 21% rate is significantly lower than the top individual rate. C-Corps can deduct fringe benefits (health insurance, retirement, education) more broadly. And IRC Section 1202 (QSBS) can exclude up to $10 million in capital gains when selling qualifying C-Corp stock held for 5+ years.</p>

            <h2>When to Choose Each</h2>
            <p>The S-Corp is generally better when you need to distribute most of the profits to yourself, your income pushes you into the highest individual brackets, and you want simplicity with a single level of taxation. The C-Corp is generally better when you can retain significant earnings in the business, you want to maximize fringe benefits, you plan to sell the business and can qualify for QSBS, and the business has significant reinvestment needs.</p>

            <h2>The Hybrid Approach</h2>
            <p>Many of our clients use both. A common structure is an S-Corp for active business operations (avoiding payroll tax on distributions) with a C-Corp management company that provides services to the S-Corp and retains earnings at the 21% rate. This gives you the best of both worlds.</p>
        """
    },
    {
        "slug": "business-owners-500k-cut-tax-bill-in-half",
        "title": "How Business Owners Making $500K+ Can Legally Cut Their Tax Bill in Half",
        "meta": "Proven strategies for business owners making $500K+ to legally reduce their tax bill by 40-50%. Entity restructuring, retirement plans, cost segregation, and more.",
        "date": "2026-03-20",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>If you are a business owner earning $500,000 or more per year, your combined federal and state tax rate probably lands between 40% and 50%. That means you are sending $200,000 to $250,000 to the government every year. Much of that is avoidable with the right strategy.</p>

            <h2>The Tax Reduction Framework</h2>
            <p>Reducing your tax bill by 40-50% does not come from a single trick. It comes from layering multiple legitimate strategies, each one reducing a portion of your taxable income or shifting income into lower-taxed categories. Here is the framework we use with every client.</p>

            <h3>Layer 1: Entity Restructuring</h3>
            <p>If you are not operating through an S-Corp (or the right combination of entities), you are likely overpaying self-employment tax by $20,000-$50,000 per year. This is the foundation.</p>

            <h3>Layer 2: Retirement Vehicles</h3>
            <p>A Solo 401(k) combined with a Cash Balance Plan can shelter $200,000-$400,000+ per year in tax-deductible contributions. This is the single largest lever most business owners have.</p>

            <h3>Layer 3: Real Estate Strategies</h3>
            <p>Cost segregation, the STR loophole, and REPS allow property owners to generate massive paper losses that offset business and W-2 income. A single STR with cost segregation can create $100,000-$200,000+ in deductions in year one.</p>

            <h3>Layer 4: Income Timing and Structure</h3>
            <p>Deferring income into future years, accelerating deductions into the current year, and strategically timing capital gains and losses can smooth your tax burden across years and reduce your lifetime effective rate.</p>

            <h3>Layer 5: Charitable Strategies</h3>
            <p>Donor-Advised Funds, Charitable Remainder Trusts, and strategic appreciated stock donations can reduce taxable income while achieving philanthropic goals.</p>

            <h2>Putting It All Together</h2>
            <p>When you layer these strategies, the combined effect can reduce your effective tax rate from 40-50% down to 20-25%. On $500,000 of income, that is $100,000+ per year kept in your pocket instead of sent to the IRS. Over a decade, the difference compounds into millions of dollars in retained wealth.</p>
        """
    },
    {
        "slug": "short-term-rental-tax-loophole-investors",
        "title": "The Short-Term Rental Tax Loophole Every Investor Should Know",
        "meta": "How the STR tax loophole lets real estate investors offset W-2 and business income with rental losses. A complete guide for high-income investors.",
        "date": "2026-03-12",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>The short-term rental tax loophole is one of the most powerful tools available to high-income investors. It allows real estate losses to offset W-2 income, business income, and investment income without limit. Here is how it works, who qualifies, and how to implement it.</p>

            <h2>Why Short-Term Rentals Are Different</h2>
            <p>Under the standard passive activity rules (IRC Section 469), rental real estate is treated as a passive activity. Losses from passive activities can only offset passive income, with a limited $25,000 exception for active participants earning under $150,000 AGI.</p>
            <p>Short-term rentals are the exception. Under Treasury Regulation 1.469-1T(e)(3)(ii), a rental activity where the average customer use is 7 days or less is not treated as a rental activity for passive loss purposes. This single distinction changes everything.</p>

            <h2>The Tax Math</h2>
            <p>Consider a business owner earning $600,000 in W-2 income who purchases a $700,000 short-term rental property. After a cost segregation study, the property generates approximately $160,000 in first-year depreciation deductions. Because the STR qualifies as non-passive, that $160,000 loss offsets W-2 income directly, saving approximately $59,000 in federal taxes.</p>
            <p>The property still generates rental cash flow. The loss is a paper loss created by accelerated depreciation. You are reducing your taxes while the property appreciates and produces income.</p>

            <h2>Implementation Checklist</h2>
            <p>To successfully execute this strategy, you need to acquire or designate a property for short-term rental use. Ensure the average guest stay is 7 days or less for the tax year. Materially participate in the operation by spending 100+ hours per year and more than any other individual. Commission a cost segregation study to accelerate depreciation. Maintain a contemporaneous activity log documenting your hours. File your return with the loss properly classified as non-passive.</p>

            <h2>Common Mistakes to Avoid</h2>
            <p>The most common mistake is failing to maintain an activity log. The IRS will challenge material participation if you cannot produce contemporaneous records. The second most common mistake is miscalculating the average stay length by including stays over 7 days that disqualify the property. Work with a tax strategist who understands these rules to ensure compliance.</p>
        """
    },
    {
        "slug": "entity-restructuring-when-to-change-business-structure",
        "title": "Entity Restructuring: When to Change Your Business Structure",
        "meta": "When and how to restructure your business entity for tax savings. S-Corp elections, C-Corp conversions, and hybrid structures for business owners.",
        "date": "2026-03-05",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>Your business entity structure has a direct impact on how much you pay in taxes every year. For business owners earning $500,000+, the wrong structure can cost $30,000 to $100,000 annually. Here is when and how to restructure.</p>

            <h2>Signs You Need to Restructure</h2>
            <p>Several indicators suggest your current entity structure is costing you money. If you are operating as a sole proprietor and earning over $100,000, you are almost certainly overpaying self-employment tax. If your S-Corp reasonable salary has not been reviewed in years, it may be too high or too low. If you are retaining significant earnings but paying pass-through rates, a C-Corp may save you money. If you own real estate inside the same entity as your operating business, you are creating unnecessary liability and tax exposure.</p>

            <h2>Common Restructuring Moves</h2>
            <p>The most common restructuring we implement is the sole proprietor or LLC to S-Corp conversion. This is done by filing Form 2553 and allows you to split income between salary (subject to payroll tax) and distributions (not subject to payroll tax). For a business owner earning $400,000 with a reasonable salary of $120,000, this saves approximately $21,000 per year.</p>
            <p>For businesses with high retained earnings, we often implement a C-Corp management company. The operating entity (S-Corp) pays management fees to the C-Corp, which are taxed at the flat 21% rate. This creates a split-rate structure where a portion of income is taxed at 21% instead of 37%.</p>

            <h2>Timing Considerations</h2>
            <p>S-Corp elections are generally most effective when made at the beginning of a tax year. Late elections are possible under Rev. Proc. 2013-30 but require additional documentation. C-Corp conversions require careful analysis of built-in gains, accumulated earnings, and the impact on existing agreements.</p>
            <p>The bottom line: if you have not reviewed your entity structure in the last 2-3 years and your income has changed, it is time for a review.</p>
        """
    },
    {
        "slug": "tax-planning-doctors-attorneys-high-income-professionals",
        "title": "Tax Planning for Doctors, Attorneys, and High-Income Professionals",
        "meta": "Specialized tax planning strategies for doctors, attorneys, and high-income professionals making $500K+. Entity structuring, retirement plans, and real estate strategies.",
        "date": "2026-02-25",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>Doctors, attorneys, and other high-income professionals face unique tax challenges. Your income is high, your deductions are often limited, and traditional tax planning advice rarely applies to someone earning $500,000 to $2 million or more per year.</p>

            <h2>The High-Income Professional Tax Problem</h2>
            <p>As a high-income professional, you face a particularly frustrating tax situation. Your income is too high for most credits and deductions (many phase out above $250,000-$400,000 AGI). Your income is primarily earned income, which is taxed at the highest rates. The 3.8% Net Investment Income Tax applies to investment returns. And the 0.9% Additional Medicare Tax kicks in on earnings above $200,000/$250,000.</p>
            <p>The result: effective tax rates of 40-50% that leave you feeling like no matter how much you earn, you can never get ahead.</p>

            <h2>Strategies That Work for Professionals</h2>
            <p>Entity optimization is the starting point. If you own your practice, the S-Corp election is typically the most impactful single change. Combined with reasonable compensation analysis, it can save $25,000-$60,000+ per year.</p>
            <p>Retirement plan maximization is the next layer. Beyond the standard 401(k), a Cash Balance Plan can shelter $150,000-$350,000+ per year in tax-deductible contributions. For a 50-year-old physician earning $800,000, this can reduce taxable income by more than a third.</p>
            <p>Real estate investment, particularly short-term rentals with cost segregation, provides a powerful offset for professional income. The STR loophole allows paper losses from real estate to offset practice income directly.</p>

            <h2>The Physician-Specific Advantage</h2>
            <p>Physicians often own their practice buildings. A cost segregation study on a medical office building can reclassify 15-25% of the building value into shorter depreciation periods, generating an immediate deduction of $100,000-$300,000+ depending on building value. Combined with the strategies above, total annual tax savings can exceed $150,000.</p>
        """
    },
    {
        "slug": "bonus-depreciation-2026-property-owners",
        "title": "Bonus Depreciation in 2026: What Property Owners Need to Know",
        "meta": "Bonus depreciation rates are changing in 2026. What property owners need to know about the phase-down and how to maximize remaining benefits.",
        "date": "2026-02-18",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>Bonus depreciation has been one of the most valuable tax tools for property owners over the past several years. Under the Tax Cuts and Jobs Act of 2017, qualifying assets received 100% first-year bonus depreciation through 2022. Since then, the rate has been phasing down, and property owners need to understand the current landscape to make informed decisions.</p>

            <h2>The Bonus Depreciation Phase-Down</h2>
            <p>The TCJA established a five-year phase-down schedule for bonus depreciation. 100% applied through 2022, then 80% in 2023, 60% in 2024, 40% in 2025, and 20% in 2026. Without legislative action, bonus depreciation drops to 0% in 2027.</p>
            <p>For property owners, this means 2026 is one of the last years to capture any first-year bonus depreciation on qualifying assets. The window is closing.</p>

            <h2>What Qualifies for Bonus Depreciation</h2>
            <p>Bonus depreciation applies to assets with a recovery period of 20 years or less. In the context of real estate, this includes all the assets identified in a cost segregation study: 5-year property (appliances, carpeting, fixtures), 7-year property (furniture, equipment), and 15-year property (land improvements, landscaping, driveways).</p>
            <p>The building structure itself (27.5 or 39-year property) does not qualify. This is exactly why cost segregation is so important. It separates out the qualifying components so they can receive bonus depreciation.</p>

            <h2>What Property Owners Should Do Now</h2>
            <p>If you own property and have not completed a cost segregation study, the time to act is now. Every year you wait, the bonus depreciation rate drops further. Properties purchased or placed in service in 2026 can still capture the remaining bonus on qualifying components.</p>
            <p>For properties you have owned for years, a lookback cost segregation study can capture all missed accelerated depreciation as a single catch-up deduction in the current year through Form 3115 (change in accounting method). This does not require amending prior returns and is taken entirely in the current tax year.</p>

            <h2>Legislative Outlook</h2>
            <p>There has been ongoing congressional discussion about restoring 100% bonus depreciation. Several proposals have been introduced, but as of early 2026, no legislation has been enacted. Property owners should plan based on current law while remaining aware that the landscape could change.</p>
        """
    },
    {
        "slug": "5-tax-strategies-business-owners-cpas-wont-tell",
        "title": "5 Tax Strategies for Business Owners That Most CPAs Won't Tell You",
        "meta": "Five advanced tax strategies most CPAs do not proactively recommend. From the STR loophole to Cash Balance Plans, learn what your CPA is missing.",
        "date": "2026-02-10",
        "author": "Centurion Tax Strategy Team",
        "content": """
            <p>Most CPAs are competent, ethical professionals who file accurate returns. But competent compliance and proactive strategy are different skill sets. Here are five strategies that can save business owners $50,000 to $200,000+ per year that most CPAs never bring to the table.</p>

            <h2>1. The Short-Term Rental Loophole</h2>
            <p>Short-term rentals with an average guest stay of 7 days or less are not classified as passive rental activities. When you materially participate, the losses (including massive depreciation from cost segregation) can offset your W-2 and business income directly. A single STR can generate $100,000-$200,000+ in paper losses that reduce your tax bill immediately. Most CPAs have never structured this strategy for a client.</p>

            <h2>2. Cash Balance Plans</h2>
            <p>A standard 401(k) lets you defer $23,500 per year (2025). A Cash Balance Plan, stacked on top of a 401(k), can shelter an additional $100,000 to $350,000+ per year in tax-deductible contributions depending on your age. For a 50-year-old business owner, total annual retirement contributions can exceed $400,000. Most CPAs do not design retirement plans and will never suggest this unprompted.</p>

            <h2>3. The Augusta Rule (Section 280A)</h2>
            <p>IRC Section 280A(g) allows you to rent your personal residence to your business for up to 14 days per year and receive the rental income tax-free. The business deducts the rent as an expense, and you pay zero tax on the income received. For high-income business owners, this creates $10,000-$20,000+ in annual tax-free income. It is perfectly legal, well-established, and almost never recommended by compliance-focused CPAs.</p>

            <h2>4. Lookback Cost Segregation (Form 3115)</h2>
            <p>If you have owned property for years without a cost segregation study, you can file Form 3115 to claim all the accelerated depreciation you missed as a single catch-up deduction in the current year. No amended returns needed. A single lookback study can generate $100,000-$500,000+ in deductions in one year. This is one of the most underutilized tools in the tax code.</p>

            <h2>5. C-Corp Management Company Structure</h2>
            <p>By creating a C-Corp management company that provides services to your S-Corp operating entity, you can shift a portion of income to the flat 21% corporate rate while deducting management fees from the S-Corp. Combined with C-Corp fringe benefits (health insurance, education, dependent care), this structure can save $20,000-$50,000+ annually for business owners in the top bracket.</p>

            <h2>Why Your CPA Does Not Recommend These</h2>
            <p>It is not malice. It is scope. Compliance CPAs are measured by accuracy and timeliness, not by how much money they save you. These strategies require proactive analysis, ongoing monitoring, and specialized knowledge that falls outside the scope of most tax preparation engagements. This is exactly why high-income business owners benefit from adding a dedicated tax strategist to their team.</p>
        """
    },
]


def build_blog_index():
    cards = ""
    for post in BLOG_POSTS:
        d = datetime.strptime(post["date"], "%Y-%m-%d").strftime("%B %d, %Y")
        cards += f"""
        <div class="blog-card">
            <div class="blog-card-body">
                <div class="blog-card-meta">{d} &middot; {post['author']}</div>
                <h3><a href="/blog/{post['slug']}/">{post['title']}</a></h3>
                <p>{post['meta']}</p>
                <a href="/blog/{post['slug']}/" class="card-link">Read Article &rarr;</a>
            </div>
        </div>
        """

    body = f"""
    <section class="inner-hero">
        <div class="container">
            <h1>Tax Strategy Blog</h1>
            <p>Insights, strategies, and analysis for business owners earning $500K+.</p>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <div class="grid-2">
                {cards}
            </div>
        </div>
    </section>
    """

    return build_page(
        "Tax Strategy Blog | Centurion Tax Strategist",
        "Expert tax strategy articles for high net worth business owners. Cost segregation, entity restructuring, STR strategies, retirement planning, and more.",
        "/blog/",
        body,
        active_nav="Blog"
    )


def build_blog_post(post):
    d = datetime.strptime(post["date"], "%Y-%m-%d").strftime("%B %d, %Y")

    schema = f"""
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{post['title']}",
        "description": "{post['meta']}",
        "datePublished": "{post['date']}",
        "dateModified": "{post['date']}",
        "author": {{
            "@type": "Organization",
            "name": "{SITE_NAME}"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "{SITE_NAME}",
            "url": "{SITE_URL}"
        }},
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "{SITE_URL}/blog/{post['slug']}/"
        }}
    }}
    </script>"""

    body = f"""
    <section class="article-hero">
        <div class="container">
            <div class="article-meta">{d} &middot; {post['author']}</div>
            <h1>{post['title']}</h1>
        </div>
    </section>

    <article class="article-body">
        {post['content']}
    </article>
    """ + get_cta_banner()

    return build_page(
        f"{post['title']} | {SITE_NAME}",
        post['meta'],
        f"/blog/{post['slug']}/",
        body,
        og_type="article",
        schema=schema
    )


# =============================================================================
# SITEMAP & ROBOTS
# =============================================================================

def build_sitemap(pages):
    urls = ""
    for page in pages:
        priority = "1.0" if page == "/" else ("0.8" if "/blog/" not in page or page == "/blog/" else "0.7")
        urls += f"""  <url>
    <loc>{SITE_URL}{page}</loc>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""


def build_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


# =============================================================================
# MAIN - GENERATE EVERYTHING
# =============================================================================

def write_file(path, content):
    full_path = os.path.join(OUTPUT_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Created: {path}")


def main():
    print("=" * 60)
    print("Centurion Tax Strategist - Site Generator")
    print("=" * 60)

    all_pages = []

    # Homepage
    print("\nGenerating pages...")
    write_file("index.html", build_homepage())
    all_pages.append("/")

    # About
    write_file("about/index.html", build_about())
    all_pages.append("/about/")

    # Services
    write_file("services/index.html", build_services())
    all_pages.append("/services/")

    # Individual service pages
    for svc in SERVICE_PAGES:
        write_file(f"{svc['slug']}/index.html", build_service_page(svc))
        all_pages.append(f"/{svc['slug']}/")

    # FAQ
    write_file("faq/index.html", build_faq())
    all_pages.append("/faq/")

    # Book a Call
    write_file("book-strategy-call/index.html", build_booking())
    all_pages.append("/book-strategy-call/")

    # Reviews
    write_file("reviews/index.html", build_reviews())
    all_pages.append("/reviews/")

    # Blog index
    write_file("blog/index.html", build_blog_index())
    all_pages.append("/blog/")

    # Blog posts
    for post in BLOG_POSTS:
        write_file(f"blog/{post['slug']}/index.html", build_blog_post(post))
        all_pages.append(f"/blog/{post['slug']}/")

    # Sitemap & Robots
    print("\nGenerating sitemap and robots.txt...")
    write_file("sitemap.xml", build_sitemap(all_pages))
    write_file("robots.txt", build_robots())

    print(f"\n{'=' * 60}")
    print(f"DONE! Generated {len(all_pages)} pages + sitemap + robots.txt")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
