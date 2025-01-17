from django.contrib import admin
from django.urls import path, include
from connections import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('connection', views.connection, name='connection'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='userlogout'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load_division/', views.load_division, name='ajax_load_division'), # AJAX
    path('ajax/load_subdivision/', views.load_subdivision, name='ajax_load_subdivision'),
]
