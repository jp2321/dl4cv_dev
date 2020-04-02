from tensorflow.keras import layers, models

def inception_block(X, F,F_bottelnack, downsample):
    if downsample == True: # downsample via strided convolutions
        strides=(2,2)
    else:
        strides=(1,1)
    
    # 1 by 1 convolution    
    conv_1 = layers.Conv2D(F, (1,1), padding="same", strides=______, activation='relu') (X)

    # 3 by 3 convolution
    conv_3 = layers.Conv2D(________, (1,1), padding="same", strides=_____, activation='relu') (X)
    conv_3 = layers.Conv2D(________, (3,3), padding="same", activation='relu') (conv_3)
    
    # 5 by 5 convolution
    conv_5 = layers.Conv2D(______, (1,1), padding="same", strides=______, activation='relu') (X)
    conv_5 = layers.Conv2D(F, (5,5), padding="same", activation="relu") (conv_5)
    
    # Pooling operation with 1 by 1 convolution to keep dimensions
    pool_3 = layers.MaxPooling2D((3,3), strides=(1,1), padding='same')(X)
    pool_3 = layers.Conv2D(F, (1,1), strides=strides, padding='same', activation='relu')(pool_3)

    # concatenate the results
    concat = layers._________(_________, axis = 3)
    
    return concat

def model_inception_blocks():
    input_ = layers.Input(shape=(224,224,3))
    
    conv=layers.Conv2D(16, (7,7), padding="same", strides=(2,2)) (input_)
    conv=layers.Activation("relu") (conv)
    
    inception_1 = inception_block(conv, 32, 16, downsample=True)
    inception_2 = inception_block(inception_1, 64 ,32, downsample=False)
    inception_3 = inception_block(inception_1, 128,64, downsample=False)
    
    gap = layers.GlobalAveragePooling2D() (inception_3)
    output = layers.Dense(1000, activation="sigmoid") (gap)
    m = models.Model(input_, output)
    
    return m

model = model_inception_blocks()
print(model.summary())