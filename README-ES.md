# leohakim_dev

Mi sitio web personal.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Resumen

`leohakim_dev` impulsa el sitio personal de Leo Hakim. Es una aplicación Django 5 estructurada con Cookiecutter Django, Tailwind CSS para estilos y `uv` para la gestión de dependencias de Python.

## Recorrido por el proyecto

- `leohakim_dev/`: aplicaciones Django, plantillas y assets estáticos.
- `config/settings/`: configuraciones de Django por entorno.
- `compose/`: configuraciones Docker para entornos local y producción.
- `docs/`: fuentes de documentación Sphinx.
- `.envs/.local/`: archivos de variables de entorno usados por los servicios de Docker Compose.

## Prerrequisitos

### Python y uv
- Instala la herramienta `uv` (gestiona sus propios builds de Python):
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Asegúrate de tener Python 3.12 disponible (lo maneja automáticamente `uv python install 3.12`).

### Node.js
- Node.js 20+ es necesario para compilar Tailwind. Instálalo mediante [Node Version Manager](https://github.com/nvm-sh/nvm) o tu gestor de paquetes.

### Docker (opcional)
- Docker Desktop (o motor compatible) solo es necesario si quieres ejecutar Mailpit mediante contenedor.

## Configuración inicial

1. Clona el repositorio y entra al directorio del proyecto.
2. Sincroniza las dependencias de Python (crea `.venv/` automáticamente):
   ```bash
   uv sync --dev
   ```
3. (Opcional) Activa el entorno virtual si prefieres el flujo clásico:
   ```bash
   source .venv/bin/activate
   ```
4. Instala las dependencias Node para Tailwind:
   ```bash
   npm ci
   ```

## Variables de entorno

Las configuraciones locales viven en `.envs/.local/`:

- `.envs/.local/.django` – Flags y overrides locales.
- `leohakim_dev.db` – Base SQLite versionada (útil para desarrollo; respáldala antes de eliminarla).

Ajusta estos archivos según sea necesario. No compartas secretos: añade nuevas variables en los mismos archivos y mantenlos bajo control de versiones solo si son seguras.

## Ejecución local del stack

### 1. (Opcional) Inicia Mailpit
```bash
docker compose -f docker-compose.local.yml up -d
```

Atajo disponible:
- `just up` (si tienes [just](https://github.com/casey/just) instalado).

### 2. Aplica migraciones de base de datos (actualiza `leohakim_dev.db`)
```bash
uv run python manage.py migrate
```
o
```bash
just migrate
```

### 3. Ejecuta el servidor de desarrollo de Django
```bash
uv run python manage.py runserver_plus 0.0.0.0:8020
```
o
```bash
just dev
```

Visita `http://127.0.0.1:8020`. Mailpit está expuesto en `http://127.0.0.1:8045` cuando el contenedor está activo.

### 4. Compila los assets de Tailwind

- Desarrollo (watch mode):
  ```bash
  npm run tailwind:watch
  ```
- Build de producción:
  ```bash
  npm run tailwind:build
  ```

## Gestión de dependencias Python con uv

- Añadir una dependencia de runtime:
  ```bash
  uv add <nombre-paquete>
  ```
- Añadir una dependencia solo de desarrollo:
  ```bash
  uv add --group dev <nombre-paquete>
  ```
- Eliminar una dependencia:
  ```bash
  uv remove <nombre-paquete>
  ```
- Resincronizar el lockfile y el entorno virtual:
  ```bash
  uv sync
  ```
- Actualizar paquetes específicos:
  ```bash
  uv lock --upgrade <nombre-paquete>
  ```

Todos los comandos se ejecutan en la carpeta del proyecto. `uv` actualiza `pyproject.toml` y `uv.lock` automáticamente.

## Comandos habituales de Django

- Crear un superusuario:
  ```bash
  uv run python manage.py createsuperuser
  ```
- Abrir la shell de Django con autocompletado:
  ```bash
  uv run python manage.py shell_plus
  ```

## Validaciones de calidad

- Lint y formato con Ruff:
  ```bash
  uv run ruff check .
  uv run ruff format .
  ```
- Comprobación de tipos:
  ```bash
  uv run mypy leohakim_dev
  ```
- Tests y coverage:
  ```bash
  uv run pytest
  uv run coverage run -m pytest
  uv run coverage html
  ```
- Hooks de pre-commit:
  ```bash
  uv run pre-commit install
  uv run pre-commit run --all-files
  ```

## Flujo con Docker (opcional)

Si prefieres que Docker ejecute también Django, construye e inicia el stack:

```bash
make build-local  # o: docker compose -f docker-compose.local.yml up --build
```

El contenedor de Django monta el proyecto, aplica migraciones contra `leohakim_dev.db` y levanta `runserver_plus`. Puedes seguir los logs con `docker compose logs -f`.

## Recursos adicionales

- Documentación de Cookiecutter Django: <https://cookiecutter-django.readthedocs.io/>
- Documentación de uv: <https://docs.astral.sh/uv/>
- Documentación de Tailwind CSS: <https://tailwindcss.com/docs>
