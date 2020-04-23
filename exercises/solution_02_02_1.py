import numpy as np
import cv2
from matplotlib import pyplot as plt


color_img = cv2.imread('exercises/dog.jpeg', cv2.IMREAD_COLOR)
print(color_img.shape)

subset=color_img[80:126,48:106,:] # select the dice with all channels

transformed_img = cv2.cvtColor(np.array(subset, dtype=np.uint8), cv2.COLOR_BGR2RGB)
plt.imshow(transformed_img)
plt.show()