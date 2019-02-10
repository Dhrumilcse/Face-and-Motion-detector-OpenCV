#Import OpenCV library
import cv2

#Loading Image
#Where, 0 = Grayscale and 1 = RGB
our_image = cv2.imread("0.jpeg",0)

#Type of 'our_image' object
print(type(our_image))
print(our_image.shape, "\n")
print(our_image)
