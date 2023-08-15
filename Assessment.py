import cv2
import numpy as np
import matplotlib.pyplot as plt

bgr_image = cv2.imread('dog_backpack.jpg')
# Convert BGR image to RGB
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.show()

flipped_image = cv2.flip(rgb_image, 0)
plt.imshow(flipped_image)
plt.show()

#Draw rectangle around the dog's face
rectangle_image = cv2.rectangle(rgb_image, pt1=(300,400), pt2=(600,700), color=(255,0,0), thickness=5)
plt.imshow(rectangle_image)
plt.show()

#Draw a triangle around the dog's face
vertices = np.array([[250, 700], [700, 600], [425,400]], dtype=np.int32)
pts = vertices.reshape((-1,1,2))
#tri_img= cv2.polylines(rgb_image, [pts], isClosed=True, color=(0,0,255), thickness=10)
tri_img= cv2.fillPoly(rgb_image, [pts], color=(0,0,255))
plt.imshow(tri_img)
plt.show()

#Draw empty red circles on the dog with a left mouse click
def draw_circle(event, x, y, flags, param):
   if event == cv2.EVENT_LBUTTONDOWN:
       cv2.circle(bgr_image, (x,y), 100, (0,0,255), 5)
   

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

while True:
    cv2.imshow('my_drawing',bgr_image)
    #Esc key pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()