from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.category_list,name='category_list'),
    path('categories/add/',views.category_create,name='category_create'),
    path("categories/edit/<int:pk>/", views.category_edit, name='category_edit'),
    path("categories/delete/<int:pk>/",views.category_delete,name='category_delete'),
    path("products/",views.product_list,name='product_list'),
    path("products/add/",views.product_add,name='product_add'),
    path("products/delete/<int:pk>/",views.product_delete,name='product_delete'),
    path("products/edit/<int:pk>/",views.product_edit,name='product_edit')


]
