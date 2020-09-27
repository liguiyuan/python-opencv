import cv2
import matplotlib.pyplot as plt

# 灰度直方图
img = cv2.imread('../images/flower.jpeg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

# 彩色直方图
img = cv2.imread('../images/flower.jpeg')
histb = cv2.calcHist([img], [0], None, [256], [0, 256])
histg = cv2.calcHist([img], [1], None, [256], [0, 256])
histr = cv2.calcHist([img], [2], None, [256], [0, 256])

plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.show()
