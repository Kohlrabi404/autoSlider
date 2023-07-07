import matplotlib.pyplot as plt
import numpy as np
import cv2

def get_transform_h():
    def onclick(event):
        # Get the x and y coordinates of the clicked point
        x = int(event.xdata)
        y = int(event.ydata)
        
        # Save the coordinates to the list
        clicked_points.append((x, y))
        print("Captured points: {} {}".format(x,y))

        # If 4 points are captured, disconnect the event handler
        if len(clicked_points) == 4:
            plt.disconnect(cid)
            plt.close()

    # Load and display the image using plt.imshow
    image = plt.imread("data\surf1\\train\s\img_0001.png")
    plt.imshow(image)

    # Create a list to store the clicked points
    clicked_points = []

    # Register the onclick event handler
    cid = plt.connect("button_press_event", onclick)

    # Show the image plot
    plt.show()
    
    input_pts = np.float32(clicked_points)
    output_pts = np.float32([[0, 0],
                            [0, 256 - 1],
                            [256 - 1, 256 - 1],
                            [256 - 1, 0]])

    # Compute the perspective transform M
    M = cv2.getPerspectiveTransform(input_pts,output_pts)

    return M

# homography, maxWidth, maxHeight = get_transform_h()

def transform(path: str, amount: int, homography) :
    for i in range(1, amount+1) :
        img = cv2.imread("{}\\img_{:04}.png".format(path, i))
        print("{}\\img_{:04}.png".format(path, i))
        out = cv2.warpPerspective(img, homography, (256, 256), flags=cv2.INTER_LINEAR)
        cv2.imwrite("{}\\img_{:04}.png".format(path, i), out)

