from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,verbose_name="Student Name")
    email=models.EmailField( max_length=254,verbose_name="Student Email")
    mobile=models.CharField(max_length=10,verbose_name="Student Phone no.",default=0000000000)
    rollno=models.CharField(max_length=50,verbose_name="Student Roll NO.",default="NULL")
    
    
    def __str__(self):
        return str(self.id)
    