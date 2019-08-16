import cv2
import time

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('2018-08-26-155735.mp4') # 从视频文件读取
fps = capture.get(cv2.CAP_PROP_FPS)
print(str(fps) + ' fps')

fps_display_interval = 1    # displays the frame rate every 1 second
frame_count = 0
frame_rate = 0
start_time = time.time()

while(True): 
    # read a frame from camera
    ret, frame = capture.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_count += 1
    end_time = time.time()
    if (end_time - start_time) > fps_display_interval:
        frame_rate = int(frame_count/ (end_time - start_time))
        start_time = time.time()
        frame_count = 0
    
    cv2.putText(frame, str(frame_rate) + " fps", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
            thickness=2, lineType=2)

    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) == ord('q'): 
    	break


capture.release() 
cv2.destroyAllWindows()

