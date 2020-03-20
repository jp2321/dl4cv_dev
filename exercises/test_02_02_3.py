def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    #assert  if (image_red[:70,:40,2].min()==255) and (image_red[:70,:40,2].max()<=255) , "This this red? Are you on the right spot?"
    assert  np.array(color_resized).shape==(50,50,3), "Are you using the right size"

    __msg__.good("WELL DONE!")
