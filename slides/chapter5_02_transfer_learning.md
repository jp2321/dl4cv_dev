---
type: slides
---

# Transfer Learning

---

# Motivation

- Extract generalizable knowledge to another task or domain
    
- Example:
    Matrix multiplication in calculus class
    Transfer it to deep learning course
    
- Aim: Increase performance
- Few observations in the target domain
- Task is very new

Note: Most of the architectures described above are getting famous by using in Transfer Learning. Transfer Learning thereby describes the process of transferring knowledge from one domain or task to another and reuse parts of a trained model. The overall aim is to boost performance when a) fewer observations are in the target domain and training a machine learning model is not possible or b) the task is very new, and thus no data is available. 

---

# Learning strategies

<html>
<table>
    <th>Learning setting</th>
    <th>Domain</th>
    <th>Task</th>
    <tr>
        <td>Inductive</td>
        <td>same</td>
        <td>different</td>
    </tr>
    <tr>
        <td>Transductive</td>
        <td>different</td>
        <td>same</td>
    </tr>
</table>
</html>

Source: Pan & Yang, 2009

Note: Two general strategies exist. Inductive learning uses the model in the same domain but for the other task (e.g., in medicine training an algorithm with CT scans for classifying cancer and transferring knowledge to dementia classification). Transductive learning uses the gathered knowledge for the same task in the other domain.

---

# Learning strategies in detail (1)

<img src="vl4/transfer_1_1.png" alt="This image is in /static" width="50%">

Image source: https://medium.com/@subodh.malgonde/transfer-learning-using-tensorflow-52a4f6bcde3e


Note: For inductive learning, the top layer of the network (output layer) is cut-off and replaced by a domain-specific layer depending on the task. One other technique for both learning strategies if freezing layers. Thus, these layers are used in the feed-forward process of the network, but the weights are not updated in the backpropagation to keep the learned knowledge in the layers untouched.

---

# Learning strategies in detail (2)

<img src="vl4/transfer_2.png" alt="This image is in /static" width="60%">

Source: Sarkar, 2018

Note: The decision to freeze or unfreeze layers is tightly linked to the number of observations available. 

---

# Learning strategies in detail (3)

<img src="vl4/strategie.png" alt="This image is in /static" width="33%" style="transform:rotate(-0deg);">

Source: Brownlee, 2019

Note: In the middle, the cut-off solution is seen. After the flatten layer, new fully connected layers are attached to the network, performing the new task in the target domain, while the rest of the network is frozen, so it does not change the weights. On the right, the last two convolutional blocks are unfrozen so that they adapt their kernels to the new task.

A larger version of the image can be found <a href="https://miro.medium.com/max/1400/1*W91k18rRAZfJnsM8bhUDXA.png">here</a>

---

# Transfer Learning Video 

<html>
<iframe width="800" height="500" src="https://www.youtube.com/embed/yofjFQddwHE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</html>

Source: https://www.youtube.com/watch?v=yofjFQddwHE

---

<html>
<h3>References</h3>
<list>
    <li>Brownlee, J. (2019). A gentle introduction to transfer learning for deep learning. Retrieved from: https://machinelearningmastery.com/transfer-learning-for-deep-learning/ . Last access: 23.01.2020</li>
        <li>Pan, S. J., & Yang, Q. (2009). A survey on transfer learning. IEEE Transactions on knowledge and data 
            engineering, 22(10), 1345-1359.</li>
    <li> Sarkar, D. (2018). A comprehensiv hands-on guide to transfer learning with real-word applications in deep learning. Retrieved from: https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a Last Access: 23.01.2020
</li>
        <li>Torrey, L., & Shavlik, J. (2010). Transfer learning. In Handbook of research on machine learning 
            applications and trends: algorithms, methods, and techniques (pp. 242-264). IGI Global.</li>
</list>
</html>

---
# Let's do some coding ... 