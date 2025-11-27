from django.db import models

from django.db import models

class Task(models.Model):
    task_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    estimated_hours = models.FloatField(null=True, blank=True)
    importance = models.IntegerField(default=5)
    dependencies = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title

