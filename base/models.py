from django.db import models

# Create your models here.

class Genere(models.Model):
    GenereId = models.AutoField(primary_key=True)
    GenereName = models.CharField(max_length=500)




