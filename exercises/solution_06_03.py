from tensorflow.keras import applications
from tensorflow.keras import layers, models, optimizers

def model(trainable=True, number_of_layers=None):
    _input = layers.Input(shape=(224,224,3))
    transfer_learning_model = applications.inception_v3.InceptionV3(include_top=False, weights='imagenet', input_tensor=_input, pooling="avg")
    
    if number_of_layers != None:
        for i in range(0, number_of_layers):
            transfer_learning_model.layers[i].trainable=trainable
    else:
        for i in range(0, len(transfer_learning_model.layers)):
            transfer_learning_model.layers[i].trainable=trainable
    
    # output
    classification = layers.Dense(43, activation="softmax", name="classification") (transfer_learning_model.output)
    x1 = layers.Dense(1, activation="linear", name="x1") (transfer_learning_model.output)
    x2 = layers.Dense(1, activation="linear", name="x2") (transfer_learning_model.output)
    y1 = layers.Dense(1, activation="linear", name="y1") (transfer_learning_model.output)
    y2 = layers.Dense(1, activation="linear", name="y2") (transfer_learning_model.output)
    
    m = models.Model(_input, [classification, x1, x2, y1, y2])
    
    m.compile(optimizer="Adam", loss={"classification": "categorical_crossentropy", "x1": "mean_squared_error", "x2": "mean_squared_error", "y1": "mean_squared_error", "y2": "mean_squared_error"}, metrics={"classification": "acc", "x1": "mean_absolute_error"})
    
    return m 

transfer_learning_not_trainable=model(trainable=False, number_of_layers=None)
first_five_layers_not_trainable=model(trainable=False, number_of_layers=4) # index starts with zero
print(first_five_layers_not_trainable.summary())