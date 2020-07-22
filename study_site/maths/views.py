from django.shortcuts import render


def index(request):
    return render(request, f"maths/index.html")


def topic_page(request, topic, page):
    return render(request, f"maths/topics/{topic}/{page}.html")
