from django.db import models
from django.contrib.auth.models import User
from student.models import Student

class Features(models.Model):
    finishing=models.FloatField()
    headingAccuracy=models.FloatField()
    shortPassing=models.FloatField()
    volleys=models.FloatField()
    dribbling=models.FloatField()
    curve=models.FloatField()
    fKAccuracy=models.FloatField()
    longPassing=models.FloatField()
    ballControl=models.FloatField()
    acceleration=models.FloatField()
    sprintSpeed=models.FloatField()
    agility=models.FloatField()
    reactions=models.FloatField()
    balance=models.FloatField()
    shotPower=models.FloatField()
    jumping=models.FloatField()
    stamina=models.FloatField()
    strength=models.FloatField()
    longShots=models.FloatField()
    aggression=models.FloatField()
    interceptions=models.FloatField()
    positioning=models.FloatField()
    vision=models.FloatField()
    penalties=models.FloatField()
    composure=models.FloatField()
    marking=models.FloatField()
    standingTackle=models.FloatField()
    slidingTackle=models.FloatField()
    gKDiving=models.FloatField()
    gKHandling=models.FloatField()
    gKKicking=models.FloatField()
    gKPositioning=models.FloatField()
    gKReflexes=models.FloatField()
    position=models.CharField(max_length=50,blank=True,null=True)
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Final result {self.position}"

