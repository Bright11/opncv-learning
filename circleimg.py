import cv2

image="img/lena.jpg"
img=cv2.imread(image)

color=(255,0,255)
thinkness=2
# where line is stating
center_coordinates=(120,50)
redius=200
image=cv2.circle(img,center_coordinates,redius, color,thinkness)
cv2.imshow("fram",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
