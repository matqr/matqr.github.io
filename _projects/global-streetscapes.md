---
layout: page
title: Global Streetscapes
description: Coming soon!
status: current
---

<center>
  <img src="/assets/img/mosaic_graphical_abstract.jpg" width="900" height="600"> <br />
   <a href="">Paper</a> |
   <a href="https://github.com/ualsg/global-streetscapes">Code</a>
   <a href="https://huggingface.co/datasets/NUS-UAL/global-streetscapes">Dataset<\a>
</center>

**Abstract**

Coming soon!

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "global-streetscapes" %}
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
