---
type: slides
---

# Neural networks 

---

# Neural networks

Historical development

- Theoretical development in the 1940s by McCulloch and Pitt
- Similarity to the human brain
- Fundamental method: Perceptron (Rosenblatt, 1958)
- AI Winter between 1974-1980 and 1987-1993
- Backpropagation 1986s 

Advantage of Deep Learning: Multiple non-linear transformations 

Source: Raschka & Mirjalili (2019), Rosenblatt (1958),  Rumelhart et al., (1986)

Notes: The idea of building an artifical object similar to the human brain that can learn somethings dates back to the ideas of McCulloch and Pitt in the 1940s. The fundamental method is a perceptron, developed by Rosenblatt in 1958. Mathematically speaking, it is the weighted sum of the inputs used in a non-linear mathematical function to map some output. In the AI Winter, the technology was not extensively researched as computational costs were high, and other machine learning algorithms performed better. The concept of AI was questioned from many researchers and practioners as the expected results could not be reached and the term seemed overhyped. Moreover a lot of companies from the AI Industrie collapsed. A huge step forward was made by development of backpropagation in 1986, which is used until today to train a neural network. Neural networks got in the last years again attention as with the increasing computing power, and the usage of Graphical processing units (GPUs), more complex neural networks could be trained with almost human performance or surpassing it in some applications. The advantage compared to classical machine learning algorithms are that deep learning models can model complex non-linear relationships between input and output to increase the prediction performance.

---

# Perceptron

<img src="vl2/perceptron.png" alt="This image is in /static" width="70%">
<img src="vl2/update_rule.png" alt="This image is in /static" width="30%">

Source: Raschka & Mirjalili (2019)

Note: The perceptron algorithm is the necessary foundation for modern deep learning algorithms. Invented by Rosenblatt in 1958, a perceptron is representing one single neuron. If a human neuron fires, it gets activated. In the computer version,  the inputs to the neuron are above a threshold. Very similar to this is the perceptron. It weights its inputs according to the weight coefficients, sum them up, and applies an activation function. In the original paper of Rosenblatt, it is a stepwise function. The weights are learned by an update rule. For each training sample, they get updated. The new weights are the weights plus the update. The learning rate (eta) determines how fast the weights are updated. When the ith sample is false predicted, the weights are pushed towards the correct direction (Raschka & Mirjalili, 2019, Rosenblatt, 1958).

---

# Neural network

<img src="vl2/neural_network.png" alt="This image is in /static" width="70%">

Source: Raschka & Mirjalili (2019)

Note: A neural network is a combination of neurons. These neurons are combined in multiple layers, whereas each neuron from a layer l is connected to all neurons in the following layer. The input of the layer l is the weighted combination of the neurons of the previous layer l-1 plus a bias (Raschka & Mirjalili, 2019). A network in its purest form has an input layer, one hidden layer, and one output layer. We call networks deep when there are multiple hidden layers. For each layer, we can use a specific activation function applied in all neurons.

---

# Process flow 

1. Forward propagation -> use network for prediction
2. Compute cost function and error of the current prediction
3. Backward propagation (calculate the gradient of the cost function)
4. Update parameters (according to the backpropagation)

Note: We will discuss these steps in the following slides

---

# Feed-forward

<img src="vl2/feedforward.png" alt="This image is in /static" width="70%">

Source: Raschka & Mirjalili (2019)

Note: In the forward pass, inputs are transformed and passed from layer to layer to predict the output.
For the first neuron in the hidden layer, the input neurons are weighted, and a bias is added. This neuron uses a specific activation function and creates its output. This is performed for all neurons in the hidden layer.
The next layer's neuron weights all the outputs of its previous layers, add a bias, and uses an activation function.
Also, the output layer uses all the inputs from the previous hidden layer weights them, activates, and creates an output. This final output is the prediction of the neural network. The weights for each neuron are learned during the second important step in a neural network: backpropagation. To initalize the weights bevor the first training, random numbers are used. 

---

# Backpropagation

<img src="vl2/backpropagation.png" alt="This image is in /static" width="50%">

Source: Raschka & Mirjalili (2019)

Note: While the feed-forward process is just the pass from inputs to predictions, this process helps the neural network to learn. Backpropagation was introduced in 1986 by Rumelhart et al. and is mostly used to train the neural network. The essential idea is that the weights should be optimized so that the loss function and the error are minimized. First of all, the error is calculated by comparing the prediction with the truth. This is the error term of the output layer. The gradients of the loss function are calculated. By gradient descent, the direction in which the weights of the output layer need to be optimized is calculated. The error of the hidden layer is the error of the output weighted by the weight it had for the output layer with respect to its change in activation of the hidden layer. Again the gradients are calculated with respect to the hidden layer, and by gradient descent, the direction in which the weights are updated is obtained. This is done until the input layer is reached.
In the final step, the updated weights of the network are the weights before the weight update plus a small step into the update direction. The small step is the learning rate. (The mathematical formula of the update rule was already discussed in the previous slides).

