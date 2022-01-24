from django.db import models

#How its stored in database
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    #String repersentation
    def __str__(self):
        return self.title

    #Everytime you make changes in model.py you need to migrate
    #Model.py concerns the database