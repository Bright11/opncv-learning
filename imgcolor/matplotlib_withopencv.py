import cv2
from matplotlib import pyplot as plt 

image="img/chika.jpg"

img=cv2.imread(image,-1)
cv2.imshow("matplolib with opencv",img)
# converting our image to the original image using matplitlib
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# the end
# to hide the xticks
plt.xticks([]),plt.yticks([])
# the end
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# opencv reads image in the BGR format
# matplolitlib reads image in the RGB format