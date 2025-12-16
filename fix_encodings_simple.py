import os

def fix_encoding_issues_in_file(file_path):
    try:
        # Read file with error handling
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # If UTF-8 fails, read with latin-1 and reprocess
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()

        # Store original content to compare
        orig_content = content
        
        # Using hex codes to avoid any encoding issues in our script
        # Replace common encoding issues - all variants we've seen
        # Arrow and bullet characters (hex representations)
        content = content.replace('\u25BC', '▼')  # Proper arrow character
        content = content.replace('â–¿', '▼')  # Arrow character (most common mis-encoded variant)
        content = content.replace('â?', '▼')  # Another variant of the same
        content = content.replace('â?', '•')  # Bullet point (common separator)
        content = content.replace('â¢', '•')  # Another bullet variant
        content = content.replace('â€¢', '•')  # Yet another bullet variant
        
        # Quotation marks
        content = content.replace('â€œ', '"') # Left double quotation mark
        content = content.replace('â€', '"') # Right double quotation mark  
        content = content.replace('â€™', "'") # Right single quotation mark
        content = content.replace('â€˜', "'") # Left single quotation mark
        
        # Dashes
        content = content.replace('â€“', '-')  # En dash
        content = content.replace('â€”', '-')  # Em dash
        
        # Trademark symbols
        content = content.replace('â„¢', '™')  # Trademark symbol
        content = content.replace('â?', '™')  # Another trademark variant

        # If we made changes, write back to file
        if content != orig_content:
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            print(f'Fixed encoding in: {file_path}')
            return True
        else:
            return False
            
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return False

def fix_all_problematic_files(base_dir):
    problematic_files = []
    
    for root, dirs, files in os.walk(os.path.join(base_dir, 'products')):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                problematic_files.append(file_path)
    
    # Process each HTML file
    fixed_count = 0
    for file_path in problematic_files:
        try:
            if fix_encoding_issues_in_file(file_path):
                fixed_count += 1
        except Exception as e:
            print(f'Error in main loop for {file_path}: {e}')
    
    print(f'Completed: Fixed encoding issues in {fixed_count} out of {len(problematic_files)} files.')

# Run on the base directory
base_dir = 'C:/Users/ymlt/Desktop/vicor'
fix_all_problematic_files(base_dir)