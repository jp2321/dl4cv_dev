---
title: 'Chapter 3: Deep Learning fundamentals'
description:
  'This chapter will introduce the deep learning fundamentals'
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="17" title="What is a neural network" type="slides">

<slides source="chapter3_01_neural_networks">
</slides>

</exercise>

<exercise id="18" title="Questions about neural networks">
<choice id=1>

<opt text="Were inspired by the human brain" correct="true">

Correct!

</opt>

<opt text="During the AI Winter most AI techniques were developed">

This is not the correct answer

</opt>

<opt text="Neural networks are highly linear functions">

This is not the correct answer

</opt>
</choice>

<choice id=2>
<opt text="Gradient descent is used to minimize the loss function" correct="true">

Correct!

</opt>

<opt text="Backpropagation is used for prediction">

This is not the correct answer

</opt>

<opt text="Feed-forward is used for updating the weights in the network">

This is not the correct answer

</opt>
</choice>

</exercise>

<exercise id="19" title="Hands on - coding a neural network">

 Use a neural network with two hidden layers with 10 and 20 neurons and 10 possible output classes. The task is a multi-class problem. The input size of the images is 32 by 32 pixels.

<codeblock id="03_01">

Multi-class problem require a special activation function.

</codeblock>


</exercise>

<exercise id="20" title="Dropout" type="slides">

<slides source="chapter3_02_dropout">
</slides>

</exercise>

<exercise id="21" title="Questions about dropout">
<choice id=1>

<opt text="Dropout increases the variance of the model" >

This is not correct!

</opt>

<opt text="Dropout can decrease the risk of overfitting" correct="true">

Correct!

</opt>

<opt text="Dropout increase the risk of overfitting">

This is not the correct answer

</opt>
</choice>

<choice id=2>
<opt text="With dropout different versions of the network are trained" correct="true">

Correct!

</opt>

<opt text="Dropout deletes completley neurons from the network">

This is not the correct answer

</opt>

<opt text="Dropout deletes layers from the network">

This is not the correct answer

</opt>
</choice>

</exercise>


<exercise id="22" title="Play with the code I">
	Use the Notebook provided in the Github to try out HOG as a feature extractor combined with a Machine Learning Algorithm. What is the performance in F1 and accuracy?
</exercise>

<exercise id = "23" title="Play with the code II">
	In the notebook use the implementation of the perceptron. Vary the learning rate and epochs and test the accuracy on the dataset. What do you notice?
</exercise>

<exercise id="24" title="Play with the code III">
	Use the Notebook provided in the Github and try out different settings for the Dense Neural network. Vary the number of hidden layers, the number of perceptrons per layer, activation functions, learning rates, batch sizes. What do you notice? Compare the performance to the ML Models with HOG/Edge Detection?
</exercise>

<exercise id="25" title="Play with the code IV">
	Create a new model and test different parameters for the dropout layer.
</exercise>