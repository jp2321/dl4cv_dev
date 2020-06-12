---
type: slides
---

# Semantic Segmentation

Note: There are several different segmentation tasks. In the course, we will focus on semantic segmentation. Semantic segmentation is the classification of each pixel belonging to a certain class or the background. Instance segmentation,  another form of segmentation is the classification of pixels belonging to an "instance" which is the combination of object detection and predicting to which object instance this pixel belongs.

---

# The characteristics of semantic segmentation

<img src="vl6/img_seg.jpg" width="50%">

Note: So far, in the course, we discovered different architectures of networks, we worked with multi-output models in object detection. For semantics segmentation, we will combine different techniques. The important difference between the previous chapters compared to segmentation is that the output of the network is an image itself. Therefore, image segmentation is one of numerous encoder-decoder tasks. The network performs an encoding of the original input to a different representation with a high abstraction of the information. The decoder part of the network transforms the representation to the output. Image segmentation is another vital technique for autonomous robotics and driving tasks. The street, sidewalk, pedestrians, etc. have to be distinguished so that the car can detect the street and where to drive. 
For n different classes to segment, the label as n different channels, each indicating a different class. A one indicates that this pixel belongs to that class.

---

# Encoder-decoder network

<img src="vl6/ConvDeconv.png" width="70%">

Source: Sarafianos, 2016

Note: Here, the structure of the encoder-decoder network can be seen very well. The encoder, a classical CNN, encodes the information from the original image in another representation. Often, the encoded part is much smaller due to the pooling-layers. However, it contains detailed information on the image features (objects, parts). The information was transformed from 3 channels (RGB) to maybe 2048 channels belonging to abstract things. Nevertheless, as the encoded part is much smaller, the spatial representation is very rough compared to the original input. 
 

The decoder uses the encoded information and tries to reproduce the output. In an auto encoder-decoder case, it would try to reproduce the input image itself from the encoded information. One can think about this as a type of compression like mp3 for images, where the image is represented in a very dense format. In the case of semantic segmentation, not the input image is reconstructed, but information about the different semantic parts of the image.


---

# Encoder-decoder network II

<iframe width="750" height="450" src="https://www.youtube.com/embed/1icvxbAoPWc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Source: Pound (2018)

---

# Network structure for segmentation - FCNs

- by Long, Shelhamer & Darrell, 2015
- first suggestion of a fully connected network
- No dense layers in the network 
- Encoder: Classical CNN e.g. VGG
- Decoder: 1 by 1 Convolutions for classification of pixels + Upsampling
- Different versions: FCN-32, FCN-16, FCN-8
- Named after the number of upsampling steps in the last layer

<img src="vl6/fcn.png" width=500 height=500>

Source:  Long, Shelhamer & Darrell, 2015

Note: The first algorithm applied for segmentation is thus called "fully convolutional network" and was published in 2015. The encoder is a normal CNN e.g. VGG. The decoder has 1 by 1 convolutions for predicting for each pixel the class label plus an upsampling layer to scale the prediction to the original size of the image. Different versions of the FCN exist, with some connecting layers between the encoder and decoder. In the original paper, a deconvolutional layer is used for the upsampling. However, we used here normal upsampling layer with bilinear interpolation. This technique can upsample the input by just duplicating the rows and columns (Long, Shelhamer & Darrell, 2015). 


---

# FCN-8

<img src="vl6/fcn_8.png" width="50%">
<br>
Image Source:  https://www.researchgate.net/figure/Fully-convolutional-neural-network-architecture-FCN-8_fig1_327521314

Note: Here, we see a FCN-8 example. For FCN-8 and FCN-16 skip-connection as in the ResNet are used to transfer some of the original representation (detailed spatial information) into the decoder part of the network. Notice here, that in FCN-8 the main path is first upsampled two times. Afterward,  the prediction of the first branch is added. The result is again upsampled two times, and the other branch is added to the result. Finally, the classification is performed, and the image is upsampled again, now by 8 times, to match the input dimensions.

---

# FCN Video explanation 

<html>
<iframe width="853" height="480" src="https://www.youtube.com/embed/-3ylPH3BCWY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Adams (2019a)

---

# U-Net

- By Ronneberger, Fischer & Brox, 2015 
- Uses also the features from lower-level layers
- Performs upsampling by deconvolution

<img src="vl6/u-net-architecture.png" width=500 height=500>

Source: Ronneberger, Fischer & Brox, 2015

Note: For the other often-used network, the U-Net, used in medicine, so-called deconvolutions are used. It is called U-Net because it looks like a U. The main characteristic is that some layers outputs from the encoder are copied and concatenated with layers in the encoder. 

---

# Deconvolution

<img src="vl6/deconv.gif" width=500 height=500>

Source: Lane (2017)

