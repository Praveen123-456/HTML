from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index),
    path('data',views.data),
    path('add',views.add),
    path('insert',views.insert),
    path('delete/<id>',views.delete),
    path('update/<id>',views.update),
    path('edit/<id>',views.edit),
]
