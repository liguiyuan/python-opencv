import numpy as np
import cv2
import matplotlib.pylab as plt

'''
对于透视变换，需要一个3x3变换矩阵。 即使在转换之后，直线仍将保持笔直，要找到此变换矩阵，
输入图像上需要4个点，输出图像上需要相应的点，在这4个点中，其中3个不应该共线，
然后可以通过函数cv2.getPerspectiveTransform找到变换矩阵，然后将cv2.warpPerspective应用于此3x3变换矩阵
'''
img = cv2.imread('../images/test3.jpg')
rows, cols = img.shape[:2]

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
