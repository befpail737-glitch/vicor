#!/usr/bin/env python3
# Script to create remaining Vicor product detail pages

import os

# Define the base HTML template
base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Vicor Power Modules - LiTong Distributor</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">

    <!-- Open Graph / Social Media Meta Tags -->
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://vicor.elec-distributor.com{og_url}">
    <meta property="og:image" content="https://vicor.elec-distributor.com/images/{image}.svg">

    <!-- Schema Markup for Product Detail -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "{schema_name}",
        "description": "{schema_description}",
        "manufacturer": {{
            "@type": "Organization",
            "name": "Vicor Corporation"
        }},
        "brand": {{
            "@type": "Brand", 
            "name": "Vicor"
        }},
        "image": "https://vicor.elec-distributor.com/images/{image}.svg",
        "category": "{schema_category}",
        "offers": {{
            "@type": "Offer",
            "seller": {{
                "@type": "Organization",
                "name": "LiTong Group"
            }},
            "availability": "https://schema.org/InStock",
            "priceCurrency": "USD"
        }}
    }}
    </script>

    <!-- Favicon -->
    <link rel="icon" href="../../../images/logo.svg" type="image/svg+xml">

    <!-- Stylesheets -->
    <link rel="stylesheet" href="../../../css/style.css">
</head>
<body>
    <!-- Header -->
    <header class="header" role="banner">
        <div class="container">
            <div class="header-top">
                <a href="../../../index.html" class="logo" aria-label="LiTong Vicor Distributor Home">
                    <img src="../../../images/logo.svg" alt="LiTong Vicor Distributor Logo" width="180" height="50">
                </a>

                <!-- Mobile Menu Toggle -->
                <button class="mobile-menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
                    <span class="hamburger"></span>
                    <span class="hamburger"></span>
                    <span class="hamburger"></span>
                </button>
            </div>

            <nav class="main-nav" role="navigation" aria-label="Main navigation">
                <ul class="nav-menu">
                    <li class="nav-item"><a href="../../../index.html" class="nav-link">Home</a></li>
                    <li class="nav-item dropdown active">
                        <a href="../../../products/" class="nav-link">Products <span class="dropdown-arrow" aria-hidden="true">▼</span></a>
                        <ul class="dropdown-menu">
                            <li><a href="../../../products/modular-power/" class="dropdown-link{mp_active}">Modular Power</a></li>
                            <li><a href="../../../products/input-filter/" class="dropdown-link{if_active}">Input Filter</a></li>
                            <li><a href="../../../products/picor/" class="dropdown-link{p_active}">Picor</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="../../../solutions/" class="nav-link{sol_active}">Solutions <span class="dropdown-arrow" aria-hidden="true">▼</span></a>
                        <ul class="dropdown-menu">
                            <li><a href="../../../solutions/data-center/" class="dropdown-link">Data Center</a></li>
                            <li><a href="../../../solutions/aerospace/" class="dropdown-link{aero_active}">Aerospace</a></li>
                            <li><a href="../../../solutions/robotics/" class="dropdown-link">Robotics</a></li>
                            <li><a href="../../../solutions/rail/" class="dropdown-link">Rail</a></li>
                            <li><a href="../../../solutions/automotive/" class="dropdown-link{auto_active}">Automotive</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="../../../support/" class="nav-link">Support <span class="dropdown-arrow" aria-hidden="true">▼</span></a>
                        <ul class="dropdown-menu">
                            <li><a href="../../../support/selection-guides/" class="dropdown-link">Selection Guides</a></li>
                            <li><a href="../../../support/application-notes/" class="dropdown-link">Application Notes</a></li>
                            <li><a href="../../../support/thermal-design/" class="dropdown-link">Thermal Design</a></li>
                            <li><a href="../../../support/packaging-technology/" class="dropdown-link">Packaging Technology</a></li>
                            <li><a href="../../../support/faq/" class="dropdown-link">FAQ</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="../../../news/" class="nav-link">News <span class="dropdown-arrow" aria-hidden="true">▼</span></a>
                        <ul class="dropdown-menu">
                            <li><a href="../../../news/industry-dynamics/" class="dropdown-link">Industry Dynamics</a></li>
                            <li><a href="../../../news/company-news/" class="dropdown-link">Company News</a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a href="../../../about/" class="nav-link">About</a></li>
                    <li class="nav-item"><a href="../../../contact/" class="nav-link cta-button">Contact</a></li>
                </ul>
            </nav>
        </div>

        <!-- Floating Contact Bar -->
        <div class="floating-contact" aria-label="Contact information">
            <div class="contact-item">
                <span class="contact-icon">📱</span>
                <span>WhatsApp: +86 15013702378</span>
            </div>
            <div class="contact-item">
                <span class="contact-icon">💬</span>
                <span>WeChat: +86 18612518271</span>
            </div>
        </div>
    </header>

    <!-- Breadcrumb -->
    <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="container">
            <a href="../../../index.html">Home</a>
            <span class="breadcrumb-separator">/</span>
            <a href="../../../products/">Products</a>
            <span class="breadcrumb-separator">/</span>
            <a href="../../../products/{prod_type}/">{prod_type_title}</a>
            <span class="breadcrumb-separator">/</span>
            <a href="../../../products/{prod_type}/{series}/">{series_title} Modules</a>
            <span class="breadcrumb-separator">/</span>
            <span class="current-page">{sub_series_title}</span>
        </div>
    </nav>

    <!-- Main Content Area -->
    <main class="main-content" id="main-content" role="main">
        <div class="container">
            <article>
                <header class="article-header">
                    <h1>Vicor {full_series_title} - Technical Details & Specifications</h1>
                    <div class="article-meta">
                        <span class="meta-item">{prod_type_title} / {series_title}</span>
                        <span class="meta-separator">•</span>
                        <time datetime="2025-01-01">January 1, 2025</time>
                        <span class="meta-separator">•</span>
                        <span class="meta-item">Technical Article</span>
                    </div>
                </header>

                <div class="article-content">
                    <p class="article-lead">
                        {lead_content}
                    </p>

                    <h2>Overview</h2>
                    <p>
                        {overview_content}
                    </p>
                    <p>
                        {overview_content2}
                    </p>

                    <h2>Key Features</h2>
                    <div class="grid grid--2">
                        <div class="card">
                            <h3>{feature1_title}</h3>
                            <p>{feature1_desc}</p>
                        </div>
                        <div class="card">
                            <h3>{feature2_title}</h3>
                            <p>{feature2_desc}</p>
                        </div>
                        <div class="card">
                            <h3>{feature3_title}</h3>
                            <p>{feature3_desc}</p>
                        </div>
                        <div class="card">
                            <h3>{feature4_title}</h3>
                            <p>{feature4_desc}</p>
                        </div>
                    </div>

                    <h2>Technical Specifications</h2>
                    <div class="table-responsive">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Model</th>
                                    <th>Power Range</th>
                                    <th>Efficiency</th>
                                    <th>Input Voltage</th>
                                    <th>Output Voltage/Current</th>
                                    <th>Package</th>
                                    <th>Applications</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>{model1}</td>
                                    <td>{power1}</td>
                                    <td>{eff1}</td>
                                    <td>{input1}</td>
                                    <td>{output1}</td>
                                    <td>{package1}</td>
                                    <td>{app1}</td>
                                </tr>
                                <tr>
                                    <td>{model2}</td>
                                    <td>{power2}</td>
                                    <td>{eff2}</td>
                                    <td>{input2}</td>
                                    <td>{output2}</td>
                                    <td>{package2}</td>
                                    <td>{app2}</td>
                                </tr>
                                <tr>
                                    <td>{model3}</td>
                                    <td>{power3}</td>
                                    <td>{eff3}</td>
                                    <td>{input3}</td>
                                    <td>{output3}</td>
                                    <td>{package3}</td>
                                    <td>{app3}</td>
                                </tr>
                                <tr>
                                    <td>{model4}</td>
                                    <td>{power4}</td>
                                    <td>{eff4}</td>
                                    <td>{input4}</td>
                                    <td>{output4}</td>
                                    <td>{package4}</td>
                                    <td>{app4}</td>
                                </tr>
                                <tr>
                                    <td>{model5}</td>
                                    <td>{power5}</td>
                                    <td>{eff5}</td>
                                    <td>{input5}</td>
                                    <td>{output5}</td>
                                    <td>{package5}</td>
                                    <td>{app5}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h2>Applications</h2>
                    <p>
                        {applications_intro}
                    </p>
                    <div class="grid grid--3">
                        <div class="card">
                            <h3>{app_card1_title}</h3>
                            <p>{app_card1_desc}</p>
                        </div>
                        <div class="card">
                            <h3>{app_card2_title}</h3>
                            <p>{app_card2_desc}</p>
                        </div>
                        <div class="card">
                            <h3>{app_card3_title}</h3>
                            <p>{app_card3_desc}</p>
                        </div>
                    </div>

                    <h2>Design Considerations</h2>
                    <div class="card">
                        <h3>{design_consideration1_title}</h3>
                        <p>
                            {design_consideration1_content}
                        </p>

                        <h3>{design_consideration2_title}</h3>
                        <p>
                            {design_consideration2_content}
                        </p>

                        <h3>{design_consideration3_title}</h3>
                        <p>
                            {design_consideration3_content}
                        </p>
                    </div>

                    <h2>Frequently Asked Questions</h2>
                    <div class="card">
                        <details class="faq-item">
                            <summary>{faq1_question}</summary>
                            <p>{faq1_answer}</p>
                        </details>
                        <details class="faq-item">
                            <summary>{faq2_question}</summary>
                            <p>{faq2_answer}</p>
                        </details>
                        <details class="faq-item">
                            <summary>{faq3_question}</summary>
                            <p>{faq3_answer}</p>
                        </details>
                    </div>

                    <h2>Related Products</h2>
                    <div class="grid grid--3">
                        <a href="../../../modular-power/dcm/" class="card-link">
                            <div class="card">
                                <h3>DCM Modules</h3>
                                <p>Fixed-ratio bus converters with galvanic isolation for voltage transformation without regulation.</p>
                            </div>
                        </a>
                        <a href="../../../modular-power/bcm/" class="card-link">
                            <div class="card">
                                <h3>BCM Modules</h3>
                                <p>Current multiplication bus converters with bidirectional power flow for non-isolated applications.</p>
                            </div>
                        </a>
                        <a href="../../../modular-power/vtm/" class="card-link">
                            <div class="card">
                                <h3>VTM Modules</h3>
                                <p>Vicor Transformer Modules for current multiplication with isolation in FPA systems.</p>
                            </div>
                        </a>
                    </div>
                </div>

                <!-- Call to Action -->
                <section class="section-cta">
                    <div class="card text-center">
                        <h3>Need {full_series_title} for Your Application?</h3>
                        <p>Our FAE team specializes in {full_series_title} selection and implementation. Contact us for technical support, custom solutions, or volume pricing.</p>
                        <div class="cta-buttons">
                            <a href="../../../contact/" class="btn btn--primary">Contact Technical Support</a>
                            <a href="../../../contact/" class="btn btn--secondary" style="margin-left: var(--spacing-md);">Request Sample</a>
                            <a href="../../../contact/" class="btn btn--ghost" style="margin-left: var(--spacing-md);">Request Quote</a>
                        </div>
                    </div>
                </section>
            </article>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="../../../modular-power/">Modular Power</a></li>
                        <li><a href="../../../input-filter/">Input Filter</a></li>
                        <li><a href="../../../picor/">Picor Solutions</a></li>
                        <li><a href="../../../data-center/">Data Center Solutions</a></li>
                        <li><a href="../../../selection-guides/">Selection Guides</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Sales Network</h3>
                    <ul>
                        <li><a href="../../../contact/#hong-kong">Hong Kong Headquarters</a></li>
                        <li><a href="../../../contact/#beijing">Beijing Office</a></li>
                        <li><a href="../../../contact/#shanghai">Shanghai Office</a></li>
                        <li><a href="../../../contact/#shenzhen">Shenzhen Office</a></li>
                        <li><a href="../../../contact/#usa">USA Office</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Contact</h3>
                    <ul>
                        <li>Email: info@elec-distributor.com</li>
                        <li>WhatsApp: +86 15013702378</li>
                        <li>WeChat: +86 18612518271</li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h3>Legal</h3>
                    <ul>
                        <li><a href="../../../privacy-policy/">Privacy Policy</a></li>
                        <li><a href="../../../terms-of-service/">Terms of Service</a></li>
                        <li><a href="../../../cookie-policy/">Cookie Policy</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; <span id="current-year">2025</span> LiTong Group. All rights reserved. Official authorized Vicor distributor.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="../../../js/main.js"></script>

    <!-- Update current year in footer -->
    <script>
        document.getElementById('current-year').textContent = new Date().getFullYear();
    </script>
