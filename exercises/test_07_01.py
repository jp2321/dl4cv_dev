def test():
    assert semantic_seg_model.layers[13].get_config()["filters"]==13, "How many filters are needed in the skip connection for the prediction?"
    assert semantic_seg_model.layers[13].input.name == 'max_pooling2d_3/Identity:0', "Is the skip connection layer correctly connected to the network?"
    assert semantic_seg_model.layers[11].get_config()["filters"]==4096, "What are the number of filters in the last part of the encoding?"
    assert semantic_seg_model.layers[11].get_config()["kernel_size"]==(1,1), "What is the kernel_size in the last part of the encoding?"
    assert semantic_seg_model.layers[14].get_config()["size"]==(2,2), "How strong does the main path need to be upsampled?"
    if (semantic_seg_model.layers[15].input[0].name == "conv2d_4/Identity:0") and (semantic_seg_model.layers[15].input[1].name == "up_sampling2d/Identity:0"): assert True, "Which layers need to be added?"
    assert semantic_seg_model.layers[16].get_config()["activation"] == "softmax", "Which activation function is necessary for the pixel class prediction?"
    assert semantic_seg_model.layers[17].get_config()["size"] == (16,16), "What is the size of the last upsampling?"

    
    __msg__.good("WELL DONE!")
