"""""
what is contours?
contours is a python list of all the contours in the image.
Each individual conturs is a numpy arry of (xy) coordinates of boundary pont of the object.

"""

import cv2
import numpy as np 

image="img/opencv-logo.png"

img=cv2.imread(image)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
value=127
maximum=255
type=0
ret,thresh=cv2.threshold(imgray,value,maximum,type)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours =" + str(len(contours)))
cv2.drawContours(img,contours, 0, (0,255,0),3)

cv2.imshow("image",img)
cv2.imshow("Image gray",imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()