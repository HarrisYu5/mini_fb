from django.urls import path
from . import views 
from .views import ShowAllProfiles

urlpatterns = [
    path('', ShowAllProfiles.as_view(), name='show_all_profiles'),
]