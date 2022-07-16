from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('porcess_money',views.porcess_money)	

]
