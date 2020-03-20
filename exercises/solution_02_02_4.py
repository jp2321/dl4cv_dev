import numpy as np
import cv2
from matplotlib import pyplot as plt


image = cv2.imread('exercises/dog.jpeg', 0)
canny_edge_1 = cv2.Canny(image, 50, 150)
print(canny_edge_1.shape)

plt.imshow(canny_edge_1, cmap="gray")
plt.show()

canny_edge_2 = cv2.Canny(image, 100, 200)
print(canny_edge_2.shape)

plt.imshow(canny_edge_2, cmap="gray")
plt.show()