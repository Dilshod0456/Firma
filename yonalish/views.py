from django.views import generic
from django.urls import reverse
from .mixins import OrganiserAndLoginRequiredMixin
from driver.models import Yonalish
from .forms import YonalishModelForms

class YonalishListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'yonalish/list.html'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Yonalish.objects.filter( organisation = organisation)

    
    
class YonalishCreateView(OrganiserAndLoginRequiredMixin,generic.CreateView):
    template_name = 'yonalish/creat.html'
    form_class = YonalishModelForms
    
    def get_success_url(self):
        return reverse('yonalish:yonalish-list')
    
    def form_valid(self, form):
        yonalish = form.save(commit=False)
        yonalish.profil = self.request.user.userprofile
        yonalish.save()
        return super(YonalishCreateView, self).form_valid(form)


class YonalishDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = "yonalish/yonalish_detail.html"
    context_object_name = "yonalish"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Yonalish.objects.filter( organisation = organisation)

class YonalishUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "yonalish/yonalish_update.html"
    form_class = YonalishModelForms

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Yonalish.objects.filter( organisation = organisation)

    def get_success_url(self):
        return reverse("yonalish:yonalish-list")

class YonalishDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = "yonalish/yonalish_delete.html"
    context_object_name = "yonalish"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Yonalish.objects.filter( organisation = organisation)

    def get_success_url(self):
        return reverse("yonalish:yonalish-list")