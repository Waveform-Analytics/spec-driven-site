---
title: Get Started
description: A 5-minute overview of spec-driven development for scientists.
---

You write code to do science. Analysis pipelines, data processing, algorithms from papers, visualization tools. The code matters because the results matter—but you're not a software developer, and you don't have time to become one.

AI coding assistants can help - but "help" is a spectrum. At one end: generating boilerplate you'll spend hours debugging. At the other: producing reliable, well-structured code you actually understand and can maintain.

The difference isn't the AI, it's how you work with it.

## The core idea

**Write specifications before code.**

A specification (spec) is a document that describes what you're building - the requirements, the expected behavior, the edge cases - before any code exists. It's not a formal software engineering artifact. It's a thinking tool.

When you write a spec first:

1. **You clarify your own thinking.** What exactly should this function do? What are the inputs and outputs? What happens when the data is missing or malformed?

2. **You give the AI something concrete to work with.** "Implement this spec" produces better results than "write a function that processes my data."

3. **You create a reference for verification.** When the AI generates code, you can check it against the spec. Does it actually do what you specified?

## The workflow

1. **Describe what you need** — Write a spec for the component you're building. Start rough; refine it.

2. **Use AI to help think it through** — Ask the AI to poke holes in your spec. What edge cases are you missing? What assumptions are you making?

3. **Generate code from the spec** — Once the spec is solid, ask the AI to implement it. The spec becomes the prompt.

4. **Verify against the spec** — Review the generated code. Does it match what you specified? Test it against the cases you defined.

5. **Update the spec as you learn** — Requirements change. You discover new edge cases. The spec evolves, and the code follows.

## Specs are the real work

A spec isn't documentation you write after the fact. It's the intellectual work itself, expressed in a form humans can reason about efficiently.

Even a skilled programmer will understand a 50-line spec faster than 700 lines of code. The spec removes syntax from the equation so you can focus on the science: the algorithm, the edge cases, the validation approach.

This efficiency benefits everyone. You think more clearly. Reviewers engage with the logic, not the implementation details. AI assistants get unambiguous instructions. And six months later, you remember *why*, not just *what*.

## Why this works

Most AI-generated code problems come from vague requests. "Write a function to normalize my data" leaves too much undefined. What kind of normalization? What's the input format? What should happen with NaN values?

Specs force you to answer these questions upfront. The AI gets clear instructions, and you get code that does what you actually need.

## What's next

Ready to try it?

1. **[Scaffold a project](/spec-driven-site/get-started/scaffold/)** — Run our scaffolding script to create a project structure with spec templates ready to go.

2. **[Write your first spec](/spec-driven-site/get-started/first-spec/)** — Walk through a minimal example: one spec, one implementation, one test.

You can get started in less than an hour, and then build up your knowledge over time. 