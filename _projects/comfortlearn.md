---
layout: page
title: TODO
description: OpenAI gym for OCC benchmarking with empirical thermal comfort 
---

Under construction!

<center>
  <img src="/assets/img/comfortlearn.jpeg"> <br />
   <a href="https://doi.org/10.1145/3563357.3566167">Paper</a> |
   <a href="https://github.com/buds-lab/ComfortLearn">Code</a>
</center>

**Abstract**

The intersection of buildings control and thermal comfort modeling may seem obvious, but there are still prevalent challenges in combining them. "Occupant centric" control strategies are mainly trained using building data but rarely leverage occupants' feedback. While thermal comfort models are developed using occupants' data but are seldom integrated into building controls. To bridge this gap, we developed an open-source simulation tool named ComfortLearn. ComfortLearn is an OpenAI Gym-based environment that leverages historical building management system data from real buildings and existing longitudinal thermal comfort datasets for occupant-centric control strategies and benchmarking. We used an evaluation metric named "exceedance" to evaluate occupants' thermal comfort and provide a more realistic picture than traditional evaluations like comfort bands. This setup allows the analysis of different building control strategies and their effect on real occupants, based on empirical data, without the need for computationally expensive co-simulations. A theoretical case study implementation shows that an as-is schedule-based controller complies with its comfort band more than 93% of the time, but the simulated occupants are comfortable for only 25% of the occupied time.

<div>
<h3> Related news</h3>
  {% if site.news  %}
    <ul>
    {% assign news = site.news | reverse %}
    {% for item in news %}
      {% if item.project == "comfortlearn" %}
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
