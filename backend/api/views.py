import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db import models

from .models import Project, Employee, Assignment

TYPE_MODEL_MAPPING = {
    "project": Project,
    "employee": Employee,
    "assignment": Assignment,
}


def get_data(request):

    if request.method != "GET":
        return invalid_request_message()

    return JsonResponse({
        "projects": [project for project in Project.objects.all().values()],
        "employees": [employee for employee in Employee.objects.all().values()],
        "assignments": [assignment for assignment in Assignment.objects.all().values()],
    })


def add_data(request, type):
    
    if request.method != "POST":
        return invalid_request_message()

    newData = json.loads(request.body)
    model = get_model(type)
    
    for key in newData.keys():
        if key not in model._meta.get_fields():
            return JsonResponse({
                "message": "Incorrect set of form fields."
            })
        
    newData = model.objects.create(**model)

    return JsonResponse({
        "type": type,
        "data": newData,
    })



def delete_data(request, type, id):

    if request.method != "DELETE":
        return invalid_request_message()

    model = get_model(type)

    if model is None:
        return JsonResponse({
            "message": "Data type not found."
        })

    model.objects.get(id=id).delete()

    return JsonResponse({
        "message": "Data deleted."
    })


def update_data(request, type, id):

    if request.method != "PUT":
        return invalid_request_message()

    return JsonResponse({
        "message": "Working"
    })


def invalid_request_message():
    return JsonResponse({
        "message": "Request method is invalid"
    })


def get_model(type) -> models.Model:
    if type not in TYPE_MODEL_MAPPING.keys():
        return None
    
    return TYPE_MODEL_MAPPING[type]