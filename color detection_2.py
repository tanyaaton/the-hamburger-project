# Importing all modules
import cv2
import numpy as np

# Specifying upper and lower ranges of color to detect in 
# #------hsv format
yellow_lower = np.array([15, 150, 20])
yellow_upper = np.array([35, 255, 255]) # (These ranges will detect Yellow)

green_lower = np.array([45, 150, 20])
green_upper = np.array([75, 255, 255])

red_lower = np.array([170, 150, 20])
red_upper = np.array([180, 255, 255])

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

while cv2.waitKey(1) != ord("q"):
    
    success, video = webcam_video.read() # Reading webcam footage
    
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format

    yellow_mask = cv2.inRange(img, yellow_lower, yellow_upper) # Masking the image to find our color
    green_mask  = cv2.inRange(img, green_lower,  green_upper )
    red_mask    = cv2.inRange(img, red_lower,    red_upper )

    yellow_mask_contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    green_mask_contours, hierarchy  = cv2.findContours(green_mask,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    red_mask_contours, hierarchy    = cv2.findContours(red_mask,    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    
    # Finding position of all contours
    #determine color of layout and textin --- BGR (RBG)

    if len(yellow_mask_contours) != 0:
        for yellow_mask_contour in yellow_mask_contours:
            if cv2.contourArea(yellow_mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(yellow_mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (30, 250, 255), 3) #drawing rectangle
                cv2.putText(video, "yellow",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 250, 255), 2, cv2.LINE_AA ) 
                #Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    

    if len(green_mask_contours) != 0:
        for green_mask_contours in green_mask_contours:
            if cv2.contourArea(green_mask_contours) > 500:
                x, y, w, h = cv2.boundingRect(green_mask_contours)
                cv2.rectangle(video, (x, y), (x + w, y + h), (60, 150, 25), 3) #drawing rectangle
                cv2.putText(video, "green",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (60, 150, 25), 2, cv2.LINE_AA ) 

    if len(red_mask_contours) != 0:
        for red_mask_contours in red_mask_contours:
            if cv2.contourArea(red_mask_contours) > 500:
                x, y, w, h = cv2.boundingRect(red_mask_contours)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 17, 255), 3) #drawing rectangle
                cv2.putText(video, "red",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 17, 255), 2, cv2.LINE_AA ) 
                

    # cv2.imshow("mask green", green_mask) # Displaying mask image
    # cv2.imshow("mask yellow", yellow_mask)
    cv2.imshow("window", video) # Displaying webcam image

    # cv2.waitKey(1)

    

