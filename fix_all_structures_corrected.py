import os
import re

def fix_all_structural_and_path_issues(base_dir):
    """Fix HTML structural and path issues in all product pages."""
    files_processed = 0
    fixed_count = 0
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith('.html'):
                file_path = os.path.join(root, file)
                
                # Skip the main template files as they are reference
                if os.path.basename(file_path) in ['detail.html', 'index.html'] and os.path.dirname(file_path) == base_dir:
                    continue
                
                print(f"Processing: {file_path}")
                
                try:
                    # Read file with error handling
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    # If UTF-8 fails, read with latin-1 and reprocess
                    with open(file_path, 'r', encoding='latin-1') as f:
                        content = f.read()
                    
                    # Encode as UTF-8 and decode properly
                    content = content.encode('utf-8').decode('utf-8')
                
                original_content = content
                
                # Calculate path depth for relative links
                # Determine how many levels to go up to reach project root
                rel_path = os.path.relpath(base_dir, os.path.dirname(file_path))
                levels_up = rel_path.count(os.sep) if rel_path != '..' else 1
                
                # Construct correct paths
                css_path = '../' * levels_up + 'css/style.css'
                img_path = '../' * levels_up + 'images/logo.svg'
                
                # Fix stylesheet references
                content = re.sub(
                    r'<link\s+rel=["\']stylesheet["\']\s+href=["\'][^"\']*["\']',
                    f'<link rel="stylesheet" href="{css_path}"',
                    content
                )
                
                # Fix favicon references
                content = re.sub(
                    r'<link\s+rel=["\']icon["\']\s+href=["\'][^"\']*["\']',
                    f'<link rel="icon" href="{img_path}" type="image/svg+xml"',
                    content
                )
                
                # Fix common structural issues
                # Replace malformed spans in dropdown arrows and special characters
                content = content.replace('鈻?\?/span>', '▼</span>')  # Arrow character issue
                content = content.replace('鈥?/span>', '•</span>')  # Bullet separator issue
                content = content.replace('鈻?\?/span>', '▼</span>')  # Arrow character issue (incomplete tags)
                content = content.replace('鈥?/span>', '•</span>')  # Bullet character issue (incomplete tags)
                
                # Fix HTML structure issues - malformed closing tags
                content = content.replace('鈻?\?/span>', '▼</span>')  # Proper arrow
                content = content.replace('鈥?/span>', '•</span>')  # Proper bullet
                
                # Write changes if there were any
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8', newline='') as f:
                        f.write(content)
                    print(f"  Fixed structure in: {file_path}")
                    fixed_count += 1

                files_processed += 1

    print(f"Completed: Processed {files_processed} files, fixed {fixed_count} files.")

# Run on the base directory
base_dir = 'C:/Users/ymlt/Desktop/vicor'
fix_all_structural_and_path_issues(base_dir)