import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../images/water_coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化处理Otsu算法
reval_O, dst_Otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# 二值化处理Triangle算法
reval_T, dst_Tri = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
kernel = np.ones((3, 3), np.uint8)
# 形态学处理:开处理,膨胀边缘
opening = cv2.morphologyEx(dst_Tri, cv2.MORPH_OPEN, kernel, iterations=2)
# 膨胀处理背景区域
dilate_bg = cv2.dilate(opening, kernel, iterations=3)
# 计算开处理图像到邻域非零像素距离
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 正则处理
norm = cv2.normalize(dist_transform, 0, 255, cv2.NORM_MINMAX)
retval_D, dst_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)

# 前景图格式转换
dst_fg = np.uint8(dst_fg)
# 未知区域计算:背景减去前景
unknown = cv2.subtract(dilate_bg, dst_fg)
# cv2.imshow("Difference value", unknown)

# 处理连接区域
retval_C, marks = cv2.connectedComponents(dst_fg)
# cv2.imshow('Connect marks', marks)

# 处理掩模
marks = marks + 1
marks[unknown==255] = 0
cv2.imshow("marks undown", marks)

# 分水岭算法分割
marks = cv2.watershed(img, marks)

# 绘制分割线
img[marks == -1] = [255, 0, 255]
cv2.imshow("Watershed", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


