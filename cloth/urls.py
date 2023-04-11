from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.ProductListView.as_view(), name='Clothes'),
    path('clothes/<int:id>', views.ProductDetailView.as_view(), name='ClothesDetail'),
    path('clothes1/', views.ProductTagFirstView.as_view(), name='tag1'),
    path('clothes2/', views.ProductTagSecondView.as_view(), name='tag2'),
    path('clothes3/', views.ProductTagThirdView.as_view(), name='tag3'),
    path('clothes4/', views.ProductTagFourthView.as_view(), name='tag4'),
    path('order/', views.OrderView.as_view(), name='ClothOrder'),
    path('order_status/', views.OrderStatusView.as_view(), name='OrderStatus'),
]