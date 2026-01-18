# Interface Design: AgentContext and CommandRegistry

## 1. AgentContext Interface
This interface abstracts the agent's interaction with the host environment.

```python
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional

class AgentContext(ABC):
    @abstractmethod
    def get_cwd(self) -> Path:
        """Returns the current working directory of the project."""
        pass

    @abstractmethod
    def read_file(self, path: Path) -> str:
        """Reads content from a file."""
        pass

    @abstractmethod
    def write_file(self, path: Path, content: str) -> None:
        """Writes content to a file safely."""
        pass

    @abstractmethod
    def list_files(self, path: Path, ignore_patterns: List[str]) -> List[Path]:
        """Lists files while respecting ignore patterns."""
        pass

    @abstractmethod
    def run_command(self, command: str) -> str:
        """Executes a shell command and returns output."""
        pass

    @abstractmethod
    def get_git_status(self) -> str:
        """Returns the current git status."""
        pass
```

## 2. CommandRegistry Interface
This interface abstracts how Conductor actions are triggered within different agents.

```python
from enum import Enum
from dataclasses import dataclass

class CommandTrigger(Enum):
    SLASH = "slash"       # e.g. /conductor:setup
    MCP_TOOL = "mcp"      # e.g. conductor_setup tool
    MANIFEST = "manifest" # e.g. TOML/JSON entry

@dataclass
class CommandDefinition:
    name: str
    description: str
    trigger_type: CommandTrigger
    action_ref: str # Reference to the core service method

class CommandRegistry(ABC):
    @abstractmethod
    def register_command(self, cmd: CommandDefinition) -> None:
        """Registers a command with the target agent's runtime."""
        pass

    @abstractmethod
    def unregister_command(self, name: str) -> None:
        """Removes a command from the target agent's runtime."""
        pass
```

## 3. Implementation Plan for Interfaces
-   **Adapters** will implement these ABCs by wrapping the host agent's native tools (e.g., Gemini's `run_shell_command`, Vibe's MCP tools).
-   **Core Services** will exclusively use these interfaces, ensuring they remain decoupled from the specific agent.
