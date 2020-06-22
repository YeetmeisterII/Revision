from django.shortcuts import render


def index(request):
    return render(request, f'computer_science/index.html')


def topic_page(request, topic, page):
    return render(request, f'computer_science/topics/{topic}/{page}.html')


def glossary(request):
    return render(request, 'computer_science/glossary.html')
