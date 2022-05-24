from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

from .models import Page, Photo, Blurb, BlurbPhoto

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

BUCKET = 'catbucket1231'
S3_BASE_URL = 'https://s3.us-west-2.amazonaws.com/'


# Define the home view
def home(request):
  blurbs = Blurb.objects.filter(page__name="Home")
  return render(request, 'home.html', {'blurbs': blurbs, })

def resume(request):
  blurbs = Blurb.objects.filter(page__name="Resume")
  return render(request, 'resume/index.html', {'blurbs': blurbs, })

def projects(request):
  print(BUCKET)
  blurbs = Blurb.objects.filter(page__name="Projects")
  print(blurbs, "<------ blurbs")
  return render(request, 'projects/index.html', {'blurbs': blurbs, })

def coding(request):
  blurbs = Blurb.objects.filter(page__name="coding")
  return render(request, 'coding/index.html', {'blurbs': blurbs, })

def personal(request):
  blurbs = Blurb.objects.filter(page__name="Personal")
  return render(request, 'personal/index.html', {'blurbs': blurbs, })

def add_photo(request, page_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, page_id=page_id)
    except:
      print('Error uploading to S3.  Go to Views!!!')
  return redirect('home')