def test():
    from tensorflow.keras import datasets

    #assert model.get_layer("class_prediction").get_config()["units"]==43, "Check the number of output classes"
    #assert model.get_layer("class_prediction").get_config()["activation"]=="softmax", "Check your activation function"
    
    assert transfer_yolo.layers[1].get_config()["filters"]==32, "Did you use Inception V3?"
    assert transfer_yolo.get_layer("classification").input.shape[1]==2048, "Did you connect the transfer part to the classification part?"
    assert transfer_yolo.output[0].name == 'classification/Identity:0', "How does the output look like?"
    assert transfer_yolo.output[1].name == "x1/Identity:0", "How does the output look like?"
    assert transfer_yolo.output[2].name == "x2/Identity:0", "How does the output look like?"
    assert transfer_yolo.output[3].name == 'y1/Identity:0', "How does the output look like?"
    assert transfer_yolo.output[4].name == 'y2/Identity:0', "How does the output look like?"

    #assert transfer_yolo.get_layer("y1_prediction").get_config()["units"]==1, "Check the number of outputs"
    #assert transfer_yolo.get_layer("x2_prediction").get_config()["units"]==1, "Check the number of outputs"
    #assert transfer_yolo.get_layer("y2_prediction").get_config()["units"]==1, "Check the number of outputs"
    #assert transfer_yolo.get_layer("x1_prediction").get_config()["units"]==1, "Check the number of outputs"
    
    __msg__.good("WELL DONE!")
