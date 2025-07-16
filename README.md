# Best practices for Python projects (PyRVA July 2025)

Notes from the meeting

## Use virtual environments
- If all you have is Python, you can create a virtual environment by using:
  - `python -m venv .venv --prompt .`
- Other tools can create virtual environments like:
  - poetry
  - uv


## Package your code
Turning your code into a package changes tells Python that your project is a cohesive unit, not just a collection of files.

Doing this also means you don't have to change your PYTHON_PATH variable.

- Create a `pyproject.toml` file with at least a `[project]` and `[build-system]` table.

- Install your project into your virtual environment via: `pip install -e .`

## Use `src` folder
Putting your code into a `src` folder protects it from several classes of bugs and errors.

## Custom scripts
You can create custom command line programs that run functions in your code.

- In your `pyproject.toml` file, add a `[project.scripts]` table that connects the name of the script you want to create (on the left side) to the function you want to run (on the right). 

```
[project.scripts]
hello = 'best:cli'
```

On the right side, tell Python how to get to the function If the function you want to run is called `run_monthly_report`, and it's located at `project_root/src/shop/services/report.py`, you should write `'shop.services.report:run_monthly_report'`.

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

- Use [justfile](https://just.systems/) to document and run common commands.

- [Jeff Tripplet's justfile](https://github.com/jefftriplett/scripts-to-rule-them-all)

- https://www.youtube.com/watch?v=TiBIjouDGuI (Hynek Schlawak has a link to his justfile)

# Other topics

- [terminal colors](https://starship.rs/presets/#gruvbox-rainbow)
- [z](https://github.com/rupa/z)  (jumping around the terminalxs)

- Secure secrets and env vars
    - direnv (local env vars, auto activating venv) [Trey Hunner's [post about direnv](https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/)]
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