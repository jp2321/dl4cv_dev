---
type: slides
---

# Dropout 

---

# Dropout

<img src="vl2/dropout.png" alt="This image is in /static" width="50%">

Overfitting: Perform well on the training set and poorly on the test set

Motivation: Prevent overfitting

Idea: Randomly dropping out neurons and their weights

Source: Srivastava et al. (2014)

Note:

The idea of dropout is straightforward: For each mini-batch in the training process, a random proportion of the neurons are "dropped out". This means, in the forward process, these neuron outputs are not considered as the input of the next layer. Moreover, during backpropagation, the weights of the neurons will not be updated. Dropout simulates the behavior of training multiple versions of the network, which would be computationally expensive if it would be done by hand. Dropout prevents models from overfitting, which means that they perform very good on the training set, but cannot generalize the predictive performance on the test set. Meanwhile, different versions of dropouts exist, spatial dropouts for convolutions, dropouts for sequences, etc. The design recommendation for the standard dropout is using p=0.5 for the hidden layers and p<0.5 for the input layer (Srivastava et al., 2014).

---

# Dropout video

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/D8PJAL-MZv8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: Deeplearning.ai (2017)

---

# Add dropout to your network 
```python
def model():
    input_layer = layers.Input(shape=(1024,))
    
    hidden_layer = layers.Dense(10, activation="relu") (input_layer)
    dropout_layer = layers.Dropout(0.5) (hidden_layer)
    hidden_layer_2 = layers.Dense(20, activation="relu") (dropout_layer)

    output_layer = layers.Dense(10, activation="softmax") (hidden_layer_2)
    
    m = models.Model(input_layer, output_layer)
    m.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])
    
    return m
```

Note: In Tensorflow one can call the Dropout layer from the layer package

---

<html>
<h3>References</h3>
<list>
    <li> Deeplearning.ai (2017). Dropout Regularization (C2W1L06). Retrieved from: https://www.youtube.com/watch?v=D8PJAL-MZv8&feature=emb_title 
    </li>
    <li>Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: a simple 
        way to prevent neural networks from overfitting. The journal of machine learning research, 15(1), 1929-
        1958.</li>
</list>
</html>

---

# Let's do some coding ... 