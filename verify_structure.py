#!/usr/bin/env python3
# Script to verify and fix structural issues in Vicor product detail pages

import os
import re

def verify_and_fix_structure(file_path):
    """Verify and fix HTML structure issues in a given file."""
    print(f"Verifying structure: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ensure proper HTML5 doctype
    if not content.startswith('<!DOCTYPE html>'):
        content = '<!DOCTYPE html>\n' + content
    
    # Ensure lang attribute is present in html tag
    content = re.sub(r'<html(?!\s+lang=)[^>]*>', '<html lang="en">', content)
    
    # Verify meta viewport tag is present
    if '<meta name="viewport"' not in content:
        content = content.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    
    # Verify proper charset declaration
    if '<meta charset="UTF-8">' not in content:
        content = content.replace('<head>', '<head>\n    <meta charset="UTF-8">')
    
    # Check if proper favicon is linked
    if 'rel="icon"' not in content:
        content = re.sub(r'(<head>)', r'\1\n    <!-- Favicon -->\n    <link rel="icon" href="../images/logo.svg" type="image/svg+xml">', content)
    
    # Verify stylesheet is properly linked
    if '<link rel="stylesheet"' not in content or 'css/style.css' not in content:
        # Find a good place to insert the stylesheet link
        head_end_match = re.search(r'</head>', content)
        if head_end_match:
            insert_pos = head_end_match.start()
            stylesheet_tag = '\n    <!-- Stylesheets -->\n    <link rel="stylesheet" href="../css/style.css">'
            content = content[:insert_pos] + stylesheet_tag + content[insert_pos:]
    
    # Fix relative paths for CSS if they're incorrect
    # This depends on the depth of the file
    directory_depth = file_path[len(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))):].count(os.sep)
    expected_css_path = '../' * directory_depth + 'css/style.css'
    expected_css_path = expected_css_path.lstrip('/').lstrip('\\')
    
    # Adjust CSS path based on directory depth
    if directory_depth == 3:  # e.g. products/modular-power/dcm/high-power
        expected_css_path = '../../../css/style.css'
    elif directory_depth == 2:  # e.g. products/modular-power/dcm
        expected_css_path = '../../css/style.css'
    elif directory_depth == 1:  # e.g. products/modular-power
        expected_css_path = '../css/style.css'
    else:  # root level
        expected_css_path = 'css/style.css'
    
    # Replace CSS link with correct path
    content = re.sub(
        r'<link\s+rel=["\']stylesheet["\']\s+href=["\'][^"\']*["\']\s*>',
        f'    <link rel="stylesheet" href="{expected_css_path}">',
        content
    )
    
    # Similarly fix favicon path based on directory depth
    expected_favicon_path = '../' * directory_depth + 'images/logo.svg'
    expected_favicon_path = expected_favicon_path.lstrip('/').lstrip('\\')
    
    if directory_depth == 3:  # e.g. products/modular-power/dcm/high-power
        expected_favicon_path = '../../../images/logo.svg'
    elif directory_depth == 2:  # e.g. products/modular-power/dcm
        expected_favicon_path = '../../images/logo.svg'
    elif directory_depth == 1:  # e.g. products/modular-power
        expected_favicon_path = '../images/logo.svg'
    else:  # root level
        expected_favicon_path = 'images/logo.svg'
    
    content = re.sub(
        r'<link\s+rel=["\']icon["\'].*?>',
        f'    <link rel="icon" href="{expected_favicon_path}" type="image/svg+xml">',
        content
    )
    
    # Write back the corrected content
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    
    print(f"  Structure verified and fixed in: {file_path}")

def verify_all_product_pages(base_dir):
    """Find and verify all HTML files in products directory."""
    product_dirs = [
        os.path.join(base_dir, 'products', 'modular-power', 'dcm'),
        os.path.join(base_dir, 'products', 'modular-power', 'bcm'),
        os.path.join(base_dir, 'products', 'modular-power', 'prm'),
        os.path.join(base_dir, 'products', 'modular-power', 'vtm'),
        os.path.join(base_dir, 'products', 'input-filter'),
        os.path.join(base_dir, 'products', 'picor'),
    ]
    
    # Find all HTML files in product subdirectories
    html_files = []
    for prod_dir in product_dirs:
        if os.path.exists(prod_dir):
            for root, dirs, files in os.walk(prod_dir):
                for file in files:
                    if file.endswith('.html'):
                        html_files.append(os.path.join(root, file))
    
    # Process each HTML file
    for html_file in html_files:
        verify_and_fix_structure(html_file)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Two levels up from script location
    verify_all_product_pages(base_dir)
    print("All HTML structures have been verified and fixed!")