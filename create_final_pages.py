#!/usr/bin/env python3
# Script to create final Vicor product detail pages

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

# Define the final pages to create
pages_to_create = [
    # VTM Aerospace Series
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/modular-power/vtm/aerospace/index.html",
        "data": {
            'title': "VTM Aerospace Series - High-Reliability Transformer Modules",
            'description': "Vicor VTM Aerospace Series - High-reliability Vicor Transformer Modules for aerospace and defense applications in Factorized Power Architecture (FPA). Enhanced environmental specifications and radiation tolerance.",
            'keywords': "VTM aerospace series, aerospace power modules, high-reliability power conversion, radiation tolerant, Vicor transformer modules, factorized power architecture",
            'og_title': "VTM Aerospace Series - High-Reliability Transformer Modules",
            'og_url': "/products/modular-power/vtm/aerospace/",
            'image': "vtm-aerospace",
            'schema_name': "Vicor VTM Aerospace Series",
            'schema_description': "High-reliability Vicor Transformer Modules for aerospace and defense applications in Factorized Power Architecture (FPA)",
            'schema_category': "Electronics > Power Supplies",
            'prod_type': "modular-power", 
            'prod_type_title': "Modular Power",
            'series': "vtm",
            'series_title': "VTM",
            'sub_series_title': "Aerospace Series",
            'full_series_title': "VTM™ Aerospace Series",
            'mp_active': " active",
            'if_active': "",
            'p_active': "",
            'sol_active': "",
            'aero_active': " active",
            'auto_active': "",
            'lead_content': "The VTM Aerospace Series features high-reliability Vicor Transformer Modules designed for aerospace, defense, and space applications in Factorized Power Architecture (FPA) systems. These modules provide current multiplication with galvanic isolation when used with PRMs (Primary Regulated Modules), delivering high current at low voltage from an intermediate bus voltage with aerospace-grade reliability and radiation tolerance.",
            'overview_content': "The VTM Aerospace Series represents Vicor's solution for aerospace applications requiring current multiplication with galvanic isolation in Factorized Power Architecture (FPA) systems.",
            'overview_content2': "VTMs (Vicor Transformer Modules) work in conjunction with PRMs (Primary Regulated Modules) to create a complete power solution. The VTM provides current multiplication and isolation, while the PRM provides regulation and power factor correction.",
            'feature1_title': "Enhanced Reliability",
            'feature1_desc': "Engineered for aerospace and defense applications with extensive life testing and enhanced screening for high-reliability performance.",
            'feature2_title': "Radiation Hardened Options",
            'feature2_desc': "Available with radiation hardened options for space exploration and satellite applications with total ionizing dose (TID) and single event effects (SEE) protection.",
            'feature3_title': "Hermetic Packaging",
            'feature3_desc': "Available in hermetically sealed packages for applications requiring maximum protection from environmental contaminants.",
            'feature4_title': "High Efficiency",
            'feature4_desc': "Achieves up to 98.2% efficiency through fixed-ratio transformation in aerospace applications.",
            'model1': "VTM4848015-M",
            'power1': "300W",
            'eff1': "98.0%",
            'input1': "42-54V",
            'output1': "1:1",
            'package1': "VIA-Hermetic",
            'app1': "Satellite systems",
            'model2': "VTM4824030-M",
            'power2': "600W",
            'eff2': "98.2%",
            'input2': "42-54V",
            'output2': "2:1",
            'package2': "VIA-Hermetic",
            'app2': "Space applications",
            'model3': "VTM4812046-M",
            'power3': "1000W",
            'eff3': "98.1%",
            'input3': "42-54V",
            'output3': "4:1",
            'package3': "VIA-Hermetic",
            'app3': "High-power aerospace",
            'model4': "VTM2412046-M",
            'power4': "1000W",
            'eff4': "97.9%",
            'input4': "21-27V",
            'output4': "2:1",
            'package4': "VIA-Hermetic",
            'app4': "Avionics systems",
            'model5': "VTM1206046-M",
            'power5': "500W",
            'eff5': "97.7%",
            'input5': "10.5-13.5V",
            'output5': "2:1",
            'package5': "VIA-Hermetic",
            'app5': "Low-voltage aerospace",
            'applications_intro': "VTM Aerospace modules are optimized for aerospace and defense applications requiring high current at low voltage with galvanic isolation. Common applications include:",
            'app_card1_title': "Satellite Power Systems",
            'app_card1_desc': "Current multiplication for satellite systems with radiation tolerance and extreme temperature operation.",
            'app_card2_title': "Avionics Power",
            'app_card2_desc': "High-current isolated power delivery for aircraft avionics systems requiring aerospace-grade reliability.",
            'app_card3_title': "Space Exploration Equipment",
            'app_card3_desc': "Power conversion for spacecraft and planetary exploration equipment with extreme environment requirements.",
            'design_consideration1_title': "Factorized Power Architecture",
            'design_consideration1_content': "VTMs must be used with PRMs to form a complete power solution. The PRM provides regulation to the intermediate bus voltage, while the VTM provides current multiplication and isolation to the load. The output voltage of the system is determined by both the PRM regulation and the VTM turns ratio.",
            'design_consideration2_title': "Extreme Environment Operation",
            'design_consideration2_content': "VTM Aerospace modules are designed for extreme temperature ranges (-55°C to +125°C) and tested for vibration, shock, and radiation exposure. Design must account for derating in extreme conditions to maintain reliability and performance.",
            'design_consideration3_title': "Radiation Effects",
            'design_consideration3_content': "For space applications, consider total ionizing dose (TID) and single event effects (SEE) impacts. Radiation hardened options are available to ensure continued operation in high-radiation environments.",
            'faq1_question': "How do VTMs differ from traditional transformers?",
            'faq1_answer': "VTMs are active transformer modules that operate at high frequency with minimal losses, achieving very high efficiency and power density. They are designed specifically for FPA systems and provide current multiplication with galvanic isolation.",
            'faq2_question': "What is the relationship between PRM and VTM in FPA?",
            'faq2_answer': "The PRM provides regulation to an intermediate bus voltage (typically 48V), while the VTM provides current multiplication and isolation to the load. The output voltage is determined by the PRM regulation and the VTM turns ratio.",
            'faq3_question': "What radiation tolerance options are available?",
            'faq3_answer': "VTM Aerospace modules are available with radiation hardened options providing protection against total ionizing dose (TID) and single event effects (SEE) for space applications."
        }
    },
    # Input Filter Digital Management
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/input-filter/digital-management/index.html",
        "data": {
            'title': "Digital Management - Vicor Input Filter Solutions",
            'description': "Vicor Digital Management Solutions for Input Filters - Advanced digital control and monitoring capabilities for intelligent power filter systems. Features PMBus interface and real-time monitoring.",
            'keywords': "digital management, input filter management, PMBus interface, power filter monitoring, intelligent power filters, Vicor input filters",
            'og_title': "Digital Management - Vicor Input Filter Solutions",
            'og_url': "/products/input-filter/digital-management/",
            'image': "digital-management",
            'schema_name': "Vicor Digital Management Solutions",
            'schema_description': "Advanced digital control and monitoring capabilities for intelligent power filter systems",
            'schema_category': "Electronics > Power Supplies > Digital Control",
            'prod_type': "input-filter", 
            'prod_type_title': "Input Filter",
            'series': "input-filter",
            'series_title': "Input Filter",
            'sub_series_title': "Digital Management",
            'full_series_title': "Digital Management Solutions",
            'mp_active': "",
            'if_active': " active",
            'p_active': "",
            'sol_active': "",
            'aero_active': "",
            'auto_active': "",
            'lead_content': "Vicor Digital Management Solutions for Input Filters provide advanced digital control and monitoring capabilities for intelligent power filter systems. These solutions feature PMBus interface, real-time monitoring, and adaptive control algorithms to optimize filter performance and provide comprehensive system diagnostic capabilities.",
            'overview_content': "Digital Management Solutions represent Vicor's approach to intelligent power filter management, offering advanced control algorithms, system monitoring, and communication capabilities.",
            'overview_content2': "These controllers can be used to manage single or multiple filter units in a system, providing coordinated control for optimal performance and real-time monitoring of critical parameters.",
            'feature1_title': "PMBus Interface",
            'feature1_desc': "Comprehensive digital communication interface for configuration, monitoring, and control of power filter systems.",
            'feature2_title': "Real-Time Monitoring",
            'feature2_desc': "Continuous monitoring of voltage, current, temperature, and filter performance parameters.",
            'feature3_title': "Adaptive Control",
            'feature3_desc': "Dynamic adjustment of filter parameters based on operating conditions for optimal performance.",
            'feature4_title': "System Coordination",
            'feature4_desc': "Simultaneous control of multiple filter units for complex power filter architectures.",
            'model1': "DMS-4CM",
            'power1': "N/A",
            'eff1': "N/A",
            'input1': "PMBus Interface",
            'output1': "4 Channels",
            'package1': "QFN-48",
            'app1': "Multi-channel monitoring",
            'model2': "DMS-8DM",
            'power2': "N/A",
            'eff2': "N/A",
            'input2': "PMBus Interface",
            'output2': "8 Channels",
            'package2': "QFN-64",
            'app2': "High-density systems",
            'model3': "DMS-2HI",
            'power3': "N/A",
            'eff3': "N/A",
            'input3': "PMBus/Ethernet",
            'output3': "2 Channels",
            'package3': "QFP-44",
            'app3': "Networked systems",
            'model4': "DMS-16CM",
            'power4': "N/A",
            'eff4': "N/A",
            'input4': "PMBus Interface",
            'output4': "16 Channels",
            'package4': "QFP-80",
            'app4': "Complex filter arrays",
            'model5': "DMS-2PMB",
            'power5': "N/A",
            'eff5': "N/A",
            'input5': "Dual PMBus",
            'output5': "2 Channels",
            'package5': "QFN-32",
            'app5': "Dual bus systems",
            'applications_intro': "Digital Management Solutions are ideal for applications requiring intelligent power filter management and monitoring. Common applications include:",
            'app_card1_title': "Data Center Infrastructure",
            'app_card1_desc': "Digital management of power filter systems for servers and networking equipment with PMBus interface.",
            'app_card2_title': "Telecommunications",
            'app_card2_desc': "Intelligent filter management for base stations and network infrastructure with real-time monitoring.",
            'app_card3_title': "Industrial Automation",
            'app_card3_desc': "Coordinated control of complex power filter systems in factory automation and process control equipment.",
            'design_consideration1_title': "System Integration",
            'design_consideration1_content': "Proper integration requires careful design of the communication bus and appropriate pull-up resistors. Consider noise immunity when routing the PMBus interface near switching power components.",
            'design_consideration2_title': "Configuration and Programming",
            'design_consideration2_content': "The controllers typically require configuration for the specific filter system topology. Vicor provides development tools and software to facilitate system configuration and tuning.",
            'design_consideration3_title': "Thermal Management",
            'design_consideration3_content': "While the controllers themselves generate minimal heat, they are often used in high-power systems where thermal management is critical. Consider the impact of temperature on the overall system performance.",
            'faq1_question': "What is PMBus?",
            'faq1_answer': "PMBus (Power Management Bus) is a standardized digital communication protocol specifically designed for power management applications. It allows bidirectional communication between power controllers and host systems for monitoring and control.",
            'faq2_question': "Can Digital Management Solutions work with non-Vicor filters?",
            'faq2_answer': "Yes, Digital Management Solutions are designed to work with a variety of power filters from different manufacturers, not just Vicor filters.",
            'faq3_question': "What benefits do digital filter management provide?",
            'faq3_answer': "Digital controllers provide real-time monitoring, adaptive control, remote configuration, and comprehensive system diagnostic capabilities that are difficult to achieve with analog control."
        }
    },
    # Picor Power Converters
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/picor/power-converters/index.html",
        "data": {
            'title': "Picor Power Converters - Digital Power Solutions",
            'description': "Vicor Picor Power Converters - Advanced digital power conversion solutions featuring PMBus interface and adaptive control algorithms. High-efficiency digital power conversion modules.",
            'keywords': "Picor power converters, digital power conversion, PMBus interface, digital power modules, adaptive control, Vicor power modules",
            'og_title': "Picor Power Converters - Digital Power Solutions",
            'og_url': "/products/picor/power-converters/",
            'image': "picor-power-converters",
            'schema_name': "Vicor Picor Power Converters",
            'schema_description': "Advanced digital power conversion solutions featuring PMBus interface and adaptive control algorithms",
            'schema_category': "Electronics > Power Supplies > Digital Control",
            'prod_type': "picor", 
            'prod_type_title': "Picor",
            'series': "picor",
            'series_title': "Picor",
            'sub_series_title': "Power Converters",
            'full_series_title': "Picor Power Converters",
            'mp_active': "",
            'if_active': "",
            'p_active': " active",
            'sol_active': "",
            'aero_active': "",
            'auto_active': "",
            'lead_content': "Picor Power Converters provide advanced digital power conversion solutions featuring PMBus interface and adaptive control algorithms. These devices offer high-efficiency digital power conversion with intelligent management capabilities for optimized performance in demanding applications.",
            'overview_content': "Picor Power Converters represent Vicor's solution for digital power conversion, offering advanced control algorithms, system monitoring, and communication capabilities.",
            'overview_content2': "These converters provide intelligent power conversion with high efficiency and precise regulation, managed through digital interfaces for adaptive performance optimization.",
            'feature1_title': "PMBus Interface",
            'feature1_desc': "Comprehensive digital communication interface for configuration, monitoring, and control of power conversion systems.",
            'feature2_title': "High Efficiency",
            'feature2_desc': "Advanced digital control algorithms optimize efficiency across the entire load range with adaptive switching frequencies.",
            'feature3_title': "Adaptive Control",
            'feature3_desc': "Dynamic adjustment of switching parameters based on operating conditions for optimal performance.",
            'feature4_title': "Precise Regulation",
            'feature4_desc': "Advanced digital control provides exceptional voltage regulation and dynamic response characteristics.",
            'model1': "PIC1200-1203",
            'power1': "120W",
            'eff1': "95.2%",
            'input1': "9-14V",
            'output1': "3.3V/5A",
            'package1': "QFN-40",
            'app1': "Non-isolated point of load",
            'model2': "PIC2400-2406",
            'power2': "240W",
            'eff2': "95.7%",
            'input2': "18-36V",
            'output2': "12V/20A",
            'package2': "QFN-64",
            'app2': "High-current POL",
            'model3': "PIC4800-4803",
            'power3': "480W",
            'eff3': "96.1%",
            'input3': "36-75V",
            'output3': "12V/40A",
            'package3': "LGA-120",
            'app3': "High-power POL",
            'model4': "PIC0600-501",
            'power4': "60W",
            'eff4': "94.8%",
            'input4': "4.5-14V",
            'output4': "1V/60A",
            'package4': "QFN-28",
            'app4': "Processor power",
            'model5': "PIC1800-2409",
            'power5': "180W",
            'eff5': "95.4%",
            'input5': "18-36V",
            'output5': "5V/36A",
            'package5': "QFN-56",
            'app5': "Multi-rail systems",
            'applications_intro': "Picor Power Converters are ideal for applications requiring intelligent power conversion and monitoring. Common applications include:",
            'app_card1_title': "Data Center Computing",
            'app_card1_desc': "Digital power supplies for servers and networking equipment with PMBus interface and adaptive control.",
            'app_card2_title': "Telecommunications",
            'app_card2_desc': "Intelligent power conversion for base stations and network infrastructure with real-time monitoring.",
            'app_card3_title': "Industrial Automation",
            'app_card3_desc': "Coordinated digital power conversion in factory automation and process control equipment.",
            'design_consideration1_title': "System Integration",
            'design_consideration1_content': "Proper integration requires careful design of the communication bus and appropriate pull-up resistors. Consider noise immunity when routing the PMBus interface near switching power components.",
            'design_consideration2_title': "Configuration and Programming",
            'design_consideration2_content': "The converters typically require configuration for the specific power system requirements. Vicor provides development tools and software to facilitate system configuration and tuning.",
            'design_consideration3_title': "Thermal Management",
            'design_consideration3_content': "While the digital control provides efficiency optimization, thermal management remains important in high-power applications. Ensure adequate cooling for reliable operation at full power.",
            'faq1_question': "What is PMBus?",
            'faq1_answer': "PMBus (Power Management Bus) is a standardized digital communication protocol specifically designed for power management applications. It allows bidirectional communication between power controllers and host systems for monitoring and control.",
            'faq2_question': "Can Picor Power Converters work with non-Vicor power modules?",
            'faq2_answer': "Yes, Picor Power Converters are designed to work with a variety of power components from different manufacturers.",
            'faq3_question': "What benefits do digital power converters provide?",
            'faq3_answer': "Digital converters provide real-time monitoring, adaptive control, remote configuration, and comprehensive system diagnostic capabilities that are difficult to achieve with analog control."
        }
    },
    # Picor Power Shelf
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/picor/power-shelf/index.html",
        "data": {
            'title': "Picor Power Shelf - Digital Power Management Systems",
            'description': "Vicor Picor Power Shelf - Integrated digital power management systems featuring multiple power rails and PMBus interface. Complete power solutions with intelligent control and monitoring.",
            'keywords': "Picor power shelf, digital power management, PMBus interface, power management systems, intelligent power control, Vicor power modules",
            'og_title': "Picor Power Shelf - Digital Power Management Systems",
            'og_url': "/products/picor/power-shelf/",
            'image': "picor-power-shelf",
            'schema_name': "Vicor Picor Power Shelf",
            'schema_description': "Integrated digital power management systems featuring multiple power rails and PMBus interface",
            'schema_category': "Electronics > Power Supplies > Digital Control",
            'prod_type': "picor", 
            'prod_type_title': "Picor",
            'series': "picor",
            'series_title': "Picor",
            'sub_series_title': "Power Shelf",
            'full_series_title': "Picor Power Shelf",
            'mp_active': "",
            'if_active': "",
            'p_active': " active",
            'sol_active': "",
            'aero_active': "",
            'auto_active': "",
            'lead_content': "Picor Power Shelf provides integrated digital power management systems featuring multiple power rails and PMBus interface. These complete power solutions offer intelligent control and monitoring for complex power architectures in demanding applications.",
            'overview_content': "Picor Power Shelf represents Vicor's solution for complex power management, offering multiple power rails with centralized digital control.",
            'overview_content2': "These systems provide complete power solutions with intelligent management, monitoring, and adaptive control for applications requiring multiple voltage rails.",
            'feature1_title': "Multiple Power Rails",
            'feature1_desc': "Integrated solution providing multiple output voltage rails in a single system with centralized control.",
            'feature2_title': "PMBus Interface",
            'feature2_desc': "Comprehensive digital communication interface for configuration, monitoring, and control of all power rails.",
            'feature3_title': "Intelligent Management",
            'feature3_desc': "Advanced algorithms coordinate power delivery across multiple rails for optimized performance.",
            'feature4_title': "System Monitoring",
            'feature4_desc': "Real-time monitoring of voltage, current, temperature, and other critical parameters across all rails.",
            'model1': "PSH-4-120W",
            'power1': "120W (4 rails)",
            'eff1': "94.5%",
            'input1': "36-75V",
            'output1': "12V/5A, 5V/6A, 3.3V/5A, 1.8V/5A",
            'package1': "1U Rack Mount",
            'app1': "Multi-rail systems",
            'model2': "PSH-8-480W",
            'power2': "480W (8 rails)",
            'eff2': "95.2%",
            'input2': "36-75V",
            'output2': "Various combinations",
            'package2': "1U Rack Mount",
            'app2': "High-power systems",
            'model3': "PSH-2-300W",
            'power3': "300W (2 rails)",
            'eff3': "94.8%",
            'input3': "18-36V",
            'output3': "12V/15A, 5V/15A",
            'package3': "Open Frame",
            'app3': "Compact systems",
            'model4': "PSH-6-240W",
            'power4': "240W (6 rails)",
            'eff4': "94.2%",
            'input4': "9-14V",
            'output4': "Various combinations",
            'package4': "Open Frame",
            'app4': "Low-voltage systems",
            'model5': "PSH-10-600W",
            'power5': "600W (10 rails)",
            'eff5': "95.5%",
            'input5': "36-75V",
            'output5': "Various combinations",
            'package5': "1U Rack Mount",
            'app5': "Complex systems",
            'applications_intro': "Picor Power Shelf systems are ideal for applications requiring multiple power rails with intelligent management. Common applications include:",
            'app_card1_title': "Data Center Equipment",
            'app_card1_desc': "Multi-rail power supplies for servers and networking equipment with centralized PMBus management.",
            'app_card2_title': "Telecommunications",
            'app_card2_desc': "Power shelf solutions for base stations and network infrastructure with intelligent control.",
            'app_card3_title': "Industrial Systems",
            'app_card3_desc': "Integrated power management for industrial automation and process control equipment with multiple rails.",
            'design_consideration1_title': "System Integration",
            'design_consideration1_content': "Proper integration requires careful planning of power rail assignments and load balancing. Consider the interaction between different rails and the central management system.",
            'design_consideration2_title': "Configuration and Programming",
            'design_consideration2_content': "The power shelf requires configuration for the specific application requirements. Vicor provides development tools and software to facilitate system configuration and tuning.",
            'design_consideration3_title': "Thermal Management",
            'design_consideration3_content': "Power shelf systems can generate significant heat at full loading. Ensure adequate cooling and thermal management in the system design for reliable operation.",
            'faq1_question': "What is PMBus?",
            'faq1_answer': "PMBus (Power Management Bus) is a standardized digital communication protocol specifically designed for power management applications. It allows bidirectional communication between power controllers and host systems for monitoring and control.",
            'faq2_question': "Can Power Shelf systems be expanded?",
            'faq2_answer': "Yes, Power Shelf systems can be configured with different numbers of rails and power levels to meet specific application requirements.",
            'faq3_question': "What monitoring capabilities are provided?",
            'faq3_answer': "Power Shelf systems provide real-time monitoring of voltage, current, temperature, and other parameters across all power rails with centralized control and status reporting."
        }
    },
    # Picor Power Supplies
    {
        "path": "C:/Users/ymlt/Desktop/vicor/products/picor/power-supplies/index.html",
        "data": {
            'title': "Picor Power Supplies - Integrated Digital Power Systems",
            'description': "Vicor Picor Power Supplies - Complete integrated digital power supply systems with PMBus interface and advanced control algorithms. High-efficiency power solutions with intelligent management.",
            'keywords': "Picor power supplies, integrated digital power, PMBus interface, power management systems, intelligent power supplies, Vicor power modules",
            'og_title': "Picor Power Supplies - Integrated Digital Power Systems",
            'og_url': "/products/picor/power-supplies/",
            'image': "picor-power-supplies",
            'schema_name': "Vicor Picor Power Supplies",
            'schema_description': "Complete integrated digital power supply systems with PMBus interface and advanced control algorithms",
            'schema_category': "Electronics > Power Supplies",
            'prod_type': "picor", 
            'prod_type_title': "Picor",
            'series': "picor",
            'series_title': "Picor",
            'sub_series_title': "Power Supplies",
            'full_series_title': "Picor Power Supplies",
            'mp_active': "",
            'if_active': "",
            'p_active': " active",
            'sol_active': "",
            'aero_active': "",
            'auto_active': "",
            'lead_content': "Picor Power Supplies provide complete integrated digital power supply systems with PMBus interface and advanced control algorithms. These high-efficiency power solutions offer intelligent management capabilities for optimized performance in demanding applications.",
            'overview_content': "Picor Power Supplies represent Vicor's solution for integrated power management, offering complete power supply systems with digital control and monitoring.",
            'overview_content2': "These power supplies provide complete solutions with advanced control algorithms, system monitoring, and communication capabilities for applications requiring intelligent power management.",
            'feature1_title': "Integrated System",
            'feature1_desc': "Complete power supply system with integrated control, protection, and monitoring functions in a single package.",
            'feature2_title': "PMBus Interface",
            'feature2_desc': "Comprehensive digital communication interface for configuration, monitoring, and control of power system parameters.",
            'feature3_title': "High Efficiency",
            'feature3_desc': "Advanced digital control algorithms optimize efficiency across the entire load range with minimal losses.",
            'feature4_title': "Intelligent Protection",
            'feature4_desc': "Advanced protection features including overvoltage, overcurrent, and overtemperature protection with digital monitoring.",
            'model1': "PS-1200-120",
            'power1': "120W",
            'eff1': "93.8%",
            'input1': "85-264VAC",
            'output1': "12V/10A",
            'package1': "Open Frame",
            'app1': "Industrial systems",
            'model2': "PS-2400-240",
            'power2': "240W",
            'eff2': "94.2%",
            'input2': "85-264VAC",
            'output2': "24V/10A",
            'package2': "Open Frame",
            'app2': "High-power systems",
            'model3': "PS-4800-480",
            'power3': "480W",
            'eff3': "94.7%",
            'input3': "85-264VAC",
            'output3': "48V/10A",
            'package3': "Open Frame",
            'app3': "Telecom systems",
            'model4': "PS-1200-125",
            'power4': "125W",
            'eff4': "93.5%",
            'input4': "18-36VDC",
            'output4': "5V/25A",
            'package4': "Open Frame",
            'app4': "DC input systems",
            'model5': "PS-600-60",
            'power5': "60W",
            'eff5': "92.8%",
            'input5': "85-264VAC",
            'output5': "12V/5A",
            'package5': "Enclosed",
            'app5': "Low-power systems",
            'applications_intro': "Picor Power Supplies are ideal for applications requiring intelligent power management and monitoring. Common applications include:",
            'app_card1_title': "Data Center Equipment",
            'app_card1_desc': "Digital power supplies for servers and networking equipment with PMBus interface and adaptive control.",
            'app_card2_title': "Telecommunications",
            'app_card2_desc': "Intelligent power supplies for base stations and network infrastructure with real-time monitoring.",
            'app_card3_title': "Industrial Automation",
            'app_card3_desc': "Digital power supplies for factory automation and process control equipment with complete monitoring.",
            'design_consideration1_title': "System Integration",
            'design_consideration1_content': "Proper integration requires careful design of the communication bus and appropriate pull-up resistors. Consider noise immunity when routing the PMBus interface in electrically noisy environments.",
            'design_consideration2_title': "Configuration and Programming",
            'design_consideration2_content': "The power supplies typically require configuration for the specific application requirements. Vicor provides development tools and software to facilitate system configuration and tuning.",
            'design_consideration3_title': "Thermal Management",
            'design_consideration3_content': "While the digital control provides efficiency optimization, thermal management remains important in enclosed systems. Ensure adequate cooling for reliable operation at full power.",
            'faq1_question': "What is PMBus?",
            'faq1_answer': "PMBus (Power Management Bus) is a standardized digital communication protocol specifically designed for power management applications. It allows bidirectional communication between power controllers and host systems for monitoring and control.",
            'faq2_question': "Can Picor Power Supplies work with non-Vicor components?",
            'faq2_answer': "Yes, Picor Power Supplies are designed to work in systems with various components from different manufacturers.",
            'faq3_question': "What protection features are included?",
            'faq3_answer': "Picor Power Supplies include overvoltage, overcurrent, and overtemperature protection with digital monitoring and status reporting capabilities."
        }
    }
]

# Create the final pages
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

print("All final pages have been created!")