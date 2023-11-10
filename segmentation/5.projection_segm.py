import cv2
import numpy as np


def get_xy_coordinate(list_data):
    for i in range(len(list_data)):
        if list_data[i] > 0:
            x1 = i
            break

    new_list_data = list(reversed(list_data))
    for i in range(len(new_list_data)):
        if new_list_data[i] > 0:
            x2 = i
            break
    x2 = len(new_list_data) - x2
    
    return x1, x2


def main(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)

    # 垂直投影
    rows, cols = binary.shape
    ver_list = [0] * cols
    for j in range(cols):
        for i in range(rows):
            if binary.item(i, j) == 0:
                ver_list[j] = ver_list[j] + 1

    ver_arr = np.array(ver_list)
    ver_arr[np.where(ver_arr < 5)] = 0  # 去除噪点
    ver_list = ver_arr.tolist()

    # 水平投影
    hor_list = [0] * rows
    for i in range(rows):
        for j in range(cols):
            if binary.item(i, j) == 0:
                hor_list[i] = hor_list[i] + 1

    hor_arr = np.array(hor_list)
    hor_arr[np.where(hor_arr < 5)] = 0
    hor_list = hor_arr.tolist()

     # 绘制垂直投影
    img_white_v = np.ones(shape=(rows, cols), dtype=np.uint8) * 255
    for j in range(cols):
        pt1 = (j, rows-1)
        pt2 = (j, rows-1-ver_list[j])
        cv2.line(img_white_v, pt1, pt2, (0,), 1)
    cv2.imshow('vertical projection', img_white_v)

    # 绘制水平投影
    img_white_h = np.ones(shape=(rows, cols), dtype=np.uint8) * 255
    for i in range(rows):
        pt1 = (cols-1, i)
        pt2 = (cols-1-hor_list[i], i)
        cv2.line(img_white_h, pt1, pt2, (0,), 1)
    cv2.imshow('horizontal projection', img_white_h)

    x1, x2 = get_xy_coordinate(ver_list)
    y1, y2 = get_xy_coordinate(hor_list)
    #print('x1, y1, x2, y2: ', x1, y1, x2, y2)

    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_path = '../images/test4.png'
    main(image_path)
