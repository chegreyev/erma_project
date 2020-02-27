from django.db import models
from django.conf import settings

Person = settings.AUTH_USER_MODEL

# Create your models here.
class Project(models.Model):
    PROGRESS_STAATUS = (
        (0 , "NOT STARTED") , 
        (1 , "IS WORKING") , 
        (3 , "DONE")
    )

    title = models.CharField(max_length = 255)
    cost = models.IntegerField()
    description = models.TextField()

    deadline = models.DateField()

    project_manager = models.ForeignKey(Person , models.DO_NOTHING , related_name="project_manager" , default = None)
    developer = models.ForeignKey(Person , models.DO_NOTHING , related_name="developer" , blank = True , null = True , default = None)
    
    progress = models.IntegerField(choices = PROGRESS_STAATUS , default= 0)

    def __str__(self):
        return self.title

    