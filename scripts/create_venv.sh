#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

git clone git@github.com:githubharald/CTCDecoder.git
cd CTCDecoder/
pip install .
cd ..
rm -rf CTCDecoder/
