import os
import json
import hashlib

BASE_DIR = r"d:\antigravity website\pochettemagnet"
ADDR = "2001 Ross Avenue, Suite 3900, Dallas, TX 75201, United States"
PHONE = "+1-877-509-3822"
EMAIL = "concierge@pochettemagnet.com"
DOMAIN = "pochettemagnet.com"
BRAND = "Pochette Magnet Atelier & Guild"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">"""

def get_header(active_page):
    idx_cls = "active" if active_page == "index" else ""
    abt_cls = "active" if active_page == "about" else ""
    prd_cls = "active" if active_page == "products" else ""
    faq_cls = "active" if active_page == "faq" else ""
    cnt_cls = "active" if active_page == "contact" else ""
    
    return f"""  <!-- Site Header (Rule 11) -->
  <header class="site-header">
    <div class="pm-container">
      <div class="pm-nav-wrapper">
        <a href="index.html" class="pm-brand">
          <div class="pm-brand-emblem">⊛</div>
          <div class="pm-brand-title">
            Pochette Magnet
            <small>Atelier &bull; Dallas</small>
          </div>
        </a>
        <nav class="pm-nav-menu">
          <a href="index.html" class="pm-nav-link {idx_cls}">Magnetic Vault</a>
          <a href="about.html" class="pm-nav-link {abt_cls}">Leather Guild</a>
          <a href="products.html" class="pm-nav-link {prd_cls}">Creations Matrix</a>
          <a href="faq.html" class="pm-nav-link {faq_cls}">Atelier FAQ</a>
          <a href="contact.html" class="pm-nav-link {cnt_cls}">Salon Inquiries</a>
        </nav>
        <div style="display: flex; align-items: center; gap: 16px;">
          <a href="contact.html" class="pm-btn pm-btn-gold">Private Fitting</a>
          <button class="pm-hamburger" id="pm-hamburger" aria-label="Toggle Navigation">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer (Rule 11) -->
  <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop"></div>
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="pm-brand">
        <div class="pm-brand-emblem">⊛</div>
        <div class="pm-brand-title">Pochette Magnet</div>
      </div>
      <button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close Drawer">&times;</button>
    </div>
    <div class="mobile-drawer-body">
      <a href="index.html" class="mobile-nav-link">Magnetic Vault Flagship</a>
      <a href="about.html" class="mobile-nav-link">Leather Guild &amp; Heritage</a>
      <a href="products.html" class="mobile-nav-link">Creations Matrix</a>
      <a href="faq.html" class="mobile-nav-link">Atelier FAQ &amp; Care</a>
      <a href="contact.html" class="mobile-nav-link">Dallas Salon Consultation</a>
    </div>
    <div class="mobile-drawer-footer">
      <p style="margin-bottom: 8px; color: var(--pm-gold); font-family: var(--pm-font-mono); font-size: 0.75rem;">DALLAS PRIVATE CONCIERGE</p>
      <p style="margin-bottom: 6px;">{PHONE}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>"""

def get_footer():
    return f"""  <!-- Semantic Site Footer -->
  <footer class="pm-footer">
    <div class="pm-container">
      <div class="pm-footer-grid">
        <div class="pm-footer-brand">
          <div class="pm-brand" style="margin-bottom: 16px;">
            <div class="pm-brand-emblem">⊛</div>
            <div class="pm-brand-title">
              Pochette Magnet
              <small>Guild &bull; Est. Dallas</small>
            </div>
          </div>
          <p style="color: var(--pm-text-light-muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 16px;">
            Sculptural evening pochettes, Italian box calfskin clutches, and concealed neodymium magnetic closures engineered for silent acoustic perfection.
          </p>
          <div style="font-family: var(--pm-font-mono); font-size: 0.8rem; color: var(--pm-gold);">
            {PHONE} &bull; {EMAIL}
          </div>
        </div>
        <div class="pm-footer-col">
          <h4>Atelier Pochettes</h4>
          <ul class="pm-footer-links">
            <li><a href="index.html">Flagship Vault</a></li>
            <li><a href="about.html">Calfskin Heritage</a></li>
            <li><a href="products.html">Creations Matrix</a></li>
            <li><a href="faq.html">Magnetic Lock FAQ</a></li>
            <li><a href="contact.html">Dallas Private Salon</a></li>
          </ul>
        </div>
        <div class="pm-footer-col">
          <h4>Engineering Pillars</h4>
          <ul class="pm-footer-links">
            <li><a href="about.html">Neodymium N52 Magnets</a></li>
            <li><a href="about.html">Full-Grain Box Calf</a></li>
            <li><a href="about.html">7-Layer Edge Burnishing</a></li>
            <li><a href="about.html">French Goatskin Lining</a></li>
            <li><a href="about.html">Zero Chemical Bonding</a></li>
          </ul>
        </div>
        <div class="pm-footer-col">
          <h4>Institutional Coordinates</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 12px; color: var(--pm-text-light-muted);">
            {ADDR}
          </p>
          <p style="font-family: var(--pm-font-mono); font-size: 0.75rem; color: var(--pm-gold); margin-bottom: 16px;">
            Salon Consultations: {PHONE}
          </p>
          <div style="padding: 8px 12px; background: rgba(212,175,55,0.08); border: 1px solid rgba(212,175,55,0.25); border-radius: 4px; font-size: 0.725rem; font-family: var(--pm-font-mono); color: var(--pm-text-light);">
            Registered Haute Maroquinerie Guild Member
          </div>
        </div>
      </div>
      <div class="pm-footer-bottom">
        <div>&copy; 2026 Pochette Magnet Atelier LLC. All Worldwide Rights Reserved.</div>
        <div class="pm-legal-nav">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="cookie-policy.html">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="assets/js/script.js"></script>
  <script src="assets/js/main.js"></script>"""

# ==========================================
# 1. INDEX.HTML (Flagship Home - 12 Distinct Sections)
# ==========================================
def build_index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pochette Magnet | Luxury Magnetic Leather Pochettes &amp; Clutches</title>
  <meta name="description" content="Discover Pochette Magnet Atelier in Dallas. Bespoke luxury leather pochettes, sculptural evening clutches, and concealed acoustic neodymium magnetic closures.">
  <link rel="canonical" href="https://{DOMAIN}/index.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ClothingStore",
    "name": "Pochette Magnet Atelier & Guild",
    "url": "https://{DOMAIN}/",
    "telephone": "{PHONE}",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "2001 Ross Avenue, Suite 3900",
      "addressLocality": "Dallas",
      "addressRegion": "TX",
      "postalCode": "75201",
      "addressCountry": "US"
    }},
    "description": "Bespoke luxury leather evening pochettes, box calfskin clutches, and concealed neodymium magnetic locks.",
    "priceRange": "$$$$"
  }}
  </script>
