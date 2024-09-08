from ultralytics import YOLO
import cv2
import cvzone
import math
import poker_fnc
 
cap = cv2.VideoCapture(1)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)
