import numpy as np
import cv2

# 将图像相对于中心逆时针旋转90度
img = cv2.imread('../images/test1.jpg')
rows, cols = img.shape[:2]

# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
