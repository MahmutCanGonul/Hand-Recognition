# Hand-Recognition
Hand Recognition With Python


Download this package on anaconda navigator:

💣Cv

Run “pip install opencv-python” to install OpenCV.

💣MediaPipe

Run “pip install mediapipe” to install MediaPipe.

💣Tensorflow

Run “pip install tensorflow” to install the tensorflow module.



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








OUTPUT: 

 
![hands](https://user-images.githubusercontent.com/75094927/144708517-b7462dd6-9fc2-4f6a-bb99-67897587e0bc.png)



![hands2](https://user-images.githubusercontent.com/75094927/144746440-868d32e2-470b-4dd7-8410-5e2fea7f8272.png)
