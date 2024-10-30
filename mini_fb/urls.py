from django.urls import path
from . import views 
from .views import ShowAllProfiles

urlpatterns = [
    path('', ShowAllProfiles.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', views.ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile_form', views.createProfileView.as_view(), name='create_profile_form'),
]