from tensorflow.keras import layers, models, datasets, optimizers
import numpy as np 

def neural_network():
    input_ = layers.Input(shape=(32,32,3))
    cnn = layers.Conv2D(16, (3,3), activation="relu") (input_)
    cnn = layers.MaxPooling2D() (cnn)
    
    cnn = layers.Conv2D(32, (3,3), activation="relu") (cnn)
    cnn = layers.MaxPooling2D() (cnn)
    
    flatten = layers.Flatten() (cnn)
    
    dense = layers.Dense(32, activation="relu") (flatten)
    dense = layers.Dense(16,  activation="relu") (dense)
    
    output = layers.Dense(10, activation="softmax") (dense)
    
    opt = optimizers.Adam()
    
    m= models.Model(input_, output)
    m.compile(optimizer=opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    
    return m
model = neural_network() # get model
print(model.summary())