import os
import re

def fix_character_encoding_issues(file_path):
    """Specifically fix UTF-8 encoding issues in the HTML file."""
    print(f"Fixing encoding in: {file_path}")
    
    # Read the file as raw bytes to handle encoding properly
    with open(file_path, 'rb') as f:
        content_bytes = f.read()
    
    # Try to decode properly, handling common encoding mismatches
    try:
        # First, try decoding as UTF-8
        content = content_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # If UTF-8 fails, try with error handling
        content = content_bytes.decode('utf-8', 'replace')
    
    original_content = content
    
    # Fix common encoding issues caused by double encoding:
    # Replace sequences that appear when UTF-8 is incorrectly interpreted as other encodings
    content = content.replace('鈻?\?', '▼')  # Triangle arrow (utf-8 bytes interpreted as cp1252)
    content = content.replace('鈥?', '•')    # Bullet point (utf-8 bytes interpreted as cp1252)
    content = content.replace('脗掳', '°')   # Degree symbol (UTF-8 continuation byte issue)
    content = content.replace('冒聼聯卤', '📱')  # Smartphone emoji (different encoding issue)
    content = content.replace('冒聼聮卢', '💬')  # Speech bubble emoji (different encoding issue)
    
    # Additional common encoding replacements
    content = content.replace('鈥淰', '"')  # Left double quotation mark
    content = content.replace('鈥?quot;', '"')  # Right double quotation mark
    content = content.replace('鈥橝', "'")  # Right single quotation mark
    content = content.replace('鈥橝', "'")  # Left single quotation mark
    content = content.replace('鈥?-', '–')  # En dash
    content = content.replace('鈥?-', '—')  # Em dash
    content = content.replace('鈄?,', '™')  # Trademark symbol
    
    # If content was changed, write back with proper encoding
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f"  Fixed encoding issues in: {file_path}")
        return True
    else:
        print(f"  No encoding issues found in: {file_path}")
        return False

def fix_all_encoding_issues():
    # Process all HTML files in the products directory
    base_dir = "C:/Users/ymlt/Desktop/vicor"
    fixed_count = 0

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # Skip the main templates that are used as reference
                if os.path.basename(file_path) in ['detail.html', 'index.html'] and os.path.dirname(file_path) == base_dir:
                    continue

                if fix_character_encoding_issues(file_path):
                    fixed_count += 1

    print(f"Completed: Fixed encoding issues in {fixed_count} files.")

# Run the function
fix_all_encoding_issues()