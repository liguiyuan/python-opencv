import cv2
import numpy as np

img = np.zeros((640, 640, 3), np.uint8)

# 画线
cv2.line(img, (10, 10), (100, 100), (255, 0, 0), 5)
# 画矩形
cv2.rectangle(img, (30,120), (230, 250), (0, 255, 0), 3)

# 画圆
# 参数2：圆心坐标  参数3：半径
cv2.circle(img, (150, 350), 60, (0, 0, 255), 3)

# 画椭圆
# 参数2：椭圆中心坐标  参数3：x/y的长度  参数4：椭圆的旋转角度  
# 参数5： 椭圆起始角度  参数6：椭圆结束角度  参数8：-1表示填充
cv2.ellipse(img, (150, 450), (100, 50), 0, 0, 180, (255, 0, 0), -1)

# 画多边形
pts = np.array([[300, 150],  [380, 150], [430, 320], [260, 320]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 参数3：true表示多边形闭合，false时不闭合
cv2.polylines(img, [pts], True, (0, 255, 255))

cv2.imshow('img', img)
cv2.waitKey(0)
