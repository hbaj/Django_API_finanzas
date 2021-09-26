from django.db import models


# Create your models here.

class Variable(models.Model):
    variable = models.CharField(max_length = 50)
    def __str__(self):
        return self.variable


class VariableMeasure(models.Model):
    variable = models.ForeignKey(Variable, on_delete = models.CASCADE)
    value = models.CharField(max_length = 100)
    date = models.DateTimeField()
    def __str__():
        return self.variable
		