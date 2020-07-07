from django.urls import path

from . import views

app_name = "physics"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:topic>/<str:page>", views.topic_page, name="topic_page"),
]
