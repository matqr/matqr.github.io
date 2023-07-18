---
layout: page
title: cozie
description: Smartwatch application for subjective feedback data collection
status: current
---

A smartwatch  application that collects momentary assessments of thermal, aural, lighting, and other subjective comfort parameters. The platform is being developed for researchers anywhere in the world to use a methodological component.

<center>
  <img src="/assets/img/cozie.png"> <br />
   <a href="https://iopscience.iop.org/article/10.1088/1742-6596/1343/1/012145/meta">Paper</a> |
   <a href="https://github.com/cozie-app">Code</a> |
   <a href="https://cozie.app/">Docs</a>
</center>

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "cozie" %}
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
