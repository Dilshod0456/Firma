from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import DriverModelForm, NewUserForm, FikirModelForm
from yonalish.mixins import OrganiserAndLoginRequiredMixin

class SigupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm
    
    def get_success_url(self):
        return reverse("driver:Home")

class HomeView(ListView):
    template_name = "Post/home.html"
    queryset = models.Post.objects.all()
    context_object_name = 'post'

class HomePostView(DetailView):
    template_name = "Post/single.html"
    queryset = models.Post.objects.all()
    context_object_name = 'post'
    
class PicView(DetailView):
    template_name = "Post/pic.html"
    queryset = models.Post.objects.all()
    context_object_name = 'post'

class ListsView(LoginRequiredMixin,ListView):
    template_name = "driver/foydalanuvchilar.html"
    context_object_name = 'drivers'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = models.Driver.objects.filter( organisation = user.userprofile)
        else:
            queryset = models.Driver.objects.filter( organisation = user.yonalish.organisation)
            queryset = queryset.filter(Yonalish__user  = self.request.user)
        if user.is_editor:
            queryset = models.Driver.objects.all()     
        return queryset
        
    

class DriverDetailView(OrganiserAndLoginRequiredMixin,DetailView):
    template_name = "driver/details.html"
    queryset = models.Driver.objects.all()
    context_object_name = 'driver'

class DriverCreatView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = 'driver/creat.html'
    form_class = DriverModelForm
    
    def get_success_url(self):
        return reverse('driver:Ro\'yxat')

class DriverDeleteView(OrganiserAndLoginRequiredMixin,DeleteView):
    template_name = 'driver/delete.html'
    form_class = DriverModelForm
    queryset = models.Driver.objects.all()
    
    def get_success_url(self):
        return reverse('driver:Ro\'yxat')

class DriverUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'driver/update.html'
    form_class = DriverModelForm
    queryset = models.Driver.objects.all()
    
    def get_success_url(self):
        return reverse('driver:Ro\'yxat')

class FikirView(ListView):
    template_name = "Fikirlar/fikirlar.html"
    queryset = models.Fikr.objects.all()
    context_object_name = 'fikirs'

class FikirDetailView(DetailView):
    template_name = "Fikirlar/detailsf.html"
    queryset = models.Fikr.objects.all()
    context_object_name = 'fikir'

class FikirCreatView(CreateView):
    template_name = 'Fikirlar/creatf.html'
    form_class = FikirModelForm
    
    def get_success_url(self):
        return reverse('driver:Fikirlar')
    
class AboutView(TemplateView):
    template_name = "Post/about.html"
    
class LabaratoriyaView(TemplateView):
    template_name = "Post/tajriba.html"