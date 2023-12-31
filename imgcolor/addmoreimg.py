import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 

image="img/gradient.png"
img= cv.imread(image,0)
_, th1=cv.threshold(img,127,255,cv.THRESH_BINARY)

_, th2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_, th3=cv.threshold(img,200,255,cv.THRESH_TRUNC)
_, th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_, th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# displaying multiple images in one frame using matplotlib

titles=['Original image','Binary','Binary_inv','Trunc','Tozero','Tozzero_inv']
images=[img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# cv.imshow("image",img)
# cv.imshow("th1",th1)
# cv.imshow("th2",th2)
# cv.imshow("th3",th3)
# cv.imshow("th4",th4)
# cv.imshow("th5",th5)




# cv.waitKey(0)
# cv.destroyAllWindows()