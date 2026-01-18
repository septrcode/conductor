from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

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
