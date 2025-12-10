# Spec-Driven Development for Scientists - Site Plan

A teaching website for scientists who write code but aren't software developers. Emphasis on using AI effectively to produce reliable, publishable scientific code.

## Project Overview

**Goal:** Convince scientists that they can use AI coding assistants to produce rigorous, reproducible scientific code—and show them how.

**Audience:** Scientists (physicists, biologists, geoscientists, etc.) who write analysis code, build algorithms, or develop computational methods—but have no formal software engineering background. Likely arriving via colleague recommendation (lukewarm traffic, not cold).

**Core message:** You can use AI coding assistants to produce rigorous, reproducible scientific code—if you know how to work with them. This site teaches a simple approach: write specifications first, use AI as a thinking partner, stay in control of the science.

**Starting point:** Existing guide at `notes/spec-driven-project-guide.md` provides the foundation. The website expands this into navigable sections with emphasis on getting started quickly.

**Meta-approach:** The site itself is built using spec-driven development. The repo is public for those curious about the process.

## Technology Stack

- **Framework:** Astro with Starlight theme
- **Language:** Python (for all code examples in content)
- **Hosting:** GitHub Pages (free, simple)
- **Source:** Markdown files in a git repo

### Why Astro + Starlight

- Modern, fast, looks polished out of the box
- Supports custom landing page outside docs layout (hero + CTA, then into docs)
- Markdown-native, similar workflow to other doc tools
- Starlight is purpose-built for documentation sites

### Site Architecture

- **Custom landing page:** Hero section with core message, "Get Started" CTA - breaks out of docs layout
- **Docs section:** Starlight handles navigation for Get Started, Guides, Reference
- Landing page confirms "this is what your colleague mentioned" → one button → into the real content

## Site Structure

Optimized for "lukewarm" traffic—people who've heard the pitch and want to try it. Get Started is the hero path; deeper content is available but doesn't compete for attention.

```
docs/
├── index.md                        # Landing page (core message + single CTA)
│
├── get-started/                    # THE HERO PATH
│   ├── index.md                    # 5-minute overview (what + why, no fluff)
│   ├── scaffold.md                 # Run the script, get a project
│   └── first-spec.md               # Write your first spec (minimal example)
│
├── guides/                         # Depth when ready
│   ├── method/
│   │   ├── index.md                # Spec-driven development overview
│   │   ├── what-is-a-spec.md       # Specs explained simply
│   │   ├── directory-structure.md  # The specs/ folder organization
│   │   ├── workflow.md             # Phase-by-phase process (includes testing)
│   │   └── when-to-use.md          # When this helps (and when overkill)
│   │
│   ├── ai/                         # THE DIFFERENTIATOR
│   │   ├── index.md                # AI as thinking partner, not code monkey
│   │   ├── writing-specs-with-ai.md
│   │   ├── rules-files.md          # CLAUDE.md, CONTRIBUTING.md, etc.
│   │   ├── what-to-ask.md          # Being methodical
│   │   ├── reviewing-output.md     # You're still the scientist
│   │   └── the-feedback-loop.md    # Specs → AI → code → refined specs
│   │
│   └── examples/
│       ├── index.md                # Example specs and implementations
│       ├── data-pipeline.md        # Simple: loading and transforming data
│       ├── algorithm.md            # Medium: implementing a published method
│       └── analysis-tool.md        # Complex: multi-component analysis
│
├── reference/
│   ├── templates.md                # All templates on one page
│   └── spec-format.md              # Spec writing style guide
│
└── changelog.md                    # What's new
```

### Landing Page Design

The landing page should:
1. Confirm what they've already heard ("yes, this is the thing your colleague mentioned")
2. State the core message clearly
3. Have ONE prominent CTA: "Get Started"
4. Not overwhelm with navigation options

Draft opening:

> You can use AI coding assistants to produce rigorous, reproducible scientific code—if you know how to work with them.
>
> This site teaches a simple approach: write specifications first, use AI as a thinking partner, stay in control of the science.
>
> **[Get Started →]**

## The AI Guide - Key Content

This is the differentiating content. Most guides ignore how AI actually fits into the workflow. Lives under `guides/ai/`.

### `index.md` - AI as Thinking Partner

The key insight: AI is most valuable during the *specification* phase, not just implementation. Using AI to help you think through what you're building produces better results than using AI to generate code from vague requirements.

