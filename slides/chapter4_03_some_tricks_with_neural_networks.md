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

More information you can hind <a href="https://machinelearningmastery.com/how-to-improve-neural-network-stability-and-modeling-performance-with-data-scaling/"> here </a>

---

# Image preprocessing

It is common practice to normalize or standardize also the image inputs.
Normalization is easy as most of them use values between 0 and 255

According to min-max normalization, x_normalized = (x-min)/(max-min) which can be simplified to diving the image by 255.0

There is a downside to normalization, and it comes in the form of hardware requirements: 
Instead of being an unsigned integer of 8 bits, now the pixel values are floating points (usually 32 bits)
Thus, the data size is quadrupled!

Note: More information can be found <a href="https://machinelearningmastery.com/how-to-normalize-center-and-standardize-images-with-the-imagedatagenerator-in-keras/"> here </a>

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

# Sources

Brownlee, J. (2019). How to use Data Scaling Improve Deep Learning Model Stability and Performance. Retrieved from: https://machinelearningmastery.com/how-to-improve-neural-network-stability-and-modeling-performance-with-data-scaling/ Last access: 26.03.2020

Brownlee, J. (2019). How to Normalize, Center, and Standardize Image Pixels in Keras. Retrieved from: https://machinelearningmastery.com/how-to-normalize-center-and-standardize-images-with-the-imagedatagenerator-in-keras/ Last access: 26.03. 2020 

Zhang, Y. (2017). Number of Parameters in Dense and Convolutional Layers in Neural Networks. Retrieved from: https://medium.com/@zhang_yang/number-of-parameters-in-dense-and-convolutional-neural-networks-34b54c2ec349 Last access: 26.03.2020

---
# Wait for chapter 5 ...