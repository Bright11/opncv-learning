# import cv2
# import os

# cap=cv2.VideoCapture(0)
# height=(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# width=(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(height)
# print(width)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('outvideo.avi',fourcc,20.0,(640,480))
# while(cap.isOpened()):
#     ret,frame=cap.read()
#     if ret==True:
#         folder="videofolder"
#         out.write(frame)
#         cv2.imshow("video",frame)

#         if cv2.waitKey(1) & 0xFF==ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()


import cv2
import os

# Create the folder if it doesn't exist
folder = "videofolder"
if not os.path.exists(folder):
    os.makedirs(folder)

cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(os.path.join(folder, 'outvideo.mp4'), fourcc, 20.0, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow("video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

