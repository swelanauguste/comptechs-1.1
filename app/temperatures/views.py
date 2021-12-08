from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q
from .forms import TemperatureCreateForm
from .models import Temperature


class TemperatureListView(LoginRequiredMixin, ListView):
    model = Temperature
    template_name = "temperatures/temperature_list.html"
    paginate_by = 25


class TemperatureCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Temperature
    form_class = TemperatureCreateForm
    success_message = "Created"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TemperatureDetailView(LoginRequiredMixin, DetailView):
    model = Temperature
    template_name = "temperatures/temperature_detail.html"
