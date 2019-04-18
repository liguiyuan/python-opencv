import cv2
import numpy as np
import imutils
from collections import deque

# camera video capture
camera=cv2.VideoCapture(0)
firstframe=None

# define the lower and upper boundaries of the green ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255,255)
pts = deque(maxlen=64)

while True: 
	ret,frame = camera.read() 
	if not ret: 
		break

	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=6)
	mask = cv2.dilate(mask, None, iterations=6)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	center = None

	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 255, 255), -1)

	pts.appendleft(center)

	for i in range(1,len(pts)):
		if pts[i-1] is None or pts[i] is None:
			continue

		thickness = int( np.sqrt(64/float(i+1))*2.5 )
		cv2.line(frame, pts[i-1], pts[i], (0, 0, 225), thickness)

	cv2.imshow("frame", frame)
	cv2.imshow("mask", mask) 

	key = cv2.waitKey(1)&0xFF
	if key == ord("q"): 
		break

camera.release() 
cv2.destroyAllWindows()
