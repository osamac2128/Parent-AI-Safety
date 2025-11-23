# Contributing to Parent AI Safety

Thank you for your interest in contributing to Parent AI Safety!

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/osamac2128/Parent-AI-Safety.git
   cd Parent-AI-Safety
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   ```

4. Install package in editable mode:
   ```bash
   pip install -e .
   ```

## Development Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the code standards below

3. Run tests:
   ```bash
   pytest tests/
   ```

4. Run linters:
   ```bash
   black src/ tests/
   ruff check src/ tests/
   mypy src/
   ```

5. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

6. Push and create a pull request

## Code Standards

- Follow PEP 8 style guide
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Maintain test coverage above 80%
- Keep functions focused and under 50 lines when possible
- Use descriptive variable and function names

## Testing

- Write tests for all new features
- Ensure existing tests pass
- Aim for high code coverage
- Include both unit and integration tests

## Security

- Never commit secrets, API keys, or credentials
- Validate all user inputs
- Follow OWASP security best practices
- Report security vulnerabilities privately

## Documentation

- Update README.md for user-facing changes
- Update architecture docs for design changes
- Include docstrings with examples
- Keep CLAUDE.md updated for AI assistant guidance

## Pull Request Process

1. Ensure all tests pass
2. Update documentation as needed
3. Reference related issues
4. Request review from maintainers
5. Address review feedback

## Questions?

Open an issue for questions or discussions about contributions.

---

**Last Updated**: 2025-11-23
