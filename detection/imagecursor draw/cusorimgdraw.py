import cv2
imgpath="img/lena.jpg"

img_raw=cv2.imread(imgpath)
roi=cv2.selectROI(img_raw)

print(roi)
cv2.waitKey(0)
cv2.destroyAllWindows()