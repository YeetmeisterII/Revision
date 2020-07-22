from django.urls import path

from . import views

app_name = 'business'
urlpatterns = [
    path('', views.index, name='index'),
    path('glossary/', views.glossary, name='glossary'),
    path('<str:topic>/<str:page>', views.topic_page, name='topic_page'),
]
