import numpy as np
import cv2
import matplotlib.pylab as plt

# 图像缩放
img = cv2.imread('test1.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC) 	# x,y 都放大2 
# 方法二
# height, width = img.shape[:2]
# res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)


# 图像平移
# 按（100,50）平移
img = cv2.imread('test1.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))


# 图像旋转
# 将图像相对于中心旋转90度而不进行任何缩放
img = cv2.imread('test1.jpg', 0)
rows, cols = img.shape

# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
'''
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 仿射变换
'''
在仿射变换中，原始图像中的所有平行线仍将在输出图像中平行。 
为了找到变换矩阵，我们需要输入图像中的三个点及其在输出图像中的相应位置。 
然后cv.getAffineTransform将创建一个2x3矩阵，该矩阵将传递给cv.warpAffine
'''
img = cv2.imread('test2.png', 0)
rows, cols = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
'''
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
'''

# 透视变换
'''
对于透视变换，需要一个3x3变换矩阵。 即使在转换之后，直线仍将保持笔直，要找到此变换矩阵，
输入图像上需要4个点，输出图像上需要相应的点.，在这4个点中，其中3个不应该共线，
然后可以通过函数cv2.getPerspectiveTransform找到变换矩阵，然后将cv2.warpPerspective应用于此3x3变换矩阵
'''
img = cv2.imread('test3.jpg', 0)
rows, cols = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