### `writing-specs-with-ai.md` - Using AI to Write Specs

How to collaborate with AI on specs:
- Start with the problem, not the solution
- Ask for alternatives and tradeoffs
- Probe for edge cases and failure modes
- Request examples and scenarios
- Iterate on the spec before any code exists

Show conversation examples demonstrating good vs. poor spec-writing sessions.

### `rules-files.md` - Collaboration Contracts

Rules files are specs for *how to work together*. Cover:

**CLAUDE.md / .cursorrules / similar:**
- What these files do
- What to put in them (preferences, project context, constraints)
- Example: "Don't edit files without explicit approval"
- Example: "Reference specs before implementing"

**CONTRIBUTING.md:**
- Not just for human contributors
- Defines commit conventions, PR process, code style
- AI assistants read and follow these

**Project-specific instructions:**
- How to structure them
- When to update them
- The compound effect over time

### `what-to-ask.md` - Being Methodical

The discipline of *how much* to ask at once:
- One concept at a time during spec writing
- Small, reviewable chunks during implementation
- Why "write me a complete module" produces worse results than iterative development
- The value of stopping to review before continuing

### `reviewing-output.md` - You're Still the Scientist

Critical: AI doesn't understand your domain the way you do.
- How to review AI-generated specs for domain accuracy
- How to review AI-generated code against specs
- Red flags to watch for
- When to push back vs. accept suggestions

### `the-feedback-loop.md` - The Virtuous Cycle

How good specs improve AI output, which reveals spec gaps, which improves specs:
- Spec → AI implementation → "wait, what about X?" → update spec
- Using implementation attempts to stress-test specifications
- The spec as living document, not write-once artifact

## Content Principles

### Tone
- Direct and practical, not academic
- Acknowledge the reality of scientific work (deadlines, changing requirements, "I just need this to work")
- No judgment about past practices
- Honest about tradeoffs (this takes time upfront)

### Examples
- Simplified scientific scenarios (not toy, not real projects)
- Show the *conversation* with AI, not just the output
- Include mistakes and iterations (not just polished results)
- Python throughout

### Living Document
- Acknowledge this will evolve
- Changelog to track updates
- Structure that accommodates growth
- Invite feedback/contributions

## Scaffolding Script

A simple Python script (`scaffold.py`) that helps users bootstrap a new spec-driven project. Lives in the repo root, downloadable from the site.

### What it does

1. **Prompts for basics:**
   - Project name
   - One-line description
   - Project type (data pipeline / analysis tool / algorithm implementation / general)
   - AI tool preference (Claude Code, Cursor, Copilot, other/none)

2. **Creates folder structure:**
   ```
   project-name/
   ├── specs/
   │   ├── spec-format.md          # How to write specs (critical reference!)
   │   ├── 00-overview.md          # Pre-filled with name/description + guidance
   │   ├── 01-requirements/
   │   │   └── functional.md       # Template with inline instructions
   │   ├── 02-architecture/
   │   │   └── .gitkeep
   │   ├── 03-implementation/
   │   │   └── .gitkeep
   │   └── 99-decisions/
   │       └── adr-000-template.md # ADR template with explanation
   ├── src/
   │   └── .gitkeep
   ├── tests/
   │   └── .gitkeep
   ├── .claude/                    # If Claude Code selected
   │   └── CLAUDE.md
   ├── .cursorrules                # If Cursor selected
   ├── CONTRIBUTING.md             # Basic contribution guidelines
   └── README.md                   # Points to specs/00-overview.md
   ```

3. **Customizes based on project type:**
   - Algorithm projects get `specs/03-algorithms/` and `specs/06-validation/`
   - Data pipelines get `specs/02-architecture/data-flow.md` starter
   - etc.

4. **Prints next steps:**
   - "Open specs/00-overview.md and flesh out your project description"
   - "Read specs/spec-format.md to understand how to write good specs"
   - "Run `git init` to start version control"
   - "Start a conversation with your AI assistant about requirements"

### The spec-format.md file

This is a key piece—a reference document that explains:
- Status labels (Draft → In Review → Approved → Implemented)
- Different formats for different spec types (requirements vs. algorithms vs. architecture)
- When to use MUST/SHOULD/COULD (only in requirements)
- Markdown conventions (code blocks, tables, cross-references)
- Change record format

Both humans and AI assistants can reference this to write consistent specs. It's the "style guide" for specifications.

