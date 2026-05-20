# adventofcode
My Solutions for Advent of Code

## Python linting

This repository uses [Ruff](https://docs.astral.sh/ruff/) for linting, import sorting,
and formatting.

Install once:

```powershell
py -m pip install --user ruff
```

Run checks:

```powershell
py -m ruff check .
```

Automatically fix safe lint issues and format code:

```powershell
py -m ruff check . --fix
py -m ruff format .
```
