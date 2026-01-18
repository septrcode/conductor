# Product Guidelines

## Brand & Tone
- **Professional & Precise**: We are building tools for engineers. The tone should be confident, technical, and accurate.
- **Concise**: Value the user's time. Avoid fluff. Get straight to the point.
- **Authoritative**: Users look to Conductor for structure. Instructions should be clear commands, not suggestions.

## Visual Identity
- **CLI First**: The primary interface is the terminal. Output should be formatted for readability in a monospaced environment (Markdown).
- **Structured**: Use headers, bullet points, and code blocks to organize information clearly.

## Design Principles
- **Measure Twice, Code Once**: Prioritize planning and specification over immediate coding.
- **Context is King**: All decisions must be grounded in the established project context.
- **Transparency**: The AI's internal state (plans, context) should be exposed to the user as readable files.
- **Interoperability**: Designs should favor standard formats (Markdown, JSON, TOML) to ensure compatibility across different agents and tools.

## Coding Standards (Project Specific)
- **Manifests**: Follow strict JSON and TOML schemas for extension definitions.
- **Templates**: Keep templates generic enough to be useful but specific enough to provide value immediately.
- **Filesystem**: Operations must be safe. Verify paths and existence before writing.
