import random
from django.views import generic
from django.urls import reverse
from django.core.mail import send_mail
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
        user = form.save(commit=False)
        user.is_organisor = False
        user.is_agent = True
        user.set_password(f"{random.randint(0,1000)}")
        user.save()
        Yonalish.objects.create(
            user = user,
            organisation = self.request.user.userprofile
        )
        send_mail(
            subject="Bu Agent yaratilingan",
            message="Yangi Agent yaratilgan",
            from_email="susyswdg@gmal.Iom",
            recipient_list=[user.email],
        )
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