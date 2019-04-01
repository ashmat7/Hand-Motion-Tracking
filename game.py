from pynput.keyboard import Key, Controller
import cv2
import numpy as np
import time
import keyboard
cap=cv2.VideoCapture(0)
hand_cascade=cv2.CascadeClassifier("rpalm.xml")
prev_x,prev_y=0,0
count=0
while True:
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hands=hand_cascade.detectMultiScale(gray,1.2,5)
	for x,y,w,h in hands:
		#time.time()
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		next_x,next_y=x,y
		if count>0:
			diff_x,diff_y=((next_x-prev_x),(next_y-prev_y))
			if diff_x>25:
				keyboard.press('left')
				keyboard.release('left')
			elif diff_x<-25:
				keyboard.press('right')
				keyboard.release('right')
			if diff_y>30:
				keyboard.press('down')
				keyboard.release('down')
			elif diff_y<-26:
				keyboard.press('up')
				keyboard.release('up')
				
		prev_x,prev_y=next_x,next_y
	#time.time()
	count+=1
	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

