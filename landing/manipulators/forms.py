from django import forms
from .models import RequestManipulator


class RequestManipulatorForm(forms.ModelForm):
    class Meta:
        model = RequestManipulator
        fields = ["name", "email", "phone_number", "message"]
