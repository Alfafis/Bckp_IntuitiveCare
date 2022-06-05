from django.db import models
from django import forms  
from record.models import Record  

# Create your models here.
class Report(models.Model):  
    ANS_Record = models.CharField(max_length=30, primary_key=True)  
    CNPJ = models.CharField(max_length=30)  
    Fantasy_Name = models.EmailField(250)  
    Modality = models.CharField(max_length=100)  
    Street = models.CharField(max_length=250)  
    Number = models.CharField(max_length=30)  
    Complement = models.CharField(max_length=100)  
    Neighborhood = models.CharField(max_length=100)  
    City = models.CharField(max_length=100)
    UF = models.CharField(max_length=100)  
    CEP = models.CharField(max_length=30)    
    DDD = models.CharField(max_length=30)  
    Phone = models.CharField(max_length=30)  
    Fax = models.CharField(max_length=30)  
    Email = models.CharField(max_length=100)  
    Representative = models.CharField(max_length=100)  
    Position_Representative = models.CharField(max_length=100)  
    ANS_Record_Date = models.CharField(max_length=30)  
    class Meta:  
        db_table = "report"

class RecordForm(forms.ModelForm):  
    class Meta:  
        model = Record  
        fields = "__all__"  