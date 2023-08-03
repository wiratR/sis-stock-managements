from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Track, EquipmentName, FailureCode, ActionCode, CauseCode
from bootstrap_datepicker_plus.widgets import DatePickerInput

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['workOrder', 'equipmentName',
                'serialNumber', 'failureCode', 'actionCode', 'causeCode', 'compleateDate', 'remark']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))
        self.fields["equipmentName"].queryset   = EquipmentName.objects.none()
        self.fields["failureCode"].queryset     = FailureCode.objects.none()
        self.fields["actionCode"].queryset      = ActionCode.objects.none()
        self.fields["causeCode"].queryset       = CauseCode.objects.none()
        
        self.fields["compleateDate"].widget     = DatePickerInput(options={"format": "DD-MM-YYYY"})
        