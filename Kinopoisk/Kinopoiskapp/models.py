from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    video = models.FileField()
    name = models.CharField(max_length=30)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    


    def __str__(self):
        return self.name    
    



class Movie_search(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    video = models.FileField()
    name = models.CharField(max_length=30)
    desc = models.TextField()
    age_category = models.CharField(max_length=20, choices=[
        ('kids', 'Kids'),
        ('teen', 'Teen'),
        ('adult', 'Adult')
    ])

    def __str__(self):
        return self.title

class Profile(models.Model):
    username = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    email = models.ImageField(upload_to="profile_pciture", null=True, default="default.jpg")
    password1 = models.CharField(max_length=200, null=True, blank=True)
    password2 = models.CharField(max_length=200, null=True, blank=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def str(self):
        return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        



def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
class Result(models.Model):
    video = EmbedVideoField()
    name = models.CharField(max_length = 100)
    desc = models.TextField()

    def __str__(self):
        return self.name
