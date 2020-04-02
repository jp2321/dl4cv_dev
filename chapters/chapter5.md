---
title: 'Chapter 5: CNN Architectures'
description:
  'This chapter will introduce different CNN architectures'
prev: /chapter4
next: /chapterend
type: chapter
id: 5
---

<exercise id="28" title="CNN Architectures" type="slides">

<slides source="chapter5_01_architectures">
</slides>

</exercise>

<exercise id="29" title="Different Architectures Repetition">
The VGG network
<choice id=1>

<opt text="VGG was the first large image classification network">

This is not the correct answer.

</opt>

<opt text="VGG uses stacked convolutions, so the number of parameters can be reduced." correct="true">

Correct!

</opt>

<opt text="The VGG network uses dropout layers by default">

This is not correct either.

</opt>
</choice>

Resnets 

<choice id=2>

<opt text="Residual networks use multiple layers with different kernel sizes in parallel">

This is not correct

</opt>

<opt text="ResNets can be very deep as the skip-connection prevents vanishing gradients" correct="true">

Good job!

</opt>

<opt text="All convolutions in ResNet have a padding type of valid">

This is not correct either.

</opt>

</choice>

Inception

<choice id=3>

<opt text="Inception networks add up the results of the parallel layers">

This is not correct

</opt>

<opt text="Inception networks won the image net challenge 2012">

This is not correct

</opt>

<opt text="Inception blocks use multiple kernel sizes" correct="true">

Well done!

</opt>

</choice>

</exercise>

<exercise id="30"  title="Hands on - ResNets">
    Code a resnet 34 architecture
<codeblock id="05_01">

Fill in the blanks.

</codeblock>
</exercise>

<exercise id="31"  title="Hands on - Inception">
    Fill in the gaps for the inception module. We will code a very small model here with 3 inception blocks.
    We assume the following simplifications: All layers in a block have the same number of filters/same number of filters in the bottleneck
<codeblock id="05_02">

Fill in the blanks.

</codeblock>
</exercise>

<exercise id="32" title="Transfer Learning" type="slides">

<slides source="chapter5_02_transfer_learning">
</slides>

</exercise>

<exercise id="33"  title="Hands on - Transfer Learning">
    Fill in the gaps
<codeblock id="05_03">

</codeblock>
</exercise>

<exercise id="34" title="Transfer Learning">
    How did the parameters changed in the previous exercise?
<choice>

<opt text="The trainable parameters decreased, the non-trainable parameters increased" correct="true">

Correct!

</opt>

<opt text="The overall parameters increased">

This is not the correct answer

</opt>

<opt text="The non-trainable parameters decreased, the trainable parameters increased">

This is not correct either.

</opt>
</choice>