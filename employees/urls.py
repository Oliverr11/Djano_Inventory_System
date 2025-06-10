from django.urls import path
from . import views


urlpatterns = [
    path('',views.employees_list,name="employees_list"),
    path('add/', views.employees_create, name='employees_create'),
    path('edit/<int:pk>/',views.employees_edit,name="employees_edit"),
    path('delete/<int:pk>/',views.employees_delete,name="employees_delete")
]