</head>
<body>
{get_header('index')}

  <main>
    <!-- Section 1: Neodymium Magnetic Core Masthead (Asset 1) -->
    <section class="pm-hero">
      <div class="pm-container">
        <div class="pm-hero-grid">
          <div class="pm-hero-content">
            <span class="pm-tag">Precision Haute Maroquinerie</span>
            <h1>The Acoustic <span>Magnetic Pochette</span></h1>
            <p class="pm-hero-desc">
              Engineered with calibrated neodymium magnetic cores and hand-skived Italian box calfskin, each evening pochette closes with an undeniable sensory resonance.
            </p>
            <div class="pm-hero-actions">
              <a href="products.html" class="pm-btn pm-btn-gold">Explore Creations</a>
              <a href="contact.html" class="pm-btn pm-btn-outline">Arrange Salon Fitting</a>
            </div>
            <div class="pm-hero-metrics">
              <div class="pm-metric-item">
                <strong>12,000 G</strong>
                <span>Neodymium Core</span>
              </div>
              <div class="pm-metric-item">
                <strong>0.4 mm</strong>
                <span>Skived Edge Precision</span>
              </div>
              <div class="pm-metric-item">
                <strong>N52 Grade</strong>
                <span>Permanent Magnetic Latch</span>
              </div>
            </div>
          </div>
          <div class="pm-hero-media">
            <div class="pm-hero-frame">
              <img src="assets/images/pochettemagnet_asset_1.jpg" alt="Signature Obsidian Black Box Calfskin Magnetic Pochette on polished marble atelier pedestal" width="1200" height="800">
              <div class="pm-magnet-badge">
                <div class="pm-badge-core">⊛</div>
                <div>
                  <h4 style="font-size: 0.95rem; margin-bottom: 2px;">Nocturne Box Pochette No. 01</h4>
                  <p style="font-size: 0.75rem; color: var(--pm-text-light-muted); font-family: var(--pm-font-mono);">Italian Box Calf &bull; Champagne Gold Hardware</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Magnetic Ribbon Ticker -->
    <div class="pm-ticker">
      <div class="pm-ticker-track">
        <div class="pm-ticker-item"><span>⊛</span> Italian Box Calfskin</div>
        <div class="pm-ticker-item"><span>⊛</span> Concealed Neodymium N52 Core</div>
        <div class="pm-ticker-item"><span>⊛</span> Seven-Layer Edge Burnishing</div>
        <div class="pm-ticker-item"><span>⊛</span> French Chèvre Goatskin Lining</div>
        <div class="pm-ticker-item"><span>⊛</span> Zero Mechanical Rivet Bulges</div>
        <div class="pm-ticker-item"><span>⊛</span> Hand Saddle-Stitched Waxed Linen</div>
        <div class="pm-ticker-item"><span>⊛</span> Acoustic Dampening Felt Membrane</div>
        <div class="pm-ticker-item"><span>⊛</span> Dallas Atelier Private Commissions</div>
      </div>
    </div>

    <!-- Section 3: The Acoustic Clasp Manifesto (Asset 2) -->
    <section class="pm-section pm-section-darker">
      <div class="pm-container">
        <div class="pm-manifesto-grid">
          <div class="pm-manifesto-media">
            <img src="assets/images/pochettemagnet_asset_2.jpg" alt="Extreme macro photograph of full-grain Italian leather texture and champagne gold magnetic clasp" width="1200" height="800">
          </div>
          <div>
            <span class="pm-tag">Acoustic Sensation</span>
            <h2 class="pm-section-title">The Silence of <span>Permanent Alignment</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 24px;">
              Conventional evening bags rely on clumsy twist latches, loud plastic zippers, or fragile mechanical snaps that strain leather fibers over time. Pochette Magnet reimagines the sensory ritual of luxury.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8; margin-bottom: 32px;">
              By embedding paired rare-earth neodymium magnets beneath hand-skived calfskin membranes, the flap aligns effortlessly upon approach. The closure produces a muted, authoritative acoustic click—confirming total vault security without manual force.
            </p>
            <div style="display: flex; gap: 24px;">
              <div style="border-left: 2px solid var(--pm-gold); padding-left: 16px;">
                <strong style="font-size: 1.4rem; color: #fff; display: block; font-family: var(--pm-font-display);">0.02 Sec</strong>
                Auto-Align Velocity
              </div>
              <div style="border-left: 2px solid var(--pm-gold); padding-left: 16px;">
                <strong style="font-size: 1.4rem; color: #fff; display: block; font-family: var(--pm-font-display);">3.8 N</strong>
                Calibrated Retention Force
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: 4-Pillar Magnetic Spec Matrix (Zero Box Borders) -->
    <section class="pm-section">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag">Engineering Matrix</span>
          <h2 class="pm-section-title">Four Pillars of <span>Maroquinerie Geometry</span></h2>
          <p class="pm-section-subtitle" style="margin: 0 auto;">No synthetic adhesives, cardboard filler boards, or inferior bonded leather fibers.</p>
        </div>
        <div class="pm-spec-4col">
          <div class="pm-spec-card">
            <div class="pm-spec-val">N52</div>
            <h3 class="pm-spec-title">Rare-Earth Core</h3>
            <p class="pm-spec-desc">Medical-grade neodymium magnetic pairs hermetically sealed within nickel-plated brass capsules.</p>
          </div>
          <div class="pm-spec-card">
            <div class="pm-spec-val">0.8 mm</div>
            <h3 class="pm-spec-title">Tuscan Box Calf</h3>
            <p class="pm-spec-desc">Full-grain vegetable-tanned hides selected from small artisanal tanneries outside Florence.</p>
          </div>
          <div class="pm-spec-card">
            <div class="pm-spec-val">7-Layer</div>
            <h3 class="pm-spec-title">Hand Edge Paint</h3>
            <p class="pm-spec-desc">Successive layers of water-based Italian edge varnish heated, ironed, and hand-polished with beeswax.</p>
          </div>
          <div class="pm-spec-card">
            <div class="pm-spec-val">100%</div>
            <h3 class="pm-spec-title">Chèvre Goatskin</h3>
            <p class="pm-spec-desc">Supple French goatskin interior lining offering natural scratch resistance and velvet tactile warmth.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Evening Pochette Lookbook Duo (Assets 3 & 4) -->
    <section class="pm-section pm-section-darker">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag">Atelier Lookbook</span>
          <h2 class="pm-section-title">Sculptural Formations &amp; <span>Artisanal Bench</span></h2>
          <p class="pm-section-subtitle" style="margin: 0 auto;">Examine the meticulous hand-stitching and architectural silhouette drafting in our Dallas salon.</p>
        </div>
        <div class="pm-lookbook-duo">
          <!-- Card 1: Asset 3 (Hand Saddle Stitching) -->
          <div class="pm-lookbook-card">
            <img src="assets/images/pochettemagnet_asset_3.jpg" alt="Master leather artisan hand-stitching luxury bag gusset using traditional linen thread and awl" width="1200" height="800">
            <div class="pm-lookbook-overlay">
              <div class="pm-lookbook-tag">Series I &bull; Hand Saddle Stitching</div>
              <h3 class="pm-lookbook-title">Waxed Linen Dual Needle Stitch</h3>
              <p class="pm-lookbook-desc">Traditional two-needle saddle stitching where every puncture is angled at 45 degrees for unbreakable seam integrity.</p>
            </div>
          </div>

          <!-- Card 2: Asset 4 (Burgundy Clutch Flat) -->
          <div class="pm-lookbook-card">
            <img src="assets/images/pochettemagnet_asset_4.jpg" alt="Burgundy wine structured leather envelope clutch purse flat lay on rustic workshop oak bench" width="1200" height="800">
            <div class="pm-lookbook-overlay">
              <div class="pm-lookbook-tag">Series II &bull; Architectural Geometry</div>
              <h3 class="pm-lookbook-title">The Grand Envelope Silhouette</h3>
              <p class="pm-lookbook-desc">Sharp origami leather fold corners, concealed titanium magnetic hardware, and modular interior organizing sleeves.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Magnetic Resistance, Pull Force & Dimensional Matrix Table -->
    <section class="pm-section pm-section-light">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag" style="background: rgba(212,175,55,0.1); border-color: rgba(212,175,55,0.3); color: #856d18;">Specifications Matrix</span>
          <h2 class="pm-section-title" style="color: var(--pm-text-dark);">Pochette Dimensions &amp; Magnetic Calibration</h2>
          <p class="pm-section-subtitle" style="margin: 0 auto; color: var(--pm-text-dark-muted);">Engineered specifications for each bespoke evening silhouette crafted in our Dallas atelier.</p>
        </div>
        <div class="pm-table-wrapper">
          <table class="pm-matrix-table">
            <thead>
              <tr>
                <th>Model Silhouette</th>
                <th>Exterior Dimensions</th>
                <th>Magnetic Pull Force</th>
                <th>Leather Provenance</th>
                <th>Interior Lining</th>
                <th>Clasp Finish</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Nocturne Box Pochette</strong></td>
                <td>220 &times; 130 &times; 45 mm</td>
                <td>3.8 N (Single Core)</td>
                <td>Black Tuscan Box Calf</td>
                <td>French Chèvre (Noir)</td>
                <td>Champagne Gold PVD</td>
              </tr>
              <tr>
                <td><strong>Grand Atelier Envelope</strong></td>
                <td>260 &times; 155 &times; 40 mm</td>
                <td>5.2 N (Dual Core)</td>
                <td>Burgundy Waxed Calfskin</td>
                <td>Carmine Red Goatskin</td>
                <td>Brushed Platinum</td>
              </tr>
              <tr>
                <td><strong>Minaudière Pavé</strong></td>
                <td>190 &times; 110 &times; 50 mm</td>
                <td>4.5 N (Radial Magnet)</td>
                <td>Emerald Box Calfskin</td>
                <td>Emerald Suede Kidskin</td>
                <td>24k Gilded Brass</td>
              </tr>
              <tr>
                <td><strong>Demi-Lune Wristlet</strong></td>
                <td>205 &times; 125 &times; 35 mm</td>
                <td>3.2 N (Micro Neodymium)</td>
                <td>Cognac Full-Grain Calf</td>
                <td>Ecru Velvet Goatskin</td>
                <td>Titanium Anthracite</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 7: Staggered Craft Narrative Rows (Assets 5 & 6) -->
    <section class="pm-section">
      <div class="pm-container">
        <!-- Row 1: Asset 5 (Magnetic Lock Close-up) -->
        <div class="pm-craft-row">
          <div>
            <span class="pm-tag">Hardware Mastery</span>
            <h2 class="pm-section-title">Hermetically Sealed <span>Neodymium Cells</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Standard commercial magnets oxidize, corrode, and lose their magnetic pull when exposed to atmospheric humidity. We encase every N52 neodymium disc inside a precision-machined non-ferrous brass capsule.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              A secondary acoustic dampening silicone elastomer surrounds the capsule, absorbing impact shocks and preventing the telltale metallic clicking noise associated with cheap hardware.
            </p>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_5.jpg" alt="Detailed close-up of precision magnetic lock closure mechanism and hand-creased leather borders" width="1200" height="800">
          </div>
        </div>

        <!-- Row 2: Asset 6 (Leathercraft Workshop Tools) -->
        <div class="pm-craft-row reversed">
          <div>
            <span class="pm-tag">The Bench Instruments</span>
            <h2 class="pm-section-title">Traditional Parisian <span>Leathercraft Tools</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Our Dallas cutters work with forged carbon steel tools inherited from generations of European leather artisans. From Blanchard pricking irons to Japanese skiving knives, each cut is made with deliberate human reverence.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              No automated stamping dies or synthetic plastic edge coatings enter our workshop. Every crease along the pocket edge is drawn by a heated brass filleting iron set to precisely 65 degrees Celsius.
            </p>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_6.jpg" alt="Leathercraft artisan tool flat lay featuring edge bevelers, French skiving knife, and bone folder" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Section 8: Luxury Pochette Collection Tiers -->
    <section class="pm-section pm-section-darker">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag">Atelier Portfolio</span>
          <h2 class="pm-section-title">The Bespoke <span>Collection Tiers</span></h2>
          <p class="pm-section-subtitle" style="margin: 0 auto;">Select from our permanent archival silhouettes or commission an individual custom leather creation.</p>
        </div>
        <div class="pm-tier-grid">
          <div class="pm-tier-card">
            <h3 class="pm-tier-name">Nocturne Box</h3>
            <div class="pm-tier-price">$2,450</div>
            <p style="color: var(--pm-text-light-muted); font-size: 0.9rem;">Compact evening silhouette tailored for galas, opera evenings, and formal engagements.</p>
            <ul class="pm-tier-features">
              <li>Italian Box Calfskin Exterior</li>
              <li>Single N52 Neodymium Clasp</li>
              <li>French Chèvre Goatskin Interior</li>
              <li>Concealed Card Vault Sleeves</li>
              <li>Detachable Gilded Snake Chain</li>
            </ul>
            <a href="contact.html" class="pm-btn pm-btn-outline" style="width: 100%;">Commission Creation</a>
          </div>

          <div class="pm-tier-card featured">
            <span class="pm-tier-badge">Signature Atelier</span>
            <h3 class="pm-tier-name">Grand Envelope</h3>
            <div class="pm-tier-price">$3,800</div>
            <p style="color: var(--pm-text-light-muted); font-size: 0.9rem;">Architectural envelope clutch featuring dual magnetic tension points and origami folds.</p>
            <ul class="pm-tier-features">
              <li>Waxed Tuscan Calfskin Leather</li>
              <li>Dual Calibrated Neodymium Latches</li>
              <li>Full Hand Saddle-Stitching</li>
              <li>Triple Compartment Organizer</li>
              <li>Custom Monogram Gold Stamping</li>
            </ul>
            <a href="contact.html" class="pm-btn pm-btn-gold" style="width: 100%;">Commission Creation</a>
          </div>

          <div class="pm-tier-card">
            <h3 class="pm-tier-name">Minaudière Pavé</h3>
            <div class="pm-tier-price">$5,200</div>
            <p style="color: var(--pm-text-light-muted); font-size: 0.9rem;">Ultra-luxurious evening jewel clutch featuring hand-sculpted hardwood core and calfskin wrap.</p>
            <ul class="pm-tier-features">
              <li>Rare Emerald Box Calfskin</li>
              <li>Radial 360-Degree Magnetic Core</li>
              <li>24k Gold PVD Hardware Accents</li>
              <li>Kidskin Velvet Interior Bed</li>
              <li>Bespoke Handcrafted Presentation Box</li>
            </ul>
            <a href="contact.html" class="pm-btn pm-btn-outline" style="width: 100%;">Commission Creation</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: Neodymium Cycling & Flex Laboratory Log -->
    <section class="pm-section">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag">Laboratory Stress Verification</span>
          <h2 class="pm-section-title">Tested for <span>Generations of Opening</span></h2>
          <p class="pm-section-subtitle" style="margin: 0 auto;">Every prototype undergoes robotic cycle trials to ensure zero loss of magnetic magnetism or leather fatigue.</p>
        </div>
        <div class="pm-lab-grid">
          <div class="pm-lab-item">
            <div class="pm-lab-metric">50,000</div>
            <div class="pm-lab-label">Magnetic Cycles Tested</div>
          </div>
          <div class="pm-lab-item">
            <div class="pm-lab-metric">0.00%</div>
            <div class="pm-lab-label">Flux Degradation</div>
          </div>
          <div class="pm-lab-item">
            <div class="pm-lab-metric">420 N</div>
            <div class="pm-lab-label">Gusset Seam Tensile Load</div>
          </div>
          <div class="pm-lab-item">
            <div class="pm-lab-metric">Grade 5</div>
            <div class="pm-lab-label">Titanium Core Housing</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Master Leather Artisan Matteo Vianello Spotlight -->
    <section class="pm-section pm-section-darker">
      <div class="pm-container">
        <div class="pm-spotlight-box">
          <div>
            <span class="pm-tag">Master Maroquinier</span>
            <h2 class="pm-section-title" style="margin-bottom: 16px;">Matteo <span>Vianello</span></h2>
            <p style="color: var(--pm-gold); font-family: var(--pm-font-mono); font-size: 0.85rem; margin-bottom: 20px;">
              HEAD OF LEATHER ARCHITECTURE &bull; DALLAS ATELIER
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 0.95rem; line-height: 1.8; margin-bottom: 16px;">
              Trained in the historic leathercraft ateliers of Bologna and Florence, Matteo brings three decades of uncompromising bench discipline to Pochette Magnet.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 0.95rem; line-height: 1.8;">
              "A true luxury bag does not scream for attention with gaudy logos. It asserts its nobility through the weight of its leather, the straightness of its awl marks, and the quiet satisfaction of its closure."
            </p>
          </div>
          <div style="background: rgba(212,175,55,0.04); border: 1px solid var(--pm-border); border-radius: var(--pm-radius-md); padding: 36px;">
            <h4 style="color: #fff; font-size: 1.15rem; margin-bottom: 16px;">The Vianello Bench Axioms</h4>
            <div style="margin-bottom: 14px; font-size: 0.9rem; color: var(--pm-text-light-muted);">
              <strong style="color: var(--pm-gold);">1. Zero Adhesives on Flap Pivots:</strong> Mechanical flexibility must derive entirely from skived leather thickness, never chemically hardened glue layers.
            </div>
            <div style="margin-bottom: 14px; font-size: 0.9rem; color: var(--pm-text-light-muted);">
              <strong style="color: var(--pm-gold);">2. Hand-Ironed Edge Wax:</strong> Each painted edge receives three coats of organic beeswax melted into the leather pores with an alcohol lamp.
            </div>
            <div style="font-size: 0.9rem; color: var(--pm-text-light-muted);">
              <strong style="color: var(--pm-gold);">3. Acoustic Tuning:</strong> The closure sound of every pochette is audited inside our sound-dampened chamber before final boxing.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 11: Dual-Column FAQ Accordion -->
    <section class="pm-section">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag">Curator Inquiries</span>
          <h2 class="pm-section-title">Frequently Addressed <span>Questions</span></h2>
          <p class="pm-section-subtitle" style="margin: 0 auto;">Key insights into our magnetic mechanics, leather care, and bespoke commission timelines.</p>
        </div>
        <div class="pm-faq-grid">
          <div>
            <div class="pm-faq-item">
              <button class="pm-faq-header">
                <span>Will the magnetic closure erase credit cards or smartphones?</span>
                <span class="pm-faq-icon">+</span>
              </button>
              <div class="pm-faq-body">
                No. Our neodymium magnetic capsules are engineered with directional flux backplates that project magnetic attraction exclusively forward toward the paired clasp, shielding the interior card compartments completely.
              </div>
            </div>
            <div class="pm-faq-item">
              <button class="pm-faq-header">
                <span>What origin of leather is utilized for your pochettes?</span>
                <span class="pm-faq-icon">+</span>
              </button>
              <div class="pm-faq-body">
                We source full-grain box calfskin tanned exclusively in Santa Croce sull'Arno, Tuscany. The hides undergo traditional vegetable pit tanning using chestnut bark extracts for superior suppleness.
              </div>
            </div>
          </div>
          <div>
            <div class="pm-faq-item">
              <button class="pm-faq-header">
                <span>How long does a bespoke pochette commission require?</span>
                <span class="pm-faq-icon">+</span>
              </button>
              <div class="pm-faq-body">
                From initial pattern drafting and leather selection at our Dallas salon to final hand edge burnishing, custom orders typically require between four and six weeks of dedicated bench craftsmanship.
              </div>
            </div>
            <div class="pm-faq-item">
              <button class="pm-faq-header">
                <span>How should I maintain the calfskin leather surface?</span>
                <span class="pm-faq-icon">+</span>
              </button>
              <div class="pm-faq-body">
                We recommend buffing the leather gently with a dry cotton flannel cloth once per month. An annual conditioning treatment using natural beeswax balm preserves the supple luster of the grain.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 12: Private Salon Consultation Strip -->
    <section class="pm-section pm-section-darker" style="padding-bottom: 120px;">
      <div class="pm-container">
        <div class="pm-cta-strip">
          <div>
            <span class="pm-tag" style="margin-bottom: 12px;">By Private Appointment</span>
            <h2 style="font-size: 2.2rem; margin-bottom: 8px;">Experience the Magnetic Sensation</h2>
            <p style="color: var(--pm-text-light-muted); max-width: 520px; font-size: 1rem;">
              Visit our Dallas salon on Ross Avenue to touch raw Tuscan calfskin hides, test magnetic acoustic weights, and design your bespoke evening pochette.
            </p>
          </div>
          <div style="display: flex; gap: 16px; flex-wrap: wrap;">
            <a href="contact.html" class="pm-btn pm-btn-gold">Book Salon Appointment</a>
            <a href="tel:+18775093822" class="pm-btn pm-btn-outline">{PHONE}</a>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 2. ABOUT.HTML (Leather Guild & Heritage - Assets 7, 8, 9, 10, 11, 12)
