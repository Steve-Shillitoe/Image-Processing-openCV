"""
This module demonstrates the use of openCV to adjust the hue, saturation 
and value of an image.
"""
import cv2
import numpy as np

# read the input image
image = cv2.imread('Syrup.jpg')
image = cv2.resize(image, (512, 512))

# Convert the image from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the values by which you want to change the HSV components
hue_shift = 210  # Change hue by 30 degrees (0-360)
saturation_scale = 1.5  # Scale saturation (1.0 is the original)
value_scale = 2.2  # Scale value (brightness) (1.0 is the original)

# Apply the adjustments to the HSV components
#Blue is typically found around the range of 90 to 120 in the HSV color space
# Set the hue value to give the image a blue hue
blue_hue_value = 105  
# Modify the hue channel in the HSV image
hsv_image[:, :, 0] = blue_hue_value
#hsv_image[:, :, 0] = (hsv_image[:, :, 0] + hue_shift) % 180  # Hue values are in the range of 0-179
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_scale, 0, 255)  # Clip saturation values to [0, 255]
hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * value_scale, 0, 255)  # Clip value (brightness) values to [0, 255]

# Convert the modified HSV image back to BGR color space
output_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Save the modified image to disk
cv2.imwrite('output_image.jpg', output_image)
cv2.imshow('adjusted', output_image)

cv2.waitKey()
cv2.destroyAllWindows()