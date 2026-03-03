import os
from capture import capture_session
from generator import generate_markdown

def sync_to_pkm(pkm_config, session_data):
    """
    Write the generated content to the PKM vault.
    """
    pkm_type = pkm_config.get('type')
    vault_path = pkm_config.get('vault_path')
    folder = pkm_config.get('folder', '')
    
    # Resolve absolute path for the vault (mock for now)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    target_dir = os.path.join(base_dir, vault_path, folder)
    os.makedirs(target_dir, exist_ok=True)
    
    # Determine filename
    date_str = session_data['date_str']
    if pkm_type == 'obsidian':
        filename = f"{date_str}.md"
    elif pkm_type == 'logseq':
        filename = f"{date_str.replace('-', '_')}.md"
    else:
        filename = f"{date_str}.md"
        
    file_path = os.path.join(target_dir, filename)
    
    # Generate content
    markdown_content = generate_markdown(session_data, pkm_type)
    
    # Append or create
    # For Obsidian, usually append if exists. For Logseq, append blocks.
    mode = 'a' if os.path.exists(file_path) else 'w'
    
    with open(file_path, mode, encoding='utf-8') as f:
        # Add some padding if appending
        if mode == 'a':
            f.write("\n\n")
        f.write(markdown_content)
        
    print(f"Synced successfully to {pkm_type.title()} vault -> {file_path}")