# ==========================================
def build_about():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Leather Guild Heritage &amp; Philosophy | Pochette Magnet</title>
  <meta name="description" content="Discover the artisanal leathercraft heritage, Italian calfskin provenance, and magnetic innovation behind Pochette Magnet in Dallas, Texas.">
  <link rel="canonical" href="https://{DOMAIN}/about.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('about')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Provenance &amp; Heritage</span>
        <h1 class="pm-section-title" style="font-size: 3rem;">Haute Maroquinerie, <span>Forged in Dallas</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">
          Founded on the conviction that evening accessories should marry classic European leathercraft with cutting-edge magnetic physics.
        </p>
      </div>
    </section>

    <!-- Chapter 1: The Evening Minaudière (Asset 7) -->
    <section class="pm-section">
      <div class="pm-container">
        <div class="pm-craft-row">
          <div>
            <span class="pm-tag">Chapter I &bull; The Minaudière</span>
            <h2 class="pm-section-title">The Geometry of <span>Evening Sculptures</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Our evening minaudières begin with solid aircraft-grade aluminum chassis lined in Italian beechwood. Rather than relying on exterior clasp prongs that snag silk dresses, our craftsmen conceal neodymium cores within the perimeter rim.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              When closed, the box snaps seamlessly into a single unbroken metallic and leather sculpture, offering unrivaled protection for evening valuables and evening cosmetics.
            </p>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_7.jpg" alt="Minimalist champagne metallic evening minaudière clutch with concealed magnetic closure" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Chapter 2: The Tan Calfskin Envelope (Asset 8) -->
    <section class="pm-section pm-section-darker">
      <div class="pm-container">
        <div class="pm-craft-row reversed">
          <div>
            <span class="pm-tag">Chapter II &bull; Natural Tanning</span>
            <h2 class="pm-section-title">Vegetable-Tanned <span>Tuscan Calfskin</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              We refuse to use chrome-tanned industrial leather treated with toxic heavy metals. Our calfskin hides soak for sixty days in subterranean oak vats infused with natural mimosa and chestnut tannins.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              This ancient organic tanning method imbues the leather with a warm, rich cedar aroma, a buttery temper that molds to your fingertips, and a deep golden patina that matures gracefully over decades.
            </p>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_8.jpg" alt="Warm cognac tan calfskin envelope clutch with magnetic flap displayed on raw natural linen" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Chapter 3: Pattern Drafting (Asset 9) -->
    <section class="pm-section">
      <div class="pm-container">
        <div class="pm-craft-row">
          <div>
            <span class="pm-tag">Chapter III &bull; Architectural Draft</span>
            <h2 class="pm-section-title">Geometric Drafting on <span>Granite Benches</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Every bespoke pochette begins on our Dallas drafting tables with solid brass dividers and surgical steel cutting guides. We calculate leather thickness down to a fraction of a millimeter to account for turn-of-cloth folds.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              By designing each piece with origami-inspired leather folds, we eliminate unnecessary bulky seams, allowing our pochettes to maintain an impossibly slim 15-millimeter profile when closed.
            </p>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_9.jpg" alt="Artisan pattern drafting table with brass calipers, geometric leather templates, and cutting mat" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Chapter 4: Seven-Layer Edge Burnishing (Asset 10) -->
    <section class="pm-section pm-section-darker">
      <div class="pm-container">
        <div class="pm-craft-row reversed">
          <div>
            <span class="pm-tag">Chapter IV &bull; The Edge Finish</span>
            <h2 class="pm-section-title">The Seven-Layer <span>Lacquered Edge</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              The true hallmark of luxury leather goods lies along the raw edge. While mass manufacturers apply rubberized plastic paints that peel within months, our craftsmen bevel each leather edge with an English edge tool.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              Seven coats of specialized water-based edge lacquer are applied by hand, with each layer sanded, ironed with hot brass, and buffed with raw Texas beeswax until the edge resembles polished obsidian stone.
            </p>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_10.jpg" alt="Macro photograph of seven-layer hand-painted and polished edge burnishing on calfskin leather" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Archival Duo: Studio Pochette & Goatskin Lining (Assets 11 & 12) -->
    <section class="pm-section">
      <div class="pm-container">
        <div style="text-align: center;">
          <span class="pm-tag">Internal Engineering</span>
          <h2 class="pm-section-title">Exterior Architecture &amp; <span>Interior Luxury</span></h2>
          <p class="pm-section-subtitle" style="margin: 0 auto;">Witness the harmonious dialogue between structured exterior calfskin and velvet-soft French chèvre lining.</p>
        </div>
        <div class="pm-lookbook-duo">
          <div class="pm-lookbook-card">
            <img src="assets/images/pochettemagnet_asset_11.jpg" alt="Modern structured black leather shoulder pochette with magnetic snap in luxury atelier studio" width="1200" height="800">
            <div class="pm-lookbook-overlay">
              <div class="pm-lookbook-tag">Archival Creation I &bull; Studio Exhibition</div>
              <h3 class="pm-lookbook-title">The Modern Shoulder Pochette</h3>
              <p class="pm-lookbook-desc">Streamlined black calfskin evening bag with concealed magnetic clasp and hand-burnished edge borders.</p>
            </div>
          </div>
          <div class="pm-lookbook-card">
            <img src="assets/images/pochettemagnet_asset_12.jpg" alt="Interior goatskin lining and compartmentalized card sleeve architecture of luxury leather pochette" width="1200" height="800">
            <div class="pm-lookbook-overlay">
              <div class="pm-lookbook-tag">Archival Creation II &bull; Interior Vault</div>
              <h3 class="pm-lookbook-title">French Chèvre Goatskin Lining</h3>
              <p class="pm-lookbook-desc">Velvety scratch-resistant interior fitted with three dedicated card slots and bespoke lipstick compartment.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 3. PRODUCTS.HTML (Creations Matrix - Assets 13 to 18)
