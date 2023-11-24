# Contributing to Malthus

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

### Setup

This project uses [poetry](https://python-poetry.org/) for dependency management. Once poetry is installed, install the dependencies with the following:

```
poetry install
```

### Tests
The tests can be run with the following command:

```
poetry run pytest
```

### Linting
Code is formatted using the PEP8 compliant `black` package. This can be run manually with the following command

```
poetry run black malthus