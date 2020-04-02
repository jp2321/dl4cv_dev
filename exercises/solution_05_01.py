from tensorflow.keras import layers, models

def resnet_block(X, F, k, downsample):
    
    # shortcut
    if downsample == True:
        x_shortcut = layers.Conv2D(F, (1,1), padding="same", strides=(2,2)) (X) # decrease input size as well
    else:
        x_shortcut = X #identity mapping
    
    # normal path
    if downsample == True:
        x = layers.Conv2D(F, (k,k), padding="same", strides=(2,2)) (X) # decrease input size with two strided convolution
    else:
        x = layers.Conv2D(F, (k,k), padding="same", strides=(1,1)) (X) # normal path
    
    x = layers.BatchNormalization() (x)
    x = layers.Activation("relu") (x)
    x = layers.Conv2D(F, (k,k), padding="same") (x)
    x = layers.BatchNormalization() (x)
   
    # add
    x = layers.Add() ([x, x_shortcut]) # add main path and skip connection
    
    x = layers.Activation("relu") (x) # final activation
    
    del X
    return x


def model():
    input_ = layers.Input(shape=(224,224,3))
    
    conv=layers.Conv2D(64, (7,7), padding="same", strides=(2,2)) (input_)
    conv=layers.Activation("relu") (conv)
    conv = layers.MaxPooling2D() (conv)
    
    block_1 = resnet_block(conv, 64, 3, downsample=False)
    block_1 = resnet_block(block_1, 64, 3, downsample=False)
    block_1 = resnet_block(block_1, 64, 3, downsample=False)
    
    block_2 = resnet_block(block_1, 128, 3, downsample=True)
    block_2 = resnet_block(block_2, 128, 3, downsample=False)
    block_2 = resnet_block(block_2, 128, 3, downsample=False)
    block_2 = resnet_block(block_2, 128, 3, downsample=False)
    
    block_3 = resnet_block(block_2, 256, 3, downsample=True)
    block_3 = resnet_block(block_3, 256, 3, downsample=False)
    block_3 = resnet_block(block_3, 256, 3, downsample=False)
    block_3 = resnet_block(block_3, 256, 3, downsample=False)
    block_3 = resnet_block(block_3, 256, 3, downsample=False)
    block_3 = resnet_block(block_3, 256, 3, downsample=False)
    
    block_4 = resnet_block(block_3, 512, 3, downsample=True)
    block_4 = resnet_block(block_4, 512, 3, downsample=False)
    block_4 = resnet_block(block_4, 512, 3, downsample=False)
    
    gap = layers.GlobalAveragePooling2D() (block_4)
    output = layers.Dense(1000, activation="sigmoid") (gap)
    m = models.Model(input_, output)
    return m

resnet_34 = model()
print(resnet_34.summary())