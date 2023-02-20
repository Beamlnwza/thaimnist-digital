import os

folder_num = 0
path = os.path.join(os.getcwd(), "data", "raw", str(folder_num))

i = 0
for file in os.listdir(path):
    new_file_name = i
    os.rename(os.path.join(path, file), os.path.join(path, str(new_file_name) + ".jpg"))
    i = i + 1