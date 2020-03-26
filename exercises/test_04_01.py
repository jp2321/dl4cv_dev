def test():
    from tensorflow.keras import datasets
    
    assert  model.layers[0].get_config()["batch_input_shape"]==(None, 32,32,3), "Check your input size"
    assert  model.layers[1].get_config()["filters"]==16, "Check the number of filters for the first conv layer"
    assert  model.layers[1].get_config()["kernel_size"]==(3,3), "Check the kernel size of the first conv layer"
    assert  model.layers[1].get_config()["activation"]=="relu", "Is this a relu activation?"
    assert  model.layers[2].get_config()["name"]=='max_pooling2d', "Do you use a max pooling layer after the first conv?"
    #assert  model.layers[2].input.shape[1] == 10, "Is the connection to the first hidden layer working?"
    assert  model.layers[3].get_config()["filters"]==32, "Check the number of filters of the second conv layer"
    assert  model.layers[3].get_config()["kernel_size"]==(3,3), "Check the kernel size of the second conv layer"
    assert  model.layers[6].get_config()["units"]==32, "Check the number of neurons in the first fully connected layer"
    assert  model.layers[6].input.shape[1]==1152, "Is the dense layer connected to the flatten layer?"
    
    __msg__.good("WELL DONE!")
