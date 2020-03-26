---
title: 'Chapter 4: Convolutional neural network'
description:
  'This chapter will introduce CNNs'
prev: /chapter3
next: /chapterend
type: chapter
id: 4
---

<exercise id="22" title="What is a cnn?" type="slides">

<slides source="chapter4_01_cnn">
</slides>

</exercise>

<exercise id="23"  title="Hands on - CNNs">
	Use a convolutional neural network for classifying the 32 by 32 colored images.
	The first convolutional layer should have 16 filters with a 3 by 3 kernel, followed by a max pooling.
	The second convolutiona layer should have 32 filters with a 3 by 3 kernel
	The first fully connected layer should connect to a flatten and have 32 neurons
	Throughout the hidden layers, relu activations are used
<codeblock id="04_01">

Fill in the blanks.

</codeblock>
</exercise>

<exercise id="24" title="Batch Norm and Spatial Dropout" type="slides">

<slides source="chapter4_02_batch_norm_spatial_dropout">
</slides>
</exercise>

<exercise id="25"  title="Hands on - CNNs (2)">
	This given network is overfitting. Therefore you decided to use Spatial Dropouts for the convolutional layers as well as Dropouts for the fully connected layers.

	Dropout rates are 0.2, 0.5, 0.5 - Fill in the blanks

<codeblock id="04_02">

Fill in the blanks.

</codeblock>
</exercise>