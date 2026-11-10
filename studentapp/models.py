from django.db import models

class Student(models.Model):
    rollNo = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    duration = models.IntegerField()
    

    def __str__(self):
        return f"{self.rollNo} - {self.firstName} {self.lastName}"
