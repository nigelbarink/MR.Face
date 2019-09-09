# Author: Nigel Barink
# Written: 09/09/2019
# Netherlands, Overijssel, Zwolle 
# From tutorial found here : https://realpython.com/face-recognition-with-python/

import sys
import cv2
import mysql.connector as mariadb

# Get user supplied input
imagePath = sys.argv[1]
cascPath = sys.argv[2]

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
    scaleFactor=1.1,
    minNeighbors=5,
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


