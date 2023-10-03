import cv2

image="img/car.jpg"
img=cv2.imread(image,1)
text="nice to learn"
coordinates=(100,100)
font=cv2.FONT_HERSHEY_SIMPLEX
fontscale=1
color=(255,255,0)
thickness=2
img=cv2.putText(img,text,coordinates,font,fontscale,color,thickness)
img=cv2.imshow("check img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
