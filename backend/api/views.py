import json
from django.core.exceptions import FieldDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .forms import EmployeeForm, ProjectForm, AssignmentForm
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
    
    updatedData = json.loads(request.body)

    if 'employee_id' in updatedData.keys():
        updatedData['employee'] = updatedData.pop('employee_id', -1)
    if 'project_id' in updatedData.keys():
        updatedData['project'] = updatedData.pop('project_id', -1)
    
    form = AssignmentForm(updatedData)
    if (form.is_valid()):
        for (field_name, value) in form.cleaned_data.items():
            setattr(assignment, field_name, value)

        assignment.save()
    else:
        return JsonResponse({"data": {}})

    assignment.save()

    assignment = Assignment.objects.filter(id=assignment_id).values()[0]
    
    return JsonResponse({
        "data": assignment
    })


def assignments_api(request):
    if request.method == "POST":
        
        newData = json.loads(request.body)

        if 'employee_id' in newData.keys():
            newData['employee'] = newData.pop('employee_id', -1)
        if 'project_id' in newData.keys():
            newData['project'] = newData.pop('project_id', -1)

        try:
            for key in newData.keys():
                print(Assignment._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered Here")
            return incorrect_form_fields_message()
        
        print(newData)
        
        form = AssignmentForm(newData)
        if (form.is_valid()):
            newRecord = Assignment.objects.create(**form.cleaned_data)
            newRecord.save()
            
            newData = Assignment.objects.filter(id=newRecord.pk).values()[0]

            return JsonResponse({
                "data": newData
            })
        else:
            return JsonResponse({"data": {}})

    assignments = Assignment.objects.all().values()
    
    return JsonResponse({
        "data": list(assignments)
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
        
        form = ProjectForm(newData)
        if (form.is_valid()):
            newData = Project.objects.create(**newData)
            newData.save()
            return JsonResponse({
                "data": model_to_dict(newData, exclude=['employees'])
            })
        else:
            return JsonResponse({"data": {}})
        
    return JsonResponse({
        "data": [project for project in Project.objects.all().values("id", "name", "description", "start_date")]
    })


def project_api(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == "DELETE":
        project.delete()
        return JsonResponse({})
    
    updatedData = json.loads(request.body)
    form = ProjectForm(updatedData)
    
    if (form.is_valid()):
        for (field_name, value) in updatedData.items():
            setattr(project, field_name, value)

        project.save()
    else:
        return JsonResponse({"data": {}})

    project = Project.objects.get(id=project_id)
    
    return JsonResponse({
        "data": model_to_dict(project, exclude=['employees'])
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
        

        form = EmployeeForm(newData)
        if (form.is_valid()):
            newData = Employee.objects.create(**newData)
            newData.save()
            return JsonResponse({
                "data": model_to_dict(newData)
            })
        else:
            return JsonResponse({"data": {}})

    return JsonResponse({
        "data": [model_to_dict(employee) for employee in Employee.objects.all()]
    })


def employee_api(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == "DELETE":
        employee.delete()
        return JsonResponse({})
    
    updatedData = json.loads(request.body)
    form = EmployeeForm(updatedData)
    
    if (form.is_valid()):
        for (field_name, value) in updatedData.items():
            setattr(employee, field_name, value)

        employee.save()
    else:
        return JsonResponse({"data": {}})

    employee = Employee.objects.get(id=employee_id)
    
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