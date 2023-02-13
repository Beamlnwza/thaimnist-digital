import cv2
import numpy as np
import os
import random

store_unit = os.path.join(os.getcwd(), "data", "raw")


# Define the size of the image
dimision = random.randint(50, 100)
img_size = (dimision, dimision)

# Define the list of alphabets to be drawn
alphabet_range = 2
--alphabet_range
alphabet = list(range(0, alphabet_range))
alphabets = [str(x) for x in alphabet]
# alphabets = ['1']

# Random brush size
brush_size = 4

# Function to handle mouse events
def draw_circle(event, x, y, flags, param):
    global prev_x, prev_y
    if event == cv2.EVENT_LBUTTONDOWN:
        prev_x, prev_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
        cv2.line(img, (prev_x, prev_y), (x, y), (0, 0, 0), brush_size)
        prev_x, prev_y = x, y

# Loop through the list of alphabets
for alphabet in alphabets:
    path = os.path.join(store_unit, alphabet)
    # Initialize the image with white color
    img = 255 * np.ones(img_size + (3,), dtype=np.uint8)

    # Create a window for drawing
    window_text = alphabet + " - " + str(img_size)
    cv2.namedWindow(alphabet, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(alphabet, 600, 600)

    # Bind the function to the window
    cv2.setMouseCallback(alphabet, draw_circle)

    # Loop until user presses 'q'
    while True:
        cv2.imshow(alphabet, img)
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

    # Check if the directory for the alphabet exists, and create it if it doesn't
    if not os.path.exists(path):
        os.makedirs(path)

    # Resize the image to 28x28
    img = cv2.resize(img, (28, 28))
    
    # Program to make find lastest and set numbers to that number
    num_path = os.path.join(store_unit, alphabet)
    lastest_number = str(len(os.listdir(num_path)))
    print(lastest_number)
    
    # Save the image to the directory
    # print(os.path.join(path, alphabet + ".jpg"))
    cv2.imwrite(os.path.join(num_path , lastest_number + ".jpg"), img)

    # Destroy the window
    cv2.destroyAllWindows()