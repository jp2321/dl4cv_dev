---
type: slides
---

# HoG: Histogram of oriented gradients

---

# HoG

- by Dalal & Triggs (2005)
- purpose: Detecting human detection in images
- Some similarities to Canny Edge Detector in the image preprocessing
- Aim: Describe with a histogram the image as accurately as possible
- Works for B&W and color images
- Can be used as a feature extractor to use in a ML pipeline

Source: Dalal & Triggs (2005)

---

# Steps HoG
1. De-noiseing with a Gaussian kernel
2. Calculate Edge Gradient and Angle of direction
3. Compute the gradients for each cell
4. Normalize results across blocks

Note: We will see all these steps in detail in the next few slides

---

# HoG

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/4ESLTAd3IOM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Ahmed (2018)

Note: This video explains very well, what HoG is

---

# Block normalization

<img src="vl1/hog-16x16-block-normalization.gif" alt="This image is in /static" width="30%">

Note:
Image source: Mallik, (2016)

--- 


# Design decisions

- how many bins has the histogram?
- how large is the cell
- how many cells are used to build a block 


Note: Cell: Area for which the histogram is calculated
Block: How many cells are considered for normalization
Bins: How many discrete categorize are in the histogram?

---

# HoG in Python

```python
image = cv2.imread("exercises/burger.jpeg", 0)
resize_img = cv2.resize(image, (150,150))

fd, hog_image = hog(resize_img, orientations=9, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=False)

print(fd.shape)

# Plot histogram
plt.plot(fd)
plt.ylabel("Normalized Magnitude")
plt.xlabel("Concatenated orientations of cells")
plt.show()

# Plot hog transformed images
plt.imshow(hog_image, cmap="gray")
plt.show()

```

```out
(729,)
```

---


# Output images 

<img src="vl1/histogram.png" alt="This image is in /static" width="25%">

<img src="vl1/burger_hog.png" alt="This image is in /static" width="25%">

---

<html>
<list>
    <li>
        Ahmed, R. (2018). Computer Vision with OpenCV: HOG Features Extraction. Retrieved from: https://www.youtube.com/watch?v=4ESLTAd3IOM
    </li>
    <li>
    Dalal, N., & Triggs, B. (2005). Histograms of oriented gradients for human detection. In 2005 IEEE 
        computer society conference on computer vision and pattern recognition (CVPR'05) (Vol. 1, pp. 886-893). 
        IEEE.
    </li>
    <li>
    	Malkik, S. (2016). Histogram of Oriented Gradients. Retrieved from: https://www.learnopencv.com/histogram-of-oriented-gradients/
    </li>
    <li>
      Scikit-image (2020). Histogram of Oriented Gradients. Last access, 22.02.2020: https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html   
    </li>
</list>

</html>

---

# Let's do some coding ... 