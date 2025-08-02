---
layout: page
title: JITAI
description: Just-In-Time Adaptive Intervention
status: current
---

The emerging just-in-time adaptive intervention (JITAI) concept is gaining momentum in fields such as mobile health as a means of influencing behavior. We propose a novel methodology using smartwatch-based JITAI combined with micro-ecological momentary assessments (EMA) for field-based data collection and occupant behavior interventions in field-based scenarios.

<center>
  <img src="/assets/img/jitai-framework.jpg"> <br />
   <!-- <a href="https://iopscience.iop.org/article/10.1088/1742-6596/1343/1/012145/meta">Paper</a> | -->
   <!-- <a href="https://github.com/cozie-app">Code</a> | -->
   <!-- <a href="https://cozie.app/">Docs</a> -->
</center>

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
          {% if project == page.title %}
            {% assign project_match = true %}
            {% break %}
          {% endif %}
        {% endfor %}
      {% comment %} Handle case where project is a single string {% endcomment %}
      {% elsif item.project == page.title %}
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
