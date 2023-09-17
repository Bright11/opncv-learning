import cv2
import numpy as np

# event=[i for i in dir(cv2) if 'EVENT' in i]
#event=[i for i in dir(cv2)]
# print(event)

# to display or show the places i click
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,', ', y) #showing where i click
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x) + ', '+ str(y)
        cv2.putText(img, strXY,(x,y), font,1, (255,255,0),2)
        
        cv2.imshow("image",img)
    # if you want to check right click
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_COMPLEX
        strBGR=str(blue) + ', '+ str(green) +', '+ str(red)
        cv2.putText(img,strBGR, (y,x), font,.5,(0,255,255),2)
        cv2.imshow("image",img)
        
        # the end

# this code below gives you a black image
#img =np.zeros((512,512,3), np.uint8)

img='img/lena.jpg'
img=cv2.imread(img)
cv2.imshow("image",img)

cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()