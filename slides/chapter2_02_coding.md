---
type: slides
---

# In this section we will see some usefull operations 

---

# Reading an image from disk as greyscale

```python
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./misc/colab.png', cv2.IMREAD_GRAYSCALE) # read the image
print(img.shape) # display the dimension of the image
plt.imshow(img, cmap="gray") # show the image
```

```out
(691, 1564)
```
<img src="vl1/colab.png" alt="This image is in /static" width="80%">

---

# The end