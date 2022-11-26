#ctrl + shift + p to change interpreter
import numpy as np
import cv2
import requests
import time
import smtplib
from email.message import EmailMessage
import data

#This will use your login details from the data.py file, the only variable
#that you need to change is the 'to' to specifcy which email you want this to go to. 
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = data.user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(data.user, data.password) 
    server.send_message(msg)
    server.quit()


URL = "http://localhost:8080/movement"

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
            print("Movement detected !!!")
            data = {}
            r = requests.post(url = URL, data = data)
            email_alert("Movement was detected in your room","Movement was detected in your room at XX:XX","YOUR_EMAIL")
            time.sleep(10)

    frame1 = frame2
    ret, frame2 = capture.read()

    #if(cv2.waitKey(1) == ord('q')): #This cheks the value of the key pressed; Wait 1ms, ord value == ASCI value
    #    break

capture.release()
cv2.destroyAllWindows()
