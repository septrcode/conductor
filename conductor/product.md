# Initial Concept
Implementation of Conductor CDD methodology for Qwen Code and Gemini CLI, with the goal of providing a structured, context-driven approach to AI-assisted software development and expanding compatibility to other coding agents.

# Product Definition

## Vision
To establish Conductor as the universal standard for Context-Driven Development across all CLI-based AI coding agents. By treating context as a managed artifact and following a "measure twice, code once" philosophy, Conductor ensures that AI agents remain grounded, consistent, and highly effective throughout the entire development lifecycle of a project.

## Target Users
- **CLI AI Agent Power Users**: Developers using Gemini CLI, Qwen Code, and similar tools who require deeper project integration.
- **Engineering Teams**: Teams looking for a standardized, documented process for AI-assisted coding to ensure quality and consistency.
- **Maintainers of Complex Codebases**: Users who need to manage large amounts of project-specific context that exceeds the immediate context window of most AI models.
- **Code Generation Enthusiasts**: "People trying to print code" who want high-quality, architecturally sound results from their AI prompts.

## Core Goals
- **Context Preservation**: Maintain a single, persistent source of truth for project context (Product, Tech Stack, Workflow).
- **Logical Work Units**: Organize development into "Tracks" that provide specific specifications and phased plans.
- **Agent Agnosticism**: Expand the extension architecture to support a wide range of coding agents beyond the initial Gemini and Qwen implementations.
- **Transparency and Control**: Give users a clear view of the AI's plan and the ability to review and modify it before execution.

## Key Features
- **Scaffolding Engine**: Automatically generates the foundation of a CDD-compliant project.
- **Track Lifecycle Management**: Tools to create, track, and implement work units.
- **Multi-Agent Compatibility Layers**: Abstracted command and context structures to support various AI ecosystems.
- **Status and Progress Tracking**: Visibility into the state of all project tracks and active tasks.
