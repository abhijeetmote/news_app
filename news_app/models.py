from django.db import models
from django.contrib.auth.models import User 
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q
# Create your models here.

class Post_news(models.Model):
    
    options = (
                ('0','Low'),
                ('1','Medium'),
                ('2','High')
           )
    
    # add new field, with hint
    message = models.CharField(max_length = 500, help_text='Message description')        
    
    # Adds new field and drop down list
    severity = models.CharField(max_length = 2, choices = options, default ='Low')
    
    # Adds new field,Automatic creation date and time 
    creation_date = models.DateTimeField(auto_now_add = True)
    
    # Adds new field,Automatic creation date and time
    updation_date = models.DateTimeField(auto_now = True)
    
    # created by user
    created_by = models.CharField(max_length = 24)
    
    
    # Creates many to many field     
    clients = models.ManyToManyField(User, blank = True,limit_choices_to= Q(groups__id=1))
    
    
