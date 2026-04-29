# Skills & Dependencies

## Hermes Agent Skills Used

1. **design-case-study-creator** - Automated creation of full end-to-end design case studies
   - [View Skill](https://github.com/hermes-agent/skills/tree/main/creative/design-case-study-creator)
   - Used for: Structuring the case study, creating documentation, interactive prototypes, and presentation decks

2. **github-repo-management** - Clone/create/fork repos; manage remotes, releases
   - [View Skill](https://github.com/hermes-agent/skills/tree/main/github/github-repo-management)
   - Used for: Creating the GitHub repository, managing commits and pushes

3. **claude-design** - Design one-off HTML artifacts (landing, deck, prototype)
   - [View Skill](https://github.com/hermes-agent/skills/tree/main/creative/claude-design)
   - Used for: Designing the interactive prototype and presentation deck with dark neon theme

## Skills Registry

**[skills.sh](https://skills.sh)** - Discoverable skill registry for AI agents. Search and install skills to extend Hermes Agent's capabilities.

## How to Use These Skills

```bash
# List available skills
hermes skills list

# View a skill's documentation
hermes skills view design-case-study-creator

# Use a skill in your workflow
hermes skills use claude-design --prompt "Create a landing page for..."
```

## Skill Installation (if not already installed)

Skills are automatically available in Hermes Agent. To update or reinstall:

```bash
hermes skills update
```

## Case Study Structure Created by Skills

```
ux-redesign-case-study/
├── README.md                    # Overview (created by github-repo-management)
├── problem.md                   # Problem statement (design-case-study-creator)
├── research.md                  # User research (design-case-study-creator)
├── wireframes/README.md         # Low-fi wireframes (design-case-study-creator)
├── hi-fi-prototype.md           # Design system (design-case-study-creator)
├── final-screens.md             # Before/after comparisons (design-case-study-creator)
├── conclusion.md                # Impact + lessons (design-case-study-creator)
├── prototype/index.html         # Interactive before/after (claude-design)
├── presentation/index.html      # LinkedIn slides (claude-design)
└── SKILLS.md                    # This file
```

## External Tools Referenced

- **GitHub API** - Used via curl + token for repo creation
- **HTML/CSS/JavaScript** - For interactive prototype and presentation
- **Git** - Version control and GitHub integration

## License

MIT — Skills are open-source and free to use for your own projects.
