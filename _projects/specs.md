---
layout: page
title: SPECS
description: A comprehensive Perception Evaluation Considering Socioeconomics (SPECS) dataset with participants' demographics and personalities.
status: current
---

<!-- <center> -->
<!--   <img src="/assets/img/TODO.jpg" width="900" height="600"> <br /> -->
<!--    <a href="TODO">Project</a> | -->
<!--    <a href="TODO">Paper</a> | -->
<!--    <a href="TODO">Code</a> | -->
<!--    <a href="TODO">Dataset</a> -->
<!-- </center> -->
<!---->
<!-- **Summary** -->
<!---->
<!---->
<!-- While both the [paper]() and [repository]() are rich in details, on [this website]() you can find a description of what we do in a nutshell. -->
<!-- For more information, please refer to the [paper](). -->
<!---->

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "specs" %}
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
