---
type: slides
---

# Object detection

Note: Instead of classifying the image into a category, often a more fine-granular view is needed for advanced business tasks. Therefore, information about which objects are in the image and where they are, are of interest. Especially in autonomous driving or tasks which include a robot, this information is necessary to "run" these machines. For autonomous driving, for example, it is necessary not only to detect if a stop sign is in the image, but to detect every stop sign and to understand where they are.

---

# An simplified example 

<img src="vl5/traffic_sign.png" width="50%">

Note: This example shows a simplified version of an object detection task, where just one object in the image exists. To perform the object localization, the bounding box area needs to be predicted plus a classification of the object itself. 

Sometimes the bounding box is framed (as this example) as the coordinates of two corners, where x1,y1 is the coordinate of edge, x2,y2 the coordinate of a diagonal edge. The height of the bounding box is y1-y2, and the width is x1-x2. Sometimes the dataset labels contain these measures. In other examples, as listed in theory on the next slide, the coordinates are annotated with b1 to b4. b1,b2 are equal to x1,y1, and are one corner of the bounding box. b3 is the height of the bounding box, and b4 annotates the width of the bounding box.

---

# Bounding Boxes and outputs

[b1,b2,b3,b4,p1,c1,c2, ...cn]

In the easiest case, one object per image:
b1-b4: b1,b2: coordinate of one edge of the bounding box, b3: height of the bounding box, b4: width of bounding box 
c1-cn: One hot encoded vector of the class
p1: Probability that object is included

--> Vector of length 5+n 


Source: Vasilev, 2019

Note: For object detection, it is not sufficient to output just the one-hot encoded vector for the object class. At a minimum, also the one coordinate of the bounding box and the height and width of the bounding box need to be predicted. Moreover, the probability of the object class needs to be calculated too. Consequently, the minimum output for one bounding box is 5+n.  

---

# Naive approach


- Divide image into regions 
- Pass regions to a normal CNN
- Bounding box has the coordinates of the region that was passed to the network

Downside: A lot of regions would need to be passed to the network if a lot of objects are in the image. This is very inefficient in terms of computation.

Source: Vasilev, 2019

Note: In a naive approach, the image would be cut into regions. Each region would be passed to a CNN to classify the whole region. The coordinates of the bounding box are the coordinates of the region. While this approach is very easy to implement, it has the downside, that a lot of regions may be passed through the CNN, being slow and inefficient in computation.

---

# Types object detection networks

One stage approach

        Detection and classification performed in one step/network

        Example: YOLO


Two stage approach

    Step 1: Proposing interesting regions
    
    Step 2: Classification and Bounding Box Regression of the regions
    Example: Fast R-CNN, Faster R-CNN

Note: In general, two different model architectures exist for object detection, One-stage, and two-stage models. While in a two-stage model, the regional proposal of objects is separated from the classification and location task, one-stage models combine everything in one network. The most commonly known one-stage method is YOLO (You only look once). R-CNN, Fast R-CNN, and Faster R-CNN are two-stage methods (Vasilev, 2019).

---

# R-CNN

- Selective search for regional proposal, 2000 suggestions
- CNN for classification
- Bounding box by image part
- Downside: slow, 45 seconds per image, no real-time possible


<img src="vl5/rcnn.png" width="35%">

Image source: Ghandi, 2018 <br>
Source: Vasilev, 2019

Note: R-CNN was the first well-performing object detection method. Via selective search, interesting regions in the image are identified. Often 2000 different regions are sampled per image. Each of the 2000 different images are passed through a CNN for object classification. The bounding box does not need to be calculated as the image part sets the bounding box itself. While this method is easy to implement, it comes with the downside of many predictions per image. Thus, it is relatively slow, 45 seconds per image, and no real-time application is possible, for example, autonomous driving (Vasilev, 2019).

---

# Fast R-CNN

- CNN used to create convolutional features
- Interesting areas are identified by selective search
- Fully Connected layers of classification and regression

<img src="vl5/fast_rcnn.png" width="50%">

Image source: Ghandi, 2018 <br>
Source: Vasilev, 2019

Note: Thus, R-CNN was improved, and Fast R-CNN was developed. While the overall idea stays the same, the whole image is first passed through and CNN. The convoluted activations are derived, and selective search is applied to the convoluted images. Thus, one pass through the CNN is needed. A special ROI pooling is performed to save the area of interest, and fully connected layers perform the classification of the object as well as the bounding box prediction (Vasilev, 2019).

---

# Faster R-CNN

- CNN used to create convolutional features
- Regional Proposal Network (RPN) identified regions
- Proposals are classification and regression

<img src="vl5/faster_rcnn.png" width="30%">

Image source: Ghandi, 2018 <br>
Source: Vasilev, 2019

