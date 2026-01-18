# Architecture Design: Core vs Adapter

## 1. Directory Structure
The refactored Conductor will use a modular Python structure to separate agent-agnostic logic from specific agent implementations.

```
conductor_core/
├── __init__.py
├── base/               # Abstract Base Classes (ABCs)
│   ├── __init__.py
│   ├── agent.py        # BaseAgent interface
│   └── context.py      # BaseContextProvider interface
├── models/             # Data structures
│   ├── __init__.py
│   ├── project.py      # Models for product.md, tech-stack.md
│   └── track.py        # Models for plan.md, tracks.md
├── services/           # Core business logic
│   ├── __init__.py
│   ├── scaffolding.py  # Initialization and setup logic
│   ├── tracker.py      # Management of tracks and plans
│   └── workflow.py     # Protocol enforcement
├── adapters/           # Agent-specific implementations
│   ├── __init__.py
│   ├── gemini.py       # Gemini CLI Adapter
│   ├── vibe.py         # Mistral Vibe Adapter
│   ├── codex.py        # OpenAI Codex Adapter
│   └── acp.py          # Generic Agent Client Protocol Adapter
└── utils/              # Shared utilities
    ├── __init__.py
    ├── filesystem.py   # Atomic and safe file writes
    └── markdown.py     # Plan/Spec parsing and generation
```

## 2. Component Responsibilities

### 2.1 Conductor Core (`services/`)
-   **Scaffolding**: Implements the logic for `/conductor:setup`. Renders templates and maintains `setup_state.json`.
-   **Tracker**: Logic for creating new tracks, updating plans, and checking status.
-   **Workflow**: Logic for TDD enforcement, checkpointing, and git note attachment.

### 2.2 Base Interfaces (`base/`)
-   `BaseAgent`: Defines how commands are registered and how the agent responds to triggers.
-   `BaseContextProvider`: Defines how project context is made "visible" to the agent (e.g., via MCP, Prompt files, or Skills).

### 2.3 Adapters (`adapters/`)
-   Translate `BaseAgent` actions into agent-specific configurations (JSON manifests, TOML, or MCP server definitions).
-   Inject core logic into the agent's specific runtime.

## 3. Benefits
-   **Testability**: Core logic can be unit-tested without an active AI agent.
-   **Extensibility**: Adding a new agent only requires implementing a new adapter.
-   **Consistency**: The same methodology is applied regardless of the host environment.
