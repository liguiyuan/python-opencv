import numpy as np
import cv2

# 图像尺寸缩放，宽、高都放大2 
img = cv2.imread('../images/test1.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# 方法二
# height, width = img.shape[:2]
# res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()