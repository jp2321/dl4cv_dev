from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import layers, models
import numpy as np
import pandas as pd 

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
categories = pd.Series(y_train)
selected = categories[(categories.values == 0) | (categories.values) == 1].index
categories = categories[selected]
print(len(categories))

train = X_train[selected]
print(len(train))
train = np.reshape(train, (12000,784))

def simple_model():
    input_layer = layers.Input(shape=(784,))
    
    hidden_layer = layers.Dense(20, activation="relu") (input_layer) # first relu --> sigmoid
    
    output_layer = layers.Dense(1, activation="sigmoid") (hidden_layer)
    
    m = models.Model(input_layer, output_layer)
    m.compile(loss="binary_crossentropy", optimizer="adam", metrics=["acc"])
    
    return m

our_first_model = simple_model()
print(our_first_model.summary())
our_first_model.fit(train, categories, epochs=60, batch_size=16)