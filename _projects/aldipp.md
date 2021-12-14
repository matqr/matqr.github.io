---
layout: page
title: ALDI++
description: Under review!
---

Under construction!

<!--
<icenter>
  <img src="/assets/img/validation_classification.jpeg"> <br />
   <a href="https://dl.acm.org/doi/10.1145/3408308.3427612">Paper</a> |
   <a href="https://github.com/buds-lab/comfortGAN">Code</a>
</center>
-->

**Abstract**
Under construction!

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
