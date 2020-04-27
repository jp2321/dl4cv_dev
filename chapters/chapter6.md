---
title: 'Chapter 6: Object Detection'
description:
  'This chapter will introduce different techniques for object detection'
prev: /chapter5
next: /chapter7
type: chapter
id: 6
---

<exercise id="41" title="Object detection" type="slides">

<slides source="chapter6_01_ObjectDetection">
</slides>

</exercise>

<exercise id="42" title="Object detection architectures">
<choice id=1>

<opt text="YOLO is a two stage method">

This is not the correct answer.

</opt>

<opt text="Two stage methods split the localization and classification task">

This is not the correct answer.

</opt>

<opt text="Two stage methods split the regional proposal and classification task" correct=True>

Perfect!

</opt>

<opt text="Faster R-CNN is a one stage method">

This is not the correct answer.

</opt>
</choice>
</exercise>


<exercise id="43"  title="Hands on - YOLO">
    Fill in the blanks of the yolo network. Code the multi-output so that first the class prediction, afterwards the x1_prediction, y1_prediction, x2_prediction, y2_prediction are predicted. Assume that the network can detect 43 different classes
    Note that the probability of the object is encoded in the network output of the classes. It is the probability distribution over all 43 classes. To include the output in a object classification task, it has to be transformed to a output containing only zeros and a one for the predicted class and the probability of the predicted class needs to be added in the result vector.
<codeblock id="06_01">
</codeblock>
</exercise>

<exercise id="44"  title="Hands on - YOLO (2)">
 	Naturally, also transfer learning models can be used for the image classification part. Use InceptionV3 in this example to classifiy the 43 objects correctly as well as to predict the bounding boxes.
<codeblock id="06_02">
</codeblock>
</exercise>

<exercise id="45"  title="Hands on - YOLO (3)">
 	Complete the code so that you can change per parameter the trainability of layers.
 	The parameter trainable indicates if you want to set set a layer trainable or not, the number_of_layers parameter indicates the maximum index of the layers. For the first model all the layers should be frozen in the transfer learning part, the second model should only freeze the first five layers.
<codeblock id="06_03">
</codeblock>
</exercise>

<exercise id="46" title="Transfer Learning and Obejct detection" type="slides">

<slides source="chapter6_02_ObjectDetection_TransferLearning">
</slides>

</exercise>

<exercise id="47" title="Playing with the code - Object Detection">
	
</exercise>