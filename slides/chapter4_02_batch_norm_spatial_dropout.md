---
type: slides
---

# ... some more layers which are frequently used

---

# Batch Norm
 Goal: Stable training, high learning rate

Reasons why BatchNorm works are highly discussed:
    1. Reduces internal covariate shift (2015-2018)
    2. Reduces wrong scaling of the activation outputs

<img src="vl3/batch_norm.png">

Source: (Ioffe & Szegedy, 2015)


Notes: Batch normalization is a technique to make the training process of the network more stable. Since the development in 2015, it is implemented in many models, not only CNN's but all types of networks. While the mechanism of batch norm is easy to explain, the reason why it works is highly discussed in research. Each batch is normalized to a mean of 0 and a variance of 1 (Ioffe & Szegedy, 2015).

The two learned parameters, gamma and beta restore the representation power. Gamma is the scaling parameter x, while beta is the interpect to shift the distribution.

The original idea was that it reduces the internal covariate shift. This phenomenon describes the shift of the activation output of the previous layer due to weight updates. As a consequence, the preceding layer has differently scaled input, which might result in a sizeable change of the weights in the next mini-batch or epoch. This effect makes learning very unstable. Current research finds very little evidence that batch normalization reduces internal covariate shift, and the reason why it works is highly discussed. For further readings, see <a href="https://arxiv.org/pdf/1805.11604.pdf" target="blank">here</a> and <a href="https://arxiv.org/abs/1805.10694" target="blank">here</a> . Nevertheless, batch normalization is very helpful in improving the stability of the learning process.

Often you choose Batch Norm or Dropout for the network. There is some evidence that when both are applied, learning can be effected negativly. 

The mathematical description is out of the scope this this course, however, for information and completness see <a href="http://openaccess.thecvf.com/content_CVPR_2019/html/Li_Understanding_the_Disharmony_Between_Dropout_and_Batch_Normalization_by_Variance_CVPR_2019_paper.html"> Li et al.</a>

---

# Batch Norm Video explanation

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/nUUqwaxLnWs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Deeplearning.ai (2017)

---

# A simple convolutional neural network in Tensorflow.keras using Batch Normalization

```python
def neural_network_2():
    input_ = layers.Input(shape=(32,32,3)) # Define the input size of the image
    cnn = layers.Conv2D(16, (3,3), activation="relu") (input_) # first conv layer with 16 filters, by a 3 by 3 kernel size, stride 2, acitvation relu
    cnn = layers.BatchNormalization() (cnn)
    cnn = layers.MaxPooling2D() (cnn) # max pooling layer to reduce dimensions, size 2 by 2 (keras default)
    
    cnn = layers.Conv2D(32, (3,3), activation="relu") (cnn)
    cnn = layers.BatchNormalization() (cnn) # Batch Normalization layer
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
# Spatial dropout

Instead of dropping out one neuron (in dense networks) or cell in the matrix, a whole feature map can be dropped out.

Example input shape: [3,3,64] 

Dropout: One of the 576 values is dropped out and not updated 
Spatial dropout: One of the 64 filters is not updated 

Works very well when having a strong correlation between neurons 

Source: Tompson et al. (2015), Brownlee, (2018).


Note: Between convolutional layers, spatial dropouts should be used for dropping filters

---

# A simple convolutional neural network in Tensorflow.keras using SpatialDropout

```python
def neural_network_2():
    input_ = layers.Input(shape=(32,32,3)) # Define the input size of the image
    cnn = layers.Conv2D(16, (3,3), activation="relu") (input_) # first conv layer with 16 filters, by a 3 by 3 kernel size, stride 2, acitvation relu
    cnn = layers.SpatialDropout2D(0.2) # Spatial dropout with dropping rate of 20%
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

<html>
<h3>References</h3>
<list>
        <li>Brownlee, J. (2018). How to Reduce Overfitting With Dropout Regularization in Keras. Retrieved 
                from: https://machinelearningmastery.com/how-to-reduce-overfitting-with-dropout-regularization-in-
                keras/ Last access: 23.02.2020. </li>
        <li>Deeplearning.ai (2017). Why does Batch Norm work? (C2W3L06). Retrieved from: https://www.youtube.com/watch?v=nUUqwaxLnWs&feature=emb_title</li>
        <li>Ioffe, S., & Szegedy, C. (2015). Batch normalization: Accelerating deep network training by reducing 
            internal covariate shift. arXiv preprint arXiv:1502.03167.</li>
        <li>Tompson, J., Goroshin, R., Jain, A., LeCun, Y., & Bregler, C. (2015). Efficient object localization 
            using convolutional networks. In Proceedings of the IEEE Conference on Computer Vision and Pattern 
            Recognition (pp. 648-656).</li>
</list>
</html>

---

# Let's do some coding ... 