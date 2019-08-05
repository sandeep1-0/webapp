from django.db import models

class College(models.Model):

    clg_name=models.CharField(max_length=100)
    clg_email=models.EmailField(unique=True)
    clg_address=models.CharField(max_length=250)


    def __str__(self):
        return self.clg_name

    class Meta:
        db_table='college'