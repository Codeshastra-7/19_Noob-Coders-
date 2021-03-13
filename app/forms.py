from django import forms 
from app.models import *

class WareForm(forms.ModelForm):

    class Meta:
        model = WareHouse
        fields = ['instockkgs', 'outfordeliverykgs', 'monthlyrevenue']


class ItemsUpdate(forms.ModelForm):
    class Meta:
        model = TransportItems
        fields = ['quantity', 'description', 'location','dispatchtime']