### Template file contents

Each generated file includes **inline guidance** explaining what belongs there. Users fill in the blanks and delete the instructions as they go.

Example `specs/01-requirements/functional.md`:
```markdown
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
- **[SHOULD]** [Important but deferrable]
- **[COULD]** [Nice to have]

## Open Questions

[What's still unclear?]

## Change Record

- YYYY-MM-DD: Initial draft
```

### AI tool flexibility

The script asks which AI tool the user prefers and generates the appropriate config:
- **Claude Code** → `.claude/CLAUDE.md` (recommended in docs, but not required)
- **Cursor** → `.cursorrules`
- **GitHub Copilot** → `.github/copilot-instructions.md`
- **Other/None** → Skip, but still create CONTRIBUTING.md

The site content covers Claude Code examples primarily (it's what we use and recommend) but the principles apply to any AI coding assistant.

### Design principles

- **Zero dependencies** - Pure Python stdlib, runs anywhere
- **Readable** - Scientists can open it and understand what it does
- **Instructive** - Generated files teach as they scaffold
- **Flexible** - Adapts to user's toolchain

### Usage

```bash
# Download and run
curl -O https://yoursite.com/scaffold.py
python scaffold.py

# Or with pipx (future)
pipx run spec-driven-scaffold
```

## Key Messages

1. **AI amplifies your approach** - Good process + AI = great results. Bad process + AI = faster bad results.
2. **Specs are thinking tools** - Writing them clarifies your own understanding
3. **Rules files compound** - Small investments in CLAUDE.md pay off across many sessions
4. **You're the domain expert** - AI doesn't know your science; you do
5. **Iterate in specs, not code** - Cheaper to fix a spec than debug an implementation

## Development Phases

### Phase 1: Foundation + Get Started Path
- [ ] Set up Astro + Starlight
- [ ] Custom landing page (hero with core message, single CTA)
- [ ] Basic structure and navigation
- [ ] Get Started section (5-min overview, scaffold instructions, first spec)
- [ ] Scaffolding script (full version—zero dependencies, instructive templates, AI tool selection)

### Phase 2: Core Content (Minimum Viable Guides)

**Method foundation** (just enough for AI content to make sense):
- [ ] `guides/method/index.md` - What is spec-driven development, why it matters
- [ ] `guides/method/what-is-a-spec.md` - The core concept, scientist-friendly framing
- [ ] `guides/method/workflow.md` - The phases, including where testing fits

**AI collaboration** (the differentiator):
- [ ] `guides/ai/index.md` - AI as thinking partner, not code generator
- [ ] `guides/ai/writing-specs-with-ai.md` - How to collaborate on specs
- [ ] `guides/ai/rules-files.md` - CLAUDE.md, CONTRIBUTING.md, etc.

**One complete example:**
- [ ] `guides/examples/data-pipeline.md` - Demonstrates both method and AI collaboration

### Phase 3: Reference + Polish
- [ ] Templates page
- [ ] Spec format guide
- [ ] Changelog
- [ ] Deploy to GitHub Pages

### Phase 4: Extended Content (Post-Launch)
- [ ] `guides/method/directory-structure.md`
- [ ] `guides/method/when-to-use.md`
- [ ] `guides/ai/what-to-ask.md`
- [ ] `guides/ai/reviewing-output.md`
- [ ] `guides/ai/the-feedback-loop.md`
- [ ] Additional examples (algorithm, analysis-tool)

## Decisions Made

- **Site name:** Spec-Driven Science
- **Testing:** Folded into workflow, not a separate section
- **Git/version control:** Assume basic familiarity, link out to resources
- **Quick start:** Yes—it's the entire Get Started section, prominently featured
- **"This site" meta section:** Removed. Repo is public for the curious, but not a nav item
- **"Problem" section:** Removed. Audience is already bought in; fold any useful framing into landing page or 5-min overview

## Open Questions

None at this time.

## Next Steps

1. Set up Astro + Starlight
2. Create custom landing page (hero with core message, single CTA)
3. Build Get Started section (the hero path)
4. Build scaffolding script
5. Then guides and reference content

---

*Plan updated: 2025-12-08*
*Revised based on UX discussion: flattened structure, Get Started as hero path, removed problem/this-site sections*
*Switched from MkDocs to Astro + Starlight for better aesthetics and custom landing page support*
