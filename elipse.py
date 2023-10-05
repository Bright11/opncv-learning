import cv2

image="img/lena.jpg"
img=cv2.imread(image)

color=(0,0,255)
thinkness=10
# where line is stating
center_coordinate=(120,100)
axeslength=(100,50)
angle=30
statangle=0
endangle=360
image=cv2.ellipse(img,center_coordinate,axeslength,angle,statangle,endangle, color,thinkness)
cv2.imshow("fram",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
