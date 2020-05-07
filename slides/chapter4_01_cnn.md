---
type: slides
---

# Convolutional Neural networks 

---

# Motivation
<list>
<li>Dense neural networks are missing sparse connectivity</li> <br>
<li>In dense neural networks, different weights are applied to different patches for input images </li> <br>
<li> Hard to compute large images, because of input sizes </li> <br>

Dense nets are great at recognizing global patterns but fail to discover local patterns
</list>
<br>
Source: Raschka & Mirjalili, 2019, Vasilev, (2019)

Notes: Convolutional neural networks were introduced in 1989 by LeCun et al. Neural networks containing only dense layers can be applied to image data; however, there are serval disadvantages. When the flattened image is used as the input, the hidden layers of a fully connected network connect to each pixel. However, the same pixel in different images mostly do not belong to the same "object" but are weighted as they would be. Thus, there is a dense connectivity. Moreover, objects or pixels belonging to the same "object" but with different places in the network might get weighted differently. A CNN has the advantage that sparse connectivity exists, meaning that local pixels are connected and weighted together, and that same weights are used for different patches of the image (parameter sharing), they are much more suitable to use in CV. Moreover, when images have large dimensions, dense neural networks are insufficient to train because of the large input vector (LeCun et al, 1990, Raschka & Mirjalili, 2019, Vasilev, 2019). 

---

# Convolutional neural networks

<img src="vl3/cnn_architecture.jpeg" alt="This image is in /static" width="80%">

Source: Saha, 2018

Notes: Depicted in the figure is a Convolutional neural network. In the next slides, a detailed look at the building blocks of a CNN is made. First of all the question arises, what is a convolution?

---

# What is a convolution?

<img src="vl3/convolution.gif" alt="This image is in /static" width="40%">

- Slide a filter about the image; This filter is looking for specific features and is learned by backpropagation
- Matrix by matrix multiplication of filter x image
- Building the sum
- Convolved feature is a new representation of the image <br>
Source: Saha (2018)

Note: A convolutional kernel thereby is a matrix of n x m, which is sled over the image. In mathematical terms, matrix multiplication is performed, and the input matrix is filtered for different objects. In the bottom layers of the network, these might be dot and edges, which are combined in the top layers to more complex shapes. The weights of the matrix are learned by backpropagation. A matrix containing positive weights in the first row and negative weights in the last row, for example, is filtering for horizontal edges (see Edge Detection). A kernel is applied to each channel of the image representation. The combined kernels are called a filter. Each convolutional layer consists of multiple filters. The parameters which need to be chosen on are the size of the kernel, the number of filters per layer, the stride size (how far is a kernel sled), the type of padding, and the activation function (Raschka & Mirjalili, 2019).


---

# Get a feeling for kernels

<a href="http://setosa.io/ev/image-kernels/" target="blank">Kernel visualization</a> 

Note: You can click on the link and try out different kernels on the image

---

# Convolution parameters

Kernel size:
- Shape of filter
- Often used 3x3, 5x5, 7x7

Stride size:
- Slide length
- Often used 1 or 2

Padding:
- Kernel strictly applied in the image slide?
- Same: The convolved feature has the same size as input; Input is extended with zeros
- Valid: Kernel only applied in image; Outputsize smaller

Source: Saha (2018)

Note: The parameters of a convolutional layer are the number of filters, the kernel size of filters, the stride size (distance of sliding) and padding (behaviour on the image edge).

---

# Convolution parameters (2)
Activation function:
- Which function is applied on the convolved image

<img src="vl3/padding.gif" alt="This image is in /static" width="20%">
Source: Saha (2018)

Note: Moreover, we can apply different activation functions to the convoled image. 
This image in the slides shows the same padding. It can be clearly seen that the kernel is going over the edge of the image and the image is extended with zeros. The original input (blue) has exactly the same dimensions as the output (green) -> "same pooling".

---

# What about color images and multi-channel?

<img src="vl3/colored_convolution.gif" alt="This image is in /static" width="50%">

Source: Saha (2018)

Note: The given concepts can also be extended to multiple channels.
Now each filter exists of multiple kernels added together.

The convolutions of the second convolutional layer are the combination of the convolved output of the first layer.
Compared to the image above:

Instead of having for example 3 channels (R,G,B), the output of the first convolution may have 16,32 or 128 or many more channels. For each filter of the first convolutional layer, there is one channel output. In the second convolutional layer, these are filtered accordingly, with a kernel for each channel and added up to build one filter/output of the second convolutional layer.

---

# CNN video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/py5byOOHZM8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Pound (2016)

Note: This video explains very well how a CNN works.

---