---

# Gradient descent and other optimizers

<img src="vl2/gradient_descent.png" alt="This image is in /static" width="70%">

Source: Raschka & Mirjalili (2019)

Note: There are multiple versions of gradient descent. The image on the slide shows a simplified, one-dimensional representation of the weights. In gradient descent, through calculating the derivate of the loss function, the slope of the loss function is obtained. Through the slope, the direction of change, one can calculate if the weights should be increased or decreased to minimize the loss.

There are three ways of how often the weight update during training is performed. In the example of gradient descent, the whole training set is used to calculate the weight updates, and afterward, the weights are updated. This method might be difficult to perform as the weights can not be calculated for the whole dataset because of hardware limitations. Moreover, one might need many epochs for optimization as the weight update is just performed once per epoche.

The other extreme is stochastic gradient descent. The weights are updated after each sample in the training set. While the update frequency is high, computation might be slow as calculating the gradients and derivates is a complex computation. Thus training time is increased. Additionally, the weights might have a high variance because of a large variance of the training set, making the training process wiggly. Therefore, the learning rate might be lowered.

Thus, most often mini-batch stochastic gradient is used, where after for each mini-batch, for example, 32 samples, the weights are updated.

Epochs are the number of passes through the whole training set. In other words, an epoch is one round of training. Neuronal networks need many "rounds" of training, until the weights are adjusted. There is no clear number of how many epochs are necessary, as the update frequency of the weights (gradient descent, mini-batch gradient descent, stochastic gradient descent), the strength of the update (learning rate), the complexity of the problem and many more factors influnece the optimal number. Often a so called early-stopping is applied, so the training stops, when no significant performance increase can be reached to prevent the network from overfitting.

Modern deep learning models use often other methods for optimization. The Adam optimizer is a well known and used alternative. While stochastic/mini-batch gradient descent (SGD) uses one learning rate for the whole model, Adam uses a learning rate for each parameter. Morevoer, the learning is adapted during the learning process. It therefore combines the advantage of AdaGrad and RMSPop optimizers. This course will often choose Adam because of the fast convergence of the algorithm and consequently less epochs needed in training.

We will not have a deeper discussion of optimizers in this course, however, if you are interested, the further readings give more details:

<a href="https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/"> Gentle Introduction to the Adam Optimization </a>

<a href="http://papers.nips.cc/paper/7003-the-marginal-value-of-adaptive-gradient-methods-in-machine-learning"> The marginal value of adaptive gradient methods in machine learning </a>

The second paper discusses the advantages and differences between adaptive and stochastic optimization methods. 

---

# Activation functions
<img src="vl2/activation_functions.png" width="65%">

Source: Jain, 2019

Note: 
The activation function can be any mathematical function.
The selection has a significant effect on the performs, especially when layers are stacked with non compatible functions.
Most often used is relu for the hidden layer. Sigmoid, and softmax were used in the past, but have a complex derivate to calculate, so the computing performance is low and suffer from a vanishing gradient problem. This problem will be discussed in chapter 5 in more detail. However, also relu is not free from hurdles. There is a phenomena called dying relu problem.

For the output layer:

softmax: multiclass

sigmoid: multilabel
 
linear: regression problems

The softmax function is a special case of the sigmoid, so that the probabilities are not per output neuron but distributed over all output neurons to mimic the one-hot encoded vector. 

A list of different activation functions and their mathematical properties can be found here: <a href="https://www.tensorflow.org/api_docs/python/tf/keras/activations" target="blank">keras activation functions</a> and <a href="https://en.wikipedia.org/wiki/Activation_function" target="blank">Wikipedia</a> or <a href="https://towardsdatascience.com/complete-guide-of-activation-functions-34076e95d044" target="blank">here</a>

---

# Loss function I 

- Neuronal networks are framed as an optimization problem
- Using Maximum Likelihood estimation

Loss functions that are often used:

Classifcation problems: cross-entropy

<img src="vl2/cross_entropy.png" width="35%">

Source: Brownlee, 2019.

Note: The loss function describes mathematically the errors in the optimization problem. 
The goal is to minimze the loss functions, so that predictions and target values are as close as possible. Neural networks use the maximum likelihood theorem that finds the optimum parameter values (weights), given an input to fit the data distribution of the target as close a possible based on the training data. For classification problems often the loss functions cross-entropy is used that minimizes the difference between the predicted class probability and the true class probability. The categorical cross-entropy measures the average number of bits that have to be changed in order to get from one distribution to the other. 

---

# Loss function II 

Regression problem: Mean squared error

<img src="vl2/mae.png" width="30%">

