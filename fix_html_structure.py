import os

def fix_html_structure_issues(file_path):
    """Fix HTML structure issues in a given file."""
    print(f"Checking HTML structure: {file_path}")
    
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
    
    # Fix HTML structure issues - the main problem identified
    content = content.replace('>▼/span>', '>▼</span>')  # Fix dropdown arrows
    content = content.replace('>•/span>', '>•</span>')  # Fix bullet separators  
    content = content.replace('>📱/span>', '>📱</span>')  # Fix contact icons
    content = content.replace('>💬/span>', '>💬</span>')
    
    # Additional HTML structure fixes
    # Look for other malformed closing tags
    import re
    # Fix any pattern like "text/span>" to "text</span>"
    content = re.sub(r'>•([^<]*)/span>', r'>•\1</span>', content)  # Fix • separator patterns
    content = re.sub(r'> ([^/<>]*)/span>', r'>\1</span>', content)  # General pattern for missing </

    # More specific replacements for the commonly occurring patterns
    content = re.sub(r'(dropdown-arrow"[^>]*>)â?–¿([^<]*)/span>', r'\1â–¿\2</span>', content)
    content = re.sub(r'(dropdown-arrow"[^>]*>)▼([^<]*)/span>', r'\1▼\2</span>', content)
    content = re.sub(r'(dropdown-arrow"[^>]*>)â?€¢([^<]*)/span>', r'\1â€¢\2</span>', content)
    content = re.sub(r'(contact-icon"[^>]*>)ğŸ“±([^<]*)/span>', r'\1ğŸ“±\2</span>', content)
    content = re.sub(r'(contact-icon"[^>]*>)ğŸ’¬([^<]*)/span>', r'\1ğŸ’¬\2</span>', content)
    
    # If we made changes, write back to file
    if content != orig_content:
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f'Fixed HTML structure in: {file_path}')
        return True
    else:
        print(f'No structure issues found in: {file_path}')
        return False

def fix_all_html_structure_issues(base_dir):
    """Find and fix HTML structure issues in all HTML files in products directory."""
    html_files = []
    
    for root, dirs, files in os.walk(os.path.join(base_dir, 'products')):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                html_files.append(file_path)
    
    # Process each HTML file
    fixed_count = 0
    for file_path in html_files:
        try:
            if fix_html_structure_issues(file_path):
                fixed_count += 1
        except Exception as e:
            print(f'Error processing {file_path}: {e}')
    
    print(f'Completed: Fixed HTML structure issues in {fixed_count} files.')

# Run on the base directory
base_dir = 'C:/Users/ymlt/Desktop/vicor'
fix_all_html_structure_issues(base_dir)