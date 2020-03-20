def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    resize_img_2 = cv2.resize(image, (300,300))
    fd_2, hog_image_2 = hog(resize_img, orientations=5, pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), visualize=True, multichannel=False)

    assert  np.array_equal(hog_image, hog_image_2)==True, "Check the pixels per cell"
    assert  np.array_equal(resize_img, resize_img_2)==True, "Did you resize the image to the right size"

    __msg__.good("Perfect!")
