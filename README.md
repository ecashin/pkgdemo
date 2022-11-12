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
Please notice that there are two files
displayed below using the UNIX numbered listing command, `nl`.

    (pkgdemo-venv) bash$ nl -b a addconst/setup.cfg
     1  [metadata]
     2  name = addconst
     3  version = 0.1.0.dev0
     4  description = Add a constant to given numbers
     5  long_description = file: README.md
     6
     7  [options]
     8  package_dir =
     9      =src
    10  packages = find:
    11  python_requires = >=3.6
    12  install_requires =
    13      click >=8.0,<9
    14
    15  [options.packages.find]
    16  where=src
    17
    18  [options.extras_require]
    19  tests =
    20      pytest
    21  dev =
    22      black
    23      flake8
    24      ipython
    25      isort
    (pkgdemo-venv) bash$

And `setup.py` has to be there but has little in it.

    (pkgdemo-venv) bash$ nl -b a addconst/setup.py
         1  #! /usr/bin/env python3
         2
         3  from setuptools import setup
         4
         5
         6  setup()
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

    (pkgdemo-venv) bash$ pwd
    /home/ecashin/src/python/pkgdemo/addconst
    (pkgdemo-venv) bash$ grep -nv friendlypotato src/addconst/addconst.py 
    1:class ConstAdder:
    2:    def __init__(self, *, constant):
    3:        self.constant = constant
    4:
    5:    def __call__(self, n):
    6:        return n + self.constant
    (pkgdemo-venv) bash$ 

## Installing Editable Package

By installing the package as "editable" with the `-e` option,
we can go on changing the sources and having the changes
take effect immediately.

The command below has much output that is omitted.

    (pkgdemo-venv) bash$ python3 -mpip install -e .[dev,tests]

## Checking the Sources

Now that the package installation has added dependencies
to the virtual environment,
we can run the linters.
Because Python's support for static type checking is recent and optional,
these are essential tools,
worth reading about and mastering.

In our case, there are no problems detected.

    (pkgdemo-venv) bash$ black src/*/*.py
    All done!
    3 files left unchanged.
    (pkgdemo-venv) bash$ flake8 src/*/*.py
    (pkgdemo-venv) bash$ 

## Testing the Sources

A test can be created in a new `tests` subdirectory,
where pytest will find it.
You can see here that we import our package
just as if it was something from a third-party software provider.

    (pkgdemo-venv) bash$ pwd
    /home/ecashin/src/python/pkgdemo/addconst
    (pkgdemo-venv) bash$ black src/*/*.py tests/*.py; flake8 src/*/*.py tests/*.py
    All done!
    4 files left unchanged.
    (pkgdemo-venv) bash$ grep -nv friendlypotato tests/test_addconst.py
    1:from addconst.addconst import ConstAdder
    2:
    3:
    4:def test_addconst():
    5:    add1 = ConstAdder(constant=1)
    6:    assert add1(2) == 3
    7:    assert add1(-1) == 0
    8:    add2 = ConstAdder(constant=2)
    9:    assert add2(2) == 4
    10:    assert add2(-20) == -18
    (pkgdemo-venv) bash$ 
    (pkgdemo-venv) bash$ pytest
    ====================================================== test session starts =======================================================
    platform linux -- Python 3.6.9, pytest-7.0.1, pluggy-1.0.0
    rootdir: /home/ecashin/src/python/pkgdemo/addconst
    collected 1 item                                                                                                                 
    
    tests/test_addconst.py .                                                                                                   [100%]
    
    ======================================================= 1 passed in 0.02s ========================================================
    (pkgdemo-venv) bash$ 

## Using Third-Party Packages

The `main.py` driver uses `click` already.
It makes command-line arguments and options easier to deal with.

Let's try it.

    (pkgdemo-venv) bash$ python3 src/addconst/main.py
    hello
    (pkgdemo-venv) bash$ 
    
