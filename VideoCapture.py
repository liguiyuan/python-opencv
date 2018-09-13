import cv2

capture = cv2.VideoCapture(0)
while(True): 
	# read a frame from camera
	ret, frame = capture.read() 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

	cv2.imshow('gray', gray)
	cv2.imshow('frame', frame) 
	if cv2.waitKey(1) == ord('q'): 
		break
capture.release() 
cv2.destroyAllWindows()

# This is for capturing from video file
'''
capture = cv2.VideoCapture('/home/liguiyuan/2018-08-26-155735.webm')
while(capture.isOpened()): 
	ret, frame = capture.read() 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

	cv2.imshow('gray', gray)
	cv2.imshow('frame', frame) 
	if cv2.waitKey(30) == ord('q'): 
		break
capture.release() 
cv2.destroyAllWindows()
'''
