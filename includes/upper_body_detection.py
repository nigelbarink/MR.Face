import cv2

class upper_body_detector:

    cascClassifier = NULL
    cascPath = "haarcascade_upperbody.xml"

    def __init__(self):
        cascClassifier = cv2.CascadeClassifier(cascPath)    

    def look_for_face(self, imagePath):
        image = cv2.imread(imagePath)
        image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        upperBodies = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.18,
            minNeighbors=12,
            minSize=(30,30),
            flags= cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        object_count = len(upperBodies)
        return (upperBodies, object_count)