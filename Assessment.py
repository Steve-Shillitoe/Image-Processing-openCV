import cv2
import numpy as np
import matplotlib.pyplot as plt

bgr_image = cv2.imread('dog_backpack.jpg')
# Convert BGR image to RGB
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.show()
