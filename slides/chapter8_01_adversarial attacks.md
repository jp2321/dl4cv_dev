---
type: slides
---

# Adversarial attacks

Note: In the recent development in Computer Vision and Deep Learning, often, the question arises of how trustworthy and reliable the results of neural networks are. Especially when it comes to security-related aspects of solutions in autonomous driving, medicine, or face recognition solutions should be very mature to guarantee accurate predictions. Research about adversarial attacks against machine learning algorithms has shown that these solutions may not be as mature as necessary. An adversarial is a generated input, in CV, an image that is based on an original image plus some noise created by perturbations. The noise is unrecognizable for the human eye. Thus, the neural network gets confused in the prediction so that it predicts the wrong label of the image. Adversarial attacks have the aim to test and confuse the neural network's decision making by adding as little noise as possible to the image. 

This course strongly focuses on how adversarial attacks work and how to prevent them. The authors distance themself from attacks to networks for creating ethical, social, monetary, or physical damage.

---

# An example of a physical adversarial attack
<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/4uGV_fRj0UA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=4uGV_fRj0UA 

Note: In the example above, a physical adversarial attack is demonstrated, where a traffic sign is slightly manipulated so that the autonomous driving wrongly recognizes the speed limit sign. For the human eye, it is not difficult to categorize the perturbed example as a 35 miles speed limit. 

This example shows two important points: 

First of all, computer vision applications are sometimes not so robust as it is required and shows impressively the limitations of CV systems.

Secondly, the field of countermeasures against adversarial attacks is important and has to be researched extensively to maintain safety and security for applications. The attacks on CV systems are an upcoming threat.

---

# Introduction to adversarial attacks

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/Exd6CLAYOh0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=Exd6CLAYOh0 

---

# Definition of adversarial attacks 

Example (image) for which a false prediction is made by a machine learning algorithms with just little perturbations of the original example

The example fools the machine learning with differences that are not visible for the human eye.

The statement can be formally be written as:

<img src="vl7/definition_attack.png">

Source: Yuan et al. (2018)

Note: The adversarial attack is a minimization problem, where the difference between the original image and the perturbed image should be as small as possible. The altered image x' should give the output class l', while the prediction of the original image x, should lead to class l, with respect to l not equal to l'.

---

# Example

<img src="vl7/adversarial.png">

Source: Goodfellow, Shlens, Szegedy (2014)

Note: In the figure on the slide, an example is shown that the original image with some noise will end up with a perturbed image, which is not distinguishable from the original one. The algorithm will, however, classify it wrongly. 

---

# Types of adversarial attacks I

An adversarial attack is the usage of adversarial examples on an existing neural network <br><br>
There are different scales on which adversarial attacks are rated: <br>

- False-positive: Aim to generate type 1 errors
    
    Generate negative example to be misclassified as a positive one
    
    Images unrecognizable to a human (noise) classified with a high confidence into a certain class 

- False-negative: Aim to generate type 2 errors 

    Generate positive sample to be misclassified as a negative one

    Mostly used as an attack

Source: Yuan et al. (2018)

Note: 

There are several types of adversarial attacks distinguished by different scales:

An attack can be rated on the falsification strategy, whether the networks make Type 1 or Type 2 errors. Type 1 errors are made when negative observations are falsely predicted as positive. In case of an attack, the pure noise which has no structure is categorized to a certain class e.g. a car. Type 2 errors are made when there are positive examples, the adversarial example shows a car with noise unrecognizable to the human eye, and it is wrongly predicted, e.g., as a dog.

---

# Types of adversarial attacks II

### Adversary’s Knowledge

- White Box

    The adversary knows all information about the network, has access to the parameters, number of layers, weights etc.
- Black Box

    Adversary as no access to the network

    This attack is mostly used against online services.

Note: Moreover, attacks are differentiated in white and black-box attacks, where most of the attacks are black-box attacks as the adversarial has access to the network's structure and parameters.

---

# Types of adversarial attacks III

### Adversarial Specificity
- Targeted

    Attack aims to misguide the network to a certain output.

- Non-targeted

    No clear aim about misguidance is set - thus non-targeted attacks are often easier to achieve as more flexibility in the noise creation can be used

Note: While non-targeted attacks have the aim that the adversarial example is misclassified, targeted attacks aim for misclassification with a specific target (class).


---

# Types of adversarial attacks IV

### Attack frequency
- One-time attack

Only one-time optimization of the adversarial example

- Iterative attacks

Multiple updates of the adversarial examples

Source: Yuan et al. (2018)

Note: While non-targeted attacks have the aim that the adversarial example is misclassified, targeted attacks aim for misclassification with a specific target (class).

---

# Types of adversarial attacks V

### Pertubation Scope
- Individual

For each example in the dataset, the individual perturbations are calculated

- Universal

A universal perturbation is created for the whole dataset.

Note: Most of the attacks are individual attacks, so that for each example in the dataset, the noise is individually calculated, while universal attacks create one noise for the whole dataset.

---

# Types of adversarial attacks VI

### Pertubation Limitation

- Optimized Perturbation

Perturbations are the goal of the minimization problem.

- Constraint Pertubation

Are the constraint of the minimization problem


Source: Yuan et al. (2018)

Note: Lastly, attacks can be distinguished on how the perturbations are calculated. Either they are part of the optimization to minimize the perturbations, thus called optimized perturbations. The attack can also be formulated from an constraint focus. Thus the perturbations are not the goal but the constraints in the optimization problem. The "only" have to be good enough to fool the network.

---

# Perturbation measures

- ℓ𝑝 is the p-normed distance between the original image and the adversarial example
- ℓ0 count the number of pixels changed in the adversarial example
- ℓ2 measures the euclidean distance between image and example
- ℓ∞ maximum change for all pixels

