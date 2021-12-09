from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def  __str__(self):
        return str(self.user.username)

class Post(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    image = models.ImageField(upload_to='images/',default='images/default.png')

    def  __str__(self):
        return self.title

class Fikr(models.Model):
    kim_tomonidan = models.CharField(max_length=50)
    discription = models.TextField()

    def  __str__(self):
        return self.kim_tomonidan

class Driver(models.Model):
    Ismi = models.CharField(max_length=20)
    Familyasi = models.CharField(max_length=20)
    Yoshi = models.IntegerField(default=0)
    Staji = models.IntegerField(default=0)
    Yonalish = models.ForeignKey("Yonalish", on_delete=models.CASCADE)

    def  __str__(self):        
        return str(self.Ismi)

class Yonalish(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def  __str__(self):
        return str(self.user)
    
def post_user_yaratish(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(post_user_yaratish, sender=User)