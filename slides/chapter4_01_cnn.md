---
type: slides
---

# Convolutional Neural networks 

---

# Motivation
Dense neural networks are missing sparse connectivity 
In dense neural networks different weights are applied to differnt patches for input images
Hard to compute large images

Dense net are great at recognizing global patterns but fail to discover local patterns

Source: Raschka & Mirjalili, 2019, Vasilev, (2019)

Notes: Convolutional neural networks were introduced in 1989 by LeCun et al. Neural networks containing only dense layers and can be applied to image data; however, there are serval disadvantages. When the flattened image is used as the input, the hidden layers of a fully connected network connect to each pixel. However, pixels mostly do not belong to the same "object" but are weighted as they would be. Thus, there is a dense connectivity. Moreover, objects or pixels belonging to the same "object" but with different places in the network might get weighted differently. A CNN has the advantage that sparse connectivity exists, meaning that local pixels are connected and weighted together, and that same weights are used for different patches of the image (parameter sharing) (LeCun et al, 1990, Raschka & Mirjalili, 2019, Vasilev, 2019). 

---

# What is a convolution?

<img src="vl3/convolution.gif" alt="This image is in /static" width="40%">

- Slide a filter about the image; These image is looking for specific features and is learned by backpropagation
- Matrix Matrix multiplication of filter x image
- Building the sum
- Convolved features is a new representation of the image

Source: Saha (2018)

Note: A convolutional kernel thereby is a matrix of n x m, which is sled over the image. In mathematical terms, matrix multiplication is performed, and the input matrix is filtered for different objects. In the bottom layers of the network, these might be dot and edges, which are combined in the top layers to more complex shapes. The weights of the matrix are learned by backpropagation. A matrix containing positive weights in the first row and negative weights in the last row, for example, is filtering for horizontal edges (see Edge Detection). A kernel is applied to each channel of the image representation, which is called a filter. In a convolutional layer consists of multiple filters. The parameters which need to be chosen on are the size of the kernel, the number of filters per layer, the stride size (how far is a kernel sled), the type of padding, and the activation function (Raschka & Mirjalili, 2019).


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
- Same: Convolved feature has same size as input; Input is extended with zeros
- Valid: Kernel only applied in image; Outputsize smaller

Source: Saha (2018)

---

# Convolution parameters (2)
Activation function:
- Which function is applied on the convolved image

<img src="vl3/padding.gif" alt="This image is in /static" width="20%">
Source: Saha (2018)

Note: This image shows the valid padding. It can be clearly seen that the kernel is going over the edge of the image.

---

# CNN video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/py5byOOHZM8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=ILsA4nyG7I0&list=PLVZqlMpoM6kaJX_2lLKjEhWI0NlqHfqzp

Note: This video explains very well, how an neural network basically works.

---

# What about color images and multi-channels?

<img src="vl3/colored_convolution.gif" alt="This image is in /static" width="50%">

The given concepts can also be extended to multiple channels.
Now each filter exists of multiple kernels added together

The convolutions of the second convolutional layer as the combination of the convolved output of the first layer.
Compared to the image above:

Instead of having for example 3 channels (R,G,B), the output of the first convolution may have 16,32 or 128 or many more channels. For each filter of the first convolutional layer there is one channel output.
Source: Saha (2018)

---

# Pooling

<img src="vl3/pooling.jpeg" alt="This image is in /static" width="40%">

Source: Raschka & Mirjalili, 2019

Note: The second important operation in a Convolutional Network is called pooling. There are three types of pooling, namely max pooling, average pooling, and global (max or average) pooling. The aim is to make the algorithm invariant to local changes. Thus neighboring pixels are treated as one area. In a max-pooling operation, the maximum activation for each area is taken, for average pooling, the average pixel value is used. The advantage of the pooling operations is that they also reduce the input size; thus, the computation gets also more efficient. Global pooling is not extracting the maximum or average pixel value for image sub-regions but for the whole input. It can be used instead of a flatten layer to connect the multi-dimensional convolutional layers to fully connected layers (Raschka & Mirjalili, 2019). Similar to the convolutional also here the parameters are the pooling size, stride size and padding. A global pooling as seen on the next slide is just a special pooling with the size of the input size. Thus, each channel is reduced to one number

---

# Global Pooling

<img src="vl3/global_average_pooling_a.png" alt="This image is in /static" width="50%">

Image source: https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/blocks/2d-global-average-pooling

Note: A flatten layer or global pooling needs to be used to connect the multi-dimensional convolution to the fully connected layers which only take one dimensional inputs.
Did you rember the reshaping of the image? The same is done in the flatten command. The convoluted output is "flattend" into a list/vector.
Using a global pooling has the advantage that the number of parameters in the network are less as the output is summarized in one number instead in a list of pixels.

---

# Overall architecture

<img src="vl3/cnn_architecture.jpeg" alt="This image is in /static" width="80%">

Note: Concluding, most CNNs follow the following architecture: A convolutional layer followed by a pooling layer form convolutional blocks. Multiple convolutional blocks are stacked sequentially together. For connecting the convolutional part with dense layers, a flatten or global pooling layer is used. The dense layers are afterward connected with the output layer.

---

# A simple convolutional neural network in Tensorflow.keras

```python
def neural_network_2():
    input_ = layers.Input(shape=(32,32,3)) # Define the input size of the image
    cnn = layers.Conv2D(16, (3,3), activation="relu") (input_) # first conv layer with 16 filters, by a 3 by 3 kernel size, stride 2, acitvation relu
    cnn = layers.MaxPooling2D() (cnn) # max pooling layer to reduce dimensions, size 2 by 2 (keras default)
    
    cnn = layers.Conv2D(32, (3,3), activation="relu") (cnn)
    cnn = layers.MaxPooling2D() (cnn) # max pooling layer to reduce dimensions, size 2 by 2 (keras default)
    
    flatten = layers.Flatten() (cnn) # flatten to connect the second convolutional layer to the fully connected layers
    
    dense = layers.Dense(32, activation="relu") (flatten)
    dense = layers.Dense(16,  activation="relu") (dense)
    
    output = layers.Dense(10, activation="softmax") (dense) # output; 10 different classes
    
    opt = optimizers.Adam()
    
    m= models.Model(input_, output)
    m.compile(optimizer=opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    
    return m
```

---

# Pooling vs strides

<html>
<iframe width="800" height="450" src="https://www.youtube.com/embed/fwNLf4t7MR8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

There is a debate going on if pooling should be replaced by strides. 
A lot of networks are using pooling - this more the "historic way"
New network architecutre (we will discuss them next week) are replacing these with strides

Source: https://youtu.be/fwNLf4t7MR8

---

# Let's do some coding ... 