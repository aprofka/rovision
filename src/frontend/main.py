#ctrl + shift + p to change interpreter
import numpy as np
import cv2

capture = cv2.VideoCapture(0) # Selecting capture device/video

ret, frame1 = capture.read() #ret is the status of the frame capture
ret, frame2 = capture.read() #ret is the status of the frame capture

while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)


    contours, _, = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        (x, y, w, h) = cv2.boundingRect (c)

        if cv2.contourArea(c) < 5000:
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 225, 0), 2)
            cv2.putText(frame1, "Status: {}".format("Movement"), (10, 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3) #font
            print("Movement detected !!!")


    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2) #This displays the camera

    #cv2.imshow('frame', frame1)
    frame1 = frame2
    ret, frame2 = capture.read()

    if(cv2.waitKey(1) == ord('q')): #This cheks the value of the key pressed; Wait 1ms, ord value == ASCI value
        break

capture.release()
cv2.destroyAllWindows()