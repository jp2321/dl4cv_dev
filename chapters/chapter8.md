---
title: 'Chapter 8: Adversarial attacks'
description:
  'This chapter will introduce adversarial attacks'
prev: /chapter7
next: /chapterend
type: chapter
id: 8
---

<exercise id="53" title="Adversarial attacks" type="slides">

<slides source="chapter8_01_adversarial attacks">
</slides>

</exercise>

<exercise id="54" title="Adversarial attacks Questions">
<choice id=1>

<opt text="White-box attacks are attacks where no access to the models parameters exist">

This is not the correct answer.

</opt>

<opt text="Targeted attacks are specific for LSTMs">

This is not the correct answer.

</opt>

<opt text="The attack can be formulated as an optimizations or constraint problem" correct=True>

Perfect!

</opt>

</choice>

</exercise>

<exercise id="55" title="Playing with the code - Adversarial attacks">

a) Select a dataset on your own. Train a Neural Network to perform classification.

b) Transform the test set and create adversarial examples - evaluate the performance in comparison to the original test set. 

c) Retrain the network, now with original images and adversarial images (generated from the test set). <br>
Is the performance changing on the adversarial test set?

</exercise>