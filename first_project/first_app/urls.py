from django.urls import path
from . import views

urlpatterns = [
    path('first_app/', views.first_app, name='first_app'),
    path('second_view/', views.second_view, name = 'second_view'),
    path('first_app/details/<int:id>', views.details, name='details'),
    path('', views.main_page, name='main_page'),
    path('testing/', views.testing, name='testing')
]