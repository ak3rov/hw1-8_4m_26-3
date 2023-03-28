from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def car_list_view(request):
    car_object = models.CarShop.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})

def car_detail_view(request, id):
    car_detail = get_object_or_404(models.CarShop, id=id)
    return render(request, 'car_detail.html', {'car_detail': car_detail})

def create_car_view(request):
    method = request.method
    if method == "POST":
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Добавлено в БД")
    else:
        form = forms.CarForm()
    return render(request, "create_car.html", {'form': form})


def delete_car_view(request, id):
    car_object = get_object_or_404(models.CarShop, id=id)
    car_object.delete()
    return HttpResponse('Телефон удален из БД')


def update_car_view(request, id):
    car_object = get_object_or_404(models.CarShop, id=id)
    if request.method == 'POST':
        form = forms.CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные обновлены')
    else:
        form = forms.CarForm(instance=car_object)

    context = {
        'form': form,
        'object': car_object
    }
    return render(request, 'update_car.html', context)


def reviews_car_view(request, id):
    car_object = get_object_or_404(models.CarShop, id=id)
    if request.method == 'POST':
        form = forms.ReviewsForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Отзыв отправлен')
    else:
        form = forms.ReviewsForm(instance=car_object)

    context = {
        'form': form,
        'object': car_object
    }
    return render(request, 'car_reviews.html', context)