# Pooling

<img src="vl3/pooling.jpeg" alt="This image is in /static" width="40%">

Source: Raschka & Mirjalili, 2019

Note: The second important operation in a Convolutional Network is called pooling. There are three types of pooling, namely max pooling, average pooling, and global (max or average) pooling. The aim is to make the algorithm invariant to local changes. Thus neighboring pixels are treated as one area. In a max-pooling operation, the maximum activation for each area is taken, for average pooling, the average pixel value is used. The advantage of the pooling operations is that they also reduce the input size; thus, the computation gets also more efficient. Global pooling is not extracting the maximum or average pixel value for image sub-regions but for the whole input. It can be used instead of a flatten layer to connect the multi-dimensional convolutional layers to fully connected layers (Raschka & Mirjalili, 2019). Similar to the convolutional hyperparameters, the parameters for pooling are the pooling size, stride size, and padding. A global pooling, as seen on the next slide, is just a special pooling with the size of the input size. Thus, each channel is reduced to one number/scalar.

---

# Global Pooling

<img src="vl3/global_average_pooling_a.png" alt="This image is in /static" width="50%">

Image source: https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/blocks/2d-global-average-pooling

Note: A flatten layer, or global pooling needs to be used to connect the multi-dimensional convolution to the fully connected layers, which only takes one-dimensional inputs.
Do you remember the reshaping of the image? The same is done in the flatten command. The convoluted output is "flattened" into a list/vector.
Using a global pooling has the advantage that the number of parameters in the network are less as the output is summarized in one number instead in a list of pixels with the length of width x height x channels of the last convolutional layer.

---

# Overall architecture

<img src="vl3/cnn_architecture.jpeg" alt="This image is in /static" width="80%">

Source: Saha, 2018

Note: Concluding, most CNNs follow the following architecture: A convolutional layer followed by a pooling layer form convolutional blocks. Multiple convolutional blocks are stacked sequentially together. For connecting the convolutional part with dense layers, a flatten or global pooling layer is used. The dense layers are afterward connected with the output layer.

---

# A simple convolutional neural network in Tensorflow.keras

```python
def convolutional_neural_network():
    input_ = layers.Input(shape=(32,32,3)) # Define the input size of the image

    cnn = layers.Conv2D(16, (3,3), activation="relu") (input_) # first conv layer with 16 filters
    # uses a 3 by 3 kernel size, stride 2, activation relu

    cnn = layers.MaxPooling2D() (cnn) # max pooling layer to reduce dimensions, size 2 by 2 (keras default)
    
    cnn = layers.Conv2D(32, (3,3), activation="relu") (cnn)
    cnn = layers.MaxPooling2D() (cnn) # max pooling layer to reduce dimensions, size 2 by 2 (keras default)
    
    flatten = layers.Flatten() (cnn) # flatten to connect the second convolutional layer 
    # to the fully connected layers
    
    dense = layers.Dense(32, activation="relu") (flatten)
    dense = layers.Dense(16,  activation="relu") (dense)
    
    output = layers.Dense(10, activation="softmax") (dense) # output; 10 different classes
    
    opt = optimizers.Adam()
    
    m= models.Model(input_, output)
    m.compile(optimizer=opt,loss='categorical_crossentropy',metrics=['accuracy'])
    return m
```

---

<html>
<h3>References</h3>
<list>
        <li> LeCun, Y., Boser, B. E., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W. E., & Jackel, L. D. 
            (1990). Handwritten digit recognition with a back-propagation network. In Advances in neural 
            information processing systems (pp. 396-404).</li>
        <li>LeCun, Y., & Bengio, Y. (1995). Convolutional networks for images, speech, and time series. The 
            handbook of brain theory and neural networks, 3361(10), 1995.</li>
        <li>LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. nature, 521(7553), 436-444.</li>
        <li>Pound, M. (2016). Neural Network that Changes Everything - Computerphile. Retrieved from: https://www.youtube.com/watch?v=py5byOOHZM8&feature=emb_title</li>
        <li>Raschka, S., & Mirjalili, V. (2019). Python Machine Learning: Machine Learning and Deep Learning with 
            Python, scikit-learn, and TensorFlow 2. Packt Publishing Ltd.</li>
        <li> Saha, S. (2018). A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way. Retrieved 
            from: https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-
            way-3bd2b1164a53. Last access: 23.02.2020 </li>
        <li>Vasilev, I. (2019). Advanced Deep Learning With Python: design and implement advanced next-generation 
            ai solutions using tensorflow and pytorch. S.l.: PACKT PUBLISHING LIMITED.</li>
</list>

</html>

---
# Let's do some coding ... 