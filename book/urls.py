from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_word_view, name='hello'),
    path('posts/', views.post_view, name='posts'),
]