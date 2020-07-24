from django.shortcuts import render


def index(request):
    return render(request, f"business/index.html")


def glossary(request):
    return render(request, "business/glossary.html")


def topic_page(request, topic, page):
    return render(request, f"business/topics/{topic}/{page}.html")
