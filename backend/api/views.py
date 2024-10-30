import json
from django.core.exceptions import FieldDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Project, Employee, Assignment







TYPE_MODEL_MAPPING = {
    "employee": Employee,
    "project": Project,
    "assignment": Assignment,
}

def get_models(request):
    return JsonResponse({"data": [str(model_name).title() for model_name in TYPE_MODEL_MAPPING.keys()]})



def assignment_api(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)

    if request.method == "DELETE":
        assignment.delete()
        return JsonResponse({})
    

    # Update the data in the assignment variable.
    
    return JsonResponse({
        "data": model_to_dict(assignment)
    })


def assignments_api(request):
    if request.method == "POST":
        
        newData = json.loads(request.body)

        try:
            for key in newData.keys():
                print(Assignment._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered Here")
            return incorrect_form_fields_message()
        
        newData = Assignment.objects.create(**newData)
        newData.save()

        return JsonResponse({
            "data": model_to_dict(newData)
        })
    
    return JsonResponse({
        "data": [model_to_dict(assignment) for assignment in Assignment.objects.all()]
    })    



def projects_api(request):
    if request.method == "POST":
        
        newData = json.loads(request.body)

        try:
            for key in newData.keys():
                print(Project._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered Here")
            return incorrect_form_fields_message()
        
        newData = Project.objects.create(**newData)
        newData.save()

        return JsonResponse({
            "data": model_to_dict(newData)
        })
    
    return JsonResponse({
        "data": [model_to_dict(project) for project in Project.objects.all()]
    })


def project_api(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == "DELETE":
        project.delete()
        return JsonResponse({})
    

    # Update the data in the project variable.
    
    return JsonResponse({
        "data": model_to_dict(project)
    })



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


def employee_api(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == "DELETE":
        employee.delete()
        return JsonResponse({})
    
    # Update the data in the employee variable.
    
    return JsonResponse({
        "data": model_to_dict(employee)
    })




# Helper Functions

def incorrect_form_fields_message():
    return JsonResponse({
        "message": "Incorrect set of form fields."
    })


def process_field_name_to_text(name):
    return str(name).replace("_", " ").title()