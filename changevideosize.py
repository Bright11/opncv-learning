import cv2
import datetime

cap=cv2.VideoCapture(0)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("main height",height)
print("main width",width)
# how to change the height and width of my video
newwidth=cap.set(3, 1208) # width
newheight=cap.set(4,720) #height
#print("newheight",cap.get(3))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        # adding text into a video
        font=cv2.FONT_HERSHEY_COMPLEX
        # here we are changing or intiger into string
        # the height and width of our video is intiger
        date=str(datetime.datetime.now())
        text='Width:'+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
        #  frame=cv2.putText(frame,date, (10,50), font, 1, (0,255,255),2,cv2.LINE_AA)
        frame=cv2.putText(frame,date, (10,50), font, 1, (0,255,255),2,cv2.LINE_AA)
        frame=cv2.putText(frame,text, (10,10), font, 1, (0,255,255),2,cv2.LINE_AA)
        # 
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
        cv2.imshow("image frame",gray)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()