<img src="vl7/pertubation.png">

Note: The strength of the perturbations can be measured with different measurements. The l0 norms counts the total number of pixel changed; the l2 norm calculates the difference between the original image and the adversarial example and the lmax norm rates the perturbations on the maxium change of all pixels.

---

# Attack methods


- L-BFGS Attack (2014), Szegedy et al
- Fast Gradient Sign Method (FGSM), 2014, Goodfellow et al.
- Fast Gradient Value method, 2016, Roza, Rudd, Boult
- One-step Target Class Method (OTCM), 2017, Kurkin, Goodfellow, Bengio
- Jacobian-based Saliency Map Attack (JSMA), 2016, Papernot et al.
- DeepFool, 2016, Moosavi-Dezfooli, Fawzi, Frossard
(...)

Source: Yuan et al. (2018)

Note: There are a lot of different attacks. Detailed information can be found in their original papers or in Yuan et al. (2018). This course will focus on the Fast Gradient Sign Method.

---

# Fast Gradient Sign Methods (FGSM)

To calculate the perturbations is often a complex and expensive linear search method 
FGSM is a technique to increase efficiency by making use of the gradient of the weights and linearity between adversarial noise and image

<img src="vl7/fast_sign.png">

ϵ is a small number and accounts for the magnitude of the perturbation

Note: Goodfellow, Shlens, and Szegedy came up with a fast method to generate adversarial examples. Their idea is to use the network properties itself to find vulnerable spaces in the network. Therefore, the gradient for a specific input image is calculated with respect to its output. The gradients of the loss function contain information about the importance of each pixel. Therefore a small noise in the form of epsilon is added or subtracted from the original image, depending on the sign of the pixel gradient. Adding errors in the direction of the gradients means increasing the loss, thus confusing the algorithm. Especially vulnerable are networks that favor linearity like LSTM or maxout networks and relu based networks. 

Source: Goodfellow, Shlens, Szegedy (2014)

In other words:

The perturbed image is the original image plus some noise. The assumption is that the relationship between image and noise is linear. The noise is the sign of the gradient multiplied with a small epsilon that accounts for the magnitude of the perturbation. The advantage of this attack is that it is very efficient to compute by the gradients, however, as the model parameters need to be accessible, it is a white-box attack

---

# Measurements against attacks

- Reactive: Detect adversarial examples after the neural network has been built
- Proactive: Make the network more robust to adversarial examples

Source: Yuan et al. (2018)

---

# Reactive measures

- Adversarial Detecting
- Input Reconstruction
- Network Verification

Source: Yuan et al. (2018)

Note: In adversarial detecting, the image that is classified is validated in a separate network with a binary outcome if this is an adversarial example or the original image. For Input reconstruction, the aim is to reconstruct the image by an autoencoder (encoder-decoder network). 

---

# Proactive measures

- Network Distillation
- Adversarial (Re) Training
- Classifier Robustifying

Source: Yuan et al. (2018)

Note: The easiest way is to train or retrain the network with original images and adversarial ones, both with the original label. The hypothesis is that the network gets more robust to adversarial patterns. Classifier robustyfing uses 

---

# Coding FSGM

```python
loss_object = tensorflow.keras.losses.CategoricalCrossentropy()

def create_adversarial_pattern(input_image, input_label):
    input_image = tensorflow.convert_to_tensor(input_image) # convert numpy array to tensor
    input_label = tensorflow.convert_to_tensor(input_label) # convert numpy array to tensor
    
    with tensorflow.GradientTape() as tape:
        tape.watch(input_image) # trace the image
        prediction = model(input_image) # get the prediction
        loss = loss_object(input_label, prediction) # calculate the loss with the truth (input_label) and prediction
        
    # Get the gradients of the loss w.r.t to the input image.
    gradient = tape.gradient(loss, input_image)
    # Get the sign of the gradients to create the perturbation
    signed_grad = tensorflow.sign(gradient)
    
    return signed_grad

# Apply the signed gradient to the original image to create adversarial example 
eps=0.005 # Strength of the pertubation
perturbations = create_adversarial_pattern(image, label) # calculate the signed gradient 
adv_x = image + eps*perturbations # alter the image

```

Source: Tensorflow (2020)

Note: This code snippet is from Tensorflow and shows how the fast signs are calculated. Therefore, first, the image is converted from a numpy array to a tensor format. The gradient tape operation records the gradients of functions. The loss is calculated by applying the loss function with the original label and the prediction as inputs. The derivative of the loss (gradients) are calculated with respect to the input image. Afterwards, the sign of the gradients are extracted. To apply the perturbations, the signs are multiplied by epsilon, a very small number to create the pixel change values. Afterward, they are added to the original image.

---

# Your task

Take your own dataset, create your own model. Train the model up to a good performance. Create adversarial examples from the test set and test the performance.
In a second step, create adversarial examples additional to the original examples. Retrain the network with both and test the performance on the test adversarial set

---
<html>
<h3>References</h3>
<list>
        <li> Goodfellow, I. J., Shlens, J., & Szegedy, C. (2014). Explaining and harnessing adversarial examples. arXiv preprint arXiv:1412.6572.</li>
    <li>Tensorflow (2020). Adversarial example using FGSM. https://www.tensorflow.org/tutorials/generative/adversarial_fgsm  Last Access on: 09.03.2020</li>
    <li>Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., & Fergus, R. (2013). Intriguing properties of neural networks. arXiv preprint arXiv:1312.6199. </li>
    <li>Yuan, X., He, P., Zhu, Q., & Li, X. (2019). Adversarial examples: Attacks and defenses for deep learning. IEEE transactions on neural networks and learning systems, 30(9), 2805-2824.</li> 
</list>
</html>
</html>

---

# Let's do some coding ...  