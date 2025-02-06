from django.urls import path
from . import views  # Import the home view

urlpatterns = [
    path('', views.lead, name='lead'),  # Home page route
]
