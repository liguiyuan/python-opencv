# 移动侦测（帧差法）
# 根据视频每帧或者几帧之间像素的差异
# 帧差法分为：单帧差、两桢差、和三桢差，这里采用三帧差来计算

import numpy as np
import cv2

def main():
    sdThresh = 10
    font = cv2.FONT_HERSHEY_SIMPLEX

    cap = cv2.VideoCapture(0)
    _, frame1 = cap.read()
    _, frame2 = cap.read()

    count = 0
    while (True):
        _, frame3 = cap.read()
        dist = cv2.absdiff(frame1, frame3)

        frame1 = frame2
        frame2 = frame3

        mod = cv2.GaussianBlur(dist, (9, 9), 0)
        _, thresh = cv2.threshold(mod, 100, 255, 0)

        _, stDev = cv2.meanStdDev(mod)
        std_mean = np.mean(stDev)

        cv2.imshow('dist', mod)
        cv2.putText(frame2, "Standard Deviation - {}".format(
            round(std_mean, 0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)

        if std_mean > sdThresh:
            print("Motion detected -> {}".format(count))
            count += 1

        cv2.imshow('frame', frame2)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

