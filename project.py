import cv2
import numpy
from color import colorizer
from face import face_detect
from gui import imgselect
import imutils
img_path=imgselect()
if img_path=='':
    print("No image selected")
    exit()
color_img=colorizer(img_path)
faces=face_detect(color_img,img_path)
faces = imutils.resize(faces, width=480)
cv2.imshow("Faces found", faces)
cv2.waitKey(0)