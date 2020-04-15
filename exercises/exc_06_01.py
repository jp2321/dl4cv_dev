from tensorflow.keras import layers, models, optimizers

def model():
    img_input=layers.Input(shape=(100,100,3))

    _model=layers.Conv2D(32, (5,5), activation="relu") (img_input)
    _model=layers.MaxPooling2D() (_model)

    _model=layers.Conv2D(64,(3,3), activation="relu") (_model)
    _model=layers.MaxPooling2D() (_model)

    _model=layers.Conv2D(128,(3,3), activation="relu") (_model)
    _model=layers.MaxPooling2D() (_model)

    _model=layers.GlobalMaxPooling2D() (_model)
    _model=layers.Dense(256, activation="relu") (_model)
    _model=layers.Dense(128, activation="relu") (_model)

    # define outputs
    class_prediction=layers.Dense(________, activation=____________, name="class_prediction") (_model)
    x1_prediction=layers.Dense(______,activation="relu", name="x1_prediction") (_model)
    y1_prediction=layers.Dense(_______,activation="relu", name="y1_prediction") (_model)

    x2_prediction=layers.Dense(_______,activation="relu", name="x2_prediction") (_model)
    y2_prediction=layers.Dense(________,activation="relu", name="y2_prediction") (_model)

    # optimizer + build model
    opt=optimizers.Adam()
    full_model=models.Model(img_input, [________, x1_prediction, ___________, ____________, __________])
    full_model.compile(optimizer=opt, loss={'class_prediction': 'categorical_crossentropy','x1_prediction': 'mae', 'x2_prediction': 'mae', 'y1_prediction': 'mae', 'y2_prediction': "mae"}, metrics={'class_prediction': 'accuracy', 'x1_prediction': 'mae'})
    
    print(full_model.summary())
    return full_model

model = model()