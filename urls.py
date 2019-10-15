from django.urls import path

from . import views

app_name = 'virtual_lawyer'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

]