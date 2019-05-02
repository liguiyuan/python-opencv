import cv2
import numpy as np

img = cv2.imread('../images/unequalized.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.equalizeHist(gray)

cv2.imshow('src', gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()