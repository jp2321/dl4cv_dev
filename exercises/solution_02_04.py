import cv2
from matplotlib import pyplot as plt
from skimage.feature import hog

image = cv2.imread("exercise/dog.jpeg", 0) # Read image as greyscale
resize_img = cv2.resize(image, (300,300)) # Resize image

fd, hog_image = hog(resize_img, orientations=5, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, multichannel=False)

print(fd.shape)

plt.imshow(hog_image, cmap="gray") #show image 
plt.show()