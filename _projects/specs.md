---
layout: page
title: SPECS
description: A comprehensive Perception Evaluation Considering Socioeconomics (SPECS) dataset with participants' demographics and personalities.
status: current
project: specs
---

<center>
<img src="/assets/img/methodology.png" width="800" height="600"> <br />
<!-- <a href="todo">project</a> | -->
<a href="https://www.nature.com/articles/s44284-025-00330-x">paper</a> |
<a href="https://github.com/matqr/specs">code</a> |
<a href="https://huggingface.co/datasets/matiasqr/specs">dataset</a>
</center>

**Summary**

Understanding people’s preferences is crucial for urban planning, yet current approaches often combine responses from multi-cultural populations, obscuring demographic differences and risking amplifying biases.
We conducted a large-scale urban visual perception survey of streetscapes worldwide using street view imagery, examining how demographics—including gender, age, income, education, race and ethnicity, and personality traits—shape perceptions among 1,000 participants with balanced demographics from five countries and 45 nationalities.
This dataset, Street Perception Evaluation Considering Socioeconomics, reveals demographic- and personality-based differences across six traditional indicators—safe, lively, wealthy, beautiful, boring, depressing—and four new ones: live nearby, walk, cycle, green.
Location-based sentiments further shape these preferences.
Machine-learning models trained on existing global datasets tend to overestimate positive indicators and underestimate negative ones compared to human responses, underscoring the need for local context.
Our study aspires to rectify the myopic treatment of street perception, which rarely considers demographics or personality traits.

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
