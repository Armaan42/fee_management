import os
import re

def remove_emojis_from_file(filepath):
    """Remove emojis from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove specific emojis commonly used in documentation
    emojis_to_remove = [
        '✅', '✨', '🎯', '🚀', '📊', '📁', '🔗', '🎉', '🔄',
        '⏳', '💡', '📝', '🔧', '⚙️', '📈', '💰', '🏆',
        '👍', '❌', '⚡', '🌟', '📌', '🎨', '🔍', '💻',
        '📱', '🖥️', '⭐', '🔔', '📢', '✔️', '❗', '⚠️',
        '📋', '📚', '📖', '🛠️', '📂', '📞', '💼', '🎓'
    ]
    
    for emoji in emojis_to_remove:
        # Remove emoji with space after it
        content = content.replace(f'{emoji} ', '')
        # Remove standalone emoji
        content = content.replace(emoji, '')
    
    # Use regex to catch any remaining emojis
    # This pattern matches most common emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"  # dingbats
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # supplemental symbols
        "\U00002600-\U000026FF"  # misc symbols
        "]+", 
        flags=re.UNICODE
    )
    content = emoji_pattern.sub('', content)
    
    # Clean up any double spaces left behind
    content = re.sub(r'  +', ' ', content)
    # Clean up lines that now start with space
    content = re.sub(r'\n ', '\n', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def process_directory(directory):
    """Process all markdown files in directory and subdirectories."""
    files_modified = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if remove_emojis_from_file(filepath):
                    files_modified += 1
                    print(f"Modified: {filepath}")
    
    return files_modified

if __name__ == "__main__":
    base_dir = r"c:\Users\Armaan\Documents\YAHWEH SOFTWARE SOLUTIONS\fee_managment"
    
    print("Removing all remaining emojis from documentation...")
    count = process_directory(base_dir)
    print(f"\nCompleted! Modified {count} files.")
