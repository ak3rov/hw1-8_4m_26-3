from django.shortcuts import render
from . import models

def post_view(request):
    post = models.Post.objects.all()
    return render(request, 'index.html', {'post_obj': post})
