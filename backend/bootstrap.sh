#!/bin/bash

export FLASK_APP=./src/main.py
source $(pipenv --venv)/bin/activate
flash run -h 0.0.0.0