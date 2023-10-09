
# An image gradient is a directional change in the intensity or color in an image
# 
# how to use opencv trashbar
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

image="img/images1.jpg"
img=cv2.imread(image,cv2.IMREAD_GRAYSCALE)
# lap=cv2.Laplacian(img, cv2.CV_64F)
lap=cv2.Laplacian(img, cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
# 
dx=1 #y direction
dy=0
sobelx=cv2.Sobel(img,cv2.CV_64F,dx,dy)
sobely=cv2.Sobel(img,cv2.CV_64F, dy,dx)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

# how to use canny
edges=cv2.Canny(img,100,200)
# the end
# how to detect the edges
sobelcombined=cv2.bitwise_or(sobelx,sobely)
# the end


originaling=cv2.imread(image)

cv2.imshow("original image",originaling)

titles=['Chika Messi','laplacian','sobelx','sobely','Canny',"real","sobelcombined"]
images=[img,lap,sobelx,sobely,edges,img,sobelcombined]
for i in range(7):
    plt.subplot(2,4,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()