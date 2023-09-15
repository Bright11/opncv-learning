import cv2

# cap=cv2.VideoCapture(0)


# while(True):
#     ret, frame = cap.read()
#     cv2.imshow("framename",frame)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
video='img/video.mp4'
#cap=cv2.VideoCapture(video)
cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    # checking the property of the frame
    widths= cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    heigth=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("width",widths)
    print("height",heigth)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("framename",gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()