def test():
    
    for i in range(0, len(transfer_learning_not_trainable.layers)-5):
        assert transfer_learning_not_trainable.layers[i].trainable == False, "Check the trainability of the transfer model part"

    for i in range(0, 4):
        assert first_five_layers_not_trainable.layers[i].trainable == False, "Are the first five layers frozen?"

    for i in range(5, len(first_five_layers_not_trainable.layers)-5):
        assert first_five_layers_not_trainable.layers[i].trainable == True, "Are the other layers trainable"

    
    __msg__.good("WELL DONE!")
