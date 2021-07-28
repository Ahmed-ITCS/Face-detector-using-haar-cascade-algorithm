import cv2
from random import  randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam =cv2.VideoCapture(0)
while True:
    successful_frame_read, frame =webcam.read()

    greyscale_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    facelocation = trained_face_data.detectMultiScale(greyscale_img)

    for (x, y, w, z) in facelocation:
        cv2.rectangle(frame, (x, y), (x + w, y + z), (0,255,0), 3)

    cv2.imshow("check", frame)
    cv2.waitKey(1)
"""""
facelocation  = trained_face_data.detectMultiScale(greyscale_img)

for (x,y,w,z) in facelocation:
    cv2.rectangle(img,(x,y),(x+w,y+z),(0,255,0),1)

cv2.imshow("check",img)
print(facelocation)

cv2.waitKey()
"""""
print("done")
