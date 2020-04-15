def test():
    from tensorflow.keras import datasets

    assert model.get_layer("class_prediction").get_config()["units"]==43, "Check the number of output classes"
    assert model.get_layer("class_prediction").get_config()["activation"]=="softmax", "Check your activation function"
    assert model.output[0].name== 'class_prediction/Identity:0', "How does the output look like?"
    assert model.output[2].name== 'y1_prediction/Identity:0', "How does the output look like?"
    assert model.output[3].name== 'x2_prediction/Identity:0', "How does the output look like?"
    assert model.output[4].name== 'y2_prediction/Identity:0', "How does the output look like?"
    assert model.get_layer("y1_prediction").get_config()["units"]==1, "Check the number of outputs"
    assert model.get_layer("x2_prediction").get_config()["units"]==1, "Check the number of outputs"
    assert model.get_layer("y2_prediction").get_config()["units"]==1, "Check the number of outputs"
    assert model.get_layer("x1_prediction").get_config()["units"]==1, "Check the number of outputs"
    
    __msg__.good("WELL DONE!")
