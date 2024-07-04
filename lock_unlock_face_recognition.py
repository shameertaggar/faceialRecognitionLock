import datetime
import os
import subprocess
import sys

import cv2


def lock_screen():
    subprocess.run(["osascript", "-e", 'tell application "System Events" to keystroke "q" using {command down, control down}'])


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


counter_correct = 0  # counter variable to count the number of times the loop runs
counter_wrong = 0

recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("/Users/shameerali/Desktop/face detection/trainer/")

recognizer.read('/Users/shameerali/Desktop/face detection/trainer/trainer.yml')  # load training model

cascadePath = "/Users/shameerali/PycharmProjects/Lock-Unlock-Laptop-PC-Screen-Using-Face-Recognition/haarcascade_frontalface_default.xml"  # cascade path

faceCascade = cv2.CascadeClassifier(cascadePath)  # load cascade

font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Set the font style

cam = cv2.VideoCapture(1)

no_face_start_time = datetime.datetime.now()

while True:
    now = datetime.datetime.now()

    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        # No face detected, check the time elapsed since no face was detected
        if (now - no_face_start_time).seconds > 8:
            lock_screen()
            sys.exit()
    else:
        # Reset the timer when a face is detected
        no_face_start_time = datetime.datetime.now()

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)

            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])  # Recognize the face belongs to which ID

            if confidence > 30:  # confidence usually comes greater than 80 for strangers
                counter_wrong += 1
                print("Unknown detected")
                print("Confidence:", confidence)
                print("Counter wrong -", counter_wrong)
                cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 0, 255), -1)
                cv2.putText(im, "Unknown", (x, y - 40), font, 1, (0, 0, 0), 2)
                # Lock the screen immediately if an unknown face is detected
                lock_screen()
                sys.exit()
            else:  # confidence usually comes less than 80 for correct user(s)
                Id = "Shameer"
                print("Verified")
                print("Confidence:", confidence)
                counter_correct += 1
                print("Counter correct -", counter_correct)
                cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (255, 255, 255), -1)
                cv2.putText(im, str(Id), (x, y - 40), font, 1, (0, 0, 0), 2)

            if counter_correct == 1000:  # if counter = 1000 then program will terminate as it has recognized correct user for 1000 times.
                cam.release()
                cv2.destroyAllWindows()
                sys.exit()

    cv2.imshow('Webcam', im)

    if cv2.waitKey(10) & 0xFF == ord('*'):
        break

cam.release()
cv2.destroyAllWindows()
