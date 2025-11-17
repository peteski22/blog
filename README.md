# Technical Blog

Private repository for technical blog posts.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Modern Python package installer

## Local Development

Start the local development server:

```bash
make docs
```

Visit http://localhost:8000

## Available Commands

```bash
make docs    # Start local MkDocs server for development
make build   # Build static site to site/ directory
make deploy  # Deploy site to GitHub Pages
make install # Install dependencies
make clean   # Remove build artifacts and virtual environment
make help    # Show available commands
```

## Deploy to GitHub Pages

When ready to publish:

```bash
make deploy
```
