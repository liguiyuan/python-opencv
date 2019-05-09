import cv2
import matplotlib.pyplot as plt

# Otsu 阈值法
img = cv2.imread('../images/book.png', 0)

ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure()
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.hist(img.ravel(), 256)	#.ravel方法将矩阵转化为一维
plt.subplot(223), plt.imshow(th1, 'gray')
plt.subplot(224), plt.imshow(th2, 'gray')
plt.show() 
