from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #no le pongo parentesis a now porq no la quiero ejecutar ahora
    author = models.ForeignKey(User, on_delete=models.CASCADE)#si elimino un usuario, se eliminan los  posts tmb

    def __str__(self):

        return self.title

    def get_absolute_url (self):
        return reverse('post-detail', kwargs={'pk': self.pk})#reverse me devuelve el url como string

