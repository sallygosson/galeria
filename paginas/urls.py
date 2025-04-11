from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'), 
    path('contato/', views.contato, name='contato'),
]
