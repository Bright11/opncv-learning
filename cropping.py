import cv2
import os
imgpath="img/car3.jpg"
createfolder = 'croppfolder'

if not os.path.exists(createfolder):
    os.makedirs(createfolder)

img_raw=cv2.imread(imgpath)
roi=cv2.selectROI(img_raw)

print(roi)
roi_croppingimg=img_raw[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
cv2.imshow("ROI image",roi_croppingimg)

createfolder=os.path.join(createfolder,"croppedimg.png")

cv2.imwrite(createfolder,roi_croppingimg)

cv2.waitKey(0)
cv2.destroyAllWindows()