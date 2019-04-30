import numpy as np
import cv2

img = cv2.imread('../images/test1.jpg')
rows, cols = img.shape[:2]

# 在x上平移100，在y上平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()