# Hand-Recognition
Hand Recognition With Python


Download this package on anaconda navigator:

💣Cv

Run “pip install opencv-python” to install OpenCV.

💣MediaPipe

Run “pip install mediapipe” to install MediaPipe.

💣Tensorflow

Run “pip install tensorflow” to install the tensorflow module.




HAND DEFINE NUMBERS:

![image](https://user-images.githubusercontent.com/75094927/144747804-4029fce8-3840-428f-bc7c-e3504e41e355.png)




🥇In this project you can see your hands skill point!! 




Code Explanition:

1-Step:  Integrate Package

      import cv2
      import numpy as np
      import mediapipe as mp
      import tensorflow as tf
      from tensorflow.keras.models import load_model


2-Step: Camera Control

      camera = cv2.VideoCapture(0)

      if camera == None:
          print("I can not find camera") 


3-Step: Design Hand Options:

          mp_hands = mp.solutions.hands
          hands = mp_hands.Hands(max_num_hands = 2, min_detection_confidence = 0.8) #I give max hands num and detection rate
          mp_draw = mp.solutions.drawing_utils

4-Step: Objects for holding hands position x, position y and counter hands recognition,time:

          hold_posX = []
          hold_posY=[]
          count_time=0
          count_hands=0

5-Step: Create our logic in While loop: 

    while True:
    
       success,img = camera.read()  # img object is read the camera input
    
       imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # we change the img to imgRGB
    
       hand_process = hands.process(imgRGB) # hands.process read the imgRGB
    
       height,width,channel = img.shape #Also we need to understand 
       
       
        if hand_process.multi_hand_landmarks != None: # if we detect hand 
    
            for hand_landmarks in hand_process.multi_hand_landmarks: #All landmarks for hands turn on for loop
               for fingers_num,landmark in enumerate(hand_landmarks.landmark): #create new objects and enumerate on landmark 
                   positionX,positionY = int(landmark.x * width),int(landmark.y * height) # we create position x and position y for understand hands position 
                
                """ # This code put the number on fingers
                   cv2.putText(img,str(fingers_num),(positionX,positionY),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
                """
                    # This numbers given on first paragraph image!   #We create a circle on all fingers
                   if fingers_num == 4: 
                      cv2.circle(img,(positionX,positionY),15,(255,255,255),cv2.FILLED) 
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
               
                   if fingers_num == 20 and landmark.y > hand_landmarks.landmark[2].y:
                       is_exit=True
                       print("exit")
                      
                
                    print(fingers_num,landmark.x,landmark.y)
               """
               
                   if len(hold_posX) > 0 and len(hold_posY) > 0: # First move first finger position hold the array and after that second move first finger compare to positions!
                      if fingers_num == 4 and hold_posX[len(hold_posX)-1] != positionX and hold_posY[len(hold_posY)-1] != positionY:
                         count_hands+=1
                         print("MOVE!")
                      elif fingers_num == 4 and hold_posX[len(hold_posX)-1] == positionX and hold_posY[len(hold_posY)-1] == positionY:
                         print("NOT MOVE!")
                   
                      if fingers_num == 4:
                        hold_posX.append(positionX)
                        hold_posY.append(positionY)
                        
                   else:
                      if fingers_num == 4:
                         hold_posX.append(positionX)
                         hold_posY.append(positionY)
                        
               
               
               
                
                
                
                
            #Draw the landmarks     
            mp_draw.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)
       
       else:
           count_time+=1 #increase the time
           
       cv2.imshow("Camera",img) #Show the camare
       
       if cv2.waitKey(1) &  0xFF == ord("q"): # When you click two time  q camera is shutdown
          result = float(count_hands/count_time)
          print("Hand Skill Point:  %",str(result))
          print("TIME: ",count_time)
          print("HAND_RECOG: ",count_hands)
          break





OUTPUT: 

 
![hands](https://user-images.githubusercontent.com/75094927/144708517-b7462dd6-9fc2-4f6a-bb99-67897587e0bc.png)



![hands2](https://user-images.githubusercontent.com/75094927/144746440-868d32e2-470b-4dd7-8410-5e2fea7f8272.png)
