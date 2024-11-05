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
    """ Returns the name of the models. """
    return JsonResponse({"data": [str(model_name).title() for model_name in TYPE_MODEL_MAPPING.keys()]})


def assignment_api(request, assignment_id):
    """ Handles the removal and updating of a specific assignment. """

    assignment = Assignment.objects.get(id=assignment_id)

    if request.method == "DELETE":
        assignment.delete()
        return JsonResponse({})
    
    updated_data = json.loads(request.body)

    if 'employee_id' in updated_data.keys():
        updated_data['employee'] = updated_data.pop('employee_id', -1)
    if 'project_id' in updated_data.keys():
        updated_data['project'] = updated_data.pop('project_id', -1)
    
    form = AssignmentForm(updated_data)
    if form.is_valid():
        for field_name, value in form.cleaned_data.items():
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
    """ Handles the retrieval of all assignments and the addition of a new assignment. """

    if request.method == "POST":
        
        new_data = json.loads(request.body)

        if 'employee_id' in new_data.keys():
            new_data['employee'] = new_data.pop('employee_id', -1)
        if 'project_id' in new_data.keys():
            new_data['project'] = new_data.pop('project_id', -1)

        try:
            for key in new_data.keys():
                print(Assignment._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered Here")
            return incorrect_form_fields_message()
                
        form = AssignmentForm(new_data)
        if form.is_valid():
            new_record = Assignment.objects.create(**form.cleaned_data)
            new_record.save()
            
            new_data = Assignment.objects.filter(id=new_record.pk).values()[0]

            return JsonResponse({
                "data": new_data
            })
        else:
            return JsonResponse({"data": {}})

    assignments = Assignment.objects.all().values()
    
    return JsonResponse({
        "data": list(assignments)
    })    


def projects_api(request):
    """ Handles the retrieval of all projects and the addition of a new project. """

    if request.method == "POST":
        
        new_data = json.loads(request.body)

        try:
            for key in new_data.keys():
                print(Project._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered Here")
            return incorrect_form_fields_message()
        
        form = ProjectForm(new_data)
        if form.is_valid():
            new_data = Project.objects.create(**new_data)
            new_data.save()
            return JsonResponse({
                "data": model_to_dict(new_data, exclude=['employees'])
            })
        else:
            return JsonResponse({"data": {}})
        
    return JsonResponse({
        "data": [project for project in Project.objects.all().values("id", "name", "description", "start_date")]
    })


def project_api(request, project_id):
    """ Handles the removal or updating of a specific project. """

    project = Project.objects.get(id=project_id)

    if request.method == "DELETE":
        project.delete()
        return JsonResponse({})
    
    updated_data = json.loads(request.body)
    form = ProjectForm(updated_data)
    
    if form.is_valid():
        for field_name, value in form.cleaned_data.items():
            setattr(project, field_name, value)

        project.save()
    else:
        return JsonResponse({"data": {}})

    project = Project.objects.get(id=project_id)
    
    return JsonResponse({
        "data": model_to_dict(project, exclude=['employees'])
    })


def employees_api(request):
    """ Handles the retrieval of all employees or the addition of a new employee. """

    if request.method == "POST":

        new_data = json.loads(request.body)

        try:
            for key in new_data.keys():
                print(Employee._meta.get_field(key))

        except FieldDoesNotExist:
            print("Entered here")
            return incorrect_form_fields_message()
        

        form = EmployeeForm(new_data)
        if form.is_valid():
            new_data = Employee.objects.create(**new_data)
            new_data.save()
            return JsonResponse({
                "data": model_to_dict(new_data)
            })
        else:
            return JsonResponse({"data": {}})

    return JsonResponse({
        "data": [model_to_dict(employee) for employee in Employee.objects.all()]
    })


def employee_api(request, employee_id):
    """ Handles the updating or removal of a specific employee. """

    employee = Employee.objects.get(id=employee_id)

    if request.method == "DELETE":
        employee.delete()
        return JsonResponse({})
    
    updated_data = json.loads(request.body)
    form = EmployeeForm(updated_data)
    
    if form.is_valid():
        for field_name, value in form.cleaned_data.items():
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
    """ Returns a message indicating that the form field set is incorrect. """

    return JsonResponse({
        "message": "Incorrect set of form fields."
    })
