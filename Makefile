.PHONY: docs
docs:
	@echo "Starting MkDocs local server..."
	@uv sync && uv run mkdocs serve --livereload

.PHONY: build
build:
	@echo "Building static site..."
	@uv sync && uv run mkdocs build

.PHONY: deploy
deploy:
	@echo "Deploying to GitHub Pages..."
	@uv sync && uv run mkdocs gh-deploy

.PHONY: clean
clean:
	@echo "Cleaning build artifacts..."
	@rm -rf site/
	@rm -rf .venv/
	@rm -rf .cache/

.PHONY: install
install:
	@echo "Installing dependencies..."
	@uv sync

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make docs    - Start local MkDocs server for development"
	@echo "  make build   - Build static site to site/ directory"
	@echo "  make deploy  - Deploy site to GitHub Pages"
	@echo "  make install - Install dependencies in virtual environment"
	@echo "  make clean   - Remove build artifacts and virtual environment"
