# copier-python-template

[Copier](https://copier.readthedocs.io/en/stable/) template for my python projects.

## Thanks to

- [KyleKing/calcipy_template](https://github.com/KyleKing/calcipy_template/).
- [Tecnativa/doodba-copier-template](https://github.com/Tecnativa/doodba-copier-template/).

<!--

FIXME: Update below.

# Install copier globally with pipx or use your preferred method
pipx install copier

# For end users, get the template with the below snippet. Replace dest_folder_name (can use ".")
copier copy gh:KyleKing/calcipy_template dest_folder_name

# Updates can be retrieved with:
copier update .

This template aims at making it easier to configure your projects that
use Docker and Python (for example, for testing) to work with Github
Actions and support a CI workflow.

It uses Copier to keep your projects updated with a unified GH Actions
structure and configuration.

## What this project adds and configures

1. Docker automated builds with Github Actions
1. Python project structure for [Pytest][https://docs.pytest.org/]
   with [Poetry][https://python-poetry.org/] (optional)

- Pre-configured tools for code formatting, quality analysis and testing:
    - [black](https://github.com/psf/black),
    - [flakehell](https://github.com/life4/flakehell)
      ([flake8](https://gitlab.com/pycqa/flake8) wrapper) and plugins,
    - [isort](https://github.com/timothycrosley/isort),
    - [mypy](https://github.com/python/mypy),
    - [safety](https://github.com/pyupio/safety)

- Tests run with [pytest](https://github.com/pytest-dev/pytest) and plugins,
  with [coverage](https://github.com/nedbat/coveragepy) support

## 1st usage

1. [Install Copier](https://copier.readthedocs.io/en/stable/#installation)
1. Enter your project folder: `cd my-project`
1. Make it a git repo: `git init`
1. Run copier `copy https://github.com/Tecnativa/image-template.git .`
1. Answer questions
1. Commit: `git commit -am 'Apply image template'`

## Quick setup and usage

Make sure all the
[requirements](https://pawamoy.github.io/copier-poetry/requirements)
are met, then:

```bash
copier "https://github.com/pawamoy/copier-poetry.git" /path/to/your/new/project
```

Or even shorter:

```bash
copier "gh:pawamoy/copier-poetry" /path/to/your/new/project
```

See the [documentation](https://pawamoy.github.io/copier-poetry)
for more details.

## Get updates

1. Enter your project folder: `cd my-project`
1. Update: `copier -a .copier-answers.image-template.yml update`
1. Answer questions, if anything changed
1. Commit: `git commit -am 'Update image template'`


<https://github.com/app-generator/copier-jinja>
<https://github.com/app-generator/copier-jinja-demo>
<https://github.com/branchvincent/python-template>
<https://github.com/Cecron/copier-python>
<https://github.com/copier-org/autopretty>
<https://github.com/eliostvs/tomate-plugin-template>
<https://github.com/maces/python-tooling-enterpy2021>
<https://github.com/NathanDeMaria/mirrorball>
<https://github.com/OCA/oca-addons-repo-template>
<https://github.com/pawamoy/copier-poetry>
<https://github.com/pawamoy/copier-pdm>
<https://github.com/pdm-project/copier-pdm>
<https://github.com/Tecnativa/doodba-copier-template>
<https://github.com/Tecnativa/image-template>
<https://github.com/ypid/debops-template>
<https://github.com/cjolowicz/cookiecutter-hypermodern-python>


https://copier.readthedocs.io/en/stable/updating/

```bash
copier copy gh:proinsias/copier-python-template .
copier update
copier -a .copier-answers.autopretty.yml update
```

-->
