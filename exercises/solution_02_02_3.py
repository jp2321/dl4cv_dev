import numpy as np
import cv2
from matplotlib import pyplot as plt


color_img = cv2.imread('exercises/dog.jpeg', cv2.IMREAD_COLOR)


color_resized = cv2.resize(color_img, (50,50)) # First the object needs to be defined that is resized.
# For defining the size, the tuple is used. 

# IMPORTANT: cv2 denotes the first parameter in the tuple as the width, the second as the height!
# In the numpy array, the first is the height, the second the width!

print(color_resized.shape)

plt.imshow(cv2.cvtColor(np.array(color_resized, dtype=np.uint8), cv2.COLOR_BGR2RGB))
plt.show()