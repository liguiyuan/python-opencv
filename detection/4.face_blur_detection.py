import cv2
import numpy as np
import time

def dct():
    filename = '../images/face.png'
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_float = np.float32(img)
    dct = cv2.dct(img_float)

    cv2.imshow('dct', dct)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class BlurDetector():
    def __init__(self):
        super(BlurDetector, self).__init__()
        self.dct_threshold = 8.0
        self.max_hist = 0.1
        self.hist_weight = np.array([8, 7, 6, 5, 4, 3, 2, 1,
                                     7, 8, 7, 6, 5, 4, 3, 2,
                                     6, 7, 8, 7, 6, 5, 4, 3,
                                     5, 6, 7, 8, 7, 6, 5, 4,
                                     4, 5, 6, 7, 8, 7, 6, 5,
                                     3, 4, 5, 6, 7, 8, 7, 6,
                                     2, 3, 4, 5, 6, 7, 8, 7,
                                     1, 2, 3, 4, 5, 6, 7, 8
                                     ]).reshape(8, 8)
        self.weight_total = 344.0

    def check_image_size(self, image, block_size=8):
        result = True
        height, width = image.shape[:2]
        _y = height % block_size
        _x = width % block_size

        pad_x = pad_y = 0

        if _y != 0:
            pad_y = block_size - _y
            result = False
        if _x != 0:
            pad_x = block_size - _x
            result = False

        image = cv2.copyMakeBorder(image, 0, pad_y, 0, pad_x, cv2.BORDER_REPLICATE)

        return result, image

    def get_blurness(self, image, block_size=8):
        # A 2D histogram
        hist = np.zeros((8, 8), dtype=int)

        # Only the illumination is considered in blur
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Split the image into patches and do DCT on the image patch
        height, width = image.shape
        round_v = int(height / block_size)
        round_h = int(width / block_size)
        for v in range(round_v):
            for h in range(round_h):
                v_start = v * block_size
                v_end = v_start + block_size
                h_start = h * block_size
                h_end = h_start + block_size

                image_patch = image[v_start:v_end, h_start:h_end]
                image_patch = np.float32(image_patch)
                patch_spectrum = cv2.dct(image_patch)
                patch_none_zero = np.abs(patch_spectrum) > self.dct_threshold
                hist += patch_none_zero.astype(int)

        _blur = hist < self.max_hist * hist[0, 0]
        _blur = (np.multiply(_blur.astype(int), self.hist_weight)).sum()
        return _blur / self.weight_total


def main():
    bd = BlurDetector()
    image = cv2.imread('../images/face2.png')

    start_time = time.time()
    result, image = bd.check_image_size(image)
    if not result:
        print("image expanded")

    blur = bd.get_blurness(image)

    print("blurness: {:.2f}".format(blur))
    print("used time: ", time.time() - start_time)

if __name__ == '__main__':
    main()

