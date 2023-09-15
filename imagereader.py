import cv2
import os

# Load the image from the 'img' folder
image_path = 'img/lena.jpg'
img = cv2.imread(image_path, -1)

# Display the loaded image
cv2.imshow("my image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Specify the folder path where you want to save the image
output_folder = 'imagesfolder'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created folder: {output_folder}")

# Specify the full path for the output image, including the folder and file extension
output_path = os.path.join(output_folder, "newimage.png")

# Save the image in the specified folder
cv2.imwrite(output_path, img)
print(f"Saved image to: {output_path}")
