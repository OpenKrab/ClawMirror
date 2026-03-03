import os
import yaml
import sys

# Ensure local imports work correctly regardless of running path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from capture import capture_session
from sync import sync_to_pkm

def load_config():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, 'config.yaml')
    if not os.path.exists(config_path):
        print("❌ Error: config.yaml not found.")
        return None
        
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def run_mirroring():
    print("Triggering ClawMirror...")
    
    config = load_config()
    if not config:
        return
        
    if not config.get('enabled', False):
        print("ClawMirror is disabled in config.yaml.")
        return
        
    # 1. Capture the session info
    print("Capturing Claw session data...")
    session_data = capture_session()
    
    # 2. Iterate through configured PKMs and sync
    pkms = config.get('pkms', [])
    for pkm in pkms:
        print(f"Syncing to {pkm.get('type').title()}...")
        sync_to_pkm(pkm, session_data)

    print("Mirroring complete!")

if __name__ == "__main__":
    run_mirroring()
