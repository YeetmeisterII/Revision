from django.shortcuts import render


def index(request):
    return render(request, f'physics/index.html')


def topic_page(request, topic, page):
    return render(request, f'physics/topics/{topic}/{page}.html')
