# Best practices for Python projects (PyRVA July 2025)

## virtual environment
- python -m venv .venv --prompt .

## Package your code
- `pip install -e .`

## Use `src` folder

## Custom scripts

## Organize your code

```
project_root/
  .venv/
  data/
    00_raw/
    01_processed/
    (look at Kedro)
    ...
  dags/
  docs/
  notebooks/
  reports/
  scripts/
  src/
    project_name/
  tests/
  pyproject.toml
  README.md
```

# One script to rule them all

- Justfile

- https://www.youtube.com/watch?v=TiBIjouDGuI (Hynek Schlawak has a link to his justfile)

# Other topics

- [terminal colors](https://starship.rs/presets/#gruvbox-rainbow)
- [z](https://github.com/rupa/z)  (jumping around the terminalxs)

- Secure secrets and env vars
    - direnv (local env vars, auto activating venv)
    - omegaconf
    - 

- Windows Subsystem for Linux
- Dev containers

## Formatter & linter
- black (formatter)
- flake8 (linter)
- ruff (both)

## other tools
- pre-commit

## Dependencies
- `pip-tools`
- `uv`
- `poetry`

- Adam Johnson pre-commit with uv blog post