from tensorflow.keras import applications
from tensorflow.keras import layers, models, optimizers, metrics

num_classes = 13

def FCN_16():
    input_ = layers.Input(shape=(256,256,3))
    
    # Encoder
    conv_1 = layers.Conv2D(32,3, activation="relu", padding="same") (input_)
    conv_1 = layers.MaxPooling2D((2,2)) (conv_1)
    
    conv_2 = layers.Conv2D(64,3, activation="relu", padding="same") (conv_1)
    conv_2 = layers.MaxPooling2D((2,2)) (conv_2)
    
    conv_3 = layers.Conv2D(128,3, activation="relu", padding="same") (conv_2)
    conv_3 = layers.MaxPooling2D((2,2)) (conv_3)
    
    conv_4 = layers.Conv2D(256,3, activation="relu", padding="same") (conv_3)
    conv_4 = layers.MaxPooling2D((2,2)) (conv_4)

    # Branch
    conv_4_pred = layers.Conv2D(num_classes,1, activation="relu", padding="same") (conv_4)

    # Main Path
    conv_5 = layers.Conv2D(512,3, activation="relu", padding="same") (conv_4)
    conv_5 = layers.MaxPooling2D((2,2)) (conv_5)
    
    
    
    conv_5 = layers.Conv2D(4096,1, activation="relu", padding="same") (conv_5)
    
    # Decoder
    pred = layers.Conv2D(num_classes,1, activation="relu", padding="same") (conv_5)
    pred = layers.UpSampling2D((2,2)) (pred)

    add = layers.Add()([conv_4_pred, pred])

    conv = layers.Conv2D(num_classes,1, activation="softmax", padding="same") (add) #filter size
    
    upsampling = layers.UpSampling2D((16,16)) (conv)
    m = models.Model(input_,upsampling)
    
    m.compile(loss="categorical_crossentropy", optimizer=optimizers.Adam(lr=0.001), metrics=["accuracy", metrics.MeanIoU(num_classes=13)])
    return m

# Create model 
semantic_seg_model = FCN_16()