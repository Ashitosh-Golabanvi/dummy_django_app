from django.contrib import admin
from django.urls import path
from home.views import TodoCRUDView

from home.views import TodoCRUDView, index

urlpatterns = [
    path('', index),  # frontend

    path('todos/', TodoCRUDView.as_view()),
    path('todos/<int:id>/', TodoCRUDView.as_view()),
]