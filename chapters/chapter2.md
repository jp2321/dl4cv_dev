---
title: 'Chapter 2: From Black and white to color'
description:
  'This chapter will introduce different image manipulation techniques about the colorcoded image'
prev: /chapter1
next: /chapterend
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

This is not correct either.

</opt>
</choice>

</exercise>


<exercise id="5" title="Coding" type="slides">

<slides source="chapter2_02_coding">
</slides>
</exercise>

<exercise id="6" title="Hands on image reading">

Read the dog.jpeg image from disk. It is in the exercise folder.
First read it as black and white image, second as colored image.
Display both image with the right color setting.

<codeblock id="02_02">

Specifiy the colorchange for the colored image.

</codeblock>
</exercise>

<exercise id="7" title="Hands on slicing and dicing">

As the image is a numpy array, one can "slice and dice" the image in an easy fashion.
Dice the dog image so that it shows the height from 81 to 127's pixel and the width of the 49's to 107 pixels with all color channels.

<codeblock id="02_02_1">

Slice and dice via the index of the array. Rember it starts by zero

</codeblock>
</exercise>

<exercise id="8" title="Hands on slicing and dicing and coloring">

Set the colorvalues for red high so that the box of 0 to 70 and 0 to 40 appears red.

<codeblock id="02_02_2">

</codeblock>
</exercise>


<exercise id="9" title="Resizing of images">
The resize command is used to change the size of the image. Instead of cropping image parts, through interpolation the image size is changed.

Resize the dog images from its original size to 50 by 50 pixels for image. Use the rescale command from cv2 for this.

<codeblock id="02_02_3">
	IMPORTANT: cv2 denotes the first parameter in the tuple as the width, the second as the height!
	In the numpy array, the first is the height, the second the width!
</codeblock>

</exercise>


<exercise id="10" title="Edge detection" type="slides">

<slides source="chapter2_03_edge">
</slides>
</exercise>

<exercise id="12" title="Exercise edge detection">
Use the canny edge detector on the dog image. Use the canny edge detector two times, first with min threshold is 50, max threshold 150, second time with 100 and 200.

<codeblock id="02_02_4">

</codeblock>
</exercise>

<exercise id="13" title="Edge detection limits">
Given the two different edge detected results in the previous exercise. What holds true?

<choice>
<opt text="When the minimum value is smaller the edges are stronger">

This is not the correct answer

</opt>

<opt text="When the maximum value is smaller the edges are stronger">

This is not the correct answer

</opt>

<opt text="Using a higher value for the minimum and maximum boundery results in less but stronger edges" correct="true">

Correct!

</opt>
</choice>

</exercise>

<exercise id="14" title="Edge detection quiz">
<choice id=1>
<opt text="In edge detection gaussian kernels are used for de-noiseing" correct="true">

Correct!

</opt>

<opt text="Sobel kernels are used in Canny Edge detection for de-noiseing">

This is not the correct answer

</opt>

<opt text="De-noiseing is done on all three input channels">

This is not correct either.

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

This is not correct either.

</opt>
</choice>

</exercise>

<exercise id="15" title="HoG" type="slides">

<slides source="chapter2_04_hog">
</slides>
</exercise>


<exercise id="16" title="HoG Feature calculation">
Given is the dog images resized to 300 by 300 pixels.
Calculate how many hog features are derived when, cells per block are 3, pixels per cell are 8 and bins are 15.

<choice>
<opt text="When the minimum value is smaller the edges are stronger">

This is not the correct answer

</opt>

<opt text="When the maximum value is smaller the edges are stronger">

This is not the correct answer

</opt>

<opt text="Using a higher value for the minimum and maximum boundery results in less but stronger edges" correct="true">

Correct!

</opt>
</choice>

<exercise id="17" title="Exercise HoG">

<codeblock id="02_04">
	Hint
</codeblock>
</exercise>

<exercise id="111" title="Test">

<codeblock id="02_03">
	Hint
</codeblock>
</exercise>

