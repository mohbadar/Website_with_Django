from django import forms

from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'contact', 'message')
        model = models.Contact 