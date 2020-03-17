import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

print('type(img) =', type(img))
print('img.shape, img.dtype =', img.shape, img.dtype)