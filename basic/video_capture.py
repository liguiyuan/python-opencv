import cv2

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('2018-08-26-155735.mp4') # 从视频文件读取

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

