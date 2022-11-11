# Python Package Demo

This minimal example covers several work practices
that have a high impact on reproducibility, productivity
and maintainability.

## Creating a Work Area

    bash$ mkdir pkgdemo
    bash$ cd pkgdemo
    bash$ git init
    Initialized empty Git repository in /home/ecashin/src/python/pkgdemo/.git/
    bash$ git checkout -b main
    Switched to a new branch 'main'
    bash$ git commit --allow-empty -m 'Initial commit'
    [main (root-commit) e26a7a9] Initial commit
    bash$ 

## Creating a Virtual Environment

    bash$ python3 -mvenv pkgdemo-venv
    bash$ . pkgdemo-venv/bin/activate
    (pkgdemo-venv) bash$ python3 -mpip install --upgrade pip
    Collecting pip
      Downloading https://files.pythonhosted.org/packages/09/bd/2410905c76ee14c62baf69e3f4aa780226c1bbfc9485731ad018e35b0cb5/pip-22.3.1-py3-none-any.whl (2.1MB)
        100% |████████████████████████████████| 2.1MB 312kB/s 
    Installing collected packages: pip
      Found existing installation: pip 8.1.1
        Uninstalling pip-8.1.1:
          Successfully uninstalled pip-8.1.1
    Successfully installed pip-22.3.1
    (pkgdemo-venv) bash$ 

## Committing Files to Git

We will ignore the use of git from here out,
although it's implied.

    (pkgdemo-venv) bash$ git add README.md 
    (pkgdemo-venv) bash$ git commit -am 'Add initial README documentation'
    [main 73a0d48] Add initial README documentation
     1 file changed, 20 insertions(+)
     create mode 100644 README.md
    (pkgdemo-venv) bash$ 

## Creating a Python Package

There have been many package-creation mechanisms
in the history of Python, leading to some confusion
and complexity.
The example below uses [setuptools](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html).

    (pkgdemo-venv) bash$ mkdir addconst

In an editor, we just created the `setuptools` configuration files
displayed below.
Please notice that there are two files.

    (pkgdemo-venv) bash$ grep -nv friendlypotato addconst/setup*
    addconst/setup.cfg:1:[metadata]
    addconst/setup.cfg:2:name = addconst
    addconst/setup.cfg:3:version = 0.1.0.dev0
    addconst/setup.cfg:4:description = Add a constant to given numbers
    addconst/setup.cfg:5:long_description = file: README.md
    addconst/setup.cfg:6:
    addconst/setup.cfg:7:[options]
    addconst/setup.cfg:8:package_dir =
    addconst/setup.cfg:9:    =src
    addconst/setup.cfg:10:packages = find:
    addconst/setup.cfg:11:python_requires = >=3.7
    addconst/setup.cfg:12:install_requires =
    addconst/setup.cfg:13:    click >=8.0,<9
    addconst/setup.cfg:14:
    addconst/setup.cfg:15:[options.packages.find]
    addconst/setup.cfg:16:where=src
    addconst/setup.cfg:17:
    addconst/setup.cfg:18:[options.extras_require]
    addconst/setup.cfg:19:tests =
    addconst/setup.cfg:20:    pytest
    addconst/setup.cfg:21:dev =
    addconst/setup.cfg:22:    black
    addconst/setup.cfg:23:    flake8
    addconst/setup.cfg:24:    ipython
    addconst/setup.cfg:25:    isort
    addconst/setup.cfg~:1:[metadata]
    addconst/setup.cfg~:2:name = 
    addconst/setup.py:1:#! /usr/bin/env python3
    addconst/setup.py:2:
    addconst/setup.py:3:from setuptools import setup
    addconst/setup.py:4:
    addconst/setup.py:5:
    addconst/setup.py:6:setup()
    (pkgdemo-venv) bash$ 

## Source Files

The sources are created now.
Note how the external `click` package is mentioned in the above config
and used in the sources via an `import`.

The first `addconst` directory is where the package is based.
The `addconst/src/addconst` directory is the one that makes it a Python package.
The `main.py` is a "driver" command that can run the code we will soon write.

    (pkgdemo-venv) bash$ mkdir addconst/src
    (pkgdemo-venv) bash$ mkdir addconst/src/addconst
    (pkgdemo-venv) bash$ grep -nv friendlypotato addconst/src/addconst/main.py 
    1:import click
    2:
    3:
    4:@click.command()
    5:def main():
    6:    print("hello")
    7:
    8:
    9:if __name__ == "__main__":
    10:    main()
    (pkgdemo-venv) bash$ 

The `__init__.py` file marks the directory as a package.
(Go figure.  Python is weird.)

    (pkgdemo-venv) bash$ touch addconst/src/addconst/__init__.py
    (pkgdemo-venv) bash$ file !$
    file addconst/src/addconst/__init__.py
    addconst/src/addconst/__init__.py: empty
    (pkgdemo-venv) bash$ 

The `addconst.py` file contains the implementation of our feature.

