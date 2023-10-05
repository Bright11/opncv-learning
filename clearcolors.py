import cv2
import os
imgpath="img/car3.jpg"
img=cv2.imread(imgpath)

g,b,r=cv2.split(img)

cv2.imshow("Blue part of the image",b)
cv2.imshow("Red part of the image",r)
cv2.imshow("Green part of the image",g)

# with this line of code, we can merge images togather
img1=cv2.merge((g,b,r))
cv2.imshow("this is the original image",img1)

cv2.waitKey(0)