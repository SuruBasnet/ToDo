from django.db import models

# Create your models here.

class ToDo(models.Model):
    status_choices = [('Done','Done'),('Not done','Not done')]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=60,choices=status_choices)

    def __str__(self):
        return self.title

