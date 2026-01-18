# Technology Stack

## Core Extension Architecture
- **Host Agents**: Gemini CLI, Qwen Code.
- **Manifests**: `gemini-extension.json`, `qwen-extension.json` (JSON).
- **Command Definitions**: TOML files located in `commands/conductor/`.

## Data & Context Management
- **Primary Format**: Markdown (.md) for all human-readable context and planning documents.
- **Metadata**: JSON (.json) for machine-readable state and tracking.
- **Templates**: `.tmpl` files for scaffolding new documents.

## Development Tools
- **Shell**: Bash/Zsh for automation and tool execution.
- **Version Control**: Git for tracking changes and logical work unit reversions.

## Methodology
- **Context-Driven Development (CDD)**: The core operating principle of the project.
