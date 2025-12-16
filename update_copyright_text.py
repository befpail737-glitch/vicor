#!/usr/bin/env python3
"""
Script to update copyright footer text with "core" instead of "Official authorized Vicor distributor"
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

def update_copyright_texts(base_dir):
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
        old_content = open(html_file, 'r', encoding='utf-8').read()
        new_content = old_content

        count1 = len(re.findall(re.escape('Official authorized Vicor distributor'), new_content))
        new_content = new_content.replace('Official authorized Vicor distributor', 'core Vicor distributor')

        count2 = len(re.findall(re.escape('Official authorized'), new_content))
        new_content = new_content.replace('Official authorized', 'core')

        count3 = len(re.findall(re.escape('official authorized'), new_content))
        new_content = new_content.replace('official authorized', 'core')

        if new_content != old_content:
            with open(html_file, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)
            print(f"  Updated copyright text in: {html_file}")

        replacements_made += count1 + count2 + count3
    
    return replacements_made

if __name__ == "__main__":
    base_dir = "C:/Users/ymlt/Desktop/vicor"

    print("Updating copyright footers...")
    count = update_copyright_texts(base_dir)
    print(f"Updated copyright text in {count} places.")

    print(f"\nCompleted updating copyright text in HTML files.")