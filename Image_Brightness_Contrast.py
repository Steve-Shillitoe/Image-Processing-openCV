"""
This module demonstrates the use of openCV to adjust an image's
brightness & contrast


cv2.convertScaleAbs(image, alpha, beta)
Where

image is the original input image.

alpha is the contrast value. To lower the contrast, use 0 < alpha < 1. And for higher contrast use alpha > 1.

beta is the brightness value. A good range for brightness value is [-127, 127]
"""
import cv2

# read the input image
image = cv2.imread('Syrup.jpg')
image = cv2.resize(image, (256, 256))

# define the alpha and beta
alpha = 2.5 # Contrast control
beta = 10 # Brightness control

# call convertScaleAbs function
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# display the output image
cv2.imshow('adjusted', adjusted)
cv2.imwrite('output_image.jpg',adjusted)
cv2.waitKey()
cv2.destroyAllWindows()