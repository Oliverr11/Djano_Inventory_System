from django.shortcuts import render,redirect
from .models import Supplier
from .forms import SupplierCreateForm,SupplierEditForm
# Create your views here.
def supplier_lsit(request):
    suppliers = Supplier.objects.all()
    return render(request,('suppliers/supplier_list.html'),{'suppliers':suppliers})

def supplier_create(request):
    form = SupplierCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request,'suppliers/supplier_add.html',{'form':form})

def supplier_edit(request,pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    form = SupplierEditForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request,'suppliers/supplier_edit.html',{'form':form})

def supplier_delete(request,pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    if request.method == "POST":
        supplier.delete()
        return redirect('supplier_list')
    return render(request,'suppliers/supplier_delete.html',{"supplier":supplier})