"""
This module demonstrates the use of openCV to give a blue hue to a  colour image
"""
import cv2
import numpy as np

# Read the image from disk
image = cv2.imread('Syrup.jpg')
image = cv2.resize(image, (512, 512))

# Increase the blue channel values
blue_hue_image = image.copy()
blue_hue_image[:, :, 0] = np.clip(blue_hue_image[:, :, 0] + 25, 0, 255)  # Increase blue channel

# Reduce the red and green channel values
blue_hue_image[:, :, 1] = np.clip(blue_hue_image[:, :, 1] - 25, 0, 255)  # Reduce green channel
blue_hue_image[:, :, 2] = np.clip(blue_hue_image[:, :, 2] - 25, 0, 255)  # Reduce red channel

# Save the image with a blue hue to disk
cv2.imwrite('blue_hue_image.jpg', blue_hue_image)
cv2.imshow('adjusted',  blue_hue_image)
cv2.waitKey()
cv2.destroyAllWindows()
