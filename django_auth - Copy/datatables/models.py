from django.db import models

#class Makse(models.Model):
#    volgneja = models.CharField(max_length=100)
#    volgnetav = models.CharField(max_length=100)
#    raha = models.TextField()

class Transaction(models.Model):

    maksja = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    saaja = models.CharField(max_length= 100)
    rahahulk = models.CharField(max_length=100)


def __str__(self):
    return self.id