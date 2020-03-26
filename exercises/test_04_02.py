def test():
    from tensorflow.keras import datasets
    
    assert  model.layers[7].get_config()["name"]=='global_max_pooling2d', "Did you use a Global Max Pooling?"
    assert  model.layers[2].get_config()["rate"]==0.2, "Check the dropout rates"
    assert  model.layers[5].get_config()["name"]=='spatial_dropout2d_1', "Check the kernel size of the first conv layer"
    assert  model.layers[5].get_config()["rate"]==0.5, "Check the dropout rates"
    assert  model.layers[9].get_config()["rate"]==0.5, "Check the dropout rates"
    
    __msg__.good("WELL DONE!")
