# Panaderno Chema
Panadero Chema is a simplistic Python project creation tool that guarantees that you have a defined structure (and testing!).

There are many Python Cookie cutters... but this is mine ¯\\_(ツ)_/¯  

## Scaffolding a new project
The main binary (well 'binary') is 'amasa' and works this way:

```bash
# Generic Syntax
./amasa <PROJECT_PATH> <PROJECT_NAME>

# Example (will create Python project called 'harina'
# on $HOME/Projects/harina/
./amasa $HOME/Projects harina

# Projet now lives on $HOME/Projects/harina
```

**Note:** _amasa-osx_ requires OSX to have gnu utils (gsed and gfind).

Once the project is created it will run _tox_ to show that testing is working (because you SHOULD DO unit testing).
