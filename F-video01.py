#Import Library
import cv2

#Capture Video
our_video = cv2.VideoCapture(0)

while True:
    #Check if loaded correctly
    check, frame = our_video.read()
    print(check, "\n", frame)

    #Show the captured frame of video
    cv2.imshow("Capturing", frame)  

    #Set q=quit
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

our_video.release()
cv2.destroyAllWindows
