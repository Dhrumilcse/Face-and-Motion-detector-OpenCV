#Importing Library
import cv2

#Load Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontface_default.xml")

#Load image
our_image_color = cv2.imread("elon-weed.jpg")
our_image_gray = cv2.cvtColor(our_image_color,cv2.COLOR_BGR2GRAY)

#detect face
faces = face_cascade.detectMultiScale(our_image_gray,
scaleFactor = 1.05,
minNeighbors = 5
)

#Print out type and values of object faces 
print(type(faces))
print(faces)
