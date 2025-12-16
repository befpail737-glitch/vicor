#!/usr/bin/env python3
# Script to fix structural issues in Vicor product detail pages by comparing with known good template

import os
import re

def fix_structure_issues(file_path):
    """Fix common structural issues in product detail pages."""
    print(f"Fixing structure: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Calculate correct relative path based on file location
    # From file location to project root
    rel_path_from_file_to_root = os.path.relpath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 
                                                os.path.dirname(file_path))
    
    # Convert to proper relative path format (using ../)
    rel_path_parts = rel_path_from_file_to_root.split(os.sep)
    if '' in rel_path_parts:
        rel_path_parts.remove('')
    css_path = '/'.join(['..'] * len(rel_path_parts) + ['css', 'style.css'])
    img_path = '/'.join(['..'] * len(rel_path_parts) + ['images', 'logo.svg'])
    
    # Update CSS and favicon links with correct relative paths
    content = re.sub(
        r'<link\s+rel=["\']stylesheet["\']\s+href=["\'][^"\']*["\']',
        f'<link rel="stylesheet" href="{css_path}"',
        content
    )
    
    content = re.sub(
        r'<link\s+rel=["\']icon["\']\s+href=["\'][^"\']*["\']',
        f'<link rel="icon" href="{img_path}"',
        content
    )
    
    # Write back the corrected content
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    
    print(f"  Structure fixed in: {file_path}")

def fix_all_product_pages(base_dir):
    """Find and fix structure issues in all HTML files in products directory."""
    product_dirs = [
        os.path.join(base_dir, 'products', 'modular-power', 'dcm'),
        os.path.join(base_dir, 'products', 'modular-power', 'bcm'),
        os.path.join(base_dir, 'products', 'modular-power', 'prm'),
        os.path.join(base_dir, 'products', 'modular-power', 'vtm'),
        os.path.join(base_dir, 'products', 'input-filter'),
        os.path.join(base_dir, 'products', 'picor'),
    ]
    
    # Also add the main product category pages
    additional_dirs = [
        os.path.join(base_dir, 'products'),
        os.path.join(base_dir, 'products', 'modular-power'),
    ]
    
    all_dirs = product_dirs + additional_dirs
    
    # Find all HTML files in product subdirectories
    html_files = []
    for prod_dir in all_dirs:
        if os.path.exists(prod_dir):
            for file in os.listdir(prod_dir):
                if file.endswith('.html'):
                    html_files.append(os.path.join(prod_dir, file))
    
    # Process each HTML file
    for html_file in html_files:
        fix_structure_issues(html_file)

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)  # Current directory
    fix_all_product_pages(base_dir)
    print("All structural issues have been fixed!")