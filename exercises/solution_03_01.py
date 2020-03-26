from tensorflow.keras import layers, models, datasets
import numpy as np 
#(X_train, y_train), (X_test,y_test) = datasets.cifar10.load_data()
X_train = np.zeros((60000,32,32))
X_train_reshape=np.reshape(X_train,(60000, 1024))

def model():
    input_layer = layers.Input(shape=(1024,))
    
    hidden_layer = layers.Dense(10, activation="relu") (input_layer)
    hidden_layer = layers.Dense(20, activation="relu") (hidden_layer)

    output_layer = layers.Dense(10, activation="softmax") (hidden_layer)
    
    m = models.Model(input_layer, output_layer)
    m.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])
    
    return m
model = model() # get model
print(model.summary())