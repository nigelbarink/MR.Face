# Author: Nigel Barink
# Written: 09/09/2019
# Netherlands, Overijssel, Zwolle 
# From tutorial found here : https://realpython.com/face-recognition-with-python/

import uuid 
import cv2
import mysql.connector as mariadb

import time
import threading

from includes.face_detection import face_detector
from includes.upper_body_detection import upper_body_detector

# Get user supplied input
imagePath = "images/group.jpg" 
cascPath = "haarcascade_frontalface_default.xml"

lift_id = 1 

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#Read the image 
# TODO: reading from video later ...
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces !!! :) 
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.18,
    minNeighbors=12,
    minSize=(30,30),
    flags= cv2.cv.CV_HAAR_SCALE_IMAGE
)
person_count = len(faces)

# NOTE:
# This kind of data should be stored in a
# configuration file. However this is such
# a small project that I (the programmer) don't
# feel like  writing code to read in a configuration file
# 
# YES  I am that lazy ;)
#
user = "Face_AI"
password = "123Cyborg"
database= "SmartLift"

db_connection = mariadb.connect(user, password, database)
cursor = db_connection.cursor()
# NOTE: This is unsafe if there was any user input here!
stmnt = "UPDATE lift SET persons = {0} WHERE lift_ID = {1}" % (person_count, lift_id)

cursor.execute(stmnt)

print ("Found {0} faces!" % (person_count))

# write the image with a green border around detected objects
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255, 0), 2)
# cv2.imshow("Objects detected!")
imageName = str(uuid.uuid5(uuid,NAMESPACE_DNS, 'barink.dev/ML'))
cv2.imwrite( "results/{0}.jpg".format(imageName) , image)
cv2.waitkey(0)


# Lets go multi threaded 
# What do you mean over engineering :)
def face_thread():
    print("-- Starting face thread --")
    detect = face_detector()
    result = detect.look_for_face("test_images/wedding.jpg")
    print("Faces found: ".format(result[1]))
    print("-- Face thread finished --")

def upperbody_thread():
    print("-- Starting upperbody thread --")
    detect = upper_body_detector()
    result = detect.look_for_face("test_images/wedding.jpg")
    print("Upperbodies found: ".format(result[1]))
    print("-- Upperbody thread finished --")


thread1 = threading.Thread(target=face_thread)

thread2 = threading.Thread(target=upperbody_thread)

thread1.start()
thread2.start()
print("Main thread finished")