import os

folder_num = 1
path = os.path.join(os.getcwd(), "data", "raw", str(folder_num))

for file in os.listdir(path):
    file_name = file.split(".")[0]
    file_ext = file.split(".")[1]
    new_file_name = file_name + "_1" + "." + file_ext
    os.rename(os.path.join(path, file), os.path.join(path, new_file_name))