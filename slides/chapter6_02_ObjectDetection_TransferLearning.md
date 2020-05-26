---
type: slides
---

# Transfer Learning in Object Detection

---

```python
def model():
    _input = layers.Input(shape=(224,224,3))
    transfer_learning_model = applications.inception_v3.InceptionV3(include_top=True, weights='imagenet', input_tensor=_input, pooling="avg")
    
    # output
    classification = transfer_learning_model.output
    x1 = layers.Dense(1, activation="linear", name="x1") (transfer_learning_model.layers[-1].output)
    x2 = layers.Dense(1, activation="linear", name="x2") (transfer_learning_model.layers[-1].output)
    y1 = layers.Dense(1, activation="linear", name="y1") (transfer_learning_model.layers[-1].output)
    y2 = layers.Dense(1, activation="linear", name="y2") (transfer_learning_model.layers[-1].output)
    
    m = models.Model(_input, [classification, x1, x2, y1, y2])
    m.compile(optimizer="Adam", loss={"predictions": "categorical_crossentropy", "x1": "mean_squared_error", "x2": "mean_squared_error", "y1": "mean_squared_error", "y2": "mean_squared_error"}, metrics={"predictions": "acc", "x1": "mean_absolute_error"})
    
    return m 

```

Note: Instead of just using the transfer model up to the global pooling or flatten layer, one can also use the classification part for the prediction. Therefore call the network with the include_top parameter on True and connect the classification output placeholder to the output of the network. For the estimation of the coordinates, the classification layer of the transfer_learning_model should not be used. Therefore, these layers are connected to the global pooling layer. In this example, Inception V3 has just the classification layer after the pooling. Thus, the connection has to be made to the second last layer or layer at index -1. 

---

# Keep coding!