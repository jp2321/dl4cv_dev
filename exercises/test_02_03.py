def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert  np.array(bw_img).shape ==(183,275), "Are you using black and white image?"
    assert np.array(color_img).shape == (183,275,3), "Are you using a colored image?"

    __msg__.good("Well done!")
