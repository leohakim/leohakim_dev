# leohakim_dev

My personal website.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Overview

`leohakim_dev` powers Leo Hakim’s personal site. It is a Django 5 application structured with Cookiecutter Django, Tailwind CSS for styling, and `uv` for Python dependency management.

## Project tour

- `leohakim_dev/`: Django apps, templates, and static assets.
- `config/settings/`: Environment-specific Django settings.
- `compose/`: Docker configurations for local and production setups.
- `docs/`: Sphinx documentation sources.
- `.envs/.local/`: Local environment variable files consumed by Docker compose services.

## Prerequisites

### Python & uv
- Install the `uv` tool (installs its own Python builds):
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Ensure Python 3.12 is available (automatically handled by `uv python install 3.12`).

### Node.js
- Node.js 20+ is required for Tailwind builds. Install via [Node Version Manager](https://github.com/nvm-sh/nvm) or your package manager.

### Docker (optional)
- Docker Desktop (or compatible engine) is only required if you want to run Mailpit via container.

## Initial setup

1. Clone the repository and enter the project directory.
2. Sync Python dependencies (creates `.venv/` automatically):
   ```bash
   uv sync --dev
   ```
3. (Optional) Activate the virtual environment if you prefer the classic workflow:
   ```bash
   source .venv/bin/activate
   ```
4. Install Node dependencies for Tailwind:
   ```bash
   npm ci
   ```

## Environment variables

Local settings live in `.envs/.local/`:

- `.envs/.local/.django` – Feature flags and local overrides.
- `leohakim_dev.db` – SQLite database tracked in the repo (safe for local development; back up before deleting).

Adjust these files as needed. Do **not** commit secrets; add new variables to the same files and keep them under version control only if they are safe.

## Running the stack locally

### 1. (Optional) Start Mailpit
```bash
docker compose -f docker-compose.local.yml up -d
```

Available helper:
- `just up` (if you have [just](https://github.com/casey/just) installed).

### 2. Apply database migrations (updates `leohakim_dev.db`)
```bash
uv run python manage.py migrate
```

### 3. Run the Django development server
```bash
uv run python manage.py runserver_plus 0.0.0.0:8000
```

Visit `http://127.0.0.1:8000`. Mailpit is exposed at `http://127.0.0.1:8045` when the container is running.

### 4. Compile Tailwind assets

- Development (watch mode):
  ```bash
  npm run tailwind:watch
  ```
- Production build:
  ```bash
  npm run tailwind:build
  ```

## Managing Python dependencies with uv

- Add a runtime dependency:
  ```bash
  uv add <package-name>
  ```
- Add a development-only dependency:
  ```bash
  uv add --group dev <package-name>
  ```
- Remove a dependency:
  ```bash
  uv remove <package-name>
  ```
- Re-sync the lockfile and virtual environment:
  ```bash
  uv sync
  ```
- Upgrade specific packages:
  ```bash
  uv lock --upgrade <package-name>
  ```

All commands run in the project folder. `uv` automatically updates `pyproject.toml` and `uv.lock`.

## Common Django commands

- Create a superuser:
  ```bash
  uv run python manage.py createsuperuser
  ```
- Load the Django shell with tab completion:
  ```bash
  uv run python manage.py shell_plus
  ```

## Quality gates

- Ruff lint & format:
  ```bash
  uv run ruff check .
  uv run ruff format .
  ```
- Type checking:
  ```bash
  uv run mypy leohakim_dev
  ```
- Tests and coverage:
  ```bash
  uv run pytest
  uv run coverage run -m pytest
  uv run coverage html
  ```
- Pre-commit hooks:
  ```bash
  uv run pre-commit install
  uv run pre-commit run --all-files
  ```

## Docker-first workflow (optional)

If you prefer to let Docker run the Django app as well, build and start the stack:

```bash
make build-local  # or: docker compose -f docker-compose.local.yml up --build
```

The Django container mounts the project directory, applies migrations against `leohakim_dev.db`, and runs `runserver_plus`. Logs can be tailed with `docker compose logs -f`.

## VPS-style production flow (web + nginx on port 8001)

This repository also includes a production layout compatible with the existing
`leohakim.dev` VPS setup:

- `production.yml` with two services: `web` (gunicorn) and `nginx`.
- `nginx` listens on container port `80` and is mapped to host `8001`.
- Static files are shared through a Docker volume.
- SQLite persists under `./db` (mounted as `/app/db` in the web container).

Steps:

1. Create `.env` from template:
   ```bash
   cp .env.example .env
   ```
2. Start production stack:
   ```bash
   docker compose -f production.yml up -d --build
   ```
   or:
   ```bash
   make run-prod
   ```

Image build/publish commands:

```bash
make xbuild
make xpublish
```

## Additional resources

- Cookiecutter Django docs: <https://cookiecutter-django.readthedocs.io/>
- uv documentation: <https://docs.astral.sh/uv/>
- Tailwind CSS docs: <https://tailwindcss.com/docs>