</body>
</html>"""

# Define the pages to create
pages_to_create = [
    # PRM Series
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/modular-power/prm/automotive/index.html",
        "data": {
            'title': "PRM Automotive Series - AEC-Q100 Qualified Regulated Converters",
            'description': "Vicor PRM Automotive Series - AEC-Q100 qualified regulated bus converters for automotive applications in Factorized Power Architecture (FPA). High-reliability regulation with enhanced environmental specifications.",
            'keywords': "PRM automotive series, AEC-Q100 qualified, regulated bus converters, automotive power modules, factorized power architecture, FPA, regulated DC-DC converters",
            'og_title': "PRM Automotive Series - AEC-Q100 Qualified Regulated Converters",
            'og_url': "/products/modular-power/prm/automotive/",
            'image': "prm-automotive",
            'schema_name': "Vicor PRM Automotive Series",
            'schema_description': "AEC-Q100 qualified regulated bus converters for automotive applications in Factorized Power Architecture (FPA)",
            'schema_category': "Electronics > Power Supplies",
            'prod_type': "modular-power", 
            'prod_type_title': "Modular Power",
            'series': "prm",
            'series_title': "PRM",
            'sub_series_title': "Automotive Series",
            'full_series_title': "PRM™ Automotive Series",
            'mp_active': " active",
            'if_active': "",
            'p_active': "",
            'sol_active': "",
            'aero_active': "",
            'auto_active': " active",
            'lead_content': "The PRM Automotive Series features AEC-Q100 qualified regulated bus converters designed specifically for automotive applications in Factorized Power Architecture (FPA) systems. These modules provide precise regulation and power factor correction while meeting automotive industry standards for reliability and environmental performance.",
            'overview_content': "The PRM Automotive Series represents Vicor's solution for automotive applications requiring regulated power conversion in Factorized Power Architecture (FPA) systems.",
            'overview_content2': "PRM (Primary Regulated Module) modules work in conjunction with VTMs (Vicor Transformer Modules) to provide a two-stage power conversion system. The PRM provides regulation and power factor correction, while the VTM provides current multiplication and isolation.",
            'feature1_title': "AEC-Q100 Qualified",
            'feature1_desc': "Full AEC-Q100 qualification ensures reliability and performance in harsh automotive environments with extreme temperature and vibration.",
            'feature2_title': "Primary Regulation",
            'feature2_desc': "Provides tightly regulated output voltage with excellent line and load regulation in automotive FPA systems.",
            'feature3_title': "Automotive-Grade Reliability",
            'feature3_desc': "Engineered and tested to meet automotive industry standards for vibration, shock, temperature range, and electromagnetic compatibility.",
            'feature4_title': "Factorized Power Architecture",
            'feature4_desc': "Works with VTMs to create high-efficiency automotive power systems with optimized performance for vehicle applications.",
            'model1': "PRM481A015-H",
            'power1': "300W",
            'eff1': "97.0%",
            'input1': "36-75V",
            'output1': "42-54V",
            'package1': "VIA",
            'app1': "48V automotive systems",
            'model2': "PRM481A030-H",
            'power2': "600W",
            'eff2': "97.2%",
            'input2': "36-75V",
            'output2': "42-54V",
            'package2': "VIA",
            'app2': "High-power automotive",
            'model3': "PRM481A046-H",
            'power3': "1000W",
            'eff3': "97.1%",
            'input3': "36-75V",
            'output3': "42-54V",
            'package3': "VIA",
            'app3': "Automotive computing",
            'model4': "PRM241A046-H",
            'power4': "1000W",
            'eff4': "96.6%",
            'input4': "18-36V",
            'output4': "21-27V",
            'package4': "VIA",
            'app4': "12V automotive systems",
            'model5': "PRM121A023-H",
            'power5': "500W",
            'eff5': "96.4%",
            'input5': "9-18V",
            'output5': "10.5-13.5V",
            'package5': "VIA",
            'app5': "Low-voltage automotive",
            'applications_intro': "PRM Automotive modules are optimized for automotive applications requiring regulated power conversion with high efficiency and reliability. Common applications include:",
            'app_card1_title': "48V Mild Hybrid",
            'app_card1_desc': "Regulated bus voltage for 48V to 12V conversion in mild hybrid vehicle power systems with FPA implementation.",
            'app_card2_title': "Electric Vehicle Power",
            'app_card2_desc': "Regulated power supplies for electric vehicle battery management and charging systems with automotive qualification.",
            'app_card3_title': "Automotive Electronics",
            'app_card3_desc': "Power supplies for automotive control units, safety systems, and electric power steering requiring high reliability.",
            'design_consideration1_title': "Factorized Power Architecture",
            'design_consideration1_content': "PRM modules must be used in conjunction with VTMs to form a complete power solution. The PRM provides regulation and power factor correction, while the VTM provides current multiplication and isolation. The output of the PRM connects to the input of the VTM for the complete FPA solution.",
            'design_consideration2_title': "Automotive Environment",
            'design_consideration2_content': "PRM Automotive modules are qualified for automotive temperature ranges (-40°C to +105°C) and tested for vibration, shock, and EMC compliance. Design must ensure proper derating in high-temperature environments to maintain reliability.",
            'design_consideration3_title': "System Integration",
            'design_consideration3_content': "PRM Automotive modules excel in applications where you need regulated power with high efficiency and automotive qualification. They are ideal for FPA systems in automotive environments.",
            'faq1_question': "What is Factorized Power Architecture (FPA)?",
            'faq1_answer': "FPA is Vicor's approach to power system design that separates regulation from current multiplication using PRM and VTM modules. This allows optimization of each function independently, resulting in higher efficiency, power density, and performance.",
            'faq2_question': "What does AEC-Q100 qualification mean?",
            'faq2_answer': "AEC-Q100 is an industry-standard qualification for integrated circuits in automotive applications. It includes tests for temperature, humidity, vibration, and electromagnetic compatibility.",
            'faq3_question': "How do PRM and VTM modules work together?",
            'faq3_answer': "The PRM provides regulation and power factor correction, while the VTM provides current multiplication and isolation. The PRM output connects to the VTM input to create a complete regulated, isolated power solution."
        }
    },
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/modular-power/prm/aerospace/index.html",
        "data": {
            'title': "PRM Aerospace Series - High-Reliability Regulated Converters",
            'description': "Vicor PRM Aerospace Series - High-reliability regulated bus converters for aerospace and defense applications in Factorized Power Architecture (FPA). Enhanced environmental specifications and radiation tolerance.",
            'keywords': "PRM aerospace series, aerospace power modules, high-reliability power conversion, radiation tolerant, regulated bus converters, factorized power architecture, FPA",
            'og_title': "PRM Aerospace Series - High-Reliability Regulated Converters",
            'og_url': "/products/modular-power/prm/aerospace/",
            'image': "prm-aerospace",
            'schema_name': "Vicor PRM Aerospace Series",
            'schema_description': "High-reliability regulated bus converters for aerospace and defense applications in Factorized Power Architecture (FPA)",
            'schema_category': "Electronics > Power Supplies",
            'prod_type': "modular-power", 
            'prod_type_title': "Modular Power",
            'series': "prm",
            'series_title': "PRM",
            'sub_series_title': "Aerospace Series",
            'full_series_title': "PRM™ Aerospace Series",
            'mp_active': " active",
            'if_active': "",
            'p_active': "",
            'sol_active': "",
            'aero_active': " active",
            'auto_active': "",
            'lead_content': "The PRM Aerospace Series features high-reliability regulated bus converters designed specifically for aerospace, defense, and space applications in Factorized Power Architecture (FPA) systems. These modules provide precise regulation and power factor correction while meeting aerospace industry standards for environmental performance and reliability.",
            'overview_content': "The PRM Aerospace Series represents Vicor's solution for aerospace applications requiring regulated power conversion in Factorized Power Architecture (FPA) systems.",
            'overview_content2': "PRM (Primary Regulated Module) modules work in conjunction with VTMs (Vicor Transformer Modules) to provide a two-stage power conversion system. The PRM provides regulation and power factor correction, while the VTM provides current multiplication and isolation.",
            'feature1_title': "Enhanced Reliability",
            'feature1_desc': "Engineered for aerospace and defense applications with extensive life testing and enhanced screening for high-reliability performance.",
            'feature2_title': "Radiation Hardened Options",
            'feature2_desc': "Available with radiation hardened options for space exploration and satellite applications with total ionizing dose (TID) and single event effects (SEE) protection.",
            'feature3_title': "Hermetic Packaging",
            'feature3_desc': "Available in hermetically sealed packages for applications requiring maximum protection from environmental contaminants.",
            'feature4_title': "High Efficiency",
            'feature4_desc': "Achieves up to 97.4% efficiency in regulation stage, contributing to overall system efficiency in aerospace FPA.",
            'model1': "PRM481A015-M",
            'power1': "300W",
            'eff1': "97.2%",
            'input1': "36-75V",
            'output1': "42-54V",
            'package1': "VIA-Hermetic",
            'app1': "Satellite systems",
            'model2': "PRM481A030-M",
            'power2': "600W",
            'eff2': "97.4%",
            'input2': "36-75V",
            'output2': "42-54V",
            'package2': "VIA-Hermetic",
            'app2': "Space applications",
            'model3': "PRM481A046-M",
            'power3': "1000W",
            'eff3': "97.3%",
            'input3': "36-75V",
            'output3': "42-54V",
            'package3': "VIA-Hermetic",
            'app3': "High-power aerospace",
            'model4': "PRM241A046-M",
            'power4': "1000W",
            'eff4': "96.8%",
            'input4': "18-36V",
            'output4': "21-27V",
            'package4': "VIA-Hermetic",
            'app4': "Avionics systems",
            'model5': "PRM121A023-M",
            'power5': "500W",
            'eff5': "96.6%",
            'input5': "9-18V",
            'output5': "10.5-13.5V",
            'package5': "VIA-Hermetic",
            'app5': "Low-voltage aerospace",
            'applications_intro': "PRM Aerospace modules are optimized for aerospace and defense applications requiring regulated power conversion with high reliability. Common applications include:",
            'app_card1_title': "Satellite Power Systems",
            'app_card1_desc': "Regulated power supplies for satellite systems with radiation tolerance and extreme temperature operation.",
            'app_card2_title': "Avionics Power",
            'app_card2_desc': "Regulated power supplies for aircraft avionics systems requiring high reliability and environmental qualification.",
            'app_card3_title': "Space Exploration Equipment",
            'app_card3_desc': "Power regulation for spacecraft and planetary exploration equipment with extreme environment requirements.",
            'design_consideration1_title': "Factorized Power Architecture",
            'design_consideration1_content': "PRM modules must be used in conjunction with VTMs to form a complete power solution. The PRM provides regulation and power factor correction, while the VTM provides current multiplication and isolation. The output of the PRM connects to the input of the VTM for the complete FPA solution.",
            'design_consideration2_title': "Extreme Environment Operation",
            'design_consideration2_content': "PRM Aerospace modules are designed for extreme temperature ranges (-55°C to +125°C) and tested for vibration, shock, and radiation exposure. Design must account for derating in extreme conditions to maintain reliability and performance.",
            'design_consideration3_title': "Radiation Effects",
            'design_consideration3_content': "For space applications, consider total ionizing dose (TID) and single event effects (SEE) impacts. Radiation hardened options are available to ensure continued operation in high-radiation environments.",
            'faq1_question': "What is Factorized Power Architecture (FPA)?",
            'faq1_answer': "FPA is Vicor's approach to power system design that separates regulation from current multiplication using PRM and VTM modules. This allows optimization of each function independently, resulting in higher efficiency, power density, and performance.",
            'faq2_question': "What radiation tolerance options are available?",
            'faq2_answer': "PRM Aerospace modules are available with radiation hardened options providing protection against total ionizing dose (TID) and single event effects (SEE) for space applications.",
            'faq3_question': "How do PRM and VTM modules work together?",
            'faq3_answer': "The PRM provides regulation and power factor correction, while the VTM provides current multiplication and isolation. The PRM output connects to the VTM input to create a complete regulated, isolated power solution."
        }
    },
    # VTM Series
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/modular-power/vtm/low-profile/index.html",
        "data": {
            'title': "VTM Low Profile Series - Compact Transformer Modules",
            'description': "Vicor VTM Low Profile Series - High-efficiency Vicor Transformer Modules for Factorized Power Architecture (FPA) in LVM packaging. Provides current multiplication with galvanic isolation.",
            'keywords': "VTM low profile series, Vicor transformer modules, factorized power architecture, FPA, current multiplication, isolated power converters, low profile power modules",
            'og_title': "VTM Low Profile Series - Compact Transformer Modules",
            'og_url': "/products/modular-power/vtm/low-profile/",
            'image': "vtm-low-profile",
            'schema_name': "Vicor VTM Low Profile Series",
            'schema_description': "High-efficiency Vicor Transformer Modules for Factorized Power Architecture (FPA) in low-profile packaging",
            'schema_category': "Electronics > Power Supplies",
            'prod_type': "modular-power", 
            'prod_type_title': "Modular Power",
            'series': "vtm",
            'series_title': "VTM",
            'sub_series_title': "Low Profile Series",
            'full_series_title': "VTM™ Low Profile Series",
            'mp_active': " active",
            'if_active': "",
            'p_active': "",
            'sol_active': "",
            'aero_active': "",
            'auto_active': "",
            'lead_content': "The VTM Low Profile Series features high-efficiency Vicor Transformer Modules designed for Factorized Power Architecture (FPA) systems in space-constrained applications. These modules provide current multiplication with galvanic isolation when used with PRMs (Primary Regulated Modules), delivering high current at low voltage from an intermediate bus voltage in a compact LVM package.",
            'overview_content': "The VTM Low Profile Series represents Vicor's solution for current multiplication with galvanic isolation in Factorized Power Architecture (FPA) systems for space-constrained applications.",
            'overview_content2': "VTMs (Vicor Transformer Modules) work in conjunction with PRMs (Primary Regulated Modules) to create a complete power solution. The VTM provides current multiplication and isolation, while the PRM provides regulation and power factor correction.",
            'feature1_title': "Current Multiplication",
            'feature1_desc': "VTM modules multiply current while reducing voltage based on the turns ratio, ideal for low-voltage, high-current applications.",
            'feature2_title': "Low Profile Design",
            'feature2_desc': "LVM packaging technology provides a compact, low-profile solution ideal for space-constrained applications with height restrictions.",
            'feature3_title': "Galvanic Isolation",
            'feature3_desc': "Provides safety isolation and noise immunity with high voltage standoff between input and output in a compact form factor.",
            'feature4_title': "High Efficiency",
            'feature4_desc': "Achieves up to 98.2% efficiency through fixed-ratio transformation at high switching frequency with minimal losses.",
            'model1': "VTM4848015-L",
            'power1': "300W",
            'eff1': "98.0%",
            'input1': "42-54V",
            'output1': "1:1",
            'package1': "LVM",
            'app1': "48V to 48V conversion",
            'model2': "VTM4824030-L",
            'power2': "600W",
            'eff2': "98.2%",
            'input2': "42-54V",
            'output2': "2:1",
            'package2': "LVM",
            'app2': "48V to 24V conversion",
            'model3': "VTM4812046-L",
            'power3': "1000W",
            'eff3': "98.1%",
            'input3': "42-54V",
            'output3': "4:1",
            'package3': "LVM",
            'app3': "48V to 12V conversion",
            'model4': "VTM2412046-L",
            'power4': "1000W",
            'eff4': "97.9%",
            'input4': "21-27V",
            'output4': "2:1",
            'package4': "LVM",
            'app4': "24V to 12V conversion",
            'model5': "VTM1206046-L",
            'power5': "500W",
            'eff5': "97.7%",
            'input5': "10.5-13.5V",
            'output5': "2:1",
            'package5': "LVM",
            'app5': "12V to 6V conversion",
            'applications_intro': "VTM Low Profile modules are optimized for applications requiring high current at low voltage with galvanic isolation in space-constrained environments. Common applications include:",
            'app_card1_title': "Aviation Electronics",
            'app_card1_desc': "High-current power delivery for aircraft systems with tight height restrictions and galvanic isolation.",
            'app_card2_title': "Medical Equipment",
            'app_card2_desc': "Compact isolated power supplies for medical devices requiring high current in limited vertical space.",
            'app_card3_title': "Telecommunications",
            'app_card3_desc': "Low-profile isolated power delivery for networking equipment with high efficiency requirements.",
            'design_consideration1_title': "Factorized Power Architecture",
            'design_consideration1_content': "VTMs must be used with PRMs to form a complete power solution. The PRM provides regulation to the intermediate bus voltage, while the VTM provides current multiplication and isolation to the load. The output voltage of the system is determined by both the PRM regulation and the VTM turns ratio.",
            'design_consideration2_title': "Thermal Management",
            'design_consideration2_content': "In space-constrained applications, thermal management becomes critical. Consider airflow and thermal vias to PCB copper to manage heat dissipation in low-profile packages. The compact design may require additional thermal management strategies compared to standard packages.",
            'design_consideration3_title': "Layout Recommendations",
            'design_consideration3_content': "For optimal performance in compact applications, ensure proper decoupling between PRM and VTM stages. Minimize loop inductance between the PRM and VTM to maintain efficiency and stability in tight spaces.",
            'faq1_question': "How do VTMs differ from traditional transformers?",
            'faq1_answer': "VTMs are active transformer modules that operate at high frequency with minimal losses, achieving very high efficiency and power density in compact form. They are designed specifically for FPA systems and provide current multiplication with galvanic isolation.",
            'faq2_question': "What is the relationship between PRM and VTM in FPA?",
            'faq2_answer': "The PRM provides regulation to an intermediate bus voltage (typically 48V), while the VTM provides current multiplication and isolation to the load. The output voltage is determined by the PRM regulation and the VTM turns ratio.",
            'faq3_question': "Can VTMs be used without PRMs?",
            'faq3_answer': "VTMs are designed for use with PRMs in FPA systems to create a complete regulated power solution. However, they can be used with other regulated sources if the input voltage and operating conditions are appropriate."
        }
    },
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/modular-power/vtm/automotive/index.html",
        "data": {
            'title': "VTM Automotive Series - AEC-Q100 Qualified Transformer Modules",
            'description': "Vicor VTM Automotive Series - AEC-Q100 qualified Vicor Transformer Modules for automotive Factorized Power Architecture (FPA). Provides current multiplication with galvanic isolation.",
            'keywords': "VTM automotive series, AEC-Q100 qualified, Vicor transformer modules, automotive power modules, factorized power architecture, FPA, current multiplication",
            'og_title': "VTM Automotive Series - AEC-Q100 Qualified Transformer Modules",
            'og_url': "/products/modular-power/vtm/automotive/",
            'image': "vtm-automotive",
            'schema_name': "Vicor VTM Automotive Series",
            'schema_description': "AEC-Q100 qualified Vicor Transformer Modules for automotive Factorized Power Architecture (FPA)",
            'schema_category': "Electronics > Power Supplies",
            'prod_type': "modular-power", 
            'prod_type_title': "Modular Power",
            'series': "vtm",
            'series_title': "VTM",
            'sub_series_title': "Automotive Series",
            'full_series_title': "VTM™ Automotive Series",
            'mp_active': " active",
            'if_active': "",
            'p_active': "",
            'sol_active': "",
            'aero_active': "",
            'auto_active': " active",
            'lead_content': "The VTM Automotive Series features AEC-Q100 qualified Vicor Transformer Modules designed for automotive Factorized Power Architecture (FPA) systems. These modules provide current multiplication with galvanic isolation when used with PRMs (Primary Regulated Modules), delivering high current at low voltage from an intermediate bus voltage with automotive-grade reliability.",
            'overview_content': "The VTM Automotive Series represents Vicor's solution for current multiplication with galvanic isolation in automotive Factorized Power Architecture (FPA) systems.",
            'overview_content2': "VTMs (Vicor Transformer Modules) work in conjunction with PRMs (Primary Regulated Modules) to create a complete power solution. The VTM provides current multiplication and isolation, while the PRM provides regulation and power factor correction.",
            'feature1_title': "AEC-Q100 Qualified",
            'feature1_desc': "Full AEC-Q100 qualification ensures reliability and performance in harsh automotive environments with extreme temperature and vibration.",
            'feature2_title': "Current Multiplication",
            'feature2_desc': "VTM modules multiply current while reducing voltage based on the turns ratio, ideal for automotive high-current applications.",
            'feature3_title': "Galvanic Isolation",
            'feature3_desc': "Provides safety isolation and noise immunity with high voltage standoff between input and output in automotive environments.",
            'feature4_title': "Automotive-Grade Reliability",
            'feature4_desc': "Engineered and tested to meet automotive industry standards for vibration, shock, temperature range, and electromagnetic compatibility.",
            'model1': "VTM4848015-H",
            'power1': "300W",
            'eff1': "98.0%",
            'input1': "42-54V",
            'output1': "1:1",
            'package1': "VIA",
            'app1': "48V automotive systems",
            'model2': "VTM4824030-H",
            'power2': "600W",
            'eff2': "98.2%",
            'input2': "42-54V",
            'output2': "2:1",
            'package2': "VIA",
            'app2': "48V to 24V automotive",
            'model3': "VTM4812046-H",
            'power3': "1000W",
            'eff3': "98.1%",
            'input3': "42-54V",
            'output3': "4:1",
            'package3': "VIA",
            'app3': "48V to 12V automotive",
            'model4': "VTM2412046-H",
            'power4': "1000W",
            'eff4': "97.9%",
            'input4': "21-27V",
            'output4': "2:1",
            'package4': "VIA",
            'app4': "24V automotive systems",
            'model5': "VTM1206046-H",
            'power5': "500W",
            'eff5': "97.7%",
            'input5': "10.5-13.5V",
            'output5': "2:1",
            'package5': "VIA",
            'app5': "12V automotive systems",
            'applications_intro': "VTM Automotive modules are optimized for automotive applications requiring high current at low voltage with galvanic isolation. Common applications include:",
            'app_card1_title': "48V Mild Hybrid",
            'app_card1_desc': "Current multiplication for 48V to 12V conversion in mild hybrid vehicle power systems with galvanic isolation.",
            'app_card2_title': "Electric Vehicle Power",
            'app_card2_desc': "High-current isolated power delivery in electric vehicle battery management and charging systems.",
            'app_card3_title': "Automotive Electronics",
            'app_card3_desc': "Isolated power supplies for automotive control units, safety systems, and electric power steering requiring high current.",
            'design_consideration1_title': "Factorized Power Architecture",
            'design_consideration1_content': "VTMs must be used with PRMs to form a complete power solution. The PRM provides regulation to the intermediate bus voltage, while the VTM provides current multiplication and isolation to the load. The output voltage of the system is determined by both the PRM regulation and the VTM turns ratio.",
            'design_consideration2_title': "Automotive Environment",
            'design_consideration2_content': "VTM Automotive modules are qualified for automotive temperature ranges (-40°C to +105°C) and tested for vibration, shock, and EMC compliance. Design must ensure proper derating in high-temperature environments to maintain reliability.",
            'design_consideration3_title': "System Integration",
            'design_consideration3_content': "VTM Automotive modules excel in applications where you need isolated, high-current power delivery with preserved dynamics in automotive environments. They are ideal for automotive FPA implementations.",
            'faq1_question': "How do VTMs differ from traditional transformers?",
            'faq1_answer': "VTMs are active transformer modules that operate at high frequency with minimal losses, achieving very high efficiency and power density. They are designed specifically for FPA systems and provide current multiplication with galvanic isolation.",
            'faq2_question': "What is the relationship between PRM and VTM in FPA?",
            'faq2_answer': "The PRM provides regulation to an intermediate bus voltage (typically 48V), while the VTM provides current multiplication and isolation to the load. The output voltage is determined by the PRM regulation and the VTM turns ratio.",
            'faq3_question': "What does AEC-Q100 qualification mean?",
            'faq3_answer': "AEC-Q100 is an industry-standard qualification for integrated circuits in automotive applications. It includes tests for temperature, humidity, vibration, and electromagnetic compatibility."
        }
    },
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/input-filter/power-filters/index.html",
        "data": {
            'title': "Power Filters - Vicor Input Filter Solutions",
            'description': "Vicor Power Filters - Advanced filtering solutions for power systems. Suppress conducted noise and improve power quality in DC and AC power systems.",
            'keywords': 'power filters, power system filters, conducted noise suppression, power quality, Vicor input filters, EMI filters, noise reduction',
            'og_title': "Power Filters - Vicor Input Filter Solutions",
            'og_url': "/products/input-filter/power-filters/",
            'image': "power-filters",
            'schema_name': "Vicor Power Filters",
            'schema_description': "Advanced filtering solutions for power systems",
            'schema_category': "Electronics > Power Supplies > Filters",
            'prod_type': "input-filter", 
            'prod_type_title': "Input Filter",
            'series': "input-filter",
            'series_title': "Input Filter",
            'sub_series_title': "Power Filters",
            'full_series_title': "Power Filters",
            'mp_active': "",
            'if_active': " active",
            'p_active': "",
            'sol_active': "",
            'aero_active': "",
            'auto_active': "",
            'lead_content': "Vicor Power Filters provide advanced filtering solutions for power systems. These filters suppress conducted noise and improve power quality in both DC and AC power applications, ensuring clean and stable power delivery to sensitive electronic equipment.",
            'overview_content': "Power filters are essential components in power systems that help manage conducted electromagnetic noise generated by switching power supplies and other electronic equipment.",
            'overview_content2': "Vicor's power filters use advanced filter topologies and components to suppress both common-mode and differential-mode noise while maintaining low insertion loss for the desired power signal.",
            'feature1_title': "Advanced Filter Topology",
            'feature1_desc': "Utilizes optimized filter configurations including common-mode and differential-mode stages to address different noise types.",
            'feature2_title': "High Frequency Performance",
            'feature2_desc': "Designed to suppress noise across a wide frequency range from kHz to GHz frequencies.",
            'feature3_title': "Low DC Resistance",
            'feature3_desc': "Minimizes power losses and voltage drop in the power delivery system while providing effective filtering.",
            'feature4_title': "High Power Handling",
            'feature4_desc': "Capable of handling high power levels while maintaining effective noise suppression.",
            'model1': "PFx-12V-10A",
            'power1': "120W",
            'eff1': "N/A",
            'input1': "12V",
            'output1': "12V",
            'package1': "Through-Hole",
            'app1': "Low-voltage systems",
            'model2': "PFx-24V-20A",
            'power2': "480W",
            'eff2': "N/A",
            'input2': "24V",
            'output2': "24V",
            'package2': "Through-Hole",
            'app2': "Industrial systems",
            'model3': "PFx-48V-30A",
            'power3': "1440W",
            'eff3': "N/A",
            'input3': "48V",
            'output3': "48V",
            'package3': "Chassis Mount",
            'app3': "High-power systems",
            'model4': "PFx-380VAC-16A",
            'power4': "6kW",
            'eff4': "N/A",
            'input4': "380VAC",
            'output4': "380VAC",
            'package4': "Panel Mount",
            'app4': "AC input systems",
            'model5': "PFx-24V-5A-SMT",
            'power5': "120W",
            'eff5': "N/A",
            'input5': "24V",
            'output5': "24V",
            'package5': "SMT Package",
            'app5': "Space-constrained systems",
            'applications_intro': "Vicor Power Filters are suitable for a wide range of applications where power quality and noise reduction are critical. Common applications include:",
            'app_card1_title': "Data Center Equipment",
            'app_card1_desc': "Filtering for power supplies in servers, networking equipment, and storage systems to ensure clean power and reduce noise coupling.",
            'app_card2_title': "Industrial Automation",
            'app_card2_desc': "Power filtering for PLCs, motor drives, and other industrial equipment to prevent noise interference and maintain system reliability.",
            'app_card3_title': "Telecommunications",
            'app_card3_desc': "Filtering for base stations, routers, and other telecom infrastructure equipment to reduce conducted emissions and improve signal integrity.",
            'design_consideration1_title': "Filter Placement",
            'design_consideration1_content': "Power filters should be placed as close as possible to the power entry point of the equipment to maximize effectiveness. Proper mounting and grounding are essential for optimal performance.",
            'design_consideration2_title': "System Integration",
            'design_consideration2_content': "Consider the interaction between the power filter and other components in the system. Load variations can affect filter performance, so verify operation across the expected range of operating conditions.",
            'design_consideration3_title': "Thermal Management",
            'design_consideration3_content': "Power filters dissipate some power as heat, particularly at higher current levels. Ensure adequate thermal management in the system design to maintain reliable operation.",
            'faq1_question': "What is the difference between common-mode and differential-mode noise?",
            'faq1_answer': "Common-mode noise appears on both power lines with respect to ground in the same direction. Differential-mode noise appears between the power lines in opposite directions. Power filters typically address both types of noise.",
            'faq2_question': "Why are power filters necessary in power systems?",
            'faq2_answer': "Switching power supplies generate high-frequency noise that can interfere with other equipment and cause system instability. Power filters suppress this noise to ensure proper operation and improve power quality.",
            'faq3_question': "How do I select the right power filter for my application?",
            'faq3_answer': "Consider the operating voltage, current, required attenuation, package constraints, and power handling requirements. The filter should have adequate current rating with margin above your application's requirements."
        }
    }
]

# Create the remaining pages
for page in pages_to_create:
    # Create directory if it doesn't exist
    directory = os.path.dirname(page['path'])
    os.makedirs(directory, exist_ok=True)
    
    # Format the template with the page data
    html_content = base_template
    for key, value in page['data'].items():
        html_content = html_content.replace('{' + key + '}', str(value))
    
    # Write the file
    with open(page['path'], 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created: {page['path']}")

print("All remaining pages have been created!")