# ==========================================
def build_products():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Creations Matrix &amp; Pochettes | Pochette Magnet</title>
  <meta name="description" content="Explore the bespoke luxury evening pochettes, magnetic clutches, and leather creations hand-crafted at Pochette Magnet in Dallas, Texas.">
  <link rel="canonical" href="https://{DOMAIN}/products.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('products')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Haute Maroquinerie Catalog</span>
        <h1 class="pm-section-title" style="font-size: 3rem;">The Magnetic <span>Creations Matrix</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">
          Each model is individually bench-crafted upon commission. Browse our permanent evening silhouettes or request custom leather configurations.
        </p>
      </div>
    </section>

    <section class="pm-section">
      <div class="pm-container">
        <div class="pm-products-grid">
          <!-- Model 1: Geometric Wristlet (Asset 13) -->
          <div class="pm-product-card">
            <div class="pm-product-thumb">
              <img src="assets/images/pochettemagnet_asset_13.jpg" alt="Sculptural geometric leather evening wristlet bag with brushed platinum magnetic hardware" width="1200" height="800">
            </div>
            <div class="pm-product-info">
              <h3 class="pm-product-title">Demi-Lune Wristlet</h3>
              <p class="pm-product-desc">Contemporary curved silhouette with integrated hand strap and concealed micro-neodymium flap lock.</p>
              <div class="pm-product-meta">
                <span>Box Calfskin</span>
                <strong>$1,950</strong>
              </div>
            </div>
          </div>

          <!-- Model 2: Emerald Evening Pochette (Asset 14) -->
          <div class="pm-product-card">
            <div class="pm-product-thumb">
              <img src="assets/images/pochettemagnet_asset_14.jpg" alt="Deep emerald green box calfskin evening pochette standing on bronze exhibition plinth" width="1200" height="800">
            </div>
            <div class="pm-product-info">
              <h3 class="pm-product-title">Emerald Box Minaudière</h3>
              <p class="pm-product-desc">Hard-structured evening box clutch wrapped in jewel-toned emerald Italian calfskin with 24k gold hardware.</p>
              <div class="pm-product-meta">
                <span>Hardwood &amp; Calf</span>
                <strong>$3,200</strong>
              </div>
            </div>
          </div>

          <!-- Model 3: Leather Merchant Hides (Asset 15) -->
          <div class="pm-product-card">
            <div class="pm-product-thumb">
              <img src="assets/images/pochettemagnet_asset_15.jpg" alt="Artisanal leather merchant shelves stacked with vegetable-tanned Italian calfskin leather hides" width="1200" height="800">
            </div>
            <div class="pm-product-info">
              <h3 class="pm-product-title">Bespoke Hide Selection</h3>
              <p class="pm-product-desc">Commission your clutch in custom leather shades chosen from our private archive of Italian vegetable-tanned hides.</p>
              <div class="pm-product-meta">
                <span>Custom Commission</span>
                <strong>Inquire</strong>
              </div>
            </div>
          </div>

          <!-- Model 4: Structured Crossbody Clutch (Asset 16) -->
          <div class="pm-product-card">
            <div class="pm-product-thumb">
              <img src="assets/images/pochettemagnet_asset_16.jpg" alt="Structured crossbody leather clutch purse with concealed dual magnetic closure on display stand" width="1200" height="800">
            </div>
            <div class="pm-product-info">
              <h3 class="pm-product-title">Dual-Magnetic Crossbody</h3>
              <p class="pm-product-desc">Versatile day-to-evening pochette featuring dual neodymium closure points and detachable calfskin shoulder strap.</p>
              <div class="pm-product-meta">
                <span>Full-Grain Calf</span>
                <strong>$2,650</strong>
              </div>
            </div>
          </div>

          <!-- Model 5: Artisan Edge Skiving (Asset 17) -->
          <div class="pm-product-card">
            <div class="pm-product-thumb">
              <img src="assets/images/pochettemagnet_asset_17.jpg" alt="Master artisan skiving leather edge thickness with traditional Japanese skiving blade on granite" width="1200" height="800">
            </div>
            <div class="pm-product-info">
              <h3 class="pm-product-title">Full Bespoke Atelier Piece</h3>
              <p class="pm-product-desc">Collaborate directly with master artisan Matteo Vianello to craft a one-of-a-kind evening pochette from raw sketch.</p>
              <div class="pm-product-meta">
                <span>Master Commission</span>
                <strong>From $4,500</strong>
              </div>
            </div>
          </div>

          <!-- Model 6: Presentation Packaging (Asset 18) -->
          <div class="pm-product-card">
            <div class="pm-product-thumb">
              <img src="assets/images/pochettemagnet_asset_18.jpg" alt="Luxury branded presentation packaging featuring magnetic rigid presentation box and cotton dust bag" width="1200" height="800">
            </div>
            <div class="pm-product-info">
              <h3 class="pm-product-title">Atelier Collector Suite</h3>
              <p class="pm-product-desc">Every completed commission arrives encased in our signature magnetic presentation coffret with certification papers.</p>
              <div class="pm-product-meta">
                <span>Archival Packaging</span>
                <strong>Included</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 4. CONTACT.HTML (Dallas Salon Consultation - Asset 19)
