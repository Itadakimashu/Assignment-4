from django.db import models
from category.models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    description = models.TextField()
    assign_date = models.DateField()

    category = models.ManyToManyField(TaskCategory, related_name='categories')

    def __str__(self):
        return self.title