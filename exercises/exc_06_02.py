from tensorflow.keras import applications
from tensorflow.keras import layers, models, optimizers

def model():
    _input = layers.Input(shape=(224,224,3))
    transfer_learning_model = applications.inception_v3.__________(include_top=False, weights='imagenet', input_tensor=_input, pooling="avg")
    
    # output
    classification = layers.Dense(43, activation="softmax", name="classification") (_____________.output)
    x1 = layers.Dense(1, activation="linear", name="x1") (transfer_learning_model.output)
    x2 = layers.Dense(1, activation="linear", name="x2") (transfer_learning_model.output)
    y1 = layers.Dense(1, activation="linear", name="y1") (transfer_learning_model.output)
    y2 = layers.Dense(1, activation="linear", name="y2") (transfer_learning_model.output)
    
    m = models.Model(_input, [_______, _______, _______, ________, ________]) # use here the outputs from classification and x1 to y2
    m.compile(optimizer="Adam", loss={"classification": "categorical_crossentropy", "x1": "mean_squared_error", "x2": "mean_squared_error", "y1": "mean_squared_error", "y2": "mean_squared_error"}, metrics={"classification": "acc", "x1": "mean_absolute_error"})
    
    return m 

transfer_yolo = model()
print(transfer_yolo.summary())