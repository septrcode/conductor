import os
import re
from pathlib import Path

def sync_prompts():
    commands_dir = Path("commands/conductor")
    prompts_dir = Path("prompts")
    
    if not commands_dir.exists():
        print(f"Error: {commands_dir} not found.")
        return

    prompts_dir.mkdir(exist_ok=True)

    for toml_file in commands_dir.glob("*.toml"):
        print(f"Processing {toml_file}...")
        try:
            with open(toml_file, "r") as f:
                content = f.read()
            
            # Simple regex to find content between prompt = """ and the closing """
            match = re.search(r'prompt\s*=\s*"""(.*?)"""', content, re.DOTALL)
            if not match:
                print(f"  Warning: No prompt content found in {toml_file}")
                continue
            
            prompt_content = match.group(1).strip()
            
            # Create filename: conductor-command.md
            md_filename = f"conductor-{toml_file.stem}.md"
            md_path = prompts_dir / md_filename
            
            with open(md_path, "w") as f:
                f.write(prompt_content)
            
            print(f"  Created {md_path}")
        except Exception as e:
            print(f"  Error processing {toml_file}: {e}")

if __name__ == "__main__":
    sync_prompts()