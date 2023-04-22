import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
# Create your models here.


class Track(models.Model):
    workOrder = models.CharField(_('Work Order'), max_length=125, null=True)
    equipmentName = models.CharField(_('Equipment Name'), max_length=125, null=True)
    compleateDate = models.DateField(_('Compleate Date'), null=True)
    
    def __str__(self):
        return self.workOrder

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
                if field.verbose_name != 'genre'
                else
                (
                    field.verbose_name, Genre.objects.get(k=field.value_from_object(self)).equipmentName
                )
                for field in self.__class__._meta.fields[1:]
                ]
