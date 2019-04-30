import numpy as np
import cv2
import matplotlib.pylab as plt

'''
在仿射变换中，原始图像中的所有平行线在输出图像中仍将平行。 
为了找到变换矩阵，我们需要输入图像中的三个点及其在输出图像中的相应位置。 
然后cv.getAffineTransform将创建一个2x3矩阵，该矩阵将传递给cv.warpAffine
'''
img = cv2.imread('../images/test2.png')
rows, cols = img.shape[:2]

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
