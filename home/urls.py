from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallary/', views.gallary, name='gallery'),
    path('register/', views.register, name='register'),
    path('courses/', views.courses, name='courses'),
    path('activity/', views.act, name='activity'),
]
