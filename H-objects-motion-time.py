#Import Library
import cv2
from datetime import datetime
import pandas

#First frame
first_frame = None
status_list = [None, None]
times=[]
df=pandas.DataFrame(columns= ["Start","End"])

#Capture Video
our_video = cv2.VideoCapture(0)

while True:
    #Check if loaded correctly
    check, frame = our_video.read()

    #For motion time
    status = 0

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
        if cv2.contourArea(contour) < 500:
            continue
        status = 1
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    #Motion time
    status_list.append(status)

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    #Show the captured frame of video
    cv2.imshow("First Frame", first_frame)
    cv2.imshow("Capturing first ", our_frame_gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_frame)
    cv2.imshow("Detecting objects", frame)

    #Set q=quit
    key = cv2.waitKey(1)
    if(key == ord('q')):
        if status is 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

#Store into DataFrame
for i in range(0, len(times), 2):
    df = df.append({
    "Start":times[i],
    "End":times[i+1]},
    ignore_index = True)

df.to_csv("Times.csv", index = False)
our_video.release()
cv2.destroyAllWindows
