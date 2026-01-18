from pathlib import Path
from typing import List
from core.base.context import AgentContext
from core.base.agent import CommandRegistry, CommandDefinition, BaseAgent

class GenericContext(AgentContext):
    def get_cwd(self) -> Path:
        return Path(".")

    def read_file(self, path: Path) -> str:
        return f"Mocked content for {path}"

    def write_file(self, path: Path, content: str) -> None:
        print(f"Generic context writing to {path}")

    def list_files(self, path: Path, ignore_patterns: List[str]) -> List[Path]:
        return []

    def run_command(self, command: str) -> str:
        return f"Output of {command}"

    def get_git_status(self) -> str:
        return ""

class GenericCommandRegistry(CommandRegistry):
    def register_command(self, cmd: CommandDefinition) -> None:
        print(f"Generic Registry: Registering {cmd.name} via {cmd.trigger_type.value}")

    def unregister_command(self, name: str) -> None:
        print(f"Generic Registry: Unregistering {name}")

class GenericAgent(BaseAgent):
    def initialize(self) -> None:
        # Generic initialization
        print("Initializing Generic Conductor Agent")
