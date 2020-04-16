---
type: slides
---

# In this section we will see some useful operations 

---

# Reading an image from disk as greyscale

```python
img = cv2.imread('./misc/burger.jpeg', cv2.IMREAD_GRAYSCALE) # read the image
print(img.shape) # display the dimension of the image
plt.imshow(img, cmap="gray") # show the image
```

```out
(1500, 2250)
```
<img src="vl1/burger_bw.jpeg" alt="This image is in /static" width="30%">

Note: CV2's imread method is used to read images. One can specify if the image should be greyscaled or colored.
The return is a NumPy array; thus, the shape command can be used to inspect this size of the element.
Pyplot can be used to show the image; For greyscaled images, the colormap needs to be specified.

---

# Reading image from disk as colored one

```python
img = cv2.imread('./misc/burger.jpeg', cv2.IMREAD_COLOR) # read the image
print(img.shape) # display the dimension of the image
plt.imshow(img) # show the image
```

```out
(1500, 2250, 3)
```
<img src="vl1/burger_bgr.jpeg" alt="This image is in /static" width="30%">

Note: Here it can be seen that cv2 uses the BGR format, which would lead to wrong color schemas when it is visualized.

---

# Change color setting to RGB

```python
img = cv2.imread('./misc/burger.jpeg', cv2.IMREAD_COLOR) # read the image
print(img.shape) # display the dimension of the image
plt.imshow(cv2.cvtColor(np.array(img, dtype=np.uint8), cv2.COLOR_BGR2RGB)) # show the image with change for BGR to RGB
```

```out
(1500, 2250, 3)
```
<img src="vl1/burger_rgb.jpeg" alt="This image is in /static" width="30%">

Note: With the cv2 cvtColor command, the image color can be changed; Here, the option BGR2RGB is used. The image is transformed moreover to an unsigned integer 8 format, which has the value range between 0 and 255.

---

# The end