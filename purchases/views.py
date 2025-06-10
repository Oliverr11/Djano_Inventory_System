from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase
from .forms import PurchaseForm, PurchaseDetailFormSet

def purchase_list(request):
    purchases = Purchase.objects.select_related('supplier', 'employee').all()
    return render(request, 'purchases/purchase_list.html', {'purchases': purchases})

def create_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            formset = PurchaseDetailFormSet(request.POST, instance=purchase)

            if formset.is_valid():
                purchase.save() 
                details = formset.save(commit=False)
                for item in details:
                    item.total_price = item.product.cost_price * item.quantity
                    item.save()
                formset.save_m2m()
                purchase.save() 
                return redirect('purchase_list')
        else:
            formset = PurchaseDetailFormSet(request.POST)
    else:
        form = PurchaseForm()
        formset = PurchaseDetailFormSet()

    return render(request, 'purchases/purchase_create.html', {'form': form,'formset': formset})

def purchase_detail(request, pk):
    purchase = Purchase.objects.get(pk=pk)
    return render(request, 'purchases/purchase_detail.html', {'purchase': purchase})
