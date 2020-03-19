def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert (183,275) in bw_image.shape, "Are you using black and white image"
    assert (183,275,3) in bw_image.shape, "Are you using a colored image"
    

    __msg__.good("Well done!")
