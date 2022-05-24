from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('resume/', views.resume, name='resume'),
  path('projects/', views.projects, name='projects'),
  path('coding/', views.coding, name='coding'),
  path('personal/', views.personal, name='personal'),
]