from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from .forms import *
from .formsf import *

def home(request):
    post = models.Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'home.html', context)

def lists(request):
    driver = Driver.objects.all()
    context = {
        "drivers" : driver
    }
    return render(request,"foydalanuvchilar.html", context)

def fikirlar(request):
    fikir = models.Fikr.objects.all()
    context = {
        "fikirs" : fikir
    }
    return render(request,"fikIrlar.html", context)

def about(request):
    return render(request, "about.html")

def creat(request):
    form = DriverModelForm()
    if request.method == "POST":
        form = DriverModelForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('/lists')
             
    context= {
        'forms': DriverModelForm
    }
    return render(request, "creat.html", context)

def creatf(request):
    form = FikrForm
    if request.method == "POST":
        form = FikrForm(request.POST)  
        if form.is_valid():
            kim_tomonidan = form.cleaned_data['kim_tomonidan']
            discription = form.cleaned_data['discription']
            models.Fikr.objects.create(
                kim_tomonidan = kim_tomonidan,
                discription = discription,
            )
            return redirect('/fikirlar')
             
    context= {
        'forms': FikrForm
    }
    return render(request, "creatf.html", context)

def  driver_detail(request, pk):
    driver = get_object_or_404(Driver, id=pk)
    context = {
        "driver" : driver
    }
    return render(request, 'details.html', context)

def  fikir_detail(request, pk):
    fikir = get_object_or_404(models.Fikr, id=pk)
    context = {
        "fikir" : fikir
    }
    return render(request, 'detailsf.html', context)

def  single(request, pk):
    post = get_object_or_404(models.Post, id=pk)
    context = {
        "post" : post
    }
    return render(request, 'single.html' ,context)

def  pic(request, pk):
    post = get_object_or_404(models.Post, id=pk)
    context = {
        "post" : post
    }
    return render(request, 'pic.html' ,context)

def tajriba(request):
    return render(request, 'tajriba.html')

def driver_update(request, pk):
    driver = Driver.objects.get(id = pk)
    form = DriverModelForm(instance=driver)
    if request.method == "POST":
        form = DriverModelForm(request.POST, instance=driver)  
        if form.is_valid():
            form.save()
            return redirect('/lists')
             
    context={
        'form':form,
        'driver':driver
    }
    return render(request, 'update.html', context)

def deleted(request, pk):
    driver = Driver.objects.get(id = pk)
    driver.delete()
    return redirect('/lists')