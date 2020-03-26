from tensorflow.keras import layers, models, datasets, optimizers
import numpy as np

def neural_network_spatial():
    input_ = layers.Input(shape=(32,32,3))
    cnn = layers.Conv2D(16, (3,3), activation="relu") (input_)
    cnn = layers.SpatialDropout2D(0.2) (cnn)
    cnn = layers.MaxPooling2D() (cnn)
    
    cnn = layers.Conv2D(32, (3,3), activation="relu") (cnn)
    cnn = layers.SpatialDropout2D(0.5) (cnn)
    cnn = layers.MaxPooling2D() (cnn)
    
    flatten = layers.GlobalMaxPooling2D() (cnn)
    
    dense = layers.Dense(32, activation="relu") (flatten)
    dense = layers.Dropout(0.5) (dense)
    dense = layers.Dense(16,  activation="relu") (dense)
    
    output = layers.Dense(10, activation="softmax") (dense)
    
    opt = optimizers.Adam()
    
    m= models.Model(input_, output)
    m.compile(optimizer=opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    
    return m
model = neural_network_spatial() # get model
print(model.summary())