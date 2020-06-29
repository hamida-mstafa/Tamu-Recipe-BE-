#Tamu Recipes

## Deployed link
https://tamu-recipes.herokuapp.com/

# Setting up your system

Make sure you already have Python3 and pipenv installed. Check that python 3.6.x is installed and pipenv:

```
python --version
Python 3.6.9

```

Install pipenv:
```
pip3 install pipenv
```

Check pipenv is installed

```

pipenv --version
pipenv, version 2018.11.26
```

## Getting started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir tamu-recipes
```

Afterwhich we go into the directory:

```
cd tamu-recipes
```

clone the project
```
git clone https://github.com/hamida-mstafa/Tamu-Recipe-BE-.git .  --> Remember the dot
```

## Testing
To test the endpoints ensure that the following tools are available the follow steps below
### Tools:
    Postman

### Commands
  The application is tested using coverage. To run the tests on the bash terminal use

     coverage run --source='.' manage.py test the-app-you-want-to-test  && coverage report
