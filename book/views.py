from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_word_view(request):
    return HttpResponse("<h1>my firs hw on 4th month!</h1>")


def post_view(request):
    post = models.Post.objects.all()
    return render(request, 'index.html', {'post_obj': post})
