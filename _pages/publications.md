---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

[//]: # ({{author.googlescholar}} for some reason this value is not present here so if won't work, just hard code)
[//]: # ({% if author.googlescholar %})
[//]: #	(You can also find a more extensive list of my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.)
[//]: # ({% endif %})

You will find a more extensive and up-to-date list of my articles on <a href="https://scholar.google.com/citations?user=oH1tIr0AAAAJ&hl=en">my Google Scholar profile</a> which does not rely on me manually adding them.

## Selected Publications
<hr>
<font size="3">
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
</font>
