"""
URL configuration for inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from customers import urls as customers_urls
from suppliers import urls as suppliers_urls
from products import urls as products_urls
from employees import urls as employees_urls
from sales import urls as sales_urls
from purchases import urls as purchases_urls
from dashboard import urls as dashboard_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(customers_urls)),
    path('customers/',include(customers_urls)),
    path('suppliers/',include(suppliers_urls)),
    path('employees/',include(employees_urls)),
    path('',include(products_urls)),
    path('sales/', include(sales_urls)),
    path('purchases/',include(purchases_urls)),
    path('dashboard/',include(dashboard_urls))
]
