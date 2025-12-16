#!/usr/bin/env python3
# Script to fix encoding issues in Vicor product detail pages

import os
import re

def fix_encoding_in_file(file_path):
    """Fix encoding issues in a given file."""
    print(f"Processing: {file_path}")
    
    # Read file with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix common encoding issues
    # Replace malformed arrows
    content = re.sub(r'<span class="dropdown-arrow"[^>]*>\?\?/span>', '<span class="dropdown-arrow" aria-hidden="true">▼</span>', content)
    content = re.sub(r'<span class="dropdown-arrow"[^>]*>\?/span>', '<span class="dropdown-arrow" aria-hidden="true">▼</span>', content)
    
    # Replace malformed contact icons
    content = re.sub(r'<span class="contact-icon">\?\?</span>', '<span class="contact-icon">📱</span>', content)
    content = re.sub(r'<span class="contact-icon">\?</span>', '<span class="contact-icon">📱</span>', content)
    content = re.sub(r'<span class="contact-icon">📱\?\?</span>', '<span class="contact-icon">📱</span>', content)
    content = re.sub(r'<span class="contact-icon">💬\?\?</span>', '<span class="contact-icon">💬</span>', content)
    
    # Fix separators
    content = re.sub(r'<span class="meta-separator">\?\?/span>', '<span class="meta-separator">•</span>', content)
    content = re.sub(r'<span class="meta-separator">\?/span>', '<span class="meta-separator">•</span>', content)
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    
    print(f"  Fixed encoding issues in: {file_path}")

def fix_all_product_pages(base_dir):
    """Find and fix all HTML files in products directory."""
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
        try:
            fix_encoding_in_file(html_file)
        except UnicodeDecodeError:
            # If UTF-8 fails, try with latin-1 and then fix encoding
            print(f"Retrying {html_file} with different encoding...")
            with open(html_file, 'r', encoding='latin-1') as f:
                content = f.read()
            
            # Fix encoding issues and save as UTF-8
            content = content.encode('utf-8', errors='ignore').decode('utf-8')
            
            # Apply the same fixes
            content = re.sub(r'<span class="dropdown-arrow"[^>]*>\?\?/span>', '<span class="dropdown-arrow" aria-hidden="true">▼</span>', content)
            content = re.sub(r'<span class="dropdown-arrow"[^>]*>\?/span>', '<span class="dropdown-arrow" aria-hidden="true">▼</span>', content)
            content = re.sub(r'<span class="contact-icon">\?\?</span>', '<span class="contact-icon">📱</span>', content)
            content = re.sub(r'<span class="contact-icon">\?</span>', '<span class="contact-icon">📱</span>', content)
            content = re.sub(r'<span class="meta-separator">\?\?/span>', '<span class="meta-separator">•</span>', content)
            content = re.sub(r'<span class="meta-separator">\?/span>', '<span class="meta-separator">•</span>', content)
            
            with open(html_file, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            print(f"  Fixed encoding issues in: {html_file}")

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)  # Current directory
    fix_all_product_pages(base_dir)
    print("All encoding issues have been fixed!")