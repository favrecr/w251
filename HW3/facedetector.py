import numpy as np
import cv2
import paho.mqtt.client as mqtt

#mosquitto broker address
broker_address="172.18.0.4"

#New client instance
client = mqtt.Client()

#connect to broker
client.connect(broker_address)

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    print("frame captured")

    # gray here is the gray frame you will be getting from a camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detection and other logic goes here
    face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        # your logic goes here
        face = frame[y:y+h, x:x+w]

        rc, jpg=cv2.imencode('.png', face)

        msg =jpg.tobytes()

        #publish face image msg
        client.publish("jetsonimage", payload=msg)

        #cv2.imshow('frame',gray)

        cv2.waitKey(1)
        break
        
cap.release()
cv2.destroyAllWindows()
