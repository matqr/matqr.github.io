---
layout: page
title: edX - Applied data science MOOC
description: Data Science for Construction, Architecture and Engineering Online EDx Course
---

The [BUDS Lab](https://www.budslab.org/) hosts the first Massive Open Online Course (MOOC) focused specifically on data analytics from the various phases of the building life cycle - design, construction, and operations. This is an introductory course that adds Python, the Pandas Data Analytics library and various visualization and machine learning techniques to the toolbox of architects, engineers, operations, and other industry professionals.

<center>
  <img src="/assets/img/edx.png"> <br />
   <!-- <a href="https://iopscience.iop.org/article/10.1088/1742-6596/1343/1/012145/meta">Paper</a> |
   <a href="https://github.com/cozie-app">Code</a> |
   <a href="https://cozie.app/">Docs</a>  -->
</center>

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "edx" %}
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
