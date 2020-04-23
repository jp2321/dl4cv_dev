---
title: 'Chapter 2: Image manipulation and feature extraction ...'
description:
  'This chapter will guide you from black and white images to feature extraction'
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="3" title="Images for a computer" type="slides">

<slides source="chapter2_01_images">
</slides>

</exercise>

<exercise id="4" title="Arrays">
<choice>
<opt text="Images are n-dimensional arrays for the computer" correct="true">

Correct!

</opt>

<opt text="Values range from 0 to 1 million for each pixel">

This is not the correct answer

</opt>

<opt text="Black and white images and colored images have the same number of channels">

This is not the correct answer

</opt>
</choice>

</exercise>


<exercise id="5" title="Coding" type="slides">

<slides source="chapter2_02_coding">
</slides>
</exercise>

<exercise id="6" title="Hands on image reading">

Read the dog.jpeg image from disk. It is in the exercise folder.
First, read it as a black and white image, second as a colored image.
Display both image.

<codeblock id="02_02">

Specify the color change for the colored image.

</codeblock>
</exercise>

<exercise id="7" title="Hands on slicing and dicing">

As the image is a NumPy array, one can "slice and dice" the image in an easy fashion.
Dice the dog image so that it shows the height from 81 to 127's pixels and the width of the 49's to 107 pixels with all color channels.

<codeblock id="02_02_1">

Slice and dice via the index of the array. Rember it starts by zero.

</codeblock>
</exercise>

<exercise id="8" title="Hands on slicing and dicing and coloring">

Set the color values for red high so that the box of 0 to 70 and 0 to 40 appears red.

<codeblock id="02_02_2">
Remember that cv2 has the order of the channels BGR.
</codeblock>
</exercise>


<exercise id="9" title="Resizing of images">
The resize command is used to change the size of the image. Instead of cropping image parts, through interpolation, the image size is changed.

Resize the dog images from its original size to 50 by 50 pixels for the image. Use the rescale command from cv2 for this.

<codeblock id="02_02_3">
    IMPORTANT: cv2 denotes the first parameter in the tuple as the width, the second as the height!
    In the NumPy array, the first is the height, the second the width!
</codeblock>

</exercise>


<exercise id="10" title="Edge detection" type="slides">

<slides source="chapter2_03_edge">
</slides>
</exercise>

<exercise id="11" title="Exercise edge detection">
Use the canny edge detector on the dog image. Use the canny edge detector two times, first with min threshold 50, max threshold 150, the second time with 100 and 200.

<codeblock id="02_02_4">
Put the hyperparameters in the Canny function
</codeblock>
</exercise>

<exercise id="12" title="Edge detection limits">
Given the two different edge detection results in the previous exercise. What holds true?

<choice>
<opt text="When the minimum value is smaller the edges are clearer pronounced">

This is not the correct answer

</opt>

<opt text="When the maximum value is smaller there are less edges">

This is not the correct answer

</opt>

<opt text="Using a higher value for the minimum and maximum boundary results in less but stronger edges" correct="true">

Correct!

</opt>
</choice>

</exercise>

<exercise id="13" title="Edge detection quiz">
<choice id=1>
<opt text="In edge detection gaussian kernels are used for denoising" correct="true">

Correct!

</opt>

<opt text="Sobel kernels are used in Canny Edge detection for denoising">

This is not the correct answer

</opt>

<opt text="Denoising is done on all three input channels">

This is not the correct answer

</opt>
</choice>

<choice id=2>
<opt text="Edges are found by the edge gradient and direction" correct="true">

Correct!

</opt>

<opt text="Edges are found by the gaussian kernel">

This is not the correct answer

</opt>

<opt text="Edges are found by standardization">

This is not the correct answer

</opt>
</choice>

</exercise>

<exercise id="14" title="HoG" type="slides">

<slides source="chapter2_04_hog">
</slides>
</exercise>

<exercise id="15" title="Exercise HoG">
 Transform the dog image into hog features.
 Rescale it to 300 by 300 pixels. Use 5 orientations, 8 by 8 pixels per cell and 2 by 2 cells per block
 
<codeblock id="02_04">
    The colormapping for showing the image should correspond to the greyscaled input
</codeblock>
</exercise>

<exercise id="16" title="Hands-on your turn">
	Select some images that you like. Create a notebook (for example in Colab) and perform the reading of the image as black and white, colored images, edge detection, hog transformation, resizing, slicing and dicing etc. to practise your image preprocessing skills. Familiarize yourself the the documentation of CV2 and scikit-image.
</exercise>
