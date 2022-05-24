from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Page Name: {self.name} ID: {self.id}"
    

class Photo(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    url = models.CharField(max_length=250)

    def __str__(self):
        return f"Page: {self.page.name} URL: {self.url}"


class Blurb(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    blurbHeader = models.CharField(max_length=100)
    blurb= models.CharField(max_length=500)

    def __str__(self):
        return f"Page: {self.page.name} Blurb: {self.blurbHeader}"

class BlurbPhoto(models.Model):
    blurb = models.ForeignKey(Blurb, on_delete=models.CASCADE)
    url = models.CharField(max_length=250)


