from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase_list, name='purchase_list'),
    path('create/', views.create_purchase, name='create_purchase'),
    path('<int:pk>/', views.purchase_detail, name='purchase_detail'),
]