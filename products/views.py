from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import ProductForm,CategoryForm
# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request,'categories/category_list.html',{'categories':categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request,'categories/category_add.html',{'form':form})
def category_edit(request,pk):
    categories = Category.objects.filter(pk=pk).first()
    form = CategoryForm(request.POST or None , instance=categories)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request,"categories/category_edit.html",{'form':form})
def category_delete(request,pk):
    categories = Category.objects.filter(pk=pk).first()
    if request.method =="POST":
        categories.delete()
        return redirect('category_list')
    return render(request,'categories/category_delete.html',{'categories':categories})


def product_list(request):
    products = Product.objects.all()
    return render(request,'products/product_list.html',{'products':products})

def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'products/product_add.html',{'form':form})
def product_edit(request,pk):
    products = Product.objects.filter(pk=pk).first()
    form = ProductForm(request.POST or None, instance=products)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,"products/product_edit.html",{'form':form})
def product_delete(request,pk):
    products = Product.objects.filter(pk=pk).first()
    if request.method =="POST":
        products.delete()
        return redirect('product_list')
    return render(request,'products/product_delete.html',{'products':products})