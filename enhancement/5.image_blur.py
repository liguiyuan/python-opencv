import cv2
import numpy as np

def motion_blur(image_src, degree=15, angle=45):
    image = np.array(image_src)

    # 生成任意角度的运动模糊kernel的矩阵，degree越大，模糊程度越高
    M = cv2.getRotationMatrix2D((degree/2, degree/2), angle, 1)
    motion_blur_kernel = np.diag(np.ones(degree))
    motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))

    motion_blur_kernel = motion_blur_kernel / degree
    bulrred = cv2.filter2D(image, -1, motion_blur_kernel)

    cv2.normalize(bulrred, bulrred, 0, 255, cv2.NORM_MINMAX)
    bulrred = np.array(bulrred, dtype=np.uint8)

    return bulrred


def gaussian_blur(image_src):
    image = cv2.GaussianBlur(image_src, ksize=(11, 11), sigmaX=0, sigmaY=0)
    return image


image_path = '../images/flower.jpeg'
image = cv2.imread(image_path)
blur1 = motion_blur(image)
blur2 = gaussian_blur(image)

cv2.imshow('src', image)
cv2.imshow('motion', blur1)
cv2.imshow('gaussian', blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()
