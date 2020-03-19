---
type: slides
---
# Intro to computer vision

---

# Computer vision applications

Computer vision is an interdisciplinary field to focuses on how computers can understand, rate, classify images and videos.
Therefore it focus on image preprocessing and feature extracting. 

Often techniques like from deep learning are used to create artifical applications. 

There are different typical applications for computer vision:

- image classification
- object detection
- image segmentation
- video classification & segmentation 

---

# Image classification

<img src="vl1/predict-dog.png" alt="This image is in /static" width="90%">

Notes: Image classification focuses on categorizing the complete image. There can be binary classifications dog yes/no or multi-class applications. One famous one is the image-net challenge where images are classified into 1000 different classes.

---

# Object detection

<img src="vl1/object_detection.jpg" alt="This image is in /static" width="90%">

Notes: In object detection the aim is to find different objects in an image. It is typically used in autonomous driving to detect other cars, pedastrians or cyclist. Therefore, not only the class of the object but also the regions where it was detected is from interest. Consequently, also a bounding box around the object needs to be predicted with the corresponding object class.

---

# Image segmentation

<img src="vl1/img_seg.jpg" alt="This image is in /static" width="90%">

Notes: Image segmentation is another wide spread application in computer vision. Special training data is needed, on the one hand a normal image, on the other hand the segmented image. In the segmented image, each pixel is labeled into a specific class. Classes could be side-walk, street, cars etc. The aim of this application is to predict for images the pixel classes as accurate as possible. 

---

# Video classification & segmentation

<img src="vl1/youtube8k.png" alt="This image is in /static" width="90%">

Notes: The previous applications can not only be performed on static images but also in videos. A video is roughly speaking nothing else than x-images per second. Without being able to perform video analysis a lot of modern business applications were not been implemented.

---

# Let's get started!
