from django.db import models

# Create your models here.
class Date(models.Model):
    date = models.DateField(primary_key=True)

    def __str__(self):
        return self.date

class Meal(models.Model):
    date = models.ForeignKey(Date, on_delete= models.CASCADE)
    time = models.TimeField()
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return self.name
