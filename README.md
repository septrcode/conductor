# Conductor - Context-Driven Development for Qwen Code

Conductor is a Qwen Code extension that implements Context-Driven Development - a structured approach to software development that treats context as a managed artifact. This is a complete 1:1 implementation of the original Gemini CLI Conductor extension, following the principle of "measure twice, code once" to ensure proper planning before implementation.

## Philosophy

- **Context as a Managed Artifact**: Treat project context with the same care as code
- **Single Source of Truth**: Maintain a centralized source of project awareness
- **Structured Workflow**: Follow a defined process from context establishment to implementation
- **Logical Work Units**: Organize work into tracks that can be tracked and managed
- **Multi-Session Support**: Enables multiple concurrent sessions working on different tracks

## Installation

To install the Conductor extension:

```bash
qwen extensions install https://github.com/septrcode/conductor.git
```

## Commands

### `/conductor:setup`
Scaffold the project and set up the Conductor environment:
- Product definition and guidelines
- Technology stack configuration
- Workflow processes and code style guides
- Initial track generation

### `/conductor:newTrack`
Start a new feature or bug track with:
- Detailed specification (spec.md)
- Actionable plan with phases and tasks (plan.md)
- Metadata tracking

### `/conductor:implement`
Execute the tasks defined in the current track's plan following the project's workflow protocols.

### `/conductor:status`
Display the current progress of the tracks file and active tracks.

### `/conductor:revert`
Revert a track, phase, or task by analyzing git history with understanding of logical work units.

## Multi-Session/Track Coordination

The Conductor extension supports multiple concurrent sessions working on different tracks:

1. **Track Isolation**: Each track operates independently with its own spec and plan files
2. **State Management**: Track states are maintained separately in metadata files
3. **Conflict Prevention**: Sessions operate on distinct track directories
4. **Progress Tracking**: Each track's progress is recorded independently

## Context Management

The extension uses `QWEN.md` as its context file, which provides persistent context to guide the AI assistant's behavior during interactions. This context includes file resolution protocols and multi-session coordination instructions.

## Usage

### 1. Project Setup
Initialize your project context:

```
/conductor:setup
```

This creates foundational documents in the `conductor/` directory that serve as the single source of truth for your project.

### 2. Track Creation
Create tracks for major units of work:

```
/conductor:newTrack
```

Provide a name and description for your track. This creates specification and planning documents in `conductor/tracks/[track-id]/`.

### 3. Implementation
Work on a specific track:

```
/conductor:implement
```

Follow the plan while maintaining alignment with project context and workflow protocols.

### 4. Monitoring
Check the status of your project:

```
/conductor:status
```

### 5. Reversion
If needed, revert changes for a track:

```
/conductor:revert
```

## Benefits

- **Deep Project Awareness**: AI interactions are informed by persistent project context
- **Consistent Outcomes**: Following structured workflows leads to more predictable results
- **Traceability**: Track work from conception to completion with detailed documentation
- **Quality Assurance**: Proper planning reduces costly mistakes and rework
- **Multi-Session Support**: Multiple sessions can work on different tracks simultaneously
- **Git Integration**: Smart revert functionality understands logical work units

## Directory Structure

After using Conductor, your project will have a `conductor/` directory with:

```
conductor/
├── product.md              # Product definition
├── product-guidelines.md   # Product guidelines
├── tech-stack.md           # Technology stack
├── workflow.md             # Development workflow
├── setup_state.json        # Setup state tracking
├── tracks.md               # Master tracks registry
├── code_styleguides/       # Code style guides
└── tracks/                 # Individual work tracks
    └── [track-id]/
        ├── spec.md         # Track specification
        ├── plan.md         # Implementation plan
        └── metadata.json   # Track metadata
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.