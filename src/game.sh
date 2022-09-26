#!/bin/bash
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 main.py
    else
        echo "Please update your Python application the version 3." >&2
    fi 
else
    echo "Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://www.python.org/downloads/" >&2
fi