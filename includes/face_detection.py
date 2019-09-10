import cv2

class face_detector:

    cascClassifier = NULL
    cascPath = "haarcascade_frontalface_default.xml"

    def __init__(self):
        cascClassifier = cv2.CascadeClassifier(cascPath)    

    def look_for_face(self, imagePath):
        image = cv2.imread(imagePath)
        image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.18,
            minNeighbors=12,
            minSize=(30,30),
            flags= cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        object_count = len(faces)
        return (faces, object_count)
    