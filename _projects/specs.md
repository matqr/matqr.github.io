---
layout: page
title: SPECS
description: A comprehensive Perception Evaluation Considering Socioeconomics (SPECS) dataset with participants' demographics and personalities.
status: current
project: specs
---

<center>
<img src="/assets/img/methodology.png" width="900" height="600"> <br />
<!-- <a href="todo">project</a> | -->
<a href="https://arxiv.org/abs/2505.12758">paper</a> |
<a href="https://github.com/matqr/specs">code</a> |
<a href="https://huggingface.co/datasets/matiasqr/specs">dataset</a>
</center>

**summary**
<!---->
<!---->
<!-- while both the [paper]() and [repository]() are rich in details, on [this website]() you can find a description of what we do in a nutshell. -->
<!-- for more information, please refer to the [paper](). -->
<!---->

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% assign project_match = false %}
      {% comment %} Handle case where project is an array {% endcomment %}
      {% if item.project.size > 1 %}
        {% for project in item.project %}
          {% if project == page.project%}
            {% assign project_match = true %}
            {% break %}
          {% endif %}
        {% endfor %}
      {% comment %} Handle case where project is a single string {% endcomment %}
      {% elsif item.project == page.project%}
        {% assign project_match = true %}
      {% endif %}
      {% if project_match %}
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
