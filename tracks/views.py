from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Track, FailureCode, ActionCode, CauseCode
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .forms import TrackForm
from django.shortcuts import render

class TrackBaseView(View):
    model = Track
    # fields = ['workOrder', 'equipmentName',
    #           'serialNumber', 'failureCode', 'actionCode', 'causeCode', 'compleateDate', 'remark']
    fields = '__all__'
    success_url = reverse_lazy('tracks:all')
    
    
class TrackListView(TrackBaseView, ListView):
    """View to list all Tracks.
    Use the 'track_list' variable in the template
    to access all Track objects"""
    queryset = Track.objects.order_by('compleateDate')


class TrackDetailView(TrackBaseView, DetailView):
    """View to list the details from one Tracks.
    Use the 'track' variable in the template to access
    the specific Track here and in the Views below"""


    
class TrackCreateView(LoginRequiredMixin, TrackBaseView, CreateView):
    """View to create a new track"""  
    
    def get_form(self):
        '''add date picker in forms'''
        form = super(TrackCreateView, self).get_form()
        form.fields['compleateDate'].widget = DatePickerInput(options={"format": "DD-MM-YYYY"})
        return form

      
class TrackUpdateView(LoginRequiredMixin, TrackBaseView, UpdateView):
    """View to update a track"""
    
    def get_form(self):
        '''add date picker in forms'''
        form = super(TrackUpdateView, self).get_form()
        form.fields['compleateDate'].widget = DatePickerInput(options={"format": "DD-MM-YYYY"})
        return form


class TrackDeleteView(LoginRequiredMixin, TrackBaseView, DeleteView):
    """View to delete a Track"""


def load_failure_code(request):
    equipmentName_id = request.GET.get('equipmentName')
    failureCodes = FailureCode.objects.filter(equipmentName_id=equipmentName_id).order_by('failureCode')
    return render(request, 'tracks/failure_code_list_options.html', {'failureCodes': failureCodes})


def load_action_code(request):
    equipmentName_id = request.GET.get('equipmentName')
    actionCodes = ActionCode.objects.filter(equipmentName_id=equipmentName_id).order_by('actionCode')
    return render(request, 'tracks/action_code_list_options.html', {'actionCodes': actionCodes})

def load_cause_code(request):
    equipmentName_id = request.GET.get('equipmentName')
    causeCodes = CauseCode.objects.filter(equipmentName_id=equipmentName_id).order_by('causeCode')
    return render(request, 'tracks/cause_code_list_options.html', {'causeCodes': causeCodes})

