from django.db.models import fields
from django.forms import ModelForm, TextInput
from .models import *
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','number','email','current_balance']

class TransitionForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['sender_name', 'amount', 'receiver_name']
