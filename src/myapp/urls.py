from django.urls import path
from . import views

urlpatterns= [
    path("", views.home, name="home"), ## redirected from project urls.py
    path("todos/", views.todos, name="Todos") ## redirected from project urls.py

]
#