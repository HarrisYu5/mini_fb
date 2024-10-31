from typing import Any
import random
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, StatusMessage
from . import *
from . forms import *


# Create your views here.
class ShowAllProfiles(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

    def get_StatusMessage(self):
        return StatusMessage.objects.filter(profile=self.object)

class createProfileView(CreateView):
    model = Profile
    template_name = 'mini_fb/create_profile_form.html'
    fields = ['firstName', 'lastName', 'city', 'email', 'profile_image_url']
    success_url = '/mini_fb/'

class createStatusMessageView(CreateView):
    model = StatusMessage
    template_name = 'mini_fb/create_status_message_form.html'
    fields = ['message', 'profile']
    form_class= CreatestatusMessageForm
    success_url = '/mini_fb/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])

        return context
    
    def form_valid(self, form):
        print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        profile = Profile.objects.get(pk=self.kwargs['pk'])

        form.instance.profile = profile

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse("show_profile", kwargs={"pk": self.kwargs})