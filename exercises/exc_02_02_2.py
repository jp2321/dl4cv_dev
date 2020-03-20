import numpy as np
import cv2
from matplotlib import pyplot as plt


color_img = cv2.imread('exercises/dog.jpeg', cv2.IMREAD_COLOR)
print(color_img.shape)

image_red = color_img.copy()
print(image_red.shape)

image_red[___:____,____:____,____]=255 #BGR
plt.imshow(cv2.cvtColor(np.array(image_red, dtype=np.uint8), cv2.COLOR_BGR2RGB))