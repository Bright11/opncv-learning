import cv2
from matplotlib import pyplot as plt 

image="img/smarties.png"

img=cv2.imread(image,cv2.IMREAD_GRAYSCALE)
titles=['image']
images=[img]
for i in range(1):
    plt.subplot(1,1, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    

plt.show()