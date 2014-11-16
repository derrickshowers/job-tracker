from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ' - ' + self.company