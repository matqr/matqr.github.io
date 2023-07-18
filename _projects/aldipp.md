---
layout: page
title: ALDI++
description: Computationally fast discord detection on energy data
status: past
---

ALDI++: Automatic and parameter-less discord and outlier detection for building energy load profiles

<center>
  <img src="/assets/img/bubbleplot_comparison-forecasting_paper.png"> <br />
   <a href="https://www.sciencedirect.com/science/article/pii/S0378778822002675?dgcid=coauthor">Paper</a> |
   <a href="https://github.com/buds-lab/aldipp">Code</a>
</center>

**Abstract**

Data-driven building energy prediction is an integral part of the process for measurement and verification, building benchmarking, and building-to-grid interaction.
The ASHRAE Great Energy Predictor III (GEPIII) machine learning competition used an extensive meter data set to crowdsource the most accurate machine learning workflow for whole building energy prediction. A significant component of the winning solutions was the pre-processing phase to remove anomalous training data. Contemporary pre-processing methods focus on filtering statistical threshold values or deep learning methods requiring training data and multiple hyper-parameters. A recent method named ALDI (Automated Load profile Discord Identification) managed to identify these discords using matrix profile, but the technique still requires user-defined parameters. We develop ALDI++, a method based on the previous work that bypasses user-defined parameters and takes advantage of discord similarity. We evaluate ALDI++ against a statistical threshold, variational auto-encoder, and the original ALDI as baselines in classifying discords and energy forecasting scenarios. Our results demonstrate that while the classification performance improvement over the original method is marginal, ALDI++ helps achieve the best forecasting error improving 6% over the winning's team approach with six times less computation time.

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "aldipp" %}
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
