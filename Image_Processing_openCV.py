from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import cv2
print(cv2.__version__)

#Lecture 1 - display an image
img = cv2.imread('00-puppy.jpg')
while True:
    cv2.imshow('puppy', img)

    #if we have waited at least 1ms and pressed the Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

#Lecture 2 - Drawing on the image
blank_img = np.zeros(shape=(512,512,3), dtype=np.int16)
#plt.imshow(blank_img)
#plt.show()

#Draw rectangle on the blank image
cv2.rectangle(blank_img, pt1=(380,0), pt2=(510,150), color=(0,255,0), thickness=10)
#plt.imshow(blank_img)
#plt.show()

cv2.circle(img=blank_img, center=(100,100), radius=50, color=(255,0,0), thickness=8)
#plt.imshow(blank_img)
#plt.show()

#filled in circle, thickness is now a negative number
cv2.circle(img=blank_img, center=(400,400), radius=50, color=(255,0,0), thickness=-1)
#plt.imshow(blank_img)
#plt.show()

cv2.line(blank_img, pt1=(0,0), pt2=(512,512), color=(255,255,255), thickness=5)
#plt.imshow(blank_img)
#plt.show()

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text='HELLO', org=(10,500), fontFace=font, fontScale=4, color=(255,255,255), thickness=5)
plt.imshow(blank_img)
plt.show()

blank_img = np.zeros(shape=(512,512,3), dtype=np.int32)
#plt.imshow(blank_img)
#plt.show()

vertices = np.array([[100,300],[200,200],[400,300],[200,400]], dtype=np.int32)
pts = vertices.reshape((-1,1,2))
cv2.polylines(blank_img, [pts], isClosed=True, color=(255,0,0), thickness=5)
plt.imshow(blank_img)
plt.show()
