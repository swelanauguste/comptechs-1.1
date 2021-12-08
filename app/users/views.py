from django.shortcuts import render
from django.views.generic import UpdateView, DetailView

from .models import Profile
from .forms import ProfileUpdateForm


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name_suffix = '_update_form'
