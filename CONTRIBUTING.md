# Contributing to Habit Tracker

This guide will help you understand our workflow and how to contribute effectively.

## Table of Contents

- [Branching Strategy](#branching-strategy)
- [Workflow Overview](#workflow-overview)
- [Step-by-Step Guide](#step-by-step-guide)
- [Code Review Process](#code-review-process)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)

---

## Branching Strategy

We follow a **three-stage Git workflow** to ensure code quality and stability:

```
Feature Branches → Develop → Main
(individual work)  (integration/testing)  (production)
```

### Branch Purposes

- **`main`** - Production-ready code. Always stable and deployable.
- **`develop`** - Integration branch for testing features before production.
- **`feat/*`** - Individual feature branches for development work.

---

## Workflow Overview

### 1. Feature Development
- Create feature branches from `develop`
- Work on your assigned user story
- Commit changes regularly with clear messages

### 2. Integration & Testing
- Merge features into `develop` via Pull Request
- Run tests and verify integration
- Fix any issues before merging to main

### 3. Production Release
- Merge `develop` into `main` when ready for release
- Tag releases appropriately
- Deploy to production

---

## Step-by-Step Guide

### Starting a New Feature

1. **Ensure you're on the latest develop branch:**
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Create a new feature branch:**
   ```bash
   git checkout -b feat/US-XX-feature-name
   ```

   **Naming Convention:**
   - Use `feat/US-XX-` prefix where XX is the user story number
   - Use descriptive kebab-case names
   - Examples:
     - `feat/US-01-user-login`
     - `feat/US-02-add-habit`
     - `feat/US-03-habit-categories`

3. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "feat(US-XX): Brief description of changes"
   ```

   **Commit Message Format:**
   - `feat(US-XX): Add new feature`
   - `fix(US-XX): Fix bug description`
   - `test(US-XX): Add tests for feature`
   - `docs: Update documentation`
   - `refactor: Code refactoring`

4. **Push your feature branch:**
   ```bash
   git push -u origin feat/US-XX-feature-name
   ```

### Creating a Pull Request

1. **Push your changes to GitHub**

2. **Create Pull Request:**
   - Go to GitHub repository
   - Click "New Pull Request"
   - Set base branch to `develop`
   - Set compare branch to your `feat/US-XX-feature-name`
   - Fill out PR template with:
     - Description of changes
     - Related user story
     - Testing performed
     - Screenshots (if UI changes)

3. **Request Review:**
   - Assign at least one team member as reviewer
   - Address any review comments
   - Make requested changes if needed

4. **Merge:**
   - Once approved, merge into `develop`
   - Delete the feature branch after merging

### Merging to Production

When `develop` is stable and ready for release:

1. **Create Pull Request from `develop` to `main`:**
   ```bash
   # Ensure develop is up to date
   git checkout develop
   git pull origin develop
   ```

2. **Create PR on GitHub:**
   - Base: `main`
   - Compare: `develop`
   - Get team approval
   - Run final tests

3. **Merge and Tag:**
   - Merge to `main`
   - Create release tag (e.g., `v1.0.0`)

---

## Code Review Process

### For Authors:
- Ensure all tests pass before requesting review
- Keep PRs small and focused (one feature/fix per PR)
- Respond to feedback promptly
- Update your branch if conflicts arise

### For Reviewers:
- Review code within 24 hours
- Check for:
  - Code quality and readability
  - Test coverage
  - Documentation updates
  - No breaking changes
- Provide constructive feedback
- Approve only when satisfied

---

## Coding Standards

### Python Style Guide
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Example:
```python
def calculate_habit_streak(user_id: int, habit_id: int) -> int:
    """
    Calculate the current streak for a user's habit.

    Args:
        user_id: The user's ID
        habit_id: The habit's ID

    Returns:
        The current streak count in days
    """
    # Implementation here
    pass
```

### File Organization
- Keep models in `models/`
- Keep routes in appropriate route files
- Keep templates in `templates/`
- Keep tests in `tests/`

---

## Testing Requirements

### Before Submitting PR:

1. **Run all tests:**
   ```bash
   uv run pytest -v
   ```

2. **Write tests for new features:**
   - Unit tests for new functions
   - Integration tests for new routes
   - Aim for >80% code coverage

3. **Test manually:**
   - Run the app locally
   - Test the feature end-to-end
   - Check for edge cases

### Test Structure:
```python
def test_feature_name():
    """Test description of what is being tested."""
    # Arrange
    # Act
    # Assert
    pass
```

---

## Getting Help

- Ask questions in team meetings (Wed 5-6 PM or Sat 9-10 PM)
- Create a GitHub Issue for bugs or feature discussions
- Reach out to team members on Teams

---

## Summary Commands

```bash
# Start new feature
git checkout develop
git pull origin develop
git checkout -b feat/US-XX-feature-name

# Make changes and commit
git add .
git commit -m "feat(US-XX): Description"
git push -u origin feat/US-XX-feature-name

# Create PR on GitHub: feat/US-XX-feature-name → develop

# After PR is merged, update your local develop
git checkout develop
git pull origin develop
git branch -d feat/US-XX-feature-name
```

---

**Happy Coding! 🚀**