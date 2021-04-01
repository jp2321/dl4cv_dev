---
type: slides
---

# In this section we will see how edges can be detected in the image 

---

# Canny Edge Detection

- Developed by Canny in 1986
- Edges are areas where the pixel value changes sharply. 
- Works only for one channel images (e.g., black and white)

Source: Canny (1986)

Note: In edge detection, areas belonging to an object's surface and their edges need to be separated. Areas belonging to the surface often have the same or similar pixel values. In contrast, edges occur where the pixel values change sharply, e.g., from bright to dark. The Canny Edge Detection algorithm developed by Canny in 1986 is one solution for detecting edges in the image. After the image transformation, only the edges will remain in the resulting image, while all the areas belonging to the surface are suppressed. The Canny edge detection algorithm works only for pictures with one channel. 

---

# Steps in Canny Edge Detection
1. De-noising with a Gaussian kernel
2. Sobel kernel to find edges
3. Calculate Edge Gradient and Angle of direction
4. Non-max suppression to get only "true" edges

Note: We will see all these steps in detail in the next few slides. Steps including in the canny edge detection are first a de-noising of the original image with a gaussain kernel, using a sobel kernel to find edges, the calculation of gradient and angle of the edge and the suppression of the content beloning to the surface. 

---

# Gaussian blur 

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/C_zFhWdM4ic" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Pound (2015c).

Note: This video explains very well what a Gaussian blur is and how kernels are applied to images. 
For now, it is enough to understand the basic concept.

The main takeaway from the video is that a gaussian blur is a simple filter applied to the image for (pre-) processing. It is often used for de-noiseing the image.  It is a kernel convolution operation, which we will discuss in a few weeks in all detail. For now, a kernel convolution is just a filter sled over the whole image to transform the input. The kernel is just a weighted average of the pixels in an area, and the gaussian blur follows a kernel with weights used from a normal distribution.  

---

# Sobel kernel 

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/uihBwtPIBxM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Pound (2015c)

Note: A sobel kernel detects edges. An edge is a sharp change in the pixel's intensity. The sobel kernel is applied for the x and y direction separately to detect vertical and horizontal edges. The result of the sobel operation is the measurement of pixel change in the area. It can also be used to calculate the direction of the edge.

---

# Edge detection

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/sRFM5IEqR2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Pound (2015a)

Note: The canny edge detection is an improvement over the sobel edge detection. It applies the gaussian blur for de-noising and the sobel operator to find the "strength" and direction of edges. Furthermore, it applies two thresholds, the first one searches for local maxima. These are possible candidates for edges. The second threshold just keeps the strongest edges. The canny process's result is to keep only edges that are strongest (above the threshold) or edges that are connected to the strong edges. 

---

# Math behind Canny

<img src="vl1/math_canny.png" alt="This image is in /static" width="30%">

Source: OpenCV (2020)

Note: The formulas on the left are the summary of the edge detection. The first one represents the Gaussian Kernel for blurring. Gx and Gy are the sobel operator for finding edges. The strength of the edge can be calculated by using Pythagoras, while the arctan function calculates the direction of the edge. 

---

# Canny Edge Detection

<img src="vl1/canny_edge_detector.jpg" alt="This image is in /static" width="30%">

<br>
<br>

<img src="vl1/canny_thresold.jpg" alt="This image is in /static" width="30%">

Image source: OpenCV (2020)

Note: The first figure visualizes that the gradient edge direction between C and A and B. As A has a higher pixel intensity as B or C, A is the point on the edge (sharp change in pixel value builds the edge, Gradient Direction).

The second visualization shows that min-max suppression. As the pixel value of A is larger than the max threshold, it is defined as a true edge. 
As points B, and C have a higher edge intensity as the minimum value, they are included in the output, if they are connected along the edge direction from A. Therefore, B and C are just named possible edges.

---

# Reading image from disk as colored one

```python
image = cv2.imread("/exercise/burger.png", 0) # read as greyscale
# Instead the Grayscale option written out as text the 0 is used here

canny_edge = cv2.Canny(image, 70, 120) # edge detection with min and max values
print(canny_edge.shape) # print the shape of the image

plt.imshow(canny_edge, cmap="gray") # visualize the image
plt.show()


```

```out
(1500, 2250)
```
<img src="vl1/burger_canny.jpeg" alt="This image is in /static" width="30%">

Note: This is the result of the edge detection. Different min-max values lead to different results.

---

<html>

<h3>References:</h3>

<list>
    <li>
    Canny, J. (1986). A computational approach to edge detection. IEEE Transactions on pattern analysis and machine 
        intelligence, (6), 679-698.
    </li>
    <li>
    	OpenCV (2020). Canny Edge Detection. Retrieved from: https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
    </li>
    <li>
    	Pound, M. (2015a). Canny Edge Detector - Computerphile. Retrieved from: https://www.youtube.com/watch?v=sRFM5IEqR2w 
    </li>
    <li>
    	Pound, M. (2015b). Finding the Edges (Sobel Operator) - Computerphile. Retrieved from: https://www.youtube.com/watch?v=uihBwtPIBxM
    </li>
    <li>
    	Pound, M. (2015c). How Blurs & Filters Work - Computerphile. Retrieved from: https://www.youtube.com/watch?v=C_zFhWdM4ic&feature=youtu.be 
    </li>

</list>
</html>

---

# The end