# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:44:55 2021

@author: Mahmut Can Gonol
"""

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

camera = cv2.VideoCapture(0)

if camera == None:
    print("I can not find camera") 
    
            
     



mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 2, min_detection_confidence = 0.8)
mp_draw = mp.solutions.drawing_utils
 
 
 
while True:
    success,img = camera.read()
    
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    hand_process = hands.process(imgRGB)
    
    height,width,channel = img.shape
    
    if hand_process.multi_hand_landmarks != None:
    
        for hand_landmarks in hand_process.multi_hand_landmarks:
            for fingers_num,landmark in enumerate(hand_landmarks.landmark):
                positionX,positionY = int(landmark.x * width),int(landmark.y * height)
                
                """ # This code put the number on fingers
                cv2.putText(img,str(fingers_num),(positionX,positionY),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
                """
                if fingers_num == 4:
                    cv2.circle(img,(positionX,positionY),15,(255,255,255),cv2.FILLED)
                """    
                if fingers_num == 8:
                    cv2.circle(img,(positionX,positionY),15,(255,255,255),cv2.FILLED)
                if fingers_num == 12:
                    cv2.circle(img,(positionX,positionY),15,(255,255,255),cv2.FILLED)
                if fingers_num == 16:
                    cv2.circle(img,(positionX,positionY),15,(255,255,255),cv2.FILLED)
                if fingers_num == 20:
                    cv2.circle(img,(positionX,positionY),15,(255,255,255),cv2.FILLED)
               """
                
                if fingers_num > 4 and landmark.y < hand_landmarks.landmark[2].y:
                     break
                
                """
                print(fingers_num,landmark.x,landmark.y)
                """
               
                if fingers_num == 20 and landmark.y > hand_landmarks.landmark[2].y:
                     break
                     print("Exit")
               
                
                
                
                
                 
            mp_draw.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)
     
    cv2.imshow("Camera",img)
    if cv2.waitKey(1) &  0xFF == ord("q"): # When you click two time  q camera is shutdown
        break


