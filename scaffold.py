#!/usr/bin/env python3
"""
Scaffold a spec-driven project.

Creates a project structure with specification templates, ready for
AI-assisted development. Zero dependencies beyond Python stdlib.

Usage:
    python scaffold.py
"""

from pathlib import Path


def prompt(question: str, default: str = "") -> str:
    """Prompt user for input with optional default."""
    if default:
        response = input(f"{question} [{default}]: ").strip()
        return response if response else default
    return input(f"{question}: ").strip()


def prompt_choice(question: str, options: list[str]) -> str:
    """Prompt user to select from numbered options."""
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")

    while True:
        try:
            choice = int(input("Enter number: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print(f"Please enter a number between 1 and {len(options)}")


def gather_inputs() -> dict:
    """Gather project information from user."""
    print("\n=== Spec-Driven Project Scaffolder ===\n")

    name = prompt("Project name (e.g., seismic-analysis)")
    while not name:
        print("Project name is required.")
        name = prompt("Project name")

    description = prompt("One-line description", "A spec-driven scientific project")

    project_type = prompt_choice(
        "Project type:",
        ["Data pipeline", "Analysis tool", "Algorithm implementation", "General"]
    )

    ai_tool = prompt_choice(
        "Primary AI coding assistant:",
        ["Claude Code", "Cursor", "GitHub Copilot", "Other/None"]
    )

    return {
        "name": name,
        "description": description,
        "project_type": project_type,
        "ai_tool": ai_tool,
    }


# =============================================================================
# Template Content
# =============================================================================

SPEC_FORMAT = """\
# Spec Format Guide

This document explains how to write specifications for this project.
Both humans and AI assistants should reference this for consistency.

## Status Labels

Every spec should have a status in its frontmatter:

- **Draft** — Initial writing, not yet reviewed
- **In Review** — Ready for feedback
- **Approved** — Accepted, ready for implementation
- **Implemented** — Code exists that fulfills this spec
- **Deprecated** — No longer applicable

## Spec Types

### Requirements Specs

Describe *what* the system should do from the user's perspective.

- Use **[MUST]**, **[SHOULD]**, **[COULD]** to indicate priority
- Write as capabilities, not implementation details
- Be specific enough to test against

Example:
```markdown
- **[MUST]** Calculate RMS amplitude for each time window
- **[SHOULD]** Support configurable window sizes (default: 1 second)
- **[COULD]** Export results to CSV format
```

### Architecture Specs

Describe *how* components fit together.

- Include diagrams where helpful (Mermaid works well)
- Define interfaces between components
- Document data flow

### Algorithm Specs

Describe computational methods in detail.

- Reference source papers/methods
- Include mathematical notation where precise
- Define expected inputs, outputs, and edge cases
- Specify validation approach

### Decision Records (ADRs)

Document significant decisions and their rationale.

- Context: What prompted this decision?
- Decision: What did we decide?
- Consequences: What are the tradeoffs?

## Markdown Conventions

- Use fenced code blocks with language tags
- Use tables for structured comparisons
- Cross-reference other specs with relative links: `[see requirements](../01-requirements/functional.md)`

## Change Records

Each spec should end with a change record:

```markdown
## Change Record

- YYYY-MM-DD: Initial draft
- YYYY-MM-DD: Added edge case handling per review feedback
```
"""

def overview_template(name: str, description: str) -> str:
    return f"""\
# {name}

**Status**: Draft

{description}

<!--
This is your project's overview spec. It should answer:
- What problem does this project solve?
- Who is it for?
- What are the key capabilities?

Keep it high-level. Details go in requirements and architecture specs.

Delete these instructions once you've written the overview.
-->

## Problem Statement

[What problem are you solving? Why does it matter?]

## Goals

[What should this project accomplish?]

## Non-Goals

[What is explicitly out of scope?]

## Key Components

[High-level overview of the main parts]

## Change Record

- {_today()}: Initial draft
"""


FUNCTIONAL_REQUIREMENTS = """\
# Functional Requirements

**Status**: Draft

<!--
This file describes WHAT your system should do from the user's perspective.
Write these as capabilities, not implementation details.

Tips:
- Start each requirement with a verb (Calculate, Display, Export...)
- Use [MUST], [SHOULD], [COULD] to prioritize (see spec-format.md)
- Be specific enough to test against later
- It's okay to start sparse and add detail as you learn more

Delete these instructions once you've got the hang of it.
-->

## Overview

[Brief context for what you're building]

## Core Capabilities

- **[MUST]** [Required capability]
- **[MUST]** [Another required capability]
- **[SHOULD]** [Important but deferrable]
- **[COULD]** [Nice to have]

## Input/Output

### Inputs

[What data or parameters does the system accept?]

### Outputs

[What does the system produce?]

## Error Handling

[How should the system behave when things go wrong?]

## Open Questions

[What's still unclear? What needs discussion?]

## Change Record

- YYYY-MM-DD: Initial draft
"""


ADR_TEMPLATE = """\
# ADR-000: Decision Record Template

**Status**: Template

**Date**: YYYY-MM-DD

<!--
Architecture Decision Records (ADRs) capture significant technical decisions.
Copy this template for each new decision. Number them sequentially (ADR-001, ADR-002, etc.).

A good ADR explains:
- What decision was made
- Why it was made (context and constraints)
- What alternatives were considered
- What the consequences are

Delete these instructions when writing a real ADR.
-->

## Context

[What is the issue? What forces are at play? What constraints exist?]

## Decision

[What did you decide to do?]

## Alternatives Considered

### Alternative 1: [Name]

[Description, pros, cons]

### Alternative 2: [Name]

[Description, pros, cons]

## Consequences

### Positive

- [Benefit 1]
- [Benefit 2]

### Negative

- [Tradeoff 1]
- [Tradeoff 2]

### Neutral

- [Side effect that's neither good nor bad]

## Change Record

- YYYY-MM-DD: Initial decision
"""


DATA_FLOW_TEMPLATE = """\
# Data Flow Architecture

**Status**: Draft

<!--
This spec describes how data moves through your pipeline.
Useful for data processing, ETL, and analysis projects.

Delete these instructions once you've documented your data flow.
-->

## Overview

[High-level description of the data flow]

## Pipeline Stages

### Stage 1: Ingestion

**Input**: [Source format, location]
**Output**: [Intermediate format]
**Processing**: [What happens here]

### Stage 2: Processing

**Input**: [From previous stage]
**Output**: [Transformed data]
**Processing**: [What happens here]

### Stage 3: Output

**Input**: [From previous stage]
**Output**: [Final format, destination]
**Processing**: [What happens here]

## Data Formats

[Describe key data structures, file formats, schemas]

## Error Handling

[What happens when a stage fails?]

## Change Record

- YYYY-MM-DD: Initial draft
"""


ALGORITHM_SPEC_TEMPLATE = """\
# Algorithm: [Name]

**Status**: Draft

<!--
This spec describes a computational algorithm in detail.
Reference papers, define mathematics precisely, specify edge cases.

Delete these instructions once you've documented the algorithm.
-->

## Overview

[What does this algorithm do? Where does it come from?]

## References

- [Paper/textbook citation]
- [Implementation reference, if any]

## Mathematical Definition

[Precise mathematical description. Use LaTeX notation if helpful.]

## Inputs

| Parameter | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| x | array | Input signal | Length > 0 |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| result | float | Computed value |

## Algorithm Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Edge Cases

- [What happens with empty input?]
- [What happens with NaN values?]
- [Numerical stability concerns?]

## Validation Approach

[How will you verify the implementation is correct?]

## Change Record

- YYYY-MM-DD: Initial draft
"""


VALIDATION_SPEC_TEMPLATE = """\
# Validation Plan

**Status**: Draft

<!--
This spec describes how you'll validate that your implementation is correct.
Especially important for scientific code where correctness matters.

Delete these instructions once you've documented your validation plan.
-->

## Overview

[What are you validating? What does "correct" mean for this project?]

## Test Cases

### Unit Tests

[Tests for individual functions/components]

### Integration Tests

[Tests for components working together]

### Known-Answer Tests

[Tests against published results or analytical solutions]

| Test Case | Input | Expected Output | Source |
|-----------|-------|-----------------|--------|
| [Name] | [Input description] | [Expected result] | [Paper/reference] |

## Validation Data

[What test datasets exist? Where do they come from?]

## Acceptance Criteria

[What must pass before the implementation is considered valid?]

## Change Record

- YYYY-MM-DD: Initial draft
"""


def readme_template(name: str, description: str) -> str:
    return f"""\
# {name}

{description}

## Overview

See [specs/00-overview.md](specs/00-overview.md) for project goals and scope.

## Project Structure

```
{name}/
├── specs/           # Specifications (start here!)
│   ├── spec-format.md      # How to write specs
│   ├── 00-overview.md      # Project overview
│   ├── 01-requirements/    # What the system should do
│   ├── 02-architecture/    # How components fit together
│   ├── 03-implementation/  # Implementation details
│   └── 99-decisions/       # Architecture decision records
├── src/             # Source code
└── tests/           # Test code
```

## Getting Started

1. Read `specs/00-overview.md` to understand the project
2. Review `specs/spec-format.md` for how to write specs
3. Start with requirements in `specs/01-requirements/`

## Development Approach

This project uses **spec-driven development**:

1. Write specifications before code
2. Use AI assistants to help refine specs and implement them
3. Verify implementations against specs
4. Update specs as requirements evolve

See [spec-driven.science](https://spec-driven.science) for more on this approach.
"""


def contributing_template(name: str) -> str:
    return f"""\
# Contributing to {name}

## Development Approach

This project uses spec-driven development. Before writing code:

1. **Check for an existing spec** in the `specs/` directory
2. **Write or update a spec** if one doesn't exist
3. **Get the spec reviewed** before implementing
4. **Reference the spec** in your code and commits

## Commit Messages

Use clear, descriptive commit messages:

```
Add amplitude calculation per spec 03-implementation/amplitude.md

Implements the RMS amplitude algorithm as specified. Includes
edge case handling for empty windows.
```

## Code Style

- Follow existing patterns in the codebase
- Include docstrings for public functions
- Write tests for new functionality

## Pull Request Process

1. Ensure your changes align with a spec
2. Update specs if your changes affect requirements
3. Include tests for new functionality
4. Reference relevant specs in your PR description

## Questions?

Open an issue for discussion before starting significant work.
"""


def claude_md_template(name: str) -> str:
    return f"""\
# Project: {name}

## Overview

This is a spec-driven scientific project. Specifications live in the `specs/` directory and should be referenced before implementing any functionality.

## Key Principles

- **Specs first**: Check `specs/` before writing code. If no spec exists, write one.
- **Small steps**: Implement incrementally. One function, one test, verify, repeat.
- **Ask questions**: If a spec is unclear, ask for clarification rather than guessing.

## Project Structure

- `specs/` — Specifications (requirements, architecture, algorithms)
- `src/` — Source code
- `tests/` — Test code

## Working With Me

- Reference specific specs when discussing implementation
- Propose spec updates if you notice gaps or issues
- Keep implementations focused—one concept at a time
- I'll verify your suggestions against the specs

## Spec Format

See `specs/spec-format.md` for how specifications are written in this project.
"""


def cursorrules_template(name: str) -> str:
    return f"""\
# Project: {name}

This is a spec-driven scientific project.

## Key Rules

1. Check `specs/` directory before implementing anything
2. Reference specific specs when discussing code
3. If no spec exists for a feature, write one first
4. Keep changes small and incremental
5. Verify implementations against spec requirements

## Project Structure

- `specs/` — Specifications (start here!)
- `src/` — Source code
- `tests/` — Test code

## Spec Format

See `specs/spec-format.md` for specification conventions.
"""


def copilot_instructions_template(name: str) -> str:
    return f"""\
# Project: {name}

This is a spec-driven scientific project. Specifications in `specs/` define what should be built.

## Guidelines

- Check `specs/` before implementing features
- Reference specs when writing code
- Write specs for new functionality before implementing
- Keep implementations focused and incremental
- Follow patterns established in existing code

## Structure

- `specs/` — Specifications (requirements, architecture, decisions)
- `src/` — Source code
- `tests/` — Test code
"""


def _today() -> str:
    """Return today's date as YYYY-MM-DD."""
    from datetime import date
    return date.today().isoformat()


# =============================================================================
# Scaffolding Logic
# =============================================================================

def create_project(inputs: dict) -> Path:
    """Create the project directory structure and files."""
    name = inputs["name"]
    description = inputs["description"]
    project_type = inputs["project_type"]
    ai_tool = inputs["ai_tool"]

    root = Path(name)

    if root.exists():
        print(f"\nError: Directory '{name}' already exists.")
        raise SystemExit(1)

    # Create directory structure
    dirs = [
        root / "specs" / "01-requirements",
        root / "specs" / "02-architecture",
        root / "specs" / "03-implementation",
        root / "specs" / "99-decisions",
        root / "src",
        root / "tests",
    ]

    # Add project-type-specific directories
    if project_type == "Algorithm implementation":
        dirs.append(root / "specs" / "04-algorithms")
        dirs.append(root / "specs" / "05-validation")

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # Write core spec files
    (root / "specs" / "spec-format.md").write_text(SPEC_FORMAT)
    (root / "specs" / "00-overview.md").write_text(overview_template(name, description))
    (root / "specs" / "01-requirements" / "functional.md").write_text(FUNCTIONAL_REQUIREMENTS)
    (root / "specs" / "99-decisions" / "adr-000-template.md").write_text(ADR_TEMPLATE)

    # Project-type-specific files
    if project_type == "Data pipeline":
        (root / "specs" / "02-architecture" / "data-flow.md").write_text(DATA_FLOW_TEMPLATE)

    if project_type == "Algorithm implementation":
        (root / "specs" / "04-algorithms" / "algorithm-template.md").write_text(ALGORITHM_SPEC_TEMPLATE)
        (root / "specs" / "05-validation" / "validation-plan.md").write_text(VALIDATION_SPEC_TEMPLATE)

    # Write root files
    (root / "README.md").write_text(readme_template(name, description))
    (root / "CONTRIBUTING.md").write_text(contributing_template(name))

    # AI tool configuration
    if ai_tool == "Claude Code":
        (root / ".claude").mkdir(exist_ok=True)
        (root / ".claude" / "CLAUDE.md").write_text(claude_md_template(name))
    elif ai_tool == "Cursor":
        (root / ".cursorrules").write_text(cursorrules_template(name))
    elif ai_tool == "GitHub Copilot":
        (root / ".github").mkdir(exist_ok=True)
        (root / ".github" / "copilot-instructions.md").write_text(copilot_instructions_template(name))

    # Add .gitkeep to empty directories
    for d in [root / "src", root / "tests"]:
        (d / ".gitkeep").touch()

    return root


def print_next_steps(root: Path, ai_tool: str) -> None:
    """Print guidance for what to do next."""
    print(f"""
✓ Project created: {root}/

Next steps:

  1. cd {root}
  2. Open specs/00-overview.md and flesh out your project description
  3. Read specs/spec-format.md to understand how to write specs
  4. Run 'git init' to start version control
  5. Start a conversation with your AI assistant about requirements
""")

    if ai_tool == "Claude Code":
        print(f"     Your .claude/CLAUDE.md is ready — Claude Code will read it automatically.\n")
    elif ai_tool == "Cursor":
        print(f"     Your .cursorrules is ready — Cursor will read it automatically.\n")
    elif ai_tool == "GitHub Copilot":
        print(f"     Your .github/copilot-instructions.md is ready for Copilot.\n")


def main():
    """Main entry point."""
    try:
        inputs = gather_inputs()
        root = create_project(inputs)
        print_next_steps(root, inputs["ai_tool"])
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        raise SystemExit(0)


if __name__ == "__main__":
    main()
