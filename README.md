![Tests Status](https://github.com/kabute/panadero/workflows/Panadero%20Tests/badge.svg)
# Panaderno Chema
Panadero Chema is a opinionated and simplistic Python project creation tool that guarantees that you have a defined structure (and testing!).

There are many Python Cookie cutters... but this is mine ¯\\_(ツ)_/¯  

## Pre-requirements
Panadero Chema requires some Python packages (please note that only Python 3.X is supported) to bootstrap the project (but any other package will be in a virtual environment), so please install first:
```bash
pip install virtualenv
```

## Scaffolding a new project
The main script  is 'amasa' and works this way:

```bash
# Generic Syntax
./amasa <PROJECT_PATH> <PROJECT_NAME>

# Example (will create Python project called 'harina'
# on $HOME/Projects/harina/
./amasa $HOME/Projects harina

# Projet now lives on $HOME/Projects/harina
```

**Note:** OSX requires gnu utils (gsed and gfind).
```bash
brew install gnu-sed
brew install gnu-find
```

Once the project is created it will run _tox_ to show that testing is working (because you SHOULD DO unit testing).
