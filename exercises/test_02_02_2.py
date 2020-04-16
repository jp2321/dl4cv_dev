def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    #assert  if (image_red[:70,:40,2].min()==255) and (image_red[:70,:40,2].max()<=255) , "This this red? Are you on the right spot?"
    i = cv2.imread('exercises/dog.jpeg', cv2.IMREAD_COLOR)
    i[:70,:40,2]=255
    assert  np.array_equal(image_red,i), "This this red? Are you on the right spot?"

    __msg__.good("Nice!")
