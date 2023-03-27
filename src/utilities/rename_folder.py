import os


def rename_folder():
    print("rename folder in process")
    path = os.path.join(os.getcwd(), "data", "raw")
    for i in os.listdir(path):
        os.rename(os.path.join(path, i), os.path.join(path, i.zfill(2)))


def rename_files():
    print("rename files in process")
    path = os.path.join(os.getcwd(), "data", "raw")
    for i in os.listdir(path):
        for j in os.listdir(os.path.join(path, i)):
            os.rename(os.path.join(path, i, j), os.path.join(path, i, j.zfill(5)))


if __name__ == "__main__":
    rename_files()
