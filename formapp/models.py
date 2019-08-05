from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table='students'