from tensorflow.keras import layers, models
import numpy as np 

X_train = np.zeros(60000,32,32) # create a dataset
X_train_reshape=np.reshape(X_train,(60000, _____)) # reshape

def model():
    input_layer = layers.Input(shape=(_____,)) # Input layer
    
    hidden_layer = layers.Dense(_____, activation="relu") (input_layer) # Hidden 1
    hidden_layer = layers.Dense(_____, activation="relu") (___________) # Hidden 2

    output_layer = layers.Dense(______, activation="_______") (hidden_layer) # Output
    
    m = models.Model(input_layer, output_layer)
    m.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])
    
    return m
model = model() # get model
print(model.summary())