---
type: slides
---

# ... some tricks with neural networks that are from time to time very useful

---

# Normalization of inputs 

Often the inputs are normalized/standardized for the neural network:

Reasons:

- stability of learning
- faster convergence

Source: Brownlee (2019)

Note: Often, when the different variables in the input are on different scales, for example, dummy variables being between 0 and 1 and numeric variables on different ranges up to infinite, weight updates in the network can get very large due to the large units of the variables. When weight updates get very large, often the learning process gets instable as with the next batch or epoch, a lot of other weights need to be adjusted according to the last large update. This is also tightly linked to the performance of learning. With normalized inputs, the optimizer converges faster, reducing training time.

More information you can found <a href="https://machinelearningmastery.com/how-to-improve-neural-network-stability-and-modeling-performance-with-data-scaling/"> here </a>

---

# Image preprocessing

It is common practice to normalize or standardize also the image inputs.
Normalization is easy as most of them use values between 0 and 255

According to min-max normalization, x_normalized = (x-min)/(max-min) which can be simplified to diving the image by 255.0

There is a downside to normalization, and it comes in the form of hardware requirements: 
Instead of being an unsigned integer of 8 bits, now the pixel values are floating points (usually 32 bits).

Thus, the data size is quadrupled!

Note: More information can be found <a href="https://machinelearningmastery.com/how-to-normalize-center-and-standardize-images-with-the-imagedatagenerator-in-keras/"> here </a>

---

# Tensorflow data pipelines I

```python
import tensorflow as tf
# function for data transformation with 2 input lists
# the filenames and the corresponding label
def transform_function(filename, label): 
    image_string = tf.io.read_file(filename) # read the filename from the filename list

    image = tf.io.decode_png(image_string, channels=3) # decode it as an png colored image
    # Different decode options are available also for jpeg or other file formats

    image = tf.image.convert_image_dtype(image, tf.float32) # normalize the image

    image = tf.image.resize(image, [224, 224]) # resize the image to 224 by 224 pixels

    # Many more operations can be found in the tensorflow documentation
    
    return image, label
```


Note: It is not convenient to read first all the data into memory, preprocess it, and use it than for training. First of all, this often requires large machines with large RAM. Secondly, if loading just one batch at the time, not the full power of the GPU can be used, as the GPU might wait for the batch to be prepared or passed to the GPU.

Using tensorflow pipelines mitigate these two downsides. In the example above, a sample pipeline is built. The dataset object can be normally passed to the fit function of the model.

For more information about data piplines see <a href="https://www.tensorflow.org/guide/data_performance">here</a>, <a href="https://towardsdatascience.com/building-efficient-data-pipelines-using-tensorflow-8f647f03b4ce">here</a> and <a href="https://cs230.stanford.edu/blog/datapipeline/"> here </a>.

It is highly useful to have a good knowledge of tensorflow data pipelines. 
In the example above, images are read, resized and normalized per batch.

---

# Tensorflow pipeline II

```python
# Definition of the pipeline
batch_size=64 # define a batch size

# create tensorf and input the files list files_ and the one hot encoded labels c_categorical
dataset = tf.data.Dataset.from_tensor_slices((files_,c_categorical))

dataset = dataset.shuffle(len(files_)) # shuffel the data

dataset = dataset.map(transform_function, num_parallel_calls=4) # transform data
# 4 threads are used

dataset = dataset.batch(batch_size) # create a data bach

dataset = dataset.prefetch(1) # prepare 1 element (batch) in advance

# Up to now, now data is loaded, this is only the definition of the pipeline. 
# The loading process will start when the dataset is passed to the model.fit() 
# method or by the enumerate command.
```

Note: In the ".map"-part, the previous written transformation function is applied to the data. This process is executed with 4 parallel sub-processes for each batch. With prefetching a number of batches, in this example 1, the network is trained efficiently, as while the GPU is training on a batch, the next batch is already prepared.

---

# What is the output of the convolution?

output_width = (input_width+2 x poolig_width - filter_width)/stride_width + 1

output_height = (input_height+2 x poolig_height - filter_heigth)/stride_height + 1

Note: At some points in the course you will find these formulas helpful to calculate the output size of a convolutional operation

---

# Number of parameters in the network

Dense layer:

parameters = number_of_neurons * (output_size_last_layer + 1)

Convolutional layer:

parameters = number_of_filters * (input_channel x kernelsize + 1)

Source: Zhang, 2017

Note: For the dense layer, each output of the subsequent layer is connected to all neurons in the next layer. The +1 in the formula accounts for the bias each neuron has. For the parameters of the convolutional layer also the plus one accounts for the bias of each filter. The kernel size here is the kernel width multiplied by the kernel height.

---

# Pooling vs strides

<html>
<iframe width="800" height="450" src="https://www.youtube.com/embed/fwNLf4t7MR8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>
Source: Becker (2018)

Note: There is a debate going on if pooling should be replaced by strides. 
Many networks are using pooling - this is more the "historic way".
New network architecture (we will discuss them next week) are replacing these with strides

---


# Sources

Becker, D. (2018). Stride Length and Dropout for Better Deep Learning Models. Retrieved from: https://youtu.be/fwNLf4t7MR8 

Brownlee, J. (2019). How to use Data Scaling Improve Deep Learning Model Stability and Performance. Retrieved from: https://machinelearningmastery.com/how-to-improve-neural-network-stability-and-modeling-performance-with-data-scaling/ Last access: 26.03.2020

Brownlee, J. (2019). How to Normalize, Center, and Standardize Image Pixels in Keras. Retrieved from: https://machinelearningmastery.com/how-to-normalize-center-and-standardize-images-with-the-imagedatagenerator-in-keras/ Last access: 26.03. 2020 

Zhang, Y. (2017). Number of Parameters in Dense and Convolutional Layers in Neural Networks. Retrieved from: https://medium.com/@zhang_yang/number-of-parameters-in-dense-and-convolutional-neural-networks-34b54c2ec349 Last access: 26.03.2020

---
# Let's do some coding ...