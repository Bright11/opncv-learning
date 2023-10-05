import cv2
image="img/car.jpg"
# you can make it 0 which is black and whit or 1
# for it's real color
img=cv2.imread(image,0)
cv2.imshow("black and whait",img)

cv2.waitKey(0)
cv2.destroyAllWindows()