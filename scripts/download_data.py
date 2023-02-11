#!.venv/bin/python

import os
import gdown
import zipfile

DATA_URL = "https://drive.google.com/uc?id=1gArBjHa9W2mxgoewTdAWSgLcdzKRp0wn"
DATA_PATH = "data/"
ZIP_PATH = "data/captcha_samples.zip"

if __name__ == "__main__":
    gdown.download(DATA_URL, ZIP_PATH, quiet=True)
    with zipfile.ZipFile(ZIP_PATH, "r") as zipper:
        zipper.extractall(DATA_PATH)
    os.remove(ZIP_PATH)
