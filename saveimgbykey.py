import cv2
import os

image='img/lena.jpg'
img=cv2.imread(image,-1)
cv2.imshow("image",img)
keypress=cv2.waitKey(0)

createfolder="savedimg"


    
    


# checking the key press
# the 27 is to check if esc key is pressed
if keypress==27:
    cv2.destroyAllWindows()
elif keypress == ord('s'):
     
     if not os.path.exists(createfolder):
         os.makedirs(createfolder)
         print("folder created")
    # the path to store image
     createfolder=os.path.join(createfolder,"newpicturename.png")

         # saving image
     cv2.imwrite(createfolder,img)
     cv2.destroyAllWindows()