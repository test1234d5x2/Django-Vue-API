from django.db import models

# Create your models here.
class Employee(models.Model):
    """ Stores data about an employee """

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    background = models.TextField()
    is_working = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Project(models.Model):
    """ Stores data about a project """

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    employees = models.ManyToManyField(Employee, through="Assignment")

    def __str__(self):
        return f"{self.name}"

class Assignment(models.Model):
    """ Stores data about a project that has benn assigned to an employee """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    weekly_hours = models.IntegerField()

    def __str__(self):
        return f"{self.employee} is working on {self.project} as a {self.role} for {self.weekly_hours} hours"