from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('car_list/<int:id>/', views.CarDetailView.as_view(), name='car_full'),
    path('car_list/<int:id>/delete/', views.CarDeleteView.as_view(), name='delete'),
    path('car_list/<int:id>/update/', views.CarUpdateView.as_view(), name='update'),
    path('create_car/', views.CreateCarView.as_view(), name='create'),
    path('car_list/<int:id>/feedback/', views.CarFeedback.as_view(), name='feedback'),
    path('catalog_list/', views.catalog_view, name='catalog'),

]