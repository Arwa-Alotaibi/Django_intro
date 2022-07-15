from django.urls import path     
from . import views
urlpatterns = [
    path('', views.number_visit),
    path('destroy_session/', views.destroy),
    path('add_counter/',views.add_counter)		   
]