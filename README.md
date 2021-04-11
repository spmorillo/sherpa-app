# Sherpa App

![Actions Workflow](https://github.com/spmorillo/sherpa-app/workflows/Flask/badge.svg)

Simple flask API that add users to a database along with their postal code and city (by using [geonames](https://www.geonames.org/)).

## SETUP

Creating a virtual environment:

```bash
python3 -m venv test_env
source test_env/bin/activate
```
Installing the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Running the server:

```bash
export set FLASK_APP=sherpa_app.webapp
python -m flask run
```

Running the tests:

```bash
python -m pytest
```

## REQUIREMENTS

Python >= 3.7

## NEXT STEPS

1. Better DB implementation
2. More tests
3. Docker container

## LICENSE

[MIT](http://www.opensource.org/licenses/mit-license.html)