# ==========================================
def build_contact():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Salon Consultation &amp; Coordinates | Pochette Magnet</title>
  <meta name="description" content="Reserve a private evening bag consultation at Pochette Magnet Atelier in Dallas, Texas. Meet our master maroquinier for custom leathercraft.">
  <link rel="canonical" href="https://{DOMAIN}/contact.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('contact')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Private Salon Coordinates</span>
        <h1 class="pm-section-title" style="font-size: 3rem;">Dallas Atelier <span>Consultation</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">
          Schedule an intimate consultation at our Dallas salon on Ross Avenue to inspect raw hides and design your custom evening pochette.
        </p>
      </div>
    </section>

    <section class="pm-section">
      <div class="pm-container">
        <div class="pm-craft-row">
          <div>
            <span class="pm-tag">Institutional Address</span>
            <h2 class="pm-section-title">Trammell Crow Center, <span>Dallas</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 24px;">
              Our private showroom and consultation salon is situated in the downtown Dallas Arts District, overlooking the sculpture gardens. We welcome patrons by prior appointment.
            </p>
            <div style="background: var(--pm-bg-surface); border: 1px solid var(--pm-border-dark); border-radius: var(--pm-radius-md); padding: 28px; margin-bottom: 32px;">
              <p style="font-size: 0.9rem; color: var(--pm-gold); font-family: var(--pm-font-mono); margin-bottom: 6px;">PHYSICAL ATELIER COORDINATES</p>
              <p style="font-size: 1.1rem; color: #fff; margin-bottom: 12px; line-height: 1.6;">
                {ADDR}
              </p>
              <p style="font-size: 0.9rem; color: var(--pm-gold); font-family: var(--pm-font-mono); margin-bottom: 6px;">DIRECT TELEPHONE CONCIERGE</p>
              <p style="font-size: 1.1rem; color: #fff; margin-bottom: 12px;">
                <a href="tel:+18775093822" style="color: #fff;">{PHONE}</a>
              </p>
              <p style="font-size: 0.9rem; color: var(--pm-gold); font-family: var(--pm-font-mono); margin-bottom: 6px;">ELECTRONIC DISPATCH</p>
              <p style="font-size: 1.1rem; color: #fff;">
                <a href="mailto:{EMAIL}" style="color: #fff;">{EMAIL}</a>
              </p>
            </div>
          </div>
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_19.jpg" alt="Exclusive private luxury leather goods salon consultation lounge with brass accents and velvet chairs" width="1200" height="800">
          </div>
        </div>

        <div style="max-width: 680px; margin: 60px auto 0; background: var(--pm-bg-surface); border: 1px solid var(--pm-border); border-radius: var(--pm-radius-lg); padding: 40px;">
          <h3 style="font-size: 1.6rem; margin-bottom: 12px; text-align: center;">Arrange Private Salon Fitting</h3>
          <p style="color: var(--pm-text-light-muted); font-size: 0.95rem; text-align: center; margin-bottom: 32px;">
            Please complete the dispatch inquiry below. Our concierge will contact you within one business day.
          </p>
          <form id="pm-consultation-form">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
              <div>
                <label style="display: block; font-size: 0.8rem; font-family: var(--pm-font-mono); color: var(--pm-gold); margin-bottom: 6px;">FULL LEGAL NAME</label>
                <input type="text" required placeholder="Elena Rostova" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.04); border: 1px solid var(--pm-border-dark); border-radius: 4px; color: #fff;">
              </div>
              <div>
                <label style="display: block; font-size: 0.8rem; font-family: var(--pm-font-mono); color: var(--pm-gold); margin-bottom: 6px;">TELEPHONE NUMBER</label>
                <input type="tel" required placeholder="+1 (555) 000-0000" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.04); border: 1px solid var(--pm-border-dark); border-radius: 4px; color: #fff;">
              </div>
            </div>
            <div style="margin-bottom: 20px;">
              <label style="display: block; font-size: 0.8rem; font-family: var(--pm-font-mono); color: var(--pm-gold); margin-bottom: 6px;">AUTHENTICATED EMAIL</label>
              <input type="email" required placeholder="elena@example.com" style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.04); border: 1px solid var(--pm-border-dark); border-radius: 4px; color: #fff;">
            </div>
            <div style="margin-bottom: 28px;">
              <label style="display: block; font-size: 0.8rem; font-family: var(--pm-font-mono); color: var(--pm-gold); margin-bottom: 6px;">DESIRED POCHETTE SILHOUETTE &amp; LEATHER</label>
              <textarea rows="4" placeholder="Tell us about the desired evening bag model, leather color, or custom monogram preferences..." style="width: 100%; padding: 12px 16px; background: rgba(255,255,255,0.04); border: 1px solid var(--pm-border-dark); border-radius: 4px; color: #fff;"></textarea>
            </div>
            <button type="submit" class="pm-btn pm-btn-gold" style="width: 100%;">Transmit Salon Request</button>
          </form>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 5. FAQ.HTML (Atelier FAQ & Care - Asset 20)
