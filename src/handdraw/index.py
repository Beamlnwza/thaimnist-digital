import cv2
import numpy as np
import os

store_unit = os.path.join(os.getcwd(), 'data', 'preps')


# Define the size of the image
dimision = 100
img_size = (dimision, dimision)

# Define the list of alphabets to be drawn
alphabet_range = 2
alphabet = list(range(0, alphabet_range))
alphabets = [str(x) for x in alphabet]

# Function to handle mouse events
def draw_circle(event, x, y, flags, param):
    global prev_x, prev_y
    if event == cv2.EVENT_LBUTTONDOWN:
        prev_x, prev_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
        cv2.line(img, (prev_x, prev_y), (x, y), (0, 0, 0), 3)
        prev_x, prev_y = x, y
        
# Loop through the list of alphabets
for alphabet in alphabets:
    path = os.path.join(store_unit, alphabet)
    # Initialize the image with white color
    img = 255 * np.ones(img_size + (3,), dtype=np.uint8)

    # Create a window for drawing
    cv2.namedWindow(alphabet, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(alphabet, 600, 600)

    # Bind the function to the window
    cv2.setMouseCallback(alphabet, draw_circle)

    # Loop until user presses 'q'
    while True:
        cv2.imshow(alphabet, img)
        if (cv2.waitKey(20) & 0xFF == ord('q')):
            break

    # Check if the directory for the alphabet exists, and create it if it doesn't
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Resize the image to 28x28
    img = cv2.resize(img, (28, 28))

    # Save the image to the directory
    cv2.imwrite(os.path.join(path, alphabet + '.jpg'), img)

    # Destroy the window
    cv2.destroyAllWindows()