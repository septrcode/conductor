# Conductor - Context-Driven Development for Qwen Code

Conductor is a Qwen Code extension that implements Context-Driven Development - a structured approach to software development that treats context as a managed artifact. Following the principle of "measure twice, code once," Conductor ensures proper planning before implementation.

## Philosophy

- **Context as a Managed Artifact**: Treat project context with the same care as code
- **Single Source of Truth**: Maintain a centralized source of project awareness
- **Structured Workflow**: Follow a defined process from context establishment to implementation
- **Logical Work Units**: Organize work into tracks that can be tracked and managed

## Installation

To install the Conductor extension:

```bash
qwen extensions install https://github.com/your-username/conductor.git
```

## Commands

### `/conductor:setup`
Initialize project context with foundational documents:
- Product definition
- Development guidelines
- Technology stack
- Workflow processes
- Code style guides

### `/conductor:newTrack`
Create a new track (high-level unit of work) with:
- Detailed specification (spec.md)
- Actionable plan with phases and tasks (plan.md)
- Metadata tracking

### `/conductor:implement`
Execute planned tasks following defined workflows while maintaining alignment with project context.

### `/conductor:status`
Get a status overview of current tracks and progress.

### `/conductor:revert`
Revert changes for a logical work unit with git-aware functionality.

## Usage

### 1. Context Phase
Start by establishing project context:

```
/conductor:setup
```

This creates foundational documents in the `conductor/` directory that serve as the single source of truth for your project.

### 2. Specification & Planning Phase
Create tracks for major units of work:

```
/conductor:newTrack
```

Provide a name and description for your track. This creates specification and planning documents in `conductor/tracks/[track-name]/`.

### 3. Implementation Phase
Work on a specific track:

```
/conductor:implement <track-name>
```

Follow the plan while maintaining alignment with project context.

### 4. Monitoring
Check the status of your project:

```
/conductor:status
```

### 5. Reversion
If needed, revert changes for a track:

```
/conductor:revert <track-name>
```

## Benefits

- **Deep Project Awareness**: AI interactions are informed by persistent project context
- **Consistent Outcomes**: Following structured workflows leads to more predictable results
- **Traceability**: Track work from conception to completion with detailed documentation
- **Quality Assurance**: Proper planning reduces costly mistakes and rework

## Directory Structure

After using Conductor, your project will have a `conductor/` directory with:

```
conductor/
├── product.md          # Product definition
├── guidelines.md       # Development guidelines
├── techstack.md        # Technology stack
├── workflow.md         # Development workflow
├── codestyle.md        # Code style guide
└── tracks/             # Individual work tracks
    └── [track-name]/
        ├── spec.md     # Track specification
        ├── plan.md     # Implementation plan
        └── metadata.json # Track metadata
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.