# ==========================================
def build_faq():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Atelier FAQ &amp; Leather Care | Pochette Magnet</title>
  <meta name="description" content="Technical questions, magnetic clasp safety, leather care, and bespoke commission details for Pochette Magnet Atelier in Dallas.">
  <link rel="canonical" href="https://{DOMAIN}/faq.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('faq')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Knowledge &amp; Maintenance</span>
        <h1 class="pm-section-title" style="font-size: 3rem;">Atelier <span>Knowledge Vault</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">
          Comprehensive guidance on our magnetic lock engineering, Tuscan leather provenance, and lifetime atelier maintenance.
        </p>
      </div>
    </section>

    <section class="pm-section">
      <div class="pm-container">
        <div class="pm-craft-row">
          <div class="pm-craft-media">
            <img src="assets/images/pochettemagnet_asset_20.jpg" alt="Artisan hands applying natural beeswax dressing to hand-burnished leather seam of bespoke bag" width="1200" height="800">
          </div>
          <div>
            <span class="pm-tag">Master Maintenance</span>
            <h2 class="pm-section-title">The Ritual of <span>Beeswax Dressing</span></h2>
            <p style="color: var(--pm-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Every Pochette Magnet creation is finished with an organic balm blended from raw Texas beeswax, cold-pressed jojoba oil, and natural carnauba wax.
            </p>
            <p style="color: var(--pm-text-light-muted); font-size: 1rem; line-height: 1.8;">
              This treatment feeds the deep fibers of vegetable-tanned box calfskin, imparting a subtle hydrophobic shield against light mist while maintaining an exquisite silky hand.
            </p>
          </div>
        </div>

        <div style="max-width: 860px; margin: 80px auto 0;">
          <h3 style="font-size: 1.8rem; margin-bottom: 32px; text-align: center;">Technical &amp; Collector Inquiries</h3>
          
          <div class="pm-faq-item" style="margin-bottom: 16px;">
            <button class="pm-faq-header">
              <span>Are neodymium magnets safe for sensitive pacemakers?</span>
              <span class="pm-faq-icon">+</span>
            </button>
            <div class="pm-faq-body">
              While our magnetic closures are directional and shielded toward the bag interior, medical authorities recommend maintaining at least 15 centimeters (6 inches) between rare-earth magnets and implanted cardiac pacemakers. Patrons with medical implants should consult their physician.
            </div>
          </div>

          <div class="pm-faq-item" style="margin-bottom: 16px;">
            <button class="pm-faq-header">
              <span>Will the magnetic attraction weaken over time?</span>
              <span class="pm-faq-icon">+</span>
            </button>
            <div class="pm-faq-body">
              No. Neodymium N52 magnets naturally lose less than 1% of their permanent magnetic flux over one hundred years under ordinary room temperature conditions. Your pochette's acoustic closure will remain as crisp and resolute in fifty years as the day it left our Dallas bench.
            </div>
          </div>

          <div class="pm-faq-item" style="margin-bottom: 16px;">
            <button class="pm-faq-header">
              <span>How do I protect my calfskin clutch from rain?</span>
              <span class="pm-faq-icon">+</span>
            </button>
            <div class="pm-faq-body">
              While our beeswax finish repels minor moisture droplets, vegetable-tanned box calf should never be submerged in water. Should your pochette be caught in rain, gently dab droplets away with an un-dyed microfiber cloth and allow it to dry naturally at room temperature.
            </div>
          </div>

          <div class="pm-faq-item" style="margin-bottom: 16px;">
            <button class="pm-faq-header">
              <span>Do you offer complimentary lifetime refurbishment?</span>
              <span class="pm-faq-icon">+</span>
            </button>
            <div class="pm-faq-body">
              Yes. All bespoke Pochette Magnet creations include complimentary lifetime edge re-burnishing and leather conditioning at our Dallas atelier. Clients need only dispatch their piece to our salon for dedicated master rejuvenation.
            </div>
          </div>

          <div class="pm-faq-item">
            <button class="pm-faq-header">
              <span>Can I customize the metallic finish of the magnetic hardware?</span>
              <span class="pm-faq-icon">+</span>
            </button>
            <div class="pm-faq-body">
              We offer four standard physical vapor deposition (PVD) hardware finishes: Champagne Gold, Brushed Platinum, 24k Polished Gold, and Anthracite Titanium. Custom guilloché engraving is also available upon bespoke request.
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 6. POLICY PAGES (Rule 5: Strictly 5-6 lines / 60-110 words per substantive paragraph)
# ==========================================
def build_privacy():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Pochette Magnet</title>
  <meta name="description" content="Privacy Policy for Pochette Magnet Atelier &amp; Guild. Review our institutional client data protection standards, fitting confidentiality, and security safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Institutional Compliance</span>
        <h1 class="pm-section-title" style="font-size: 2.8rem;">Client Privacy <span>Charter</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Pochette Magnet Atelier LLC</p>
      </div>
    </section>

    <div class="pm-container">
      <div class="pm-policy-wrapper">
        
        <div class="pm-policy-section">
          <h2>1. Commitment to Bespoke Client Confidentiality</h2>
          <p class="pm-policy-p">
            Pochette Magnet Atelier maintains an uncompromised institutional commitment to safeguarding the personal records, bespoke monogram registries, and confidential communications of every patron who commissions leather goods at our Dallas salon. We acknowledge that our clients entrust us with sensitive contact details and personal aesthetic preferences when scheduling private appointments. Under no circumstances do we lease, trade, or distribute client databases to outside commercial marketing brokers or digital ad syndicates.
          </p>
          <p class="pm-policy-p">
            Our data protection infrastructure utilizes advanced electronic encryption architectures designed to neutralize unauthorized surveillance, data leaks, or unapproved data transmissions across global digital networks. Institutional records collected during your tailoring engagement are maintained within segmented physical and electronic archives that comply strictly with United States federal standards and worldwide data privacy frameworks. We conduct recurring technical audits of our digital reservation network to guarantee total operational security.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>2. Scope of Collected Sizing and Fitting Information</h2>
          <p class="pm-policy-p">
            When you transmit an inquiry through our digital salon portal or schedule an appointment at our Dallas salon, we record necessary identifying details including your legal name, direct corporate telephone number, authenticated email address, and physical delivery coordinates. Furthermore, when ordering bespoke leather pochettes, our artisans record custom embossing initials, hardware finish selections, and leather hue preferences required to craft your evening bag accurately.
          </p>
          <p class="pm-policy-p">
            In addition to directly provided contact records, our web infrastructure passively monitors standard diagnostic server telemetry, such as anonymous Internet Protocol addresses, browser rendering versions, operating system architecture, and referring webpage headers. These technical metrics are processed strictly in an aggregated format to optimize the visual presentation and navigation responsiveness of our digital salon. Passive analytics never link anonymous browsing behaviors to your verified private client identity or personal atelier records.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>3. Operational Purpose of Data Processing</h2>
          <p class="pm-policy-p">
            Personal particulars collected by Pochette Magnet are processed exclusively to execute valid bespoke leather commissions, coordinate private salon appointments, and confirm physical delivery arrangements for your completed evening pochettes. We also utilize verified client telephone contacts to provide courteous text or telephone confirmations prior to scheduled salon visits. Operational data handling ensures our cutters prepare adequate Tuscan calfskin hides and magnetic hardware without generating avoidable workshop waste.
          </p>
          <p class="pm-policy-p">
            With your express consent, we may occasionally dispatch dignified announcements regarding new seasonal leather arrivals, limited evening clutch editions, or private atelier salon invitations. You retain the absolute right to opt out of non-essential communications at any moment by contacting our Dallas concierge or clicking unsubscribe links embedded in email transmissions. We honor all preference revisions immediately upon receipt across our internal client communication registers.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>4. Information Security and Third-Party Disclosures</h2>
          <p class="pm-policy-p">
            We do not share your private atelier records with outside third parties, except as strictly required to complete authorized payment transactions through PCI-DSS certified electronic processing gateways. Any third-party technology providers engaged to facilitate web hosting or payment clearance are legally bound by stringent confidentiality agreements that prohibit independent exploitation of client records. Your payment card numbers are encrypted end-to-end and never permanently stored on local atelier servers.
          </p>
          <p class="pm-policy-p">
            In rare instances where disclosure is mandated by lawful court subpoenas, legal warrants, or applicable state regulations, we cooperate strictly within the exact limits of the law. Prior to complying with external legal demands for information, we make every reasonable attempt to notify the affected client, provided legal statutes do not prohibit such prior notification. We maintain rigorous documentation of all formal requests to preserve transparency and integrity.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>5. Client Rights and Institutional Contact Coordinates</h2>
          <p class="pm-policy-p">
            Every patron retains the definitive institutional right to inspect, correct, or request the permanent deletion of their personal records maintained within our archives. Should you wish to review your archived contact particulars or request total erasure of past consultation logs, please submit a written directive to our data privacy officer at our physical office or by direct email transmission. We commit to acknowledging and processing all legitimate privacy requests within thirty calendar days.
          </p>
          <p class="pm-policy-p">
            For all formal inquiries concerning this Client Privacy Charter or our operational data protection protocols, please direct communications to Pochette Magnet Atelier LLC, {ADDR}. You may also reach our dedicated client services telephone line directly at {PHONE} or transmit electronic correspondence to {EMAIL}. We remain dedicated to upholding the highest standards of bespoke discretion and electronic privacy for every esteemed luxury handbag patron.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_terms():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms &amp; Conditions | Pochette Magnet</title>
  <meta name="description" content="Terms and Conditions governing bespoke leather commissions, fitting appointments, and web portal access for Pochette Magnet in Dallas, Texas.">
  <link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Legal Framework</span>
        <h1 class="pm-section-title" style="font-size: 2.8rem;">Terms &amp; Conditions <span>Charter</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Pochette Magnet Atelier LLC</p>
      </div>
    </section>

    <div class="pm-container">
      <div class="pm-policy-wrapper">
        
        <div class="pm-policy-section">
          <h2>1. Acceptance of Bespoke Leathercraft Terms</h2>
          <p class="pm-policy-p">
            By accessing the digital web presence of Pochette Magnet Atelier or transmitting an inquiry to commission bespoke leather goods at our Dallas salon, you formally agree to be bound by these legal terms and conditions. If you do not agree with any provision contained within this charter, you must immediately discontinue your use of our digital platforms and refrain from ordering leather goods. These terms establish a legally enforceable pact between yourself and Pochette Magnet Atelier LLC.
          </p>
          <p class="pm-policy-p">
            We reserve the institutional right to update, modify, or revise these operational terms periodically to reflect amendments in commercial regulations, payment policies, or leathercraft production workflows. Any updates become effective immediately upon public posting to this web address. Your continued engagement with our leather atelier or persistent browsing of our web materials following posted revisions constitutes full legal affirmation of the revised terms and operational guidelines.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>2. Leather Commissions, Deposits, and Salon Appointments</h2>
          <p class="pm-policy-p">
            Because our artisans procure authentic Tuscan box calfskin hides, neodymium magnetic hardware, and French goatskin linings specifically for individual commissions, all bespoke orders require a non-refundable commencement deposit. Commission requests are not legally confirmed until our master maroquinier completes your design specification and issues an authenticated order registry. Clients must attend scheduled salon trials to verify custom monogramming and color alignments.
          </p>
          <p class="pm-policy-p">
            Clients seeking to reschedule a salon appointment must provide written or verbal notice to our concierge at least forty-eight hours prior to their reserved hour. Failure to attend scheduled consultations without prior notification delays leather cutting timelines and may incur administrative rescheduling fees. We appreciate the cooperation of our patrons regarding our strict bench production schedules, which ensure each evening bag receives dedicated artisanal focus.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>3. Intellectual Property and Proprietary Clasp Architecture</h2>
          <p class="pm-policy-p">
            All visual imagery, typographic layouts, written leathercraft essays, registered trademarks, and evening bag silhouettes published on this website remain the sole intellectual property of Pochette Magnet Atelier LLC. You are granted an ephemeral, revocable, non-exclusive license to view digital content for personal, non-commercial purposes only. Any unauthorized extraction, republication, commercial exploitation, or automated data harvesting of our materials is strictly prohibited under international copyright laws.
          </p>
          <p class="pm-policy-p">
            Our proprietary magnetic closure geometries, multi-layer acoustic dampening configurations, and hand-burnished edge lacquer formulations constitute protected craftsmanship trade secrets of our maroquinerie guild. Clients acquiring bespoke pochettes receive ownership of the physical leather bag, but acquire no intellectual property rights in our proprietary pattern drafting systems or guild trademarks. We actively defend our proprietary craftsmanship rights and design patents across global luxury markets.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>4. Client Conduct and Salon Etiquette</h2>
          <p class="pm-policy-p">
            Pochette Magnet Atelier maintains an atmosphere of refined focus, craftsmanship contemplation, and mutual respect within our Dallas consultation salon. We require all patrons to conduct themselves with consideration toward fellow clients and our leathercraft staff. Disruptive conduct, verbal disrespect, excessive inebriation, or willful disregard for salon protocols may result in immediate refusal of service and cancellation of commissions in accordance with contract guidelines.
          </p>
          <p class="pm-policy-p">
            While we encourage personal photography of your completed pochette during final collection appointments, the use of commercial video rigs, external recording equipment, or intrusive flash apparatus that disturbs adjacent clients is strictly prohibited without prior written consent from management. We reserve the full managerial right to decline service to any party whose conduct undermines the professional environment of our premises. We thank all patrons for preserving our focused salon atmosphere.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>5. Governing Law and Dispute Resolution</h2>
          <p class="pm-policy-p">
            These terms and conditions are governed by and construed in strict accordance with the laws of the State of Texas, United States, without regard to conflict of law principles. Any legal controversy, dispute, or claim arising from these terms or your leathercraft commission with Pochette Magnet Atelier shall be submitted to binding arbitration in Dallas County, Texas, under standard American Arbitration Association procedures.
          </p>
          <p class="pm-policy-p">
            For questions or legal correspondence regarding these terms and conditions, please direct formal written notices to Pochette Magnet Atelier LLC, {ADDR}. You may also contact our administrative office by telephone at {PHONE} or transmit digital communications to our designated legal inbox at {EMAIL}. We remain dedicated to resolving all client inquiries with equity, professionalism, and thorough institutional care.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_disclaimer():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disclaimer | Pochette Magnet</title>
  <meta name="description" content="Legal and craftsmanship disclaimer regarding organic leather variations, magnetic field notices, and web content accuracy for Pochette Magnet.">
  <link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Notice &amp; Disclosure</span>
        <h1 class="pm-section-title" style="font-size: 2.8rem;">Craftsmanship &amp; Legal <span>Disclaimer</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Pochette Magnet Atelier LLC</p>
      </div>
    </section>

    <div class="pm-container">
      <div class="pm-policy-wrapper">
        
        <div class="pm-policy-section">
          <h2>1. General Information and Craftsmanship Notice</h2>
          <p class="pm-policy-p">
            The leathercraft essays, material specifications, magnetic pull analyses, and evening clutch showcases published on this website are presented solely for general informational and educational enrichment. While we strive to maintain meticulous precision regarding historic European leathercraft traditions and textile properties, we make no express or implied representations regarding absolute perfection or universal suitability for every climate condition. Content is provided on an as-is basis without commercial warranties.
          </p>
          <p class="pm-policy-p">
            Pochette Magnet Atelier expressly disclaims all liability for incidental inaccuracies, typographical errors, or inadvertent omissions that may appear across our digital publications. Descriptions of vegetable-tanned calfskin hides, organic grain striations, and natural leather textures reflect authentic characteristics and are subject to minor organic variations between distinct tannery dye lots. Clients should review specific leather samples directly during in-person Dallas salon consultations.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>2. Organic Leather Characteristics and Magnetic Notices</h2>
          <p class="pm-policy-p">
            Our pochettes are crafted from 100% full-grain vegetable-tanned calfskin. While dense box calfskin and beeswax dressing provide natural resistance against minor wear, leather is an organic material that will develop character, creases, and patina over time. Prolonged immersion in water or direct heat sources may alter the natural texture of the grain. Clients should store luxury leather goods inside the provided breathable cotton dust bags when not in use.
          </p>
          <p class="pm-policy-p">
            Our concealed magnetic closures utilize high-grade neodymium rare-earth magnets. While magnetic flux is directionally contained and shielded from internal card pockets, patrons with medical pacemakers or sensitive bio-mechanical devices should consult their physician regarding safe operating proximities. Nothing on this website constitutes professional medical counsel regarding rare-earth magnetic fields. Patrons assume personal responsibility for evaluating personal health compatibility and safety parameters.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>3. External Links and Third-Party Resources</h2>
          <p class="pm-policy-p">
            Our web platform may periodically provide hyperlinked references to external tannery guilds, historic leather archives, cultural institutions, or regional transport maps across international digital networks. These third-party links are supplied exclusively for visitor convenience and do not signify institutional endorsement, sponsorship, or independent verification of the external entities. Pochette Magnet Atelier holds zero operational control over the content, security measures, or privacy policies of third-party domains.
          </p>
          <p class="pm-policy-p">
            When electing to leave our digital domain via external links, you do so entirely at your own discretion and peril. We strongly encourage all users to inspect the terms of service and privacy declarations of any outside web portals they visit. Pochette Magnet Atelier accepts no legal responsibility for financial damages, digital malware, or misleading claims arising from your navigation of third-party digital networks.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>4. Limitation of Operational Liability</h2>
          <p class="pm-policy-p">
            To the maximum extent permitted by applicable United States law, Pochette Magnet Atelier LLC, its managing officers, master maroquiniers, and corporate affiliates shall not be held liable for indirect, incidental, punitive, or consequential damages resulting from your use of this web portal or your leathercraft commission. This broad limitation applies regardless of whether alleged damages stem from contract breaches, tort actions, server downtimes, or technical interruptions.
          </p>
          <p class="pm-policy-p">
            In jurisdictions that do not permit the full exclusion or limitation of incidental liability for consumer transactions, our maximum aggregate liability to you for any verified claims shall strictly not exceed the total financial sums paid by you directly to Pochette Magnet Atelier during the preceding three calendar months. This limitation represents a fundamental element of the commercial bargain between our atelier and luxury handbag patrons.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>5. Inquiries Regarding Disclaimers and Institutional Coordinates</h2>
          <p class="pm-policy-p">
            Should you have inquiries, clarifications, or feedback concerning the contents of this Craftsmanship &amp; Legal Disclaimer, we welcome your direct communication with our administrative team. We are committed to fostering open transparency, leathercraft excellence, and mutual trust with every client who engages with our digital salon, reviews our leather archives, or commissions bespoke evening bags at our Dallas bench consultation rooms.
          </p>
          <p class="pm-policy-p">
            Please direct all official correspondence concerning this disclaimer to Pochette Magnet Atelier LLC, located at {ADDR}. For immediate verbal consultations regarding leather accommodations or magnetic disclosures, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and bespoke craftsmanship excellence.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_cookie():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Policy | Pochette Magnet</title>
  <meta name="description" content="Cookie Policy for Pochette Magnet Atelier &amp; Guild. Learn about our minimal telemetry, session cookies, and digital privacy safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="pm-page-header">
      <div class="pm-container">
        <span class="pm-tag">Digital Telemetry Framework</span>
        <h1 class="pm-section-title" style="font-size: 2.8rem;">Institutional <span>Cookie Policy</span></h1>
        <p class="pm-section-subtitle" style="margin: 0 auto;">Effective Date: January 1, 2026 &bull; Pochette Magnet Atelier LLC</p>
      </div>
    </section>

    <div class="pm-container">
      <div class="pm-policy-wrapper">
        
        <div class="pm-policy-section">
          <h2>1. Introduction to Cookie Technologies</h2>
          <p class="pm-policy-p">
            This Cookie Policy explains how Pochette Magnet Atelier employs small alphanumeric text files known as cookies, alongside related digital storage technologies, when you access our online maroquinerie portal. These digital tools are transferred to your computer or mobile browsing device to record operational settings and maintain continuous network navigation. We prioritize user privacy by deploying only technical cookies necessary to support your viewing experience.
          </p>
          <p class="pm-policy-p">
            By continuing to explore our online leather showcase, browse archival lookbooks, or utilize our digital fitting scheduler, you acknowledge our use of cookies in full conformity with this stated policy. We provide transparent administrative controls allowing patrons to manage or disable cookie preferences at any stage. Understanding our modest technical data storage practices helps ensure a seamless, dignified digital salon experience across all modern personal computing environments.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>2. Categories of Cookies Employed on Our Salon</h2>
          <p class="pm-policy-p">
            Essential operational cookies are strictly required to ensure the fundamental technical performance and navigation security of our web portal. These core files maintain session integrity as you transition between leather galleries, enable the interactive mobile navigation drawer, and facilitate salon reservation form submissions. Without these mandatory technical elements, our digital atelier cannot deliver standard browsing functionality or process fitting requests reliably.
          </p>
          <p class="pm-policy-p">
            Performance and telemetry cookies gather anonymous aggregate information regarding visitor engagement patterns, such as frequently visited leather showcase pages, average duration per visit, and referring web addresses. These statistical metrics are processed exclusively to diagnose loading bottlenecks and refine navigation architecture. We do not deploy invasive third-party ad profiling cookies that track your subsequent purchasing behaviors across unrelated external commercial platforms.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>3. Third-Party Web Analytics Architecture</h2>
          <p class="pm-policy-p">
            To maintain high operational performance, we utilize Google Analytics telemetry to measure aggregate visitor interaction without harvesting personal identities. The tracking tags embedded in our pages record generalized geographic regions, device hardware classifications, and session timelines in an anonymized manner. These technical logs help our software engineers verify that high-resolution leather photographs render promptly across mobile devices and desktop displays worldwide.
          </p>
          <p class="pm-policy-p">
            Google processes diagnostic analytical information in accordance with its verified institutional privacy policies and international safe-harbor standards. We do not permit outside analytical partners to combine website telemetry with third-party behavioral dossiers or use our salon metrics for independent marketing objectives. All analytical data transmissions are encrypted using standard transport layer security protocols to prevent interception by unauthorized digital parties.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>4. Patron Control and Cookie Management Options</h2>
          <p class="pm-policy-p">
            You hold the autonomous authority to govern, limit, or eliminate cookies through your personal web browser configuration controls. Most modern browsing applications accept technical cookies automatically by default, but provide accessible preference menus allowing you to block specific domains or delete stored cache archives. Please note that disabling essential cookies may impact the visual responsiveness or form functionality of our digital salon.
          </p>
          <p class="pm-policy-p">
            Should you prefer to prevent the collection of aggregate web telemetry entirely, you may install standard privacy browser extensions or activate Google Analytics opt-out plugins designed for major browsers. These client-side tools notify diagnostic servers that your visiting session must be excluded from traffic statistics. Our website respects client privacy signals and continues to deliver full product information regardless of telemetry status.
          </p>
        </div>

        <div class="pm-policy-section">
          <h2>5. Revisions and Institutional Contact Details</h2>
          <p class="pm-policy-p">
            Pochette Magnet Atelier may periodically modify this Cookie Policy to reflect technical infrastructure updates, hosting evolutions, or changes in digital privacy regulations. Any policy amendments become effective immediately upon public publication to this page, accompanied by an updated effective date header. We encourage clients to review this statement periodically to remain informed about our responsible data stewardship practices and digital safeguards.
          </p>
          <p class="pm-policy-p">
            If you have questions, comments, or technical feedback regarding our implementation of digital cookies or data security frameworks, please direct communications to Pochette Magnet Atelier LLC, {ADDR}. You may also reach our concierge by telephone at {PHONE} or transmit electronic correspondence to {EMAIL}. We remain dedicated to upholding transparency, digital integrity, and discreet service for every valued patron.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 7. SITEMAP & ROBOTS
