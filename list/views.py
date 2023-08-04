from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import EmployeeModel
# Create your views here.


def employeeFormView(request):  
    if request.method=='POST':
         form = EmployeeForm(request.POST)
         if form.is_valid():
            form.save()
            print(form.cleaned_data) 
            return redirect('datashow')
    else:
        form = EmployeeForm()  
    return render(request,'filldata.html',{'form':form})


def employeeshowdata(request):
    form = EmployeeModel.objects.all()
    return render(request,'showdata.html',{'form':form})


def employeeDataUpdate(request,id):
    data = EmployeeModel.objects.get(pk=id)
    # form = EmployeeForm(instance=data)
    if request.method=='POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('datashow')
    
    else:
        form = EmployeeForm(instance=data)
    return render(request,'filldata.html',{'form':form})


def employeeDataDel(request,id):
    data = EmployeeModel.objects.get(pk=id).delete()
    return redirect('datashow')