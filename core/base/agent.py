from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import List

class CommandTrigger(Enum):
    SLASH = "slash"
    MCP_TOOL = "mcp"
    MANIFEST = "manifest"

@dataclass
class CommandDefinition:
    name: str
    description: str
    trigger_type: CommandTrigger
    action_ref: str

class CommandRegistry(ABC):
    @abstractmethod
    def register_command(self, cmd: CommandDefinition) -> None:
        """Registers a command with the target agent's runtime."""
        pass

    @abstractmethod
    def unregister_command(self, name: str) -> None:
        """Removes a command from the target agent's runtime."""
        pass

class BaseAgent(ABC):
    def __init__(self, context: 'AgentContext', registry: CommandRegistry):
        self.context = context
        self.registry = registry

    @abstractmethod
    def initialize(self) -> None:
        """Initializes the agent with Conductor commands."""
        pass
