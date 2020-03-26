def test():
    from tensorflow.keras import datasets
    
    assert  X_train_reshape.shape==(60000,1024), "What is the reshape size?"
    assert  model.layers[0].get_config()["batch_input_shape"]==(None, 1024), "Check your input size"
    assert  model.layers[1].get_config()["units"]==10, "Check the number of neurons in the first layer"
    assert  model.layers[2].get_config()["units"]==20, "Check the number of neurons in the second layer"
    assert  model.layers[2].input.shape[1] == 10, "Is the connection to the first hidden layer working?"
    assert  model.layers[3].get_config()["units"]==10, "Check the number of neurons in the output layer"
    assert  model.layers[3].get_config()["activation"]=="softmax", "Is this the activation function for multi-class"

    __msg__.good("WELL DONE!")
