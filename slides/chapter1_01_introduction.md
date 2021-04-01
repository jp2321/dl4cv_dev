---
type: slides
---

# Intro to computer vision

---

# Computer vision applications

Computer vision is an interdisciplinary field that focuses on how computers can understand, rate, classify images, and videos.
Therefore it focuses on image preprocessing and feature extraction. 

Often techniques like deep learning are used to create artificial applications. 

There are different typical applications for computer vision:

- image classification
- object detection
- image segmentation
- video classification & segmentation 

---

# Image classification

<img src="vl1/predict-dog.png" alt="This image is in /static" width="90%">

Notes: Image classification focuses on categorizing the complete image. There can be binary classifications dog yes/no or multi-class applications. One famous one is the image-net challenge, where images are classified into 1000 different classes.

source = https://github.com/apache/incubator-mxnet/tree/master/example/image-classification 

---

# Object detection

<img src="vl1/object_detection.jpg" alt="This image is in /static" width="90%">

Notes: In object detection, the aim is to find different objects in an image. It is typically used in autonomous driving to detect other cars, pedestrians, or cyclists. Therefore not only the class of the object, but also the regions where it was detected is from interest. Consequently, a bounding box around the object with the corresponding object class needs to be predicted.

source = https://paperswithcode.com/task/real-time-object-detection

---

# Image segmentation

<img src="vl1/img_seg.jpg" alt="This image is in /static" width="90%">

Notes: Image segmentation is another widespread application in computer vision. Special training data is needed, on the one hand, a normal image, on the other hand, the segmented image. In the segmented image, each pixel is labeled into a specific class. Classes could be side-walk, street, cars, etc. This application aims to predict pixel classes as accurately as possible. 

source = https://paperswithcode.com/task/semantic-segmentation

---

# Video classification & segmentation

<img src="vl1/youtube8k.png" alt="This image is in /static" width="90%">

Notes: The previous applications can not only be performed on static images but also in videos. A video is roughly speaking nothing else than x-images per second. Without being able to perform video analysis, a lot of modern business applications would not be implemented.

source = https://research.google.com/youtube8m/

---

# Let's get started!
