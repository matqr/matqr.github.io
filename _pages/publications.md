---
layout: page
permalink: /publications/
title: publications
description: Conferences and Journal papers.
---

<p>
Check my latest work at <a href="https://scholar.google.com/citations?user=Ott9sHkAAAAJ&hl=en">Google Scholar</a> and my <a href="https://github.com/matqr">GitHub page</a>.
</p>

{% assign pubs = site.data.publications %}

{% assign filtered_pubs = pubs %}

{%- if page.filter_year -%}
  {% assign filtered_pubs = filtered_pubs | where: "year", page.filter_year %}
{%- endif -%}

{%- if page.filter_type -%}
  {% assign filtered_pubs = filtered_pubs | where: "type", page.filter_type %}
{%- endif -%}

{% assign grouped = filtered_pubs | group_by: "year" | sort: "name" | reverse %}

{% for year_group in grouped %}
    <h3>{{ year_group.name }}</h3>
    {% for pub in year_group.items %}
        {% include publication_item.html pub=pub %}
    {% endfor %}
{% endfor %}
