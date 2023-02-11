import os

import torch
from torch.utils.data import Dataset
from PIL import Image


class CaptchaDataset(Dataset):
    TEST_PATH = "data/test"
    TRAIN_PATH = "data/train"

    def __init__(self, is_train, transform=None, target_transform=None):
        self.__is_train = is_train

        self.__paths_to_image = []
        self.__targets = []
        root_dir = CaptchaDataset.TRAIN_PATH if self.__is_train \
            else CaptchaDataset.TEST_PATH
        for file_name in os.listdir(root_dir):
            file_path = os.path.join(root_dir, file_name)
            if not os.path.isfile(file_path) or not file_name.endswith(".png"):
                continue

            self.__paths_to_image.append(file_path)
            self.__targets.append(file_name.split(".")[0])

        self.__transform = transform
        self.__target_transform = target_transform

    def __len__(self):
        return len(self.__paths_to_image)

    def __getitem__(self, index):
        image, target = self.__paths_to_image[index],  self.__targets[index]

        image = Image.open(image)
        image = image.convert("RGB")

        if self.__transform is not None:
            image = self.__transform(image)

        if self.__target_transform is not None:
            target = self.__target_transform(target)
            target = target.type(torch.int32)

        return image, target
