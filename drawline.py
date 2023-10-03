import cv2

image="img/lena.jpg"
img=cv2.imread(image)

color=(255,255,255)
thinkness=2
# where line is stating
stating_point=(0,0)
end_pont=(250,250)
image=cv2.line(img,stating_point,end_pont,color,thinkness)
cv2.imshow("fram",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
