import os
import shutil

path = os.path.join(os.getcwd(), "data", "raw")


def remove_last_file(folder_path):
    range = len(os.listdir(folder_path))

    os.remove(os.path.join(folder_path, str(range - 1) + ".jpg"))


for i in range(0, 44):
    folder_path = os.path.join(path, str(i))
    remove_last_file(folder_path)
