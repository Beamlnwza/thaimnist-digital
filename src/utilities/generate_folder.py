import os


def generate_folder():
    output_path = os.path.join(os.getcwd(), "data", "rawtest")
    for i in range(0, 44):
        path = os.path.join(output_path, "{:02d}".format(i))
        if not os.path.exists(path):
            os.makedirs(path)


if __name__ == "__main__":
    generate_folder()
