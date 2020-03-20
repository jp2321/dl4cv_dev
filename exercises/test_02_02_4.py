def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert  np.array_equal(canny_edge_1, cv2.Canny(image, 50, 150))==True, "Are you using the right thresholds?"
    assert  np.array_equal(canny_edge_2, cv2.Canny(image, 100, 200))==True, "Are you using the right thresholds?"

    __msg__.good("WELL DONE!")
