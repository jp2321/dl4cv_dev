---
type: slides
---

# What is special about image data

Notes: You probabily know that the set-up in classical machine learning is that there is a target and tabular data. Each row in table represents one observations. This data is called structured as the table has specific column names and structures the features.

However, text and image data are unstructured data, as they not follow a specific schema. The cat in the image for example does not need to be always in the left lower edge. Moreover, different lighting in the image, zoom level, perspectives etc will give millions of possibilities how a cat may look like. Additionally, image data is also n-dimensional. Thus each observation (image) has a certain width, height and channels. Therefore each image is often represented in a n-dimensional array.

This data structure might be very counterintuitiv when you work with it for the first time but you will get used to it very fast.

---

# Black and white images

<img src="vl1/grey_scaled.png" alt="This image is in /static" width="80%">

- Two dimensional array 
- rows = height 
- columns = width 
- shape: (5,8) or (5,8,1) 
- minimum value: 0 
- maximum value: 255 

Note: A grey-sclaed image in a two dimensional array of shape (height, width). Sometimes it is also represented in a three dimensional array of (height, width, channels), where just one channel exists. The magnitutde of the whiteness of the image.

---

# Colored images 

<img src="vl1/rgb.png" alt="This image is in /static" width="90%">

Note: Images are n-dimensional arrays with each element in the range of 0 to 255. The size of the image is determining the array size. The array has the dimensions of (height, width, channels). For a grey scaled image, there is just one channel, describing the intensity of the whiteness of that pixel. In normal colored images, there are three different channels, namely red, green, and blue (RGB). Through the combination of these three colors, each color can be displayed. There might be special cases where more than three channels exist, for example, satellite images, including also radar, infrared, or other waves. For more details see <a href="https://sentinel.esa.int/web/sentinel/missions/sentinel-2/satellite-description">here</a>. Other examples are medical images from a CT scan, where multiple slices exist.
---

# Libraries used 

In the course we will discover different libraries used for image preprocessing in python.

CV2 is a library which can be used in C, Python und Java for image preprocessing

Scikit-image an other well known library for preprocessing in python

Note: CV2 per default displays colored images not in RGB but BGR. Thus the channels are changed. For displaying the cv2 read images in the correct color schema a transformation is needed. We will discover this in the following coding exercises.

---

# Hurray!