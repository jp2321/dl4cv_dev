from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, models

def transfer_learning_model():
    input_=layers.Input(shape=(224,224,3)) # input layer
    base = VGG16(include_top=False, input_tensor=_______, pooling=_______) # transfer learning model
    top = layers.Dense(50, activation="relu") (base._________) # dense layer connected to the base model
    output = layers.Dense(10, activation="softmax") (top) # output layer 
    
    m = models.Model(input_, output)
    
    return m

transf_model = transfer_learning_model() # create model
print(transf_model.summary()) 

for l in range(0,10): # iterate through the layers list 
    transf_model.layers[l].trainable=________ # set trainable to false

print(transf_model.summary()) # Number of trainable parameters has changed

transf_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"]) # compile model