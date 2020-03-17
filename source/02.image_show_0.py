import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)
cv2.waitKey()
