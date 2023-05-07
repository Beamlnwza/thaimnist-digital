import os


def rename_02():
    """
    try to rename folder with zfill(2)
    """

    print("Rename Process")
    raw_path = os.path.abspath(os.getcwd() + "/data/raw")
    for i in os.listdir(raw_path):
        folder_path = raw_path + "/" + i
        files_path = [x for x in os.listdir(folder_path) if x.endswith(".jpg")]
        for j in files_path:
            name_no_jpg = j.split(".")[0]
            name_no_jpg = name_no_jpg.zfill(2)
            os.rename(
                folder_path + "/" + j,
                folder_path + "/" + name_no_jpg + ".jpg"
            )


if __name__ == "__main__":
    rename_02()
