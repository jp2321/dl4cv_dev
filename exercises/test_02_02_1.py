def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert  np.array_equal(subset,color_img[80:128,50:107,:])==True, "Are you sure this is the right dice"

    __msg__.good("Great job!")
