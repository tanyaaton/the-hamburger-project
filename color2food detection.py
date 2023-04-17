# Importing all modules
import cv2
import numpy as np

#import color range list from color_range.py
from color_range import *

#ingredient list

ingred = {}
ingred_list = [ "cheese", "cabbage",     "bellpepper",  "bacon",  "tomato",  "steak",  "onion",  "mashroom", "egg"   ]
color_list =  [ "yellow", "green_light", "green_dark",  "pink",   "red",     "brown",  "purple", "grey",     "white" ]

for i in ingred_list:
    ingred[i] = False

print(ingred)


# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

while cv2.waitKey(1) != ord("c"):
    success, video = webcam_video.read() # Reading webcam footage
    cv2.imshow("window", video) # Displaying webcam image
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format


yellow_mask = cv2.inRange(img, yellow_lower, yellow_upper) # Masking the image to find our color
# green_mask  = cv2.inRange(img, green_dark_lower,  green_dark_upper )
red_mask    = cv2.inRange(img, red_lower,    red_upper )

yellow_mask_contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
# green_mask_contours, hierarchy  = cv2.findContours(green_mask,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
red_mask_contours, hierarchy    = cv2.findContours(red_mask,    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



# Finding position of all contours
#determine color of layout and textin --- BGR (RBG)

if len(yellow_mask_contours) != 0:
    for yellow_mask_contour in yellow_mask_contours:
        if cv2.contourArea(yellow_mask_contour) > 2000:
            print("found cheese")
            ingred["cheese"] = True
            

if len(red_mask_contours) != 0:
    for red_mask_contours in red_mask_contours:
        if cv2.contourArea(red_mask_contours) > 500:
            print("found tomato")
            ingred["tomato"] = True

print(ingred)

# cv2.imshow("mask green", green_mask) # Displaying mask image
# cv2.imshow("mask yellow", yellow_mask)


# cv2.waitKey(1)



