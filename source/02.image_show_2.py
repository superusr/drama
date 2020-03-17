# Show image until 'esc' gets pressed
import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img)

while True:
    key = cv2.waitKey(30)
    if key == 27: break
