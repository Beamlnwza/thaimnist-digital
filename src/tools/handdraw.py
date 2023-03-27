# create class for handdraw
import cv2
import random
import os
import numpy as np


class Handdraw:
    def __init__(
        self, brush_size=2, alphabet_class=44, dimension=random.randint(50, 100)
    ) -> None:
        self.dimension = dimension
        self.img_dimension = (self.dimension, self.dimension)

        self.alphabet_class = alphabet_class
        self.alphabet_folder = self.get_alphabet_folder

        self.brush_size = brush_size
        self.canva = 255 * np.ones(self.img_dimension + (3,), dtype=np.uint8)

        self.example_size = 42
        self.example_path = os.path.join(
            os.getcwd(), "src", "tools", "alphabet_example.jpg"
        )

        self.output_path = os.path.join(os.getcwd(), "data", "rawtest")
        self.output_size = (28, 28)
        self.output_canva = ""

        self.windows_titles = "Alphabets"
        pass

    @property
    def get_alphabet_folder(self):
        """
        get folder alphabet name and turn it to list
        """
        alphabet_folder = [
            "{:02d}".format(i) for i in range(0, self.alphabet_class - 1)
        ]

        return alphabet_folder

    def get_info(self):
        """
        get all basic info
        """

        print("Alphabet class: ", self.alphabet_class)
        print("Alphabet folder: ", self.alphabet_folder)
        print("Image dimension: ", self.img_dimension)
        print("Brush size: ", self.brush_size)
        print("Output path: ", self.output_path)
        print("Output size: ", self.output_size)
        print("Example path: ", self.example_path)
        print("Example size: ", self.example_size)

    def startpoints(self, nums):
        """
        get starting points for rectangle inside example pictures
        if more than 8 return to 1
        """
        x = nums % 8 * self.example_size
        y = self.example_size * (nums // 8)
        return (x, y)

    def endpoints(self, nums):
        """
        get ending points for rectangle inside example pictures
        if more than 8 go to next lines
        """
        return ((nums % 8) + 1) * self.example_size, self.example_size * (
            (nums // 8) + 1
        )

    def setCanva(self, canva):
        self.canva = canva

    @staticmethod
    def get_lastest_number(path) -> str:
        """
        get last number by count all items and return
        if that path is not exisits then 0
        """
        if not os.path.exists(path):
            lastest_number = "0"
        else:
            lastest_number = str(len(os.listdir(path)))

        # format lastest_number to 5 digits
        lastest_number = "{:05d}".format(int(lastest_number))
        return str(lastest_number)

    @classmethod
    def draw_circle(self, event, x, y, flags, param):
        global prev_x, prev_y
        if event == cv2.EVENT_LBUTTONDOWN:
            prev_x, prev_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(self.canva, (prev_x, prev_y), (x, y), (0, 0, 0), self.brush_size)
            prev_x, prev_y = x, y

    def initial_canva(self, alphabet):
        store_path = os.path.join(self.output_path, alphabet)
        lastest_number = self.get_lastest_number(store_path)
        window_titles = "Alphabets " + alphabet
        return store_path, lastest_number, window_titles

    def getWindows_titles(self) -> str:
        titles = self.alphabet_class + " " + self.img_dimension + " " + self.brush_size
        return titles

    def update_example(self, alphabet, lastest_number):
        print("update_example")

    def reset_canva(self):
        return 255 * np.ones(self.img_dimension + (3,), dtype=np.uint8)

    def set_cv2(self, window_titles, main_window):
        cv2.namedWindow(main_window, cv2.WINDOW_GUI_EXPANDED)
        cv2.resizeWindow(main_window, 800, 800)
        cv2.setWindowTitle(main_window, window_titles)
        cv2.moveWindow(main_window, 450, 75)
        cv2.setMouseCallback(main_window, self.draw_circle)

    def save_canva(self, store_path, lastest_number):
        self.output_canva = cv2.resize(self.canva, self.output_size)

        if np.mean(self.output_canva) == 255:
            return

        cv2.imwrite(
            os.path.join(store_path, lastest_number + ".jpg"), self.output_canva
        )

    def start_draw(self) -> None:
        for index, alphabet in enumerate(self.alphabet_folder):

            store_path, lastest_number, window_titles = self.initial_canva(alphabet)

            img_example = self.initial_example(index)

            main_window = alphabet

            self.set_cv2(window_titles, main_window)

            while True:
                cv2.imshow(main_window, self.canva)
                cv2.imshow("Example", img_example)

                if cv2.waitKey(20) & 0xFF == ord("q"):
                    break

            self.save_canva(store_path, lastest_number)
            self.canva = self.reset_canva()
            cv2.destroyAllWindows()

    def initial_example(self, index):
        img_example = cv2.imread(self.example_path)
        cv2.rectangle(
            img_example,
            self.startpoints(index),
            self.endpoints(index),
            (0, 0, 255),
            2,
        )

        return img_example

    def test(self):
        print("test")


if __name__ == "__main__":
    handdraw = Handdraw(dimension=50)
    handdraw.get_info()
    handdraw.start_draw()
    pass
