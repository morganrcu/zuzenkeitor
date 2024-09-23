from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('students/',views.students),
    path('exercises/',views.exercices),
]