---
layout: page
title: Global Streetescapes
description: TODO
status: current
---

<center>
  <img src="/assets/img/TODO"> <br />
   <a href="">Paper</a> |
   <a href="https://github.com/ualsg/global-streetscapes">Code</a>
</center>

**Abstract**

TODO

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "cohort-model" %}
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
