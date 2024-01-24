from django.urls import path

from . import views


#use this urlpatterns for mapping the multiple urls
urlpatterns = [
    path('', views.home, name ='home'),
    path('add', views.add, name ='add')

]