# Show for at most 3 secs and print key value
import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)
key = cv2.waitKey(3000)
print('key =', key)
