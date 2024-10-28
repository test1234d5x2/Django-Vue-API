import json
from django.core.exceptions import FieldDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from django.forms.models import model_to_dict

from .models import Project, Employee, Assignment

TYPE_MODEL_MAPPING = {
    "project": Project,
    "employee": Employee,
    "assignment": Assignment,
}



def employees_api(request):
    if request.method == "POST":

        newData = json.loads(request.body)

        try:
            for key in newData.keys():
                print(Employee._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered here")
            return incorrect_form_fields_message()
        
        newData = Employee.objects.create(**newData)
        newData.save()

        return JsonResponse({
            "data": model_to_dict(newData)
        })

    return JsonResponse({
        "data": [model_to_dict(employee) for employee in Employee.objects.all()]
    })


def employee_api(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "DELETE":
        employee.delete()
        return JsonResponse({})
    
    # Update the data in the employee variable.
    
    return JsonResponse({
        "data": model_to_dict(employee)
    })




def invalid_request_message():
    return JsonResponse({
        "message": "Request method is invalid"
    })


def incorrect_form_fields_message():
    return JsonResponse({
        "message": "Incorrect set of form fields."
    })


def model_not_found():
    return JsonResponse({
        "message": "Data type not found."
    })


def get_model(type) -> models.Model:
    if type not in TYPE_MODEL_MAPPING.keys():
        return None
    
    return TYPE_MODEL_MAPPING[type]