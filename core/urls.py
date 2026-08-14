from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),

    # comments + likes
    path('projects/<slug:slug>/comment/', views.add_project_comment, name='add_project_comment'),
    path('projects/<slug:slug>/like/', views.like_project, name='like_project'),

    path('contact/', views.contact, name='contact'),
]