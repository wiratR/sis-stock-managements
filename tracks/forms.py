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

        self.fields["failureCode"].queryset     = FailureCode.objects.none()
        self.fields["actionCode"].queryset      = ActionCode.objects.none()
        self.fields["causeCode"].queryset       = CauseCode.objects.none()
        self.fields["compleateDate"].widget     = DatePickerInput(options={"format": "DD-MM-YYYY"})
        
        # Dropdown list for Failure Code , Action Code , Cause Code
        if 'equipmentName' in self.data:
            try:
                equipmentName_id = int(self.data.get('equipmentName'))
                self.fields['failureCode'].queryset = FailureCode.objects.filter(equipmentName_id=equipmentName_id).order_by('failureCode')
                self.fields['actionCode'].queryset  = ActionCode.objects.filter(equipmentName_id=equipmentName_id).order_by('actionCode')
                self.fields['causeCode'].queryset   = CauseCode.objects.filter(equipmentName_id=equipmentName_id).order_by('causeCode')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty FailureCode queryset
        elif self.instance.pk:
            self.fields['failureCode'].queryset     = self.instance.EquipmentName.FailureCode.order_by('failureCode')
            self.fields['actionCode'].queryset      = self.instance.EquipmentName.ActionCode.order_by('actionCode')
            self.fields['causeCode'].queryset       = self.instance.EquipmentName.CauseCode.order_by('causeCode')
            
   