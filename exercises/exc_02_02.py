import numpy as np
import cv2
from matplotlib import pyplot as plt

bw_img = cv2.imread(_______, _______)
print(bw_img.shape)
plt.imshow(bw_img, ______)
plt.show()

color_img = cv2.imread(______,_______)
print(color_img.shape)
transformed_img = cv2.cvtColor(________, _______)
plt.imshow(transformed_img)
plt.show()