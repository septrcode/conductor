# Universal Agent Interface (UAI) Specification [Draft]

## 1. Overview
The Universal Agent Interface (UAI) is a proposed abstraction layer for the Conductor extension. It enables Conductor to operate across diverse AI agent ecosystems by decoupling the core methodology and context management from agent-specific implementation details.

## 2. Core Abstractions

### 2.1 Agent Definition
An `Agent` in Conductor is defined by its interaction capabilities:
- **Manifest-driven**: Requires a static manifest (e.g., `gemini-extension.json`).
- **Protocol-driven**: Supports standard protocols like MCP (Model Context Protocol) or ACP (Agent Client Protocol).
- **Prompt-driven**: Loads instructions from specific filesystem locations (e.g., Mistral Vibe's `prompts/` directory).

### 2.2 Context Provider
Responsible for making Conductor's context files (`product.md`, `plan.md`, etc.) available to the agent.
- **MCP Resource Provider**: Exposes files as MCP resources.
- **Skill/Plugin Injector**: Registers Conductor as a "skill" or "plugin" in the agent's native system.
- **Filesystem Shadowing**: Symlinks or copies Conductor files into the agent's expected context directories.

### 2.3 Command Translator
Maps Conductor's high-level commands to agent-specific triggers:
- **Slash Commands**: `/conductor:setup` -> `/vibe:setup` or native slash command registration.
- **MCP Tools**: Exposes Conductor actions as MCP tools.
- **Static Manifests**: Generates the necessary JSON/TOML files for agents that require them.

## 3. Implementation Strategy

### 3.1 The "Conductor Core" Module
A central, agent-agnostic module containing:
- State management (`setup_state.json`).
- Template rendering logic.
- Workflow enforcement rules.

### 3.2 Agent Adapters
Specific implementations for each target agent:
- `GeminiAdapter`: Current implementation using `gemini-extension.json`.
- `VibeAdapter`: Integrates via `~/.vibe/prompts` and MCP.
- `CodexAdapter`: Integrates via MCP server and "skills" system.
- `GenericACPAdapter`: Uses the Agent Client Protocol for any compliant agent.

## 4. Proposed Directory Structure
```
vibe/ (or core/)
├── agents/
│   ├── base.py         # Abstract base classes
│   ├── gemini.py       # Gemini CLI implementation
│   ├── vibe.py         # Mistral Vibe implementation
│   └── codex.py        # OpenAI Codex implementation
├── context/
│   ├── mcp.py          # MCP resource handling
│   └── prompt.py       # Prompt injection logic
└── commands/           # Core command logic (agent-agnostic)
```

## 5. Next Steps
1. Finalize the `BaseAgent` and `BaseContextProvider` interfaces in Python.
2. Prototype the `VibeAdapter` as the first multi-agent target.
3. Refactor the `setup` command to use the `UAI`.
