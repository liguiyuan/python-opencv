import cv2
import matplotlib.pyplot as plt

# 自适应阈值
img = cv2.imread('../images/book.png', 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 窗口大小使用的为25，当窗口越小的时候，得到的图像越细
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 5)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 5)

images = [img,th1,th2,th3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
plt.show()    
