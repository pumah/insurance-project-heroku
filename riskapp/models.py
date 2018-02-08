from django.db import models
from django_mysql.models import EnumField, Model

# Create your models here.

class risk_type(Model):
    risk_type = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.risk_type)

class risk_field(Model):
    field_name = models.CharField(max_length=255, blank=False)
    field_type = EnumField(choices=['DATE', 'ENUM', 'DECIMAL', 'TEXT'])
    field_metadata = models.CharField(max_length=255, default=None, blank=True, null=True)
    risk_type = models.ForeignKey('risk_type',related_name='rfields',on_delete=models.DO_NOTHING)
