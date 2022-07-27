#!/bin/bash

# remove old packages
rm -rf build
rm -rf dist
rm -rf *.egg-info

# build new packages
python3 setup.py sdist bdist_wheel

# push to pypi
python3 -m twine upload dist/*
