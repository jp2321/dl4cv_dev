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


<exercise id="111" title="Test">

<codeblock id="02_03">
	Hint
</codeblock>
</exercise>

