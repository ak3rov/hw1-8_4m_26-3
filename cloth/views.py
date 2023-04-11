from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views.generic import DetailView, ListView, CreateView


class ProductListView(ListView):
    template_name = 'clothes/clothes_list.html'
    queryset = models.ProductCL.objects.filter().order_by('-id')

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')


class ProductTagFirstView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="Юбки")
    template_name = "clothes/product_tag_one.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="Юбки")


class ProductTagSecondView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="Брюки")
    template_name = "clothes/clothes/product_tag_two.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="Брюки")


class ProductTagThirdView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="Шарф")
    template_name = "clothes/product_tag_three.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="Шарф")


class ProductTagFourthView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="Свитер")
    template_name = "clothes/product_tag_four.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="Свитер")


class ProductDetailView(DetailView):
    template_name = 'clothes/clothes_detail.html'

    def get_object(self, **kwargs):
        clothes_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductCL, id=clothes_id)


class OrderView(CreateView):
    template_name = "clothes/order.html"
    form_class = forms.ClothForm
    queryset = models.ProductCL.objects.all()
    success_url = '/'

    def get_object(self, **kwargs):
        review_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductCL, id=review_id)

    def form_valid(self, form):
        print(form.clean)
        return super(OrderView, self).form_valid(form=form)


class OrderStatusView(CreateView):
    template_name = "clothes/order_status.html"
    form_class = forms.ClothForm
    queryset = models.OrderCL.objects.all()
    success_url = '/clothes/catalog_list/'

    def get_object(self, **kwargs):
        review_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderCL, id=review_id)

    def form_valid(self, form):
        print(form.clean)
        return super(OrderStatusView, self).form_valid(form=form)