#!.venv/bin/python

import os
import gdown
import zipfile
import shutil
import random

DATA_URL = "https://drive.google.com/uc?id=1gArBjHa9W2mxgoewTdAWSgLcdzKRp0wn"
DATA_PATH = "data"
DATA_FOLDER = "captcha_samples"
TEST_FOLDER = "test"
TRAIN_FOLDER = "train"
ZIP_FILE_NAME = "captcha_samples.zip"

if __name__ == "__main__":
    zip_path = os.path.join(DATA_PATH, ZIP_FILE_NAME)
    gdown.download(DATA_URL, zip_path, quiet=True)

    with zipfile.ZipFile(zip_path, "r") as zipper:
        zipper.extractall(DATA_PATH)

    os.remove(zip_path)

    files = []
    data_folder_path = os.path.join(DATA_PATH, DATA_FOLDER)
    for file_name in os.listdir(data_folder_path):
        file_path = os.path.join(data_folder_path, file_name)
        if not os.path.isfile(file_path) or not file_name.endswith(".png"):
            continue

        files.append((file_name, file_path))

    random.shuffle(files)

    test_len = int(len(files) / 5)
    test_files = files[:test_len]
    train_files = files[test_len:]

    assert len(test_files) + len(train_files) == len(files)

    test_data_path = os.path.join(DATA_PATH, TEST_FOLDER)
    if not os.path.exists(test_data_path):
        os.mkdir(test_data_path)
    for file in test_files:
        shutil.move(file[1], os.path.join(test_data_path, file[0]))

    train_data_path = os.path.join(DATA_PATH, TRAIN_FOLDER)
    if not os.path.exists(train_data_path):
        os.mkdir(train_data_path)
    for file in train_files:
        shutil.move(file[1], os.path.join(train_data_path, file[0]))

    shutil.rmtree(data_folder_path)
