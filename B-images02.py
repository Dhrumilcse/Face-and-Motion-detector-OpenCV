#Import OpenCV library
import cv2

#Loading Image
#Where, 0 = Grayscale and 1 = RGB
our_image = cv2.imread("0.jpeg",0)

#Resizing our image
resized_image = cv2.resize(our_image, (600,188))

#Show Imaage in a window
cv2.imshow("Memes",resized_image)
cv2.imwrite("generated_memes.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
