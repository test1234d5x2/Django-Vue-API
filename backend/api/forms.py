from django import forms
from django.core.exceptions import ValidationError
import re

from .models import Employee, Project, Assignment


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    background = forms.CharField(widget=forms.Textarea())
    is_working = forms.BooleanField()



    class Meta:
        model = Employee
        fields = "__all__"


    def clean_name(self):
        name = self.cleaned_data.get("name")

        if not valid_name(name):
            raise ValidationError("Name is invalid.")

        return name


    def clean_surname(self):
        surname = self.cleaned_data.get("surname")

        if not valid_name(surname):
            raise ValidationError("Surname is invalid.")

        return surname
    

    def clean_background(self):
        background = self.cleaned_data.get("background")

        if len(str(background).strip()) == 0:
            raise ValidationError("Background is not valid.")
        
        return background



    def clean_is_working(self):
        is_working = self.cleaned_data.get("is_working")

        if not (type(is_working) == bool):
            raise ValidationError("Is Working is not valid.")

        return is_working







class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.Textarea()
    start_date = forms.DateField()

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date')

    def clean_name(self):
        name = self.cleaned_data.get("name")
        
        if not name or len(str(name).strip()) == 0:
            raise ValidationError("Name is not valid.")
        
        return name
    
    def clean_description(self):
        description = self.cleaned_data.get("description")

        if not description or len(description.strip()) == 0:
            raise ValidationError("Description is not valid.")
        
        return description
    
    def clean_start_date(self):
        start_date = self.cleaned_data.get("start_date")

        if start_date is None:
            raise ValidationError("Start date is not valid.")
        
        return start_date





class AssignmentForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    role = forms.CharField(max_length=100)
    weekly_hours = forms.IntegerField(min_value=1, max_value=40)

    class Meta:
        model = Assignment
        fields = "__all__"

    def clean_role(self):
        role = self.cleaned_data.get("role")
        if not role or len(role.strip()) == 0:
            raise ValidationError("Role is not valid.")
        return role
    
    def clean_weekly_hours(self):
        weekly_hours = self.cleaned_data.get("weekly_hours")
        if weekly_hours < 1 or weekly_hours > 40:
            raise ValidationError("Weekly hours must be between 1 and 40.")
        return weekly_hours














# Validate name
def valid_name(name):
    cleaned_name = re.sub(r"[ -]", name)

    if not str(cleaned_name).isalpha():
        return False
    
    if str(name) != str(name).strip():
        return False
    
    return True