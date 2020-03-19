import numpy as np
import cv2
from matplotlib import pyplot as plt

bw_img = cv2.imread('dog.jpeg', cv2.IMREAD_GRAYSCALE)
print(bw_img.shape)
plt.imshow(bw_img, cmap="gray")

color_img = cv2.imread('dog.jpeg', cv2.IMREAD_COLOR)
print(color_img.shape)
color_img = cv2.cvtColor(np.array(color_img, dtype=np.uint8), cv2.COLOR_BGR2RGB)
plt.imshow(color_img)