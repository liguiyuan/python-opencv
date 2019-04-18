import cv2

# 读取图片
img = cv2.imread('test1.jpg')

# 显示图片
cv2.namedWindow('Image')		# 先创建一个窗口
cv2.imshow('Image', img)		# 在窗口中显示图像
cv2.waitKey(0)					# 使窗口始终保持住
cv2.destroyAllWindows()			# 别忘了释放窗口

# 复制图像
img1 = img.copy()

# 保存图像
cv2.imwrite('test.jpg', img1)
#cv2.imwrite("test1.png", img1, [cv2.IMWRITE_PNG_COMPRESSION, 0])	# 对于png，第三个参数表示的是压缩级别
#cv2.imwrite("test2.png", img1, [cv2.IMWRITE_PNG_COMPRESSION, 9])	# 从0到9,压缩级别越高，图像尺寸越小，默认为3