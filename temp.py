import cv2, time
video=cv2.VideoCapture(0)
check,frame=video.read()
print(check)
print(frame)
time.sleep(300)

video.release()

cv2.imshow("temp",frame,1)
cv2.DestroyAllWindows()


#test comment for change!
