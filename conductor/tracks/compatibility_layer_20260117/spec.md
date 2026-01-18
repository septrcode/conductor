# Track Specification: Multi-Agent Compatibility Layer Research and Prototype

## Overview
Research and design an abstraction layer to enable the Conductor extension to operate across multiple CLI-based AI agent ecosystems (e.g., Windsurf, Cursor) in addition to the existing Gemini CLI and Qwen Code support.

## Goals
1.  Analyze the extension architectures of target CLI agents.
2.  Define a unified "Agent Interface" that abstracts command registration and context management.
3.  Create a prototype implementation demonstrating the abstraction working for at least one new agent type (or a mocked generic agent).
4.  Document the architectural changes required to support the "Agent Agnosticism" product goal.

## Scope
-   **In Scope:**
    -   Analysis of provided CLI tool repositories.
    -   Design of `AgentAdapter` interfaces.
    -   Refactoring of core Conductor logic to use adapters.
    -   Prototype adapter for one new target.
-   **Out of Scope:**
    -   Full production release for all targets.
    -   UI/Frontend adaptations (focus is on CLI/Protocol level).

## User Context
The user has specific repositories for other CLI tools that should be analyzed during the research phase.