Source: Brownlee, 2019.

Note: The loss function for regression problems is the mean squared difference between the prediction and the true value, also known as mean squared error. 

However, there are many more loss functions like: mean absolute deviation for regression or hinge loss for classification.
Tensorflow gives also the possibility to combine loss functions. Therefore a function needs to be coded, that adds, weights or combines the pre-defined loss functions.

---

# Neural network video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/ILsA4nyG7I0?list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Rohrer (2017)

Note: This video explains very well how a neural network works.

---

# Tensorflow 

<img src="vl2/Tensorflow_logo.png" width="35%">

Note: This course will use Googles Tensorflow library for deep learning. Tensorflow has the opportunity to write basic tensorflow code for developing new layers and algorithms as well as to use the high-level Keras API. Keras is a wrapper for different deep learning frameworks, which is easy to use and a good start for making first experiences in deep learning. The most used deep learning functions are precoded, so that just the parameters have to be defined and the model needs to be "stacked" together by combing different layers. This course will focus on using the functional API of Keras, providing more flexibilty to the Sequential API for building advanced models. 

---

# How to use images in a dense neural network

As dense neural networks cannot use a multidimensional array as an input, first, the images need to be transformed into a flat vector representation for learning. Thus, instead of height and width, the image is now a list of pixels starting from the first pixel to the last. Each input neuron will match one of these pixels.

```python
print(X_train.shape) # the original dataset size
train = np.reshape(X_train, (12000,784)) # as images have the size 28 by 28, there are 784 pixels in each image
# with the numpy reshape command the shape of the trainings array can be changed
# you could also used the np.flatten command here; Additional the flatten array needs to be reshaped with the reshaped command
```

```out
(12000,28,28)
(12000,784)
```

---

# A simple neural network in Tensorflow.keras

```python
def simple_model():
    input_layer = layers.Input(shape=(784,)) # expect an input of 784 for each observation
    
    hidden_layer = layers.Dense(20, activation="relu") (input_layer) # 20 neurons with reul activation; connect to input
    
    output_layer = layers.Dense(1, activation="sigmoid") (hidden_layer)
    
    m = models.Model(input_layer, output_layer)
    m.compile(loss="binary_crossentropy", optimizer="adam", metrics=["acc"]) # define the optimization algorithm used
    # define which metrics to use for the loss -> here: binary_crossentropys
    # define the metrics for evaluating results -> here: accuracy
    
    return m
```

Note: Relu activations are used for the hidden layer, while sigmoid activations are used for the output layer, as there is just a single label per image. In this course, we will use the functional API of Keras. Instead of the sequential API where layers can be stacked, we can create more complex architectures with the functional API. To connect a layer to the previous layer, the previous layer is called in breackets after the commands for the current layer. In the example in the slides, you can see that the hidden layer is first defined and than connected to the input_layer. 

---

# Create our neural network object

```python
our_first_model = simple_model()
print(our_first_model.summary())
```

```out

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 784)               0         
_________________________________________________________________
dense (Dense)                (None, 20)                15700     
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 21        
=================================================================
Total params: 15,721
Trainable params: 15,721
Non-trainable params: 0
_________________________________________________________________

```

Note: There are 784 inputs, 20 neurons in the hidden unit and 1 output neuron, that classifies whether the image belongs to the target category or not.

By calling the fit method, the network can be trained. 

---

<html>
<h3>References</h3>
<list>
    <li>Babel, P. (2019). Deep Neural Networks from scratch in Python. https://towardsdatascience.com/deep-neural-networks-from-scratch-in-python-451f07999373  </li>
    <li> Brownlee, J. (2019). Loss and Loss functions for training deep learning neural networks. Retrieved from: https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/ 
    <li>Jain, P. (2019). Complete Guide of Activation functions. Retrieved from: https://towardsdatascience.com/complete-guide-of-activation-functions-34076e95d044</li>
    <li>Raschka, S., & Mirjalili, V. (2019). Python Machine Learning: Machine Learning and Deep Learning with 
            Python, scikit-learn, and TensorFlow 2. Packt Publishing Ltd.</li>
    <li>Rohrer, B. (2017). How Deep Neural Networks Work. Retrieved from: https://www.youtube.com/watch?v=ILsA4nyG7I0&list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp </li>
    <li>Rosenblatt, F. (1958). The perceptron: a probabilistic model for information storage and organization in 
        the brain. Psychological review, 65(6), 386.</li>
    <li>Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating 
        errors. nature, 323(6088), 533-536.</li>
   <li>Xiao, H., Rasul, K., & Vollgraf, R. (2017). Fashion-mnist: a novel image dataset for benchmarking machine 
       learning algorithms. arXiv preprint arXiv:1708.07747.</li>
</list>
</html>

---

# Let's do some coding ... 