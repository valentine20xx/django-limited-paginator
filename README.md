# django-limited-paginator

1. Add Paginator to your view

```Python
class SomeList(ListView):
    ...
    paginator_class = LimitedPaginator
    ...
```

2. Configure your template:

```
<ul class="pagination">
    <li {% if not page_obj.has_first %}class="disabled"{% endif %}>
        <a {% if page_obj.has_first %}href="?page=1"{% endif %} aria-label="First">
                 <span class="glyphicon glyphicon-fast-backward"
                       aria-hidden="true"></span>
        </a>
    </li>
    <li {% if not page_obj.has_previous %}class="disabled"{% endif %}>
        <a {% if page_obj.has_previous %}href="?page={{ page_obj.previous_page_number }}"{% endif %}
           aria-label="Previous">
                          <span class="glyphicon glyphicon-chevron-left"
                                aria-hidden="true"></span>
        </a>
    </li>
    {% for x in page_obj.main_range %}
        <li {% if x == page_obj.number %}class="active"{% endif %}><a
                {% if not x == page_obj.number %}href="?page={{ x }}"{% endif %}>
            {{ x }}{% if x == page_obj.number %}<span class="sr-only">(current)</span>{% endif %}</a>
        </li>
    {% endfor %}
    <li {% if not page_obj.has_next %}class="disabled"{% endif %}>
        <a {% if page_obj.has_next %}href="?page={{ page_obj.next_page_number }}"{% endif %}
           aria-label="Next">
                 <span class="glyphicon glyphicon-chevron-right"
                       aria-hidden="true"></span>
        </a>
    </li>
    <li {% if not page_obj.has_last %}class="disabled"{% endif %}>
        <a {% if page_obj.has_last %}href="?page=last"{% endif %} aria-label="Last">
                 <span class="glyphicon glyphicon-fast-forward"
                       aria-hidden="true"></span>
        </a>
    </li>
</ul>
```
