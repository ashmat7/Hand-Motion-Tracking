#import cv2,time
#print(check)
#print(frame)
#cv2.imshow("capturing",frame)



import cv2,time
video=cv2.VideoCapture(0)
check,frame=video.read()
print(video.isOpened()) # False
print(video.read()) # (False, None)
time.sleep(4)
cv2.imshow("capturing",frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()