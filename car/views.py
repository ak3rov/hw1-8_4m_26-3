from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
#CRUD
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


class CarListView(ListView):
    template_name = 'car_list.html'
    queryset = models.Car.objects.all()

    def get_queryset(self):
        return models.Car.objects.all()


#full-view of id object
class CarDetailView(DetailView):
    template_name = 'car_full_list.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)

#creating objects from forms


class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = forms.CarForm
    queryset = models.Car.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.clean)
        return super(CreateCarView, self).form_valid(form=form)


#Удаление из базы
class CarDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)


class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    form_class = forms.CarForm
    success_url = '/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)

    def form_valid(self, form):
        print(form.clean)
        return super(CarUpdateView, self).form_valid(form=form)


class CarFeedback(CreateView):
    template_name = 'feedback.html'
    form_class = forms.FeedbackForm
    queryset = models.CarReview.objects.all()
    success_url = '/'

    def get_object(self, **kwargs):
        review_id = self.kwargs.get('id')
        return get_object_or_404(models.CarReview, id=review_id)

    def form_valid(self, form):
        print(form.clean)
        return super(CarFeedback, self).form_valid(form=form)


def catalog_view(request):
    return render(request, 'catalog.html')


#кнопка поиск
class Search(ListView):
    template_name = 'car_list.html'
    context_object_name = 'car'
    paginate_by = 5

    def get_queryset(self):
        return models.Car.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context