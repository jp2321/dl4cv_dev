def test():
    from tensorflow.keras import datasets

    for i in range(0,10): 
        if transf_model.layers[i].trainable != False:
            assert transf_model.layers[i].trainable != False, "Are the first 10 layers frozen?"
    assert transf_model.layers[19].get_config()["name"] == 'global_average_pooling2d', "Did you use a global average pooling?"
    assert transf_model.layers[0].get_config()['batch_input_shape'] == (None, 224, 224, 3) , "Do you use the right input?"
    
    __msg__.good("WELL DONE!")
