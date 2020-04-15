---
title: 'Chapter 7: Semantic Segmentation'
description:
  'This chapter will introduce different techniques for semantic segmentation'
prev: /chapter6
next: /chapterend
type: chapter
id: 7
---

<exercise id="40" title="Image segmentation" type="slides">

<slides source="chapter7_01_semantic_segmentation">
</slides>

</exercise>

<exercise id="41" title="Image segmentation Theorie Questions">
<choice id=1>

<opt text="FCN-32 have often the best output as they are very fine-granular">

This is not the correct answer.

</opt>

<opt text="FCN-32 are often better than FCN-16 as they upsample more">

This is not the correct answer.

</opt>

<opt text="The U-Net gives often the best output as regions are fine-granular" correct=True>

Perfect!

</opt>

</choice>

</exercise>

<exercise id="42" title="Coding a FCN-16" >
	Code a FCN-16 Network. Use 4096 and kernel size (1,1) in the last layer of the encoding.
	<img src="vl6/fcn_16.png" width=500 height=5‚00>
	Image source: Tsang (2018)

<codeblock id="07_01">
</codeblock>
</exercise>


<exercise id="43" title="Image segmentation Results of the Notebook">
	Run the given notebook about image segmentation.
<choice id="1">

<opt text="FCN-16 performs better than FCN-32 in the mean accuracy metric">

This is not the correct answer.

</opt>

<opt text="FCN-16 performs best in IoU">

This is not the correct answer.

</opt>

<opt text="The U-Net has a higer IoU for classes 0 and 1 for the test set" correct=True>

Perfect!

</opt>
</choice>

Change now the epochs of the U-Net to 50. What happens to the performance

<choice id="2">

<opt text="The U-Net performance breaks down due to overfitting" correct=True>

Perfect!

</opt>

<opt text="The U-Net performance increases to an IoU of 0.85 in class 1">

This is not the correct answer!

</opt>

<opt text="The performance stays the same">
	This is not the correct answer!
</opt>

</choice>

</exercise>