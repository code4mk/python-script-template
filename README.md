# python-script-template

A batteries-included Python script boilerplate for quickly spinning up new projects.

## Features

- **Environment management** -- layered `.env` / `.env.local` loading via `python-dotenv` + `pydantic-settings`
- **HTTP client** -- unified sync/async wrapper around `httpx` (`common/httpx_client.py`)
- **Typed settings** -- validated config with sensible defaults (`config/settings.py`)
- **Data directories** -- `data/input/` and `data/output/` ready for file I/O scripts

## Project Structure

```
.
├── main.py                  # Entry point
├── config/
│   └── settings.py          # Pydantic-based settings (reads from .env)
├── common/
│   ├── dot_env_loader.py    # Layered .env loader
│   └── httpx_client.py      # Sync/async HTTP client wrapper
├── scripts/                 # Standalone helper scripts
├── data/
│   ├── input/               # Raw / source data
│   └── output/              # Generated / processed data
├── _docs/                   # Internal documentation
├── .env.example             # Template for environment variables
└── pyproject.toml           # Project metadata & dependencies (uv)
```

## Quick Start

```bash
# 1. Clone / use as template
gh repo create my-script --template code4mk/python-script-template
cd my-script

# 2. Install dependencies (requires uv)
uv sync

# 3. Set up environment variables
cp .env.example .env
# edit .env with your values

# 4. Run
uv run python main.py
```

## Configuration

Environment variables are loaded in order:

1. `.env` -- base config
2. `.env.local` -- local overrides (gitignored)

Define your own settings in `config/settings.py` and access them anywhere:

```python
from config.settings import settings

print(settings.db_host)
```

See `_docs/` for detailed documentation on included utilities.

## License

MIT
