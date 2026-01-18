from pathlib import Path
from typing import Optional, Dict
import json
from core.base.context import AgentContext

class ScaffoldingService:
    STATE_FILE = Path("conductor/setup_state.json")

    def __init__(self, context: AgentContext):
        self.context = context

    def get_setup_state(self) -> Dict:
        """Reads the setup state from the filesystem via context."""
        try:
            content = self.context.read_file(self.STATE_FILE)
            return json.loads(content)
        except Exception:
            return {"last_successful_step": ""}

    def save_setup_state(self, step: str) -> None:
        """Saves the current setup step to the state file."""
        state = {"last_successful_step": step}
        self.context.write_file(self.STATE_FILE, json.dumps(state))

    def detect_project_maturity(self) -> str:
        """Determines if the project is Greenfield or Brownfield."""
        # Check for VCS
        git_status = self.context.run_command("git status --porcelain")
        if git_status is not None:
            return "brownfield"
        
        # Check for common manifest files
        manifests = ["package.json", "requirements.txt", "go.mod", "pom.xml"]
        for m in manifests:
            try:
                self.context.read_file(Path(m))
                return "brownfield"
            except:
                continue
        
        return "greenfield"

    def initialize_project(self, goal: str) -> None:
        """Initializes the conductor directory and product.md."""
        self.context.run_command("mkdir -p conductor")
        self.save_setup_state("")
        
        product_content = f"# Initial Concept\n{goal}\n"
        self.context.write_file(Path("conductor/product.md"), product_content)
