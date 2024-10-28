from django import forms
from django.core.exceptions import ValidationError

import re


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    background = forms.Textarea()
    is_working = forms.BooleanField()


    def clean_name(self):
        name = self.cleaned_data.get("name")

        if not is_valid(name):
            raise ValidationError("Name is invalid.")

        return name


    def clean_surname(self):
        surname = self.cleaned_data.get("surname")

        if not is_valid(surname):
            raise ValidationError("Surname is invalid.")

        return surname






























# Validate name
def is_valid(name):
    cleaned_name = re.sub(r"[ -]", name)

    if not str(cleaned_name).isalpha():
        return False
    
    if str(name) != str(name).strip():
        return False
    
    return True