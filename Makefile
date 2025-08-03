.PHONY: run lint format check test install

# Run the FastAPI app in development
run:
	poetry run uvicorn trader_tip.main:app --reload --app-dir src

# Install dependencies
install:
	poetry install

# Lint with Ruff
lint:
	poetry run ruff check src

# Auto-fix lint issues
fix:
	poetry run ruff check src --fix

# Format with Black
format:
	poetry run black src

# Check code formatting without changing
check:
	poetry run black --check src

# Run tests
test:
	poetry run pytest -v
