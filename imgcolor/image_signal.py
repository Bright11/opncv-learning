# Here we are going to know or learn about pyramind or pyramid
""""
Pyramid or pyramid representation is a type of multi-scal signal represention in which a signal of an image is subject to repeated smoothing and susamping
"""""
import cv2
import numpy as np 

image="img/lena.jpg"

img=cv2.imread(image)

lr1=cv2.pyrDown(img) #we can use pyrdwon to reduse image resolution
# we use pyrUp to increase an image to a ahigh resolution, although the quality of the image will be lose
lr2=cv2.pyrDown(lr1)

pyrup=cv2.pyrUp(lr2)




cv2.imshow("original image",img)
cv2.imshow("Pyrdown 1 image",lr1)
cv2.imshow("pyrdown 2 image",lr2)
cv2.imshow("Pyreup 3 image",pyrup)


cv2.waitKey(0)
cv2.destroyAllWindows()