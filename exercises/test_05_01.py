def test():
    from tensorflow.keras import datasets

    assert resnet_34.layers[1].get_config()["kernel_size"] == (7,7), "Check the kernel sizes"
    assert resnet_34.layers[1].get_config()["strides"] == (2,2), "Check strides in the first convolutional layer"
    assert resnet_34.layers[3].get_config()["name"] == "max_pooling2d", "Do you use max pooling?"
    assert resnet_34.layers[4].get_config()["filters"] == 64, "Check the number of filters in the first block"
    assert resnet_34.layers[4].get_config()["kernel_size"] == (3,3), "Check the kernel sizes"
    assert resnet_34.layers[7].get_config()["strides"] == (1,1), "What is the normal stride size?"
    assert resnet_34.layers[25].output.shape[1] == 28, "Did you downsample="
    assert resnet_34.layers[25].get_config()["filters"] == 128, "What are the number of filters in the second conv block?"
    assert resnet_34.layers[25].get_config()["padding"] == "same", "Did you use same padding?"
    assert resnet_34.layers[25].get_config()["kernel_size"] == (1,1), "Did you use 1,1 convolutions?"
    __msg__.good("WELL DONE!")
