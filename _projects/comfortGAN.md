---
layout: page
title: comfortGAN
description: Conditional Wasserstein GAN (cWGAN) for imbalanced thermal comfort datasets
status: past
---

Balancing thermal comfort datasets: We GAN, but should we?

<center>
  <img src="/assets/img/validation_classification.jpeg"> <br />
   <a href="https://dl.acm.org/doi/10.1145/3408308.3427612">Paper</a> |
   <a href="https://github.com/buds-lab/comfortGAN">Code</a>
</center>

**Abstract**

Thermal comfort assessment for the built environment has become more available to analysts and researchers due to the proliferation of sensors and subjective feedback methods. These data can be used for modeling comfort behavior to support design and operations towards energy efficiency and well-being. By nature, occupant subjective feedback is imbalanced as indoor conditions are designed for comfort, and responses indicating otherwise are less common. This situation creates a scenario for the machine learning workflow where class balancing as a pre-processing step might be valuable for developing predictive thermal comfort classification models with high-performance. This paper investigates the various thermal comfort dataset class balancing techniques from the literature and proposes a modified conditional Generative Adversarial Network (GAN), <tt>comfortGAN</tt>, to address this imbalance scenario. These approaches are applied to three publicly available datasets, ranging from 30 and 67 participants to a global collection of thermal comfort datasets, with 1,474; 2,067; and 66,397 data points, respectively. This work finds that a classification model trained on a balanced dataset, comprised of real and generated samples from <tt>comfortGAN</tt>, has higher performance (increase between 4% and 17% in classification accuracy) than other augmentation methods tested. However, when classes representing discomfort are merged and reduced to three, better imbalanced performance is expected, and the additional increase in performance by <tt>comfortGAN</tt> shrinks to 1-2%. These results illustrate that class balancing for thermal comfort modeling is beneficial using advanced techniques such as GANs, but its value is diminished in certain scenarios. A discussion is provided to assist potential users in determining which scenarios this process is useful and which method works best.


<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "comfortGAN" %}
      <li>
        <strong>{{ item.date | date: "%b %-d, %Y" }}:</strong>
          {% if item.inline %}
            {{ item.content | remove: '<p>' | remove: '</p>' | emojify }}
          {% endif %}
      </li>
      {% endif %}
    {% endfor %}
    </ul>
  {% else %}
    <p>No news so far...</p>
  {% endif %}
</div>
