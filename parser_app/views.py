from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import models, forms, parser


class ParserFilmView(ListView):
    model = models.CinemaKg
    template_name = 'film_list.html'

    def get_queryset(self):
        return models.CinemaKg.objects.all()


class ParserFormView(FormView):
    template_name = 'start_parsing.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<center> <h1>Данные взяты......</h1> \
             <button> <a href="/film_list/">На список фильмов</a> </button> </center>')
        else:
            return super(ParserFormView).post(request, *args, **kwargs)


class Search(ListView):
    template_name = 'film_list.html'
    context_object_name = 'film'
    paginate_by = 5

    def get_queryset(self):
        return models.CinemaKg.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context