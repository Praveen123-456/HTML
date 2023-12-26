from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employees

# Create your views here.
def index(request):
    return render(request,'index.html')
def data(request):
    data={
        'em_data':Employees.objects.all()
    }
    return render(request,'data.html',data)
def add(request):
    return render(request,'add.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        time=request.POST.get('time')
        salary=request.POST.get('salary')
        query=Employees(name=name,time=time,salary=salary)
        query.save()
    return redirect('/data')
def delete(request,id):
    del_data=Employees.objects.get(id=id)
    del_data.delete()
    return redirect('/data')
def update(request,id):
    upd_data={
        'upd':Employees.objects.get(id=id)
    }
    return render(request,'update.html',upd_data)
def edit(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        time=request.POST.get('time')
        salary=request.POST.get('salary')
        ed_data=Employees.objects.get(id=id)
        ed_data.name=name
        ed_data.time=time
        ed_data.salary=salary
        ed_data.save()
    return redirect('/data')
        