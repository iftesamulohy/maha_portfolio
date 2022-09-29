from django.urls import path
from . import views

urlpatterns = [
path("", views.Portfolio.as_view())
]