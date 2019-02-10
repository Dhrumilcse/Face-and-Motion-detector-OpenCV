#Importing Library
import cv2

#Load Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontface_default.xml")

#Load image
our_image_color = cv2.imread("elon-weed.jpg")
our_image_gray = cv2.cvtColor(our_image_color,cv2.COLOR_BGR2GRAY)

#Detect face
faces = face_cascade.detectMultiScale(our_image_gray,
scaleFactor = 1.05,
minNeighbors = 5
)

#Draw a rectangle around face
for x, y, w, h in faces:
    our_image_rect = cv2.rectangle(our_image_color, (x,y), (x+w,y+h), (0,255,0), 3)

#Show Image
cv2.imshow("Face Detection", our_image_rect)
cv2.waitKey(0)
cv2.destroyAllWindows
