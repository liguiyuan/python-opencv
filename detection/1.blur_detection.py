import cv2

def lapulase(filename):
    img = cv2.imread(filename)
    img = cv2.resize(img, (112, 112), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 压缩为单通道灰度图
    res = cv2.Laplacian(gray, cv2.CV_64F)               # 拉普拉斯算子
    score = res.var()

    print('blur score: ', score)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filename = '../images/face.png'
lapulase(filename)
