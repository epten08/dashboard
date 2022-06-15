from socket import fromshare
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from .models import Sale

class Orders(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'