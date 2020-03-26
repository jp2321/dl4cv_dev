from tensorflow.keras import layers, models, optimizers
import numpy as np 

def neural_network():
    input_ = layers.Input(shape=(____,____,_____))
    cnn = layers.Conv2D(____, (____,3), activation="_____") (input_)
    cnn = layers.___________ (cnn)
    
    cnn = layers.Conv2D(______, (____,_____), activation="relu") (cnn)
    cnn = layers.MaxPooling2D() (cnn)
    
    flatten = layers.Flatten() (cnn)
    
    dense = layers.Dense(_________, activation="relu") (__________)
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