from functools import lru_cache

from django.urls import reverse


# Lazy evaluation
@lru_cache
def links():
    context = [
        ["Main", "pages:index"],
        ["Physics", "physics:index"],
        ["Maths", "maths:index"],
        ["Computer Science", "computer_science:index"],
        ["Business", "business:index"],
    ]
    return {"global_links": list(map(lambda data: get_name_and_link(*data), context))}


def get_global_app_links(request):
    return links()


def get_name_and_link(display_name: str, page_name: str):
    return {"name": display_name, "link": reverse(page_name)}
