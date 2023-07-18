---
layout: page
title: Cohort-Comfort Model (CCM)
description: Personalized Transfer of User Preferences for Cross-domain Recommendation
status: past
---

<center>
  <img src="/assets/img/cohort_framework_v2.jpeg"> <br />
   <a href="">Paper</a> |
   <a href="https://github.com/buds-lab/ccm">Code</a>
</center>

**Abstract**

Cohort Comfort Models (CCM) are introduced as a technique for creating a personalized thermal prediction for a new building occupant without the need to collect large amounts of individual comfort-related data. This approach leverages historical data collected from a sample population, who have some underlying preference similarity to the new occupant. The method uses background information such as physical and demographic characteristics and one-time onboarding surveys (satisfaction with life scale, highly sensitive person scale, personality traits) from the new occupant, as well as physiological and environmental sensor measurements paired with a few thermal preference responses. The framework was implemented using two personal comfort datasets containing longitudinal data from 55 people.
The datasets comprise more than 6,000 unique right-here-right-now thermal comfort surveys.  The results show that a CCM that uses only the one-time onboarding survey information of an individual occupant has generally as good or better performance as compared to conventional general-purpose models, but uses no historical longitudinal data as compared to personalized models. In the second dataset, one-third of the occupants increased their thermal preference prediction by 5% on average and up to 46%. CCM can be an important step toward the development of personalized thermal comfort models without the need to collect a large number of datapoints per person.

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
