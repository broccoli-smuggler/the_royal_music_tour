import cv2
import os
import glob

images_path = os.curdir + "/assets/images/"
os.chdir(images_path)
os.mkdir("compressed")

for file in glob.glob("*.jpg"):
    print(file)
    i = cv2.imread(file)
    cv2.imwrite("compressed/" + file, i, [cv2.IMWRITE_JPEG_QUALITY, 70])

