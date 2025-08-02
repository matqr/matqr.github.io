---
layout: page
title: Global Streetscapes
description: A comprehensive dataset of 10 million street-level images across 688 cities for urban science and analytics
status: current
---

<center>
  <img src="/assets/img/mosaic_graphical_abstract.jpg" width="900" height="600"> <br />
   <a href="https://ual.sg/project/global-streetscapes/">Project</a> |
   <a href="https://www.sciencedirect.com/science/article/pii/S0924271624002612">Paper</a> |
   <a href="https://github.com/ualsg/global-streetscapes">Code</a> |
   <a href="https://huggingface.co/datasets/NUS-UAL/global-streetscapes">Dataset</a>
</center>

**Summary**

[Street-level imagery](https://ual.sg/publication/2021-land-svi-review/) is a popular data source in urban informatics, GIScience, urban studies, and computer vision, but datasets usually come without much context and metadata.
We devised a set of hundreds of attributes that indicate a variety of characteristics of photos (e.g. type of road and weather) and may be useful for downstream analyses.
Then, we labelled manually a number of images according to them and developed models and a workflow to do so automatically.
We obtained millions of crowdsourced images from Mapillary and KartaView from hundreds of geographically balanced cities from around the world, and enriched them with these attributes and provided the enhanced dataset for everyone to use for any purpose.
Further, we pre-computed myriads of those that researchers commonly use, such as green view index, to save time and lower the technical barriers.
The code is also shared to enable extensions and updates to the dataset.
Enjoy!

The project was carried out by the [Urban Analytics Lab (UAL)](https://ual.sg/) at the [National University of Singapore](https://nus.edu.sg/).

While both the [paper](https://www.sciencedirect.com/science/article/pii/S0924271624002612) and [repository](https://github.com/ualsg/global-streetscapes) are rich in details, on [this website](https://ual.sg/project/global-streetscapes/) you can find a description of what we do in a nutshell.
For more information, please refer to the [paper](https://www.sciencedirect.com/science/article/pii/S0924271624002612).

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
