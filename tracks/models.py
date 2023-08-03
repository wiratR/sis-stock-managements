import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
# Create your models here.


class EquipmentName(models.Model):
    equipmentName = models.CharField(_('Equipment Name'), max_length=125, null=True)

    def __str__(self):
        return self.equipmentName
    
    
class FailureCode(models.Model):
    
    equipmentName       = models.ForeignKey(EquipmentName, on_delete=models.CASCADE)
    failureShortName    = models.CharField(_('Failure Short Name'), max_length=125, null=True)
    failureCode         = models.CharField(_('Failure Code'), max_length=125, null=True)

    def __str__(self):
        return self.failureCode
    
class ActionCode(models.Model):
    
    equipmentName       = models.ForeignKey(EquipmentName, on_delete=models.CASCADE)
    actionShortName     = models.CharField(_('Action Short Name'), max_length=125, null=True)
    actionCode          = models.CharField(_('Action Code'), max_length=125, null=True)

    def __str__(self):
        return self.actionCode


class CauseCode(models.Model):
    
    equipmentName       = models.ForeignKey(EquipmentName, on_delete=models.CASCADE)
    causeShortName      = models.CharField(_('Cause Short Name'), max_length=125, null=True)
    causeCode           = models.CharField(_('Cause Code'), max_length=125, null=True)

    def __str__(self):
        return self.causeCode

    
class Track(models.Model):
    workOrder = models.CharField(_('Work Order'), max_length=125, null=True)
    equipmentName = models.ForeignKey(EquipmentName, on_delete=models.SET_NULL, null=True)
    serialNumber  = models.CharField(_('Serial Number'), max_length=125, null=True)
    failureCode   = models.ForeignKey(FailureCode, on_delete=models.SET_NULL, null=True)
    actionCode    = models.ForeignKey(ActionCode, on_delete=models.SET_NULL, null=True)
    causeCode     = models.ForeignKey(CauseCode, on_delete=models.SET_NULL, null=True)
    compleateDate = models.DateField(_('Compleate Date'), null=True)
    remark        = models.CharField(_('Remark'), max_length=125, null=True, blank=True)
    
    def __str__(self):
        return self.workOrder

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                if field.verbose_name != 'genre'
                else(field.verbose_name, Genre.objects.get(k=field.value_from_object(self)).equipmentName)
                for field in self.__class__._meta.fields[1:]]



