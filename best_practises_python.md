# Python Best Practises

Here we define the standards and best practices we follow when developing Python projects.

## 1. Repository Layout - Top-Level Directories

Source: [Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)

## 2. Style

Source: [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## 3. Quality Ensurance Tools

### a) Formatter

- [black - uncompromising Python code formatter](https://github.com/psf/black)
- [docformatter - formats docstrings to follow PEP 257](https://github.com/PyCQA/docformatter)
- [isort - a Python utility / library to sort imports](https://github.com/PyCQA/isort)

### b) Static Code Analyser

- [Bandit - a tool designed to find common security issues in Python code](https://github.com/PyCQA/bandit)
- [Flake8 - a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code](https://github.com/pycqa/flake8)
  - includes: [mccabe - complexity checker for Python](https://github.com/PyCQA/mccabe)
  - includes: [pycodestyle - a simple Python style checker in one Python file](https://github.com/PyCQA/pycodestyle)
  - includes: [pyflakes - a simple program which checks Python source files for errors](https://github.com/PyCQA/pyflakes)
  - includes: [radon - various code metrics for Python code](https://github.com/rubik/radon)
- [Pylint - it's not just a linter that annoys you](https://github.com/PyCQA/pylint/)
- [mypy - optional static typing for Python](https://github.com/python/mypy)
- [pydocstyle - docstring style checker](https://github.com/PyCQA/pydocstyle)

### c) Testing Frameworks

- [pytest - the pytest framework makes it easy to write small tests, yet scales to support complex functional testing](https://github.com/pytest-dev/pytest/)
- [pytest-cov - coverage plugin for pytest](https://github.com/pytest-dev/pytest-cov)
- [pytest-deadfixtures - plugin to list unused fixtures in your tests](https://github.com/jllorencetti/pytest-deadfixtures)
- [pytest-helpers-namespace - enables you to register helper functions in your conftest.py](https://github.com/saltstack/pytest-helpers-namespace)
- [pytest-random-order - pytest plugin to randomise the order of tests with some control over the randomness](https://github.com/jbasko/pytest-random-order)

### d) Documentation

- [Material for MkDocs - a material design theme for MkDocs](https://github.com/mkdocs/mkdocs/)
- [MkDocs - project documentation with Markdown](https://github.com/mkdocs/mkdocs/)
- [mkdocs-autoref - Automatically link across pages in MkDoc](https://github.com/mkdocstrings/autorefs/)
- [mkdocstrings - automatic documentation from sources for MkDocs](https://github.com/mkdocstrings/mkdocstrings)
- [mkdocstrings-python - a Python handler for mkdocstrings](https://github.com/mkdocstrings/python)

### e) Miscellaneous

- [pipenv - Python development workflow for humans](https://github.com/pypa/pipenv)
- [python-coveralls - Python API for http://coveralls.io](https://github.com/z4r/python-coveralls)

## 4. Resources

### a) Books

- Lott, Steven F., "Functional Python Programming", 2. Edition, Packt Publishing, 2018, in `docs/books/functional_python_programming.pdf`
