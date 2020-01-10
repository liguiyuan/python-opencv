import cv2
import numpy as np

img = cv2.imread('../images/water_coins.jpg', 0)    #转化为灰度图

# canny边缘检测
blur = cv2.GaussianBlur(img, (3, 3), 0)     # 用高斯滤波处理原图像降噪
edges = cv2.Canny(blur, 50, 150)            # 50是最小阈值,150是最大阈值

cv2.imshow('edge', edges)
cv2.waitKey(0)
