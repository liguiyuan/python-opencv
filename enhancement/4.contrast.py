import cv2
import numpy as np

c = 1.3     # 用来调整对比度，一般在0.0~3.0之间
b = 3       # 用来调节亮度

img = cv2.imread('../images/flower.jpeg')
rows, cols, channels = img.shape

# 新建一个全零(黑色)图片数组
blank = np.zeros([rows, cols, channels], img.dtype)
dst = cv2.addWeighted(img, c, blank, 1-c, b)

cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

