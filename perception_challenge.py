import cv2
import numpy as np

# Load the image
image = cv2.imread("red.png")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper ranges for red color in HSV
lower_red = np.array([0, 80, 100])
upper_red = np.array([5, 245, 245])

# Create a mask for the red color
mask = cv2.inRange(hsv, lower_red, upper_red)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Convert to grayscale for edge detection
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Edge Detection using Canny
edges = cv2.Canny(blurred, 50, 100)

# Calculate the width and height of the image
height, width, _ = image.shape

# Split the image in half vertically
left_half = edges[:, :width // 2]
right_half = edges[:, width // 2:]

def MagicLineLeftDrawerWOW(half, img, offset):
    # Contour Detection
    contours, _ = cv2.findContours(half, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i in range(len(contours) - 1):
        # Calculate the moments of the current contour to find its centroid
        M1 = cv2.moments(contours[i])
        
        if M1["m00"] != 0:
            # Calculate the centroid coordinates of the current contour
            cx1 = int(M1["m10"] / M1["m00"])
            cy1 = int(M1["m01"] / M1["m00"])

            # Calculate the moments of the next contour to find its centroid
            M2 = cv2.moments(contours[i + 1])

            if M2["m00"] != 0:
                # Calculate the centroid coordinates of the next contour
                cx2 = int(M2["m10"] / M2["m00"])
                cy2 = int(M2["m01"] / M2["m00"])

                # Draw a line connecting the centroids of the current and next contours
                cv2.line(img, (cx1 + offset, cy1), (cx2 + offset, cy2), (0, 0, 255), 2)
    return img;

image = MagicLineLeftDrawerWOW(left_half, image, 0)
image = MagicLineLeftDrawerWOW(right_half, image, width // 2)

# Save the image as "answer.png"
cv2.imwrite("answer.png", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