Note: While Fast R-CNN is faster than R-CNN, it might not be fast enough, so Faster R-CNN comes into play. Compared to Fast R-CNN, instead of using selective search, a regional proposal network is trained for suggesting intelligently areas of interest. The Regional Proposal Network is a separately trained CNN for just predicting interesting regions in images (Vasilev, 2019).

---

# YOLO

- One stage method
- Divide image into S by S grid
- Each grid can have m objects; Anchorbox resembles 1-to-m relationship
- CNN does classification and regression for each grid
- Fastest detection algorithm: less than 1 second per image

<img src="vl5/yolo.png" width="50%">

Image source: Ghandi, 2018

Note: Yolo is up to now the fastest method for object detection. As it is built on just one neural network, different assumptions need to be made. First, the image is divided into an S by S grid. In each grid, m objects can be found. On each grid, the CNN is applied with the output of m times the 5+n output vector. The Anchorboxes are in a 1 to m relationship so that each object belongs to one anchor box (which can be spread over multiple grids). However, each grid has maximum of m objects. It is with less than 1 second per image the fasted object detection methods (Vasilev, 2019).

---

# IoU

- "Intersection over union"
- Denoising the prediction
- Discard box when IoU larger than the threshold (mostly 0.5)

<img src="vl5/iou_equation.png" width=300 height=300>

Source: Rosenbrock, 2016

Note: For the described methods, the IoU concept is used to denoise the predictions. IoU stands for intersection over union, where for all the derived object predictions, the area of overlap is divided by the area of union. Most of the time, a fixed threshold, for example, 0.5, is applied, discarding all the predicted bounding boxes and detection above the threshold. This deletes multiple detections of the same object (Rosenbrock, 2016, Vasilev, 2019). This is also often known as non-max suppression. In the image in the slides, one bounding box is the prediction, the other box is the ground truth.

IoU is not only used for the non-max suppression in the prediction but can also be used as a performance measure for the bounding box regression. It is extremely difficult to predict the bounding box and interpret the performance as a regression problem. The IoU states, how well the predicted bounding box overlaps with the ground truth labeled bounding box and thus combines the performance for the bounding box in one number (Ganesh, 2019).

---

# Bounding Box Video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/yo9S3eNtkXc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Deeplearning.ai (2017b)


---

# Anchor Boxes 

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/RTlwl2bv0Tg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Deeplearning.ai (2017a)

---

# Yolo Video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/9s_FpMpdYW8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Deeplearning.ai (2017c)

---

# Advice

- Use one of the pre-implemented models of R-CNN, Fast/Faster R-CNN or Yolo for the project

Note: While we will have a closer look at how object detection works on a simple case with just one object per image, it is worthwhile to use one of the various implementations of R-CNN, Fast/Faster R-CNN, Yolo etc. already written for Keras and Tensorflow.

---

<html>
<h3>References</h3>
<list>
    <li>Deeplearning.ai (2017). C4W3L08 Anchor Boxes. Retrieved from: https://www.youtube.com/watch?v=RTlwl2bv0Tg </li>
    <li>Deeplearning.ai (2017). CNN W3L05 : Bounding Box Predictions. Retrieved from: https://www.youtube.com/watch?v=yo9S3eNtkXc </li>
    <li>Deeplearning.ai (2017). C4W3L09 YOLO Algorithm. Retrieved from: https://www.youtube.com/watch?v=9s_FpMpdYW8 </li>
    <li>Ganesh, P. (2019). Object Detection Simplified. Retrieved from: https://towardsdatascience.com/object-detection-simplified-e07aa3830954 </li>
    <li>Ghandi, R. (2018). R-CNN, Fast R-CNN, Faster R-CNN, YOlo. Retrieved from https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e Last accesss: 28.02.2020</li>
        <li>Raschka, S., & Mirjalili, V. (2019). Python Machine Learning: Machine Learning and Deep Learning with 
            Python, scikit-learn, and TensorFlow 2. Packt Publishing Ltd.</li>
    <li>Rosenbrock, A. (2016). Intersection over union (IoU) for object detection. Retrieved from: https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/ Last access: 28.02.2020</li>
    <li>
        Stallkamp,J.,Schlipsing, M., Salmen, J., Igel, C. (2012).  Man vs. computer: Benchmarking machine learning 
        algorithms for traffic sign recognition, Neural Networks, Available online 20 February 2012, ISSN 0893-
        6080, 10.1016/j.neunet.2012.02.016. (http://www.sciencedirect.com/science/article/pii/S0893608012000457) 
    </li>
        <li>Vasilev, I. (2019). Advanced Deep Learning With Python: design and implement advanced next-generation 
            ai solutions using tensorflow and pytorch. S.l.: PACKT PUBLISHING LIMITED.</li>
        
</list>
</html>

---

# Let's do some coding ... 