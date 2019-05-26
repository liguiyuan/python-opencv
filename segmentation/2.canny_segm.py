import cv2
import numpy as np

img = cv2.imread('../images/paper.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # 灰度化
blurred = cv2.GaussianBlur(gray, (9, 9), 0)             # 高斯滤波

# canny边缘检测
edged = cv2.Canny(blurred, 10, 100)

cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[1] # if imutils.is_cv2() else cnts[1]
docCnt = None

if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02*peri, True)

        if len(approx) == 4:
            docCnt = approx
            break

newimage = img.copy()
for i in docCnt:
    cv2.circle(newimage, (i[0][0], i[0][1]), 10, (255, 0, 0), -1)

cv2.imshow("newimage", newimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


