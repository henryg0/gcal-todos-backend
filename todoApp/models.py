from django.db import models

# Create your models here.
class Status(models.TextChoices):
    PENDING = 'P', 'Pending'
    COMPLETED = 'C', 'Completed'
    IN_PROGRESS = 'IP', 'In Progress'
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('todoApp.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length= 2, choices=Status.choices, default=Status.PENDING)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=15)