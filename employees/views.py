from django.shortcuts import render,redirect
from .models import Employee 
from .forms import EmployeeCreateForm
# Create your views here.
def employees_list(request):
    employees = Employee.objects.all()
   
    return render(request, 'employees/employees_list.html', {'employees':employees})
def employees_create(request):
    form = EmployeeCreateForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('employees_list')
    return render(request, 'employees/employees_create.html',{'form':form})

def employees_edit(request,pk):
    employee = Employee.objects.filter(pk=pk).first()
    form = EmployeeCreateForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employees_list')
    return render(request, 'employees/employees_edit.html', {'form': form})
def employees_delete(request,pk):
    employee = Employee.objects.filter(pk=pk).first()
    if request.method == "POST":
        employee.delete()
        return redirect('employees_list')
    return render(request,"employees/employees_delete.html",{"employees":employee})