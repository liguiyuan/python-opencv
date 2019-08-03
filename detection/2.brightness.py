import cv2
import numpy as np
from PIL import Image, ImageStat

img = cv2.imread('../images/unequalized.jpg')
im = Image.open('../images/unequalized.jpg').convert('L')     # 打开并转为灰度图
sta = ImageStat.Stat(im)

sta_value1 = sta.mean[0]        # 平均亮度值
sta_value2 = sta.rms[0]         # rms计算法

print('sta_value1: ', sta_value1)
print('sta_value2: ', sta_value2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
