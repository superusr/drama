# bgr -> rgb using slicing [stgart:stop:step]

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

plt.imshow(img[:,:,::-1], interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