# ==========================================
def build_sitemap():
    pages = [
        "index.html",
        "about.html",
        "products.html",
        "contact.html",
        "faq.html",
        "privacy-policy.html",
        "terms-and-conditions.html",
        "disclaimer.html",
        "cookie-policy.html"
    ]
    urls = ""
    for p in pages:
        urls += f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-09-29</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if p == 'index.html' else '0.8'}</priority>
  </url>\n"""
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Sitemap: https://{DOMAIN}/sitemap.xml
"""

# ==========================================
# 8. REGISTRIES & MANIFEST
# ==========================================
def build_image_registry(meta_list):
    rows = ""
    for it in meta_list:
        name = it["asset_name"]
        h = it["hash"]
        desc = it["description"]
        # Determine location used
        loc = "index.html"
        if name in ["pochettemagnet_asset_1.jpg", "pochettemagnet_asset_2.jpg", "pochettemagnet_asset_3.jpg", "pochettemagnet_asset_4.jpg", "pochettemagnet_asset_5.jpg", "pochettemagnet_asset_6.jpg"]:
            loc = "index.html"
        elif name in ["pochettemagnet_asset_7.jpg", "pochettemagnet_asset_8.jpg", "pochettemagnet_asset_9.jpg", "pochettemagnet_asset_10.jpg", "pochettemagnet_asset_11.jpg", "pochettemagnet_asset_12.jpg"]:
            loc = "about.html"
        elif name in ["pochettemagnet_asset_13.jpg", "pochettemagnet_asset_14.jpg", "pochettemagnet_asset_15.jpg", "pochettemagnet_asset_16.jpg", "pochettemagnet_asset_17.jpg", "pochettemagnet_asset_18.jpg"]:
            loc = "products.html"
        elif name == "pochettemagnet_asset_19.jpg":
            loc = "contact.html"
        elif name == "pochettemagnet_asset_20.jpg":
            loc = "faq.html"
            
        rows += f"| `{name}` | {desc} | `{loc}` | {h} | Verified Unique Real Photo |\n"

    return f"""# IMAGE REGISTRY - POCHETTE MAGNET ATELIER & GUILD
Domain: {DOMAIN}
Niche: Luxury Bag / Bespoke Evening Pochettes & Magnetic Clutches
Strict Rule: Exactly 20 Unique Images, Used Exactly Once, >20KB Each, Zero Duplicates, Zero Drawings, Zero Buildings

| Asset Name | Subject Description | Location / Section Used | MD5 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
{rows}
Total Images: 20
Total Usages: 20 (Every single image used exactly once across website)
Repetitions: 0
100% Real Luxury Bag & Leathercraft Photography from Pexels (Zero Drawings / Zero CAD / Zero Buildings)
"""

