# CLAUDE.md - AI Assistant Guide for Parent-AI-Safety

This document provides comprehensive guidance for AI assistants working on the Parent-AI-Safety repository.

## Project Overview

**Repository**: Parent-AI-Safety
**Owner**: osamac2128
**Status**: Early stage / Initial setup
**Purpose**: [To be defined - appears to be related to AI safety with focus on parental oversight/controls]

## Current Repository State

As of the last update, this is a new repository with minimal structure:

```
Parent-AI-Safety/
├── .git/
├── README.md          # Project name only
└── CLAUDE.md         # This file
```

## Repository Structure Guidelines

As the project develops, follow this recommended structure:

```
Parent-AI-Safety/
├── docs/              # Documentation
│   ├── architecture/  # Architecture decision records
│   ├── api/          # API documentation
│   └── guides/       # User and developer guides
├── src/              # Source code
│   ├── core/         # Core functionality
│   ├── utils/        # Utility functions
│   └── tests/        # Unit and integration tests
├── examples/         # Usage examples
├── scripts/          # Build and utility scripts
├── .github/          # GitHub workflows and templates
│   └── workflows/    # CI/CD pipelines
├── .gitignore        # Git ignore rules
├── README.md         # Project overview and quick start
├── CLAUDE.md         # This file
├── CONTRIBUTING.md   # Contribution guidelines
├── LICENSE           # Project license
└── [config files]    # package.json, requirements.txt, etc.
```

## Development Workflows

### Before Starting Work

1. **Understand the Task**: Read the issue/request completely
2. **Explore Context**: Use Task tool with Explore agent for codebase understanding
3. **Plan**: Use TodoWrite for multi-step tasks
4. **Read First**: Always read files before modifying them

### During Development

1. **Branch Strategy**:
   - Work on feature branches (format: `claude/description-sessionid`)
   - Never push directly to main
   - Current branch: `claude/add-claude-documentation-016ynrKHfM6FeSunDWrinunA`

2. **Commit Practices**:
   - Write clear, descriptive commit messages
   - Focus on "why" rather than "what"
   - Follow existing commit message style
   - Use heredoc for multi-line messages

3. **Code Quality**:
   - Avoid over-engineering
   - Only make requested changes
   - Don't add unrequested features or refactoring
   - Keep solutions simple and focused
   - Don't add comments where code is self-evident

### Git Operations

**Push Commands**:
```bash
git push -u origin <branch-name>
```
- Branch must start with 'claude/' and end with session ID
- Retry up to 4 times on network errors (exponential backoff: 2s, 4s, 8s, 16s)

**Fetch/Pull Commands**:
```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```

## Code Conventions

### General Principles

1. **Security First**:
   - No command injection vulnerabilities
   - No XSS, SQL injection, or OWASP top 10 vulnerabilities
   - Validate at system boundaries only
   - Trust internal code and framework guarantees

2. **Simplicity**:
   - Minimum viable complexity
   - No premature abstractions
   - No helpers/utilities for one-time operations
   - Three similar lines > premature abstraction

3. **No Backwards Compatibility Hacks**:
   - Delete unused code completely
   - No `_var` renaming, re-exports, or `// removed` comments
   - Clean deletions over compatibility layers

### Error Handling

- Only add error handling for scenarios that can actually occur
- Validate user input and external APIs
- Don't add fallbacks for impossible scenarios

### Testing

[To be defined based on chosen testing framework]

- Write tests for new features
- Ensure existing tests pass before pushing
- Follow existing test patterns

## Documentation Standards

### Code Documentation

- Add docstrings/comments only where logic isn't self-evident
- Keep documentation up-to-date with code changes
- Document public APIs thoroughly
- Internal functions: document only if complex

### README Updates

Update README.md when adding:
- New features or capabilities
- Installation requirements
- Configuration options
- Usage examples

## AI Assistant Specific Guidelines

### Tool Usage Priority

1. **File Operations**: Use specialized tools
   - Read (not cat/head/tail)
   - Edit (not sed/awk)
   - Write (not echo/heredoc)
   - Glob (not find)
   - Grep (not grep/rg commands)

2. **Exploration**: Use Task tool with Explore agent for:
   - Understanding codebase structure
   - Finding error handling patterns
   - Non-specific searches

3. **Parallel Execution**: Run independent tools in parallel

### Task Management

- Use TodoWrite for tasks with 3+ steps
- Mark tasks in_progress before starting
- Complete tasks immediately after finishing
- One task in_progress at a time
- Remove irrelevant tasks

### Communication

- No emojis unless explicitly requested
- Concise, technical responses
- Output text directly (not via echo/comments)
- Professional objectivity over validation
- Disagree when necessary

### Reference Format

When referencing code, use: `file_path:line_number`

Example: "Client connection handled in src/client.js:145"

## Project-Specific Considerations

### AI Safety Focus

This project appears related to AI safety with parental oversight. Consider:

1. **Privacy**: Handle any user data with care
2. **Safety Controls**: Implement robust safety mechanisms
3. **Transparency**: Clear documentation of safety features
4. **Accountability**: Audit trails for critical operations

### Future Development Areas

Areas likely to be developed (update as project evolves):

- [ ] Core safety framework
- [ ] Parental control mechanisms
- [ ] AI behavior monitoring
- [ ] Logging and audit systems
- [ ] User interface/API
- [ ] Configuration management
- [ ] Testing infrastructure
- [ ] Documentation

## Common Tasks

### Creating New Features

1. Read relevant existing code
2. Plan with TodoWrite (if complex)
3. Implement minimally
4. Test thoroughly
5. Update documentation
6. Commit and push

### Fixing Bugs

1. Reproduce the issue
2. Identify root cause
3. Fix with minimal changes
4. Verify fix works
5. Don't refactor surrounding code
6. Commit and push

### Adding Documentation

1. Read existing docs for style
2. Focus on clarity and accuracy
3. Include examples where helpful
4. Keep it maintainable
5. Commit and push

## Questions and Support

For questions about:
- **Claude Code usage**: Use Task tool with claude-code-guide agent
- **Project decisions**: Ask the repository owner
- **Unclear requirements**: Use AskUserQuestion before proceeding

## Updates and Maintenance

This CLAUDE.md file should be updated when:
- Project structure changes significantly
- New conventions are established
- Technology stack is chosen
- Major features are added
- Development workflow changes

**Last Updated**: 2025-11-23
**Last Updated By**: Claude (Initial creation)

---

## Quick Reference

### Essential Commands

```bash
# Check status
git status

# Create and switch to branch
git checkout -b claude/feature-name-sessionid

# Stage changes
git add <files>

# Commit
git commit -m "message"

# Push
git push -u origin <branch-name>

# View history
git log --oneline -10
```

### Essential File Locations

- **Documentation**: `docs/`
- **Source Code**: `src/`
- **Tests**: `src/tests/` or `tests/`
- **Examples**: `examples/`
- **Config**: Root directory

### Key Principles

1. Read before modifying
2. Plan complex tasks
3. Keep changes minimal
4. Security first
5. Simple over clever
6. Delete unused code
7. Test before pushing
