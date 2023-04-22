from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Track
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.mixins import LoginRequiredMixin

class TrackBaseView(View):
    model = Track
    fields = '__all__'
    success_url = reverse_lazy('tracks:all')
    
    
class TrackListView(TrackBaseView, ListView):
    """View to list all Tracks.
    Use the 'track_list' variable in the template
    to access all Track objects"""


class TrackDetailView(TrackBaseView, DetailView):
    """View to list the details from one Tracks.
    Use the 'track' variable in the template to access
    the specific Track here and in the Views below"""


class TrackCreateView(LoginRequiredMixin, TrackBaseView, CreateView):
    """View to create a new track"""
    # class attributes ...
    def get_form(self):
        form = super().get_form()
        form.fields["compleateDate"].widget = DatePickerInput()
        return form

    
class TrackUpdateView(LoginRequiredMixin, TrackBaseView, UpdateView):
    """View to update a track"""
    # class attributes ...

    def get_form(self):
        form = super().get_form()
        form.fields["compleateDate"].widget = DatePickerInput()
        return form


class TrackDeleteView(LoginRequiredMixin, TrackBaseView, DeleteView):
    """View to delete a Track"""
