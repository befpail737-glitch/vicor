#!/usr/bin/env python3
"""
Script to update "Official authorized" text to "core" in all HTML files
"""

import os
import re

def update_text_in_file(file_path, old_text, new_text):
    """Update specific text in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count occurrences before replacement
        count_before = len(re.findall(re.escape(old_text), content))
        
        if count_before == 0:
            return 0  # No replacements needed
        
        # Perform the replacement
        updated_content = content.replace(old_text, new_text)
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(updated_content)
        
        print(f"  Updated {count_before} occurrence(s) of '{old_text}' to '{new_text}' in: {file_path}")
        return count_before
        
    except Exception as e:
        print(f"  Error updating {file_path}: {str(e)}")
        return 0

def update_all_html_files(base_dir):
    """Find and update all HTML files in the website."""
    replacements_made = 0
    html_files = []
    
    # Find all HTML files
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files to process.")
    
    # Update "Official authorized" to "core" in all HTML files
    for html_file in html_files:
        replacements = update_text_in_file(html_file, 'Official authorized', 'core')
        replacements_made += replacements
    
    return replacements_made

def update_copyright_text(base_dir):
    """Update copyright footer text to reflect the new branding."""
    replacements_made = 0
    html_files = []
    
    # Find all HTML files
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    # Update copyright statements that mention "Official authorized Vicor distributor"
    for html_file in html_files:
        # Replace the full phrase with updated text
        replacements = update_text_in_file(html_file, 'Official authorized Vicor distributor', 'core Vicor distributor')
        replacements_made += replacements
    
    return replacements_made

if __name__ == "__main__":
    base_dir = "C:/Users/ymlt/Desktop/vicor"
    
    print("Updating 'Official authorized' text to 'core' in all HTML files...")
    count1 = update_all_html_files(base_dir)
    print(f"Updated 'Official authorized' in {count1} places.")
    
    print("\nUpdating copyright footers...")
    count2 = update_copyright_text(base_dir)
    print(f"Updated copyright text in {count2} places.")
    
    print(f"\nCompleted updating text in HTML files.")