Note: Deconvolution, also known as transposed convolution or subpixel convolution, can transform the input through applying a kernel so that the output has larger dimensions than the original input. The best and most intuitive way of thinking of a deconvolution is depicted above. In this case, a single input value is multiplied by a kernel, the black square box with dimensions 3 by 3 to build a new output of 3 by 3. With strides 1, the blue input of 4 by 4 is transformed to an 6 by 6 output (Ronneberger, Fischer & Brox, 2015, Dumoulin & Visin, 2016). 

More details for deconvolutions can be found <a href="https://arxiv.org/abs/1603.07285">here</a>

---

U-Net video explanation

<html>
<iframe width="857" height="482" src="https://www.youtube.com/embed/I0xqVK329Og" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Adams (2019b)

---

# Evaluation of segmentation networks

- Pixel-wise accuracy
- IoU

---

# Pixel-wise accuracy 

Percentage of pixel classified correctly in the image.

- Easy to understand
- Class imbalance can be a significant problem


<img src="vl6/accuracy.png" width=500 height=500>

Image source: (Tiu, 2019)

Note: For evaluating the performance of image segmentation models, there are multiple possibilities. Two of them are pixel-wise accuracy and IoU. While pixel-wise accuracy is easy to understand as it is the mean accuracy of the predicted pixels per class, the major disadvantage of this evaluation method is that the scores are effected by class imbalances. In the segmenting example above, 5% of the pixels are showing a ship (colored blocks). The other 95% of the pixel does not belong to the ship class. Thus, an accuracy of 95% in the ship class would mean that actually, no ship is segmented as this is the baseline performance when predicting that there are no ships at all (and  all pixels are predicted to be background). 

A prediction would than look like this

<img src="vl6/accuracy_2.png" width=200 height=200>



---

# IoU

- Intersection over union also known as Jaccard Index measure the overlap of the predicted segmentation and the ground truth over the by the area of the predicted segmentation and the ground truth.

<img src="vl6/iou_equation.png" width=500 height=500>

<img src="vl6/iou_formula.png">


Note: For a more realistic evaluation, IoU is used. This concept is known from our last lesson about object detection. The area of the overlap of prediction and target is compared to the area of union of target and prediction. Scores of 0 would mean that the area is not classified correctly at all. The IoU is calculated per class and can then be averaged to give an overall score for the image.

---

<html>
<h3>References</h3>
<list>
        <li>Adams, S. (2019a). Fully Convolutional Network - Custom Semantic Segmentation p.10. Retrieved from: https://www.youtube.com/watch?v=-3ylPH3BCWY</li>
        <li>Adams, S. (2019b). U-Net - Custom Semantic Segmentation p.11. Retrieved from: https://www.youtube.com/watch?v=I0xqVK329Og</li>
        <li>Dumoulin, V., & Visin, F. (2016). A guide to convolution arithmetic for deep learning. arXiv preprint 
            arXiv:1603.07285.</li>
        <li> Jorden, J. (2018). Evaluating image segmentation models. Retrieved from: 
            https://www.jeremyjordan.me/evaluating-image-segmentation-models/ </li>
        <li> Lane, T. (2018). Transposed convolutions with MS Excel. Retrieved from: https://medium.com/apache-mxnet/transposed-convolutions-explained-with-ms-excel-52d13030c7e8 </li>
        <li>Long, J., Shelhamer, E., & Darrell, T. (2015). Fully convolutional networks for semantic segmentation. 
            In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 3431-3440).</li>
        <li>Pound, M. (2018). Encoder Decoder Network. Retrieved from: https://www.youtube.com/watch?v=1icvxbAoPWc</li>
        <li>Pröve, P. (2017). An Introduction to different types of convolutions in deep learning: Retrieved from: https://towardsdatascience.com/types-of-convolutions-in-deep-learning-717013397f4d
        <li>Raschka, S., & Mirjalili, V. (2019). Python Machine Learning: Machine Learning and Deep Learning with 
            Python, scikit-learn, and TensorFlow 2. Packt Publishing Ltd.</li>
        <li>Ronneberger, O., Fischer, P., & Brox, T. (2015, October). U-net: Convolutional networks for biomedical 
            image segmentation. In International Conference on Medical image computing and computer-assisted 
            intervention (pp. 234-241). Springer, Cham.</li>
        <li>Sarafianos, N. (2016). ICIP 2016: Deep Learning Trends and Open Problems. Retrieved from: https://nsarafianos.github.io/icip16 </li>
        <li> Tiu, E. (2019). Metrics to evaluate your semantic segmentation model. Retrieved from: 
                https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2 
        </li>
        <li></li> Tshang, S. (2018). Review: FCN- Fully Convolutional Network (Image segmentation). Retrieved from: https://towardsdatascience.com/review-fcn-semantic-segmentation-eb8c9b50d2d1
        <li>Vasilev, I. (2019). Advanced Deep Learning With Python: design and implement advanced next-generation 
            ai solutions using tensorflow and pytorch. S.l.: PACKT PUBLISHING LIMITED.</li>
        
</list>
</html>

---

# Let's do some coding ... 