# https://www.jb51.net/article/183678.htm
# https://www.jb51.net/article/164106.htm

import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

def main():
    img1 = cv2.imread('../images/3.jpg')
    img2 = cv2.imread('../images/4.jpg')
    img1_height, img1_width, _ = img1.shape[:]
    img2_height, img2_width, _ = img2.shape[:]
    print(img1_height, img1_width, _)

    starttime = time.time()
    hessian = 400                   # hessian 的阈值为400，阈值越大能检测的特征就越小
    surf = cv2.xfeatures2d.SURF_create(hessian, nOctaves=4, extended=False, upright=True)

    kp1, descrip1 = surf.detectAndCompute(img1, None) # 查找关键点和描述符
    kp2, descrip2 = surf.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0          # 建立FLANN匹配器的参数
    indexParams = dict(algorithm = FLANN_INDEX_KDTREE, tree=5)  # 匹配索引，密度树的数量为5
    searchParams = dict(checks=50)  # 指定递归次数

    flann = cv2.FlannBasedMatcher(indexParams, searchParams)    # FlannBasedMatcher 是目前最快的特征匹配算法（最近邻搜索）
    match = flann.knnMatch(descrip1, descrip2, k=2)             # 得出匹配的关键点

    # 提取优秀的特征点
    good = []
    for i, (m, n) in enumerate(match):
        if (m.distance < 0.75*n.distance):  # 如果第一个邻近距离比第二个邻近距离的0.75倍小，则保留
            good.append(m)
    print(len(good))

    MIN = 10
    if len(good) > MIN:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)  # 查询图像的特征描述子索引
        ano_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)  # 训练（模板）图像的特征描述子索引
        M, mask = cv2.findHomography(src_pts, ano_pts, cv2.RANSAC, 5.0)             # 生成变换矩阵
        warpImg = cv2.warpPerspective(img2, np.linalg.inv(M), (img1_width+img2_width, img2_height)) # 透视变换，新图像可容纳完整的两幅画
        print('warpImg shape: ', warpImg.shape)

        direct = warpImg.copy()
        direct[0:img1_height, 0:img1_width] = img1              # 把图像1拼接在warpImg上，因为warpImg此时只有img2的像素
        cv2.imwrite('simplepanorma.png', direct)
        simple = time.time()
        print('simple stich cost: ', (simple-starttime))
        
        img3 = cv2.cvtColor(direct, cv2.COLOR_BGR2RGB)
        plt.imshow(img3)
        plt.show()

        # 平滑处理
        """
        rows, cols = img1_height, img1_width
        for col in range(0, cols):
            if img1[:, col].any() and warpImg[:,col].any():     # 开始重叠的最左端
                left = col
                break

        for col in range(cols-1, 0, -1):
            if img1[:, col].any() and warpImg[:, col].any():    # 重叠的最右一列
                right = col
                break

        res = np.zeros([rows, cols, 3], np.uint8)
        for row in range(0, rows):
            for col in range(0, cols):
                if not img1[row, col].any():            # 如果没有原图，用旋转的填充
                    res[row, col] = warpImg[row, col]
                elif not warpImg[row, col].any():
                    res[row, col] = img1[row, col]

                else:
                    scrImgLen = float(abs(col-left))
                    testImgLen = float(abs(col - right))
                    alpha = scrImgLen / (scrImgLen + testImgLen)
                    res[row, col] = np.clip(img1[row, col]*(1-alpha) + warpImg[row, col]*alpha, 0, 255)

        warpImg[0:img1_height, 0:img1_width] = res
        final = time.time()
        

        img4 = cv2.cvtColor(warpImg, cv2.COLOR_BGR2RGB)
        plt.imshow(img4,)
        plt.show()
        print('total cost: ', (final-starttime))
        
        cv2.imwrite('bestpanorma.png', warpImg)
        """
    else:
        print('not enough matches!')


if __name__ == '__main__':
    main()
