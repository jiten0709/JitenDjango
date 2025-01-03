from django import forms
from .models import Menu

class MenuForm(forms.Form):
    menu_items = forms.ModelChoiceField(queryset=Menu.objects.all(), label="Select Menu Items")
    