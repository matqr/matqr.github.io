---
layout: page
permalink: /projects/
title: projects
description: Research projects and little creations of mine
---

<div>
  {% for project in site.projects %}
    <ul>
      <li>
        <h4> 
        <a href="{{ project.url | relative_url }}"> {{project.title}} </a>
        </h4>
        <h5> {{project.description}} </h5>
      </li>
    </ul>
  {% endfor %}
</div>
