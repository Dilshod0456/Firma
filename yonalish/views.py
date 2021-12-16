from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from driver.models import Yonalish
from .forms import YonalishModelForms

class YonalishListView(LoginRequiredMixin, generic.ListView):
    template_name = 'yonalish/list.html'
    
    def get_queryset(self):
        return Yonalish.objects.all()
    
    
class YonalishCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'yonalish/creat.html'
    form_class = YonalishModelForms
    
    def get_success_url(self):
        return reverse('yonalish:yonalish-list')
    
    def form_valid(self, form):
        yonalish = form.save(commit=False)
        yonalish.profile = self.request.user.userprofile
        yonalish.save()
        return super(YonalishCreateView, self).form_valid(form)


class YonalishDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "yonalish/yonalish_detail.html"
    context_object_name = "yonalish"

    def get_queryset(self):
        return Yonalish.objects.all()

class YonalishUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "yonalish/yonalish_update.html"
    form_class = YonalishModelForms

    def get_queryset(self):
        return Yonalish.objects.all()

    def get_success_url(self):
        return reverse("yonalish:yonalish-list")

class YonalishDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "yonalish/yonalish_delete.html"
    context_object_name = "yonalish"

    def get_queryset(self):
        return Yonalish.objects.all()

    def get_success_url(self):
        return reverse("yonalish:yonalish-list")