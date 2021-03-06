from django.db import models
from django.core.validators import *
from hub.validators import is_Esprit_Email
from .validators import is_Esprit_Email
# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(
        validators=[
            is_Esprit_Email #custom validator
                    ]
        
        ) #de base Chrafield
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Student(User):
    pass
class Coach(User):
    pass
class Projet(models.Model):
    project_name=models.CharField(max_length=50)
    dure=models.IntegerField()
    temp_allocated=models.IntegerField(
        validators=[
            MinValueValidator(1,"the min value must be equal to 1"),
            MaxValueValidator(50,"//")
            ]
        )
    besoin=models.TextField(max_length=250)
    description=models.TextField(max_length=250)
    isValid=models.BooleanField(default=False)
    creator=models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='creators'
    )
    supervisor=models.ForeignKey(
        Coach,
        on_delete=models.CASCADE, #en cas ou en supprime le user ,l'attribut va etre null
        related_name='supervisors'
    )
    member=models.ManyToManyField(
        Student,
        through='MemberShip' ,
        related_name='membres'   
    ) #il va genere une classe intermidiare nommé membreShip
    def __str__(self) -> str:
        return f"{self.project_name}"
class MemberShip(models.Model):
    projet=models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='students'
    )
    allocated_time_by_member=models.IntegerField(default=0)