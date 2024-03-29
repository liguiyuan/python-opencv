import cv2
import numpy as np


def main(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # 灰度化
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)             # 高斯滤波

    # 提取图像的梯度
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)  # 以Sobel算子计算x，y方向上的梯度，之后在x方向上减去y方向上的梯度
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)  # 通过这个减法，我们留下具有高水平梯度和低垂直梯度的图像区域

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    # 图像二值化
    blurred = cv2.GaussianBlur(gradient, (9, 9), 0)
    _, threshold = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

    # 形态学操作
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))     # 建立一个核函数
    closed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)       # 形态学闭运算

    # 分别进行4次形态学的腐蚀与膨胀
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    # 找出区域的轮廓
    outs = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(outs) == 3:
        cnts = outs[1]
    elif len(outs) == 2:
        cnts = outs[0]

    # 画出轮廓
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    # draw a bounding box arounded the detected barcode and display the image
    draw_img = cv2.drawContours(img.copy(), [box], -1, (0, 0, 255), 1)

    cv2.imshow("draw_img", draw_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_path = '../images/insect.png'
    main(image_path)