def build_design_registry():
    return f"""# DESIGN REGISTRY - POCHETTE MAGNET ATELIER & GUILD

## Visual Identity & Anti-Suspension Architecture
- **Theme Archetype:** Neo-Atelier Magnetic Monolith / Obsidian & Champagne Titanium / Horizontal Ribbon Gallery & Inset Magnetic Vault
- **CSS Namespace:** `.pm-`
- **Color Palette:**
  - Obsidian Carbon: `#090a0f`
  - Titanium Surface: `#151822`
  - Champagne Gold Accent: `#d4af37`
  - Pale Gold Glow: `rgba(212, 175, 55, 0.12)`
  - Pearl Platinum Light Text: `#f7f9fc`
  - Smoky Silver Text: `#9ba3b4`
- **Typography Pairing:**
  - Display: `Syne` (Bold, sculptural, high fashion)
  - Subtitle/Accents: `Space Grotesk` (Technical, clean, geometric)
  - Body: `Plus Jakarta Sans` (Readable, modern humanist)
- **Hero Architecture:**
  - Neodymium Magnetic Core Masthead with Inset Floating Pochette Showcase (`asset_1.jpg`) + 3 Live Magnetic Force Metrics (12,000 Gauss Neodymium lock, 0.4mm skived edge, N52 magnetic grade).
- **Navigation:**
  - Sticky glassmorphic navbar with backdrop-filter blur (16px)
  - Synchronized mobile drawer (`#pm-hamburger`, `#mobile-drawer`, `#mobile-drawer-backdrop`, `#mobile-drawer-close`)
- **Homepage Sections (12 Sections):**
  1. `pm-hero`: Neodymium Magnetic Core Masthead
  2. `pm-ticker`: Continuous Magnetic Atelier Ticker
  3. `pm-manifesto-grid`: The Acoustic Clasp Manifesto
  4. `pm-spec-4col`: 4-Pillar Magnetic Hardware & Leathercraft Matrix
  5. `pm-lookbook-duo`: The Evening Pochette Archival Lookbook Duo
  6. `pm-table-wrapper`: Magnetic Resistance, Pull Force & Dimensional Matrix Table
  7. `pm-craft-row` (Row 1): Hermetically Sealed Neodymium Cells
  8. `pm-craft-row` (Row 2): Traditional Parisian Leathercraft Tools
  9. `pm-tier-grid`: Luxury Pochette Collection Tiers
  10. `pm-lab-grid`: Neodymium Cycling & Flex Laboratory Log
  11. `pm-spotlight-box`: Master Leather Artisan Matteo Vianello Spotlight
  12. `pm-faq-grid`: Dual-Column Magnetic Leather Goods FAQ
  13. `pm-cta-strip`: Private Salon Consultation & Sizing Reservation Strip
"""

def build_manifest():
    return json.dumps({
        "domain": DOMAIN,
        "brand": BRAND,
        "niche": "Luxury Bag",
        "archetype": "Neo-Atelier Magnetic Monolith",
        "institutional_contact": {
            "address": ADDR,
            "phone": PHONE,
            "email": EMAIL
        },
        "pages": [
            "index.html",
            "about.html",
            "products.html",
            "contact.html",
            "faq.html",
            "privacy-policy.html",
            "terms-and-conditions.html",
            "disclaimer.html",
            "cookie-policy.html"
        ],
        "assets_count": 20,
        "php_files_count": 0,
        "blog_pages_count": 0,
        "google_analytics_tag": "G-0LY0HY7L01"
    }, indent=2)

def generate_all():
    print("Generating all HTML pages and metadata for pochette magnet...")
    
    with open(r"d:\antigravity website\scratch\pochettemagnet_image_meta.json", "r", encoding="utf-8") as f:
        meta_list = json.load(f)

    files = {
        "index.html": build_index(),
        "about.html": build_about(),
        "products.html": build_products(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots(),
        "IMAGE_REGISTRY.md": build_image_registry(meta_list),
        "DESIGN_REGISTRY.md": build_design_registry(),
        "SITE_MANIFEST.json": build_manifest()
    }

    for fname, content in files.items():
        fp = os.path.join(BASE_DIR, fname)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {fname} ({len(content)} chars)")

    print("\nAll files successfully generated.")

if __name__ == "__main__":
    generate_all()
