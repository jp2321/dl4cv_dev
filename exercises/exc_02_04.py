import cv2
from matplotlib import pyplot as plt
from skimage.feature import hog

image = cv2.imread("exercises/dog.jpeg", ____) # Read image as greyscale
resize_img = cv2.resize(______, (____,____)) # Resize image

fd, hog_image = ___(resize_img, orientations=___, pixels_per_cell=(___, ____),
                    cells_per_block=(___, ____), visualize=True, multichannel=False)

print(fd.shape)

plt.imshow(hog_image, cmap=_____) #show image 
plt.show()