---
layout: page
permalink: /publications/
title: publications
description: Conferences and Journal papers.
---

<p>
Check my latest work at <a href="https://scholar.google.com/citations?user=Ott9sHkAAAAJ&hl=en">Google Scholar</a> and my <a href="https://github.com/matqr">GitHub page</a>.
</p>

{% assign last_year = nil %}
{% for pub in site.data.publications %}
  {% if pub.year != last_year %}
    <h3>{{ pub.year }}</h3>
    {% assign last_year = pub.year %}
  {% endif %}
  {% include publication_item.html pub=pub %}
{% endfor %}
