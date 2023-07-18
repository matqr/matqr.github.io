---
layout: page
permalink: /projects/
title: projects
description: Research projects and little creations of mine
---

<h3> Current </h3>
<div>
  {% for project in site.projects %}
    {% if project.status == "current" %}
    <ul>
      <li>
        <h4>
        <a href="{{ project.url | relative_url }}"> {{project.title}} </a>
        </h4>
        <h5> {{project.description}} </h5>
      </li>
    </ul>
    {% endif %}
  {% endfor %}
</div>

<h3> Past </h3>
<div>
  {% for project in site.projects %}
    {% if project.status == "past" %}
    <ul>
      <li>
        <h4>
        <a href="{{ project.url | relative_url }}"> {{project.title}} </a>
        </h4>
        <h5> {{project.description}} </h5>
      </li>
    </ul>
    {% endif %}
  {% endfor %}
</div>
