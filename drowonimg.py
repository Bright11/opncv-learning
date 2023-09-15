import cv2

image="img/lena.jpg"
img=cv2.imread(image,1)
# on the imread, we can put 0 or 1
# 1 is the main color of the image and 0 is black
# img=cv2.line(img,(0,0),(255,255),(0,0,255),5)
# drow a line on the image 
# (0,255,0),5) is the color and the last 5 is the tickness
# https://rgbacolorpicker.com/
# rgba(196, 49, 125, 0.8)
img=cv2.line(img,(0,0),(255,255),(196, 125, 0.8),10)
# arrow color
img=cv2.arrowedLine(img,(0,255),(255,255),(196, 125, 0.8),10)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),10)
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'My God',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)
# the text color (0,255,255)
cv2.imshow("drow image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()