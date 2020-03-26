---
type: slides
---

# Neural networks 

---

# Neural networks

Historical development

- Theoretical developement in the 1940s by McCulloch and Pitt
- Similarity to the human brain
- Fundamental method: Perceptron (Rosenblatt, 1958)
- AI Winter
- Backpropagation 1986s 

Advantage of Deep Learning: Multiple non-linear transformations 

Source: Raschka & Mirjalili, 2019, Rosenblatt, 1958,  Rumelhart et al., 1986

Notes: The idea of building a artifical object similar to the human brain that can learn somethings dates back to the ideas of McCulloch and Pitt in the 1940s. The fundamental methods is a perceptron, developed by Rosenblatt in 1958. Mathematically speaking it is the weighted sum of the inputs used in a non-linear mathematical function to map some output. In the AI Winter, the technology was not extensivley researched as computational costs were high and other machine learning algorithms performed better. This changed with the development of backpropagation in 1986, which is used until today to train a neural network. Neural networks got in the last years again attention as with the increasing computing power and the usage of Graphical processing units (GPUs) more complex neural networks could be trained with almost human performance or surpassing it in some applications. The advantage compared to classical machine learning algorithms are that deep learning models can model complex non-linear relationships between input and output to increase the prediction performance.

---

# Perceptron

<img src="vl2/perceptron.png" alt="This image is in /static" width="70%">
<img src="vl2/update_rule.png" alt="This image is in /static" width="30%">

Source: Raschka & Mirjalili, 2019

Note: The perceptron algorithm is the necessary foundation for modern deep learning algorithms. Invented by Rosenblatt in 1958, a perceptron is representing one single neuron. If a human neuron fires, the inputs to the neuron are above a threshold so that it gets activated. Very similar to this is the perceptron. It weights its inputs according to the weight coefficients, sum them up, and applies an activation function. In the original paper of Rosenblatt, it is a stepwise function. The weights are learned by an update rule. For each training sample, they get updated. The new weights are the weights plus the update. The learning rate (eta) determines how fast the weights are updated. When the ith sample is false predicted, the weights are pushed towards the correct direction (Raschka & Mirjalili, 2019, Rosenblatt, 1958).

---

# Neural network

<img src="vl2/neural_network.png" alt="This image is in /static" width="70%">

Source: Raschka & Mirjalili, 2019

Note: A neural network is a combination of neurons. These neurons are combined in multiple layers, whereas each neuron from a layer l is connected to all neurons in the following layer. The input of the layer l is the weighted combination of the neurons of the previous layer l-1 plus a bias (Raschka & Mirjalili, 2019). A network in it purest form has an input layer, one hidden layer and one output layer. We call networks deep, when there are multiple hidden layers. For each layer we can use a specific activation function applied in all neurons.

---

# Process flow 

1. Forward propagation -> use network for prediction
2. Compute cost function and error of the current prediction
3. Backward propagation (calculate gradient of the cost function)
4. Update parameters (according to the backpropagation)

Note: We will discuss these steps in the following slides

---

# Feed-forward

<img src="vl2/feedforward.png" alt="This image is in /static" width="70%">

Note: In the forward pass, inputs are transformed and passed from layer to layer to predict the output.
For the first neuron in the hidden layer, the input neurons are weighted and a bias is added. This neuron uses a specific activation function and creates its output. This is performed for all neurons in the hidden layer.
The next layer's neuron weights all the outputs of its previous layers, adds a bias and uses an activation function.
Also the output layer uses all the inputs from the previous hidden layer weights them, activates and creates an ouput. This final output is the prediction of the neural network. The weights for each neuron are learned during the second important step in a neural network: backpropagation. To initalize the weights bevor the first training, random numbers are used. 

---

# Backpropagation

<img src="vl2/backpropagation.png" alt="This image is in /static" width="50%">

Note: While the feed-forward process is just the pass from inputs to preditions, this process helps the neural network to learn. Backpropagation was introduced in 1986 by Rumelhart et al. and is mostly used to train the neural network. The essential idea is that the weights should be optimized so that the loss function and the error are minimized. First of all the error is calculated by comparing the prediction with the truth. This is the error term of the output layer. The gradients of the loss function are calculated. By gradient descent, the direction in which the weights of the output layer need to be optimized are calculated. The error of the hidden layer is the error of the output weighted by the weight it had for the output layer with respect to its change in activation of the hidden layer. Again the gradients are calculated with respect to hidden layer and by gradient descnt the direction in which the weights are updated is optained. This is done until the input layer is reached.
In the final step, the updated weights of the network are the weights bevor the weight update plus a small step into the update direction. The small step is the learning rate. (The mathematical formula of the update rule was already discussed in the previous slides).

---

# Gradient descent

<img src="vl2/gradient_descent.png" alt="This image is in /static" width="70%">

Note: There are multiple version of gradient descent. The image on the slide shows is simplified one dimensional representation of the weights. In gradient descent, through calculating the derivate of the loss function, the slope of the loss function is optained. Through the slope, the direction of change, one can calculate if the weights should be increased or decreased to minimize the loss.

There are three ways of how often the weight update during training is performed. In the example of gradient descent, the whole training set is used to calculate the weight updates, and afterward, the weights are updated. This method might be difficult to perform as the weights can not be calculated for the whole dataset because of hardware limitations. Moreover, one might need many epochs for optimization as the weight update is just performed once per epoche.

The other extreme is stochastic gradient descent. The weights are updated after each sample in the training set. While the update frequency is high, computation might be slow as calculating the gradients and derivates is a complex computation. Thus training time is increased. Additionally, the weights might have a high variance because of a large variance of the training set, making the training process wiggly. Therefore, the learning rate might be lowered.

Thus, most often mini-batch stochastic gradient is used, where after for each mini-batch, for example, 32 samples, the weights are updated.

---

# Activation functions

- Any mathematical function
- Significant effect on the performance

Note: Often used are relu, sigmoid and softmax for the hidden layers

For the output layer:
softmax: multiclass
sigmoid: multilabel 
linear: regression problems

A list of different activation function and their mathematical properties can be found here: <a href="https://keras.io/activations/" target="blank">keras activation functions</a> and <a href="https://en.wikipedia.org/wiki/Activation_function" target="blank">Wikipedia</a>

---

# Neural network video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/ILsA4nyG7I0?list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=ILsA4nyG7I0&list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp

Note: This video explains very well, how an neural network basically works.

---

# How to use images in a dense neural network

As dense neural networks can not use a multi dimensional array as an input, first the images need to be transformed into a flat vector representation for learning. Thus, instead of height and widht, the image is now a list of pixels starting from the first pixel to the last. Each input neuron will match one of these pixels.

```python
print(X_train.shape) # the original dataset size
train = np.reshape(X_train, (12000,784)) # as images have the size 28 by 28, there are 784 pixels in each image
# with the numpy reshape command the shape of the trainings array can be changed
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

Note: For the hidden layer relu activations are used, for the output layer sigmoid activations as there is just one class. In this course we will use the functional API of Keras. Instead of the sequential api where layers can be stacked, we can create more complex architectures with the functional api. To connect two layers, create the layer with calling one layer type from the layers package and add the previous layer where it should connect in the brackets after the call

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

Note: There are 784 inputs, 20 neurons in the hidden unit and 1 output neuron classifying if the image belongs to the target category or not

By calling the fit method the network could be trained 

---

# Let's do some coding ... 