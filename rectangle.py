import cv2

image="img/car.jpg"
img=cv2.imread(image)

color=(255,0,255)
thinkness=2
# where line is stating
stat_pont=(120,50)
end_pont=(250,250)
image=cv2.rectangle(img,stat_pont,end_pont, color,thinkness)
cv2.imshow("fram",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
