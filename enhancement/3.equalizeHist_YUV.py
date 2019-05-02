import cv2
import numpy as np

img = cv2.imread('../images/flower.jpeg')
imgYUV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 通道分割
channelsYUV = cv2.split(imgYUV)
channelsYUV[0] = cv2.equalizeHist(channelsYUV[0])

# 通道合并
channels = cv2.merge(channelsYUV)
result = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', img)
cv2.imshow('dst', result)
cv2.waitKey(0)
cv2.destroyAllWindows()