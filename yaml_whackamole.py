#!/usr/bin/env python3
"""YAML Whack-a-Mole: Because YAML errors hide better than your car keys."""

import sys
import yaml
from pathlib import Path

def main():
    """Main function - the mole whacker-in-chief."""
    if len(sys.argv) != 2:
        print("Usage: python yaml_whackamole.py <file.yaml>")
        print("Pro tip: You need to actually give me a file to whack.")
        sys.exit(1)
    
    yaml_file = Path(sys.argv[1])
    
    if not yaml_file.exists():
        print(f"Error: '{yaml_file}' not found. Did you look under the couch?")
        sys.exit(1)
    
    try:
        with open(yaml_file, 'r') as f:
            content = f.read()
            
        # Try to load it - this is where YAML laughs at your indentation
        yaml.safe_load(content)
        
        print(f"✅ '{yaml_file}' looks valid! No moles to whack today.")
        print("But stay vigilant - they're probably just hiding better.")
        
    except yaml.YAMLError as e:
        print(f"🔨 WHACK! Found a mole in '{yaml_file}':")
        print(f"   Error: {e}")
        print("   Common culprits: missing colons, wonky indentation, or spaces that aren't spaces.")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        print("   This isn't a YAML error - it's something else. Maybe aliens?")
        sys.exit(1)

if __name__ == "__main__":
    # PyYAML is the only non-stdlib dependency because YAML is special
    try:
        import yaml
    except ImportError:
        print("Error: PyYAML not installed. YAML is too fancy for the standard library.")
        print("Install it: pip install PyYAML")
        sys.exit(1)
    
    main()