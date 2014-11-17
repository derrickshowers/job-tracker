from django.db import models

# Create your models here.
class Connection(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    @classmethod
    def addConnection(cls, id, firstName, lastName, company):
        connection = cls(id=id, firstName=firstName, lastName=lastName, company=company)
        return connection