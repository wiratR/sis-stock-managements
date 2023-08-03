from django.contrib import admin
from .models import Track
from .models import EquipmentName
from .models import FailureCode
from .models import ActionCode
from .models import CauseCode
# Register your models here.

class EquipmentFailureCode(admin.ModelAdmin):
    list_display = ("equipmentName", "failureShortName", "failureCode",)
class EquipmentActionCode(admin.ModelAdmin):
    list_display = ("equipmentName", "actionShortName", "actionCode",)
class EquipmentCauseCode(admin.ModelAdmin):
    list_display = ("equipmentName", "causeShortName", "causeCode",)


admin.site.register(Track)
admin.site.register(EquipmentName)
admin.site.register(FailureCode, EquipmentFailureCode)
admin.site.register(ActionCode, EquipmentActionCode)
admin.site.register(CauseCode, EquipmentCauseCode)
