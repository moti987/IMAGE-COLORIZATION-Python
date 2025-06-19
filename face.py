import cv2
from emotion import detect_emotion
def face_detect(image,img_path):
    emotion=detect_emotion(img_path)
    facecascade=cv2.CascadeClassifier("Model\\face\haarcascade_frontalface_default.xml")
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    print("Found " + str(len(faces)) + " faces!")
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(image, emotion, (int(x), int(y)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),thickness=1)
    return image
