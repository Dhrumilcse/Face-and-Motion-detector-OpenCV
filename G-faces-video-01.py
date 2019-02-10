#Import Library
import cv2

#First frame
first_frame = None

#Capture Video
our_video = cv2.VideoCapture(0)

while True:
    #Check if loaded correctly
    check, frame = our_video.read()

    #Conver to Gray
    our_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    our_frame_gray = cv2.GaussianBlur(our_frame_gray,(21,21),0)

    #Set first frame
    if first_frame is None:
        first_frame=our_frame_gray
        continue

    #Delta frame
    #Compare first frame to current frame
    delta_frame = cv2.absdiff(first_frame, our_frame_gray)

    #Thresold frame
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    #Contours
    cnts, hierarchy = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Draw rectangle for moving objects
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    #Show the captured frame of video
    cv2.imshow("First Frame", first_frame)
    cv2.imshow("Capturing first ", our_frame_gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Detecting objects", frame)

    #Set q=quit
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

our_video.release()
cv2.destroyAllWindows
