def test():
    from tensorflow.keras import datasets

    assert model.layers[3].get_config()["strides"] == (2,2), "Check the stride sizes"
    assert model.layers[3].get_config()["filters"] == 16, "Check the number of filters"
    assert model.layers[4].get_config()["filters"] == 16, "Check the number of filters in the bottelnack"
    assert model.layers[4].get_config()["strides"] == (2,2), "Check the stride sizes"
    assert model.layers[7].get_config()["filters"] == 32, "Check the number of filters in the bottelnack"
    assert model.layers[7].get_config()["strides"] == (1,1), "Check the stride sizes"
    assert model.layers[10].get_config()["name"] == "concatenate", "Did you concatenate the results"
    assert model.layers[10].output.shape[3] == 128, "You might missed some layers in the concatenation"
    assert model.layers[11].get_config()["strides"]==(1,1), "In the second inception module there is no downsampling anymore"
    
    __msg__.good("WELL DONE!")
