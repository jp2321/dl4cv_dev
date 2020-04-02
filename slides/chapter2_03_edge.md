---
type: slides
---

# In this section we will see how edges can be detected in the image 

---

# Canny Edge Detection

- Developed by Canny in 1986
- Edges are pixels where the pixel's magnitude changes the strongest
- Works only for one channel images (e.g., black and white)

Source: Canny (1986)

---

# Steps in Canny Edge Detection
1. De-noiseing with a Gaussian kernel
2. Sobel kernel to find edges
3. Calculate Edge Gradient and Angle of direction
4. Non-max suppression to get only "true" edges

Note: We will see all these steps in detail in the next few slides

---

# Gaussian blur 

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/C_zFhWdM4ic" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=uihBwtPIBxM 

Note: This video explains very well what a Gaussian blur is and how kernels are applied to images. 
For now, it is enough to understand the basic concept. We will talk about kernels in a few more sessions in detail.

---

# Sobel kernel 

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/uihBwtPIBxM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=uihBwtPIBxM

---

# Edge detection

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/sRFM5IEqR2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=sRFM5IEqR2w 

---

# Math behind Canny

<img src="vl1/math_canny.png" alt="This image is in /static" width="30%">

Source: OpenCV (2020)

---

# Canny Edge Detection

<img src="vl1/canny_edge_detector.jpg" alt="This image is in /static" width="30%">

<br>
<br>

<img src="vl1/canny_thresold.jpg" alt="This image is in /static" width="30%">

Image source: OpenCV (2020)

Note: The first figure visualizes that the gradient edge direction between C and A and B is used to identify B as an edge point. The second visualization shows that min-max suppression. As the pixel value of A is larger than the max threshold, it is defined as a true edge, B, and C as possible edges.  

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
</list>
</html>

---

# The end