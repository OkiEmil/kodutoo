from django.db import models
from django.forms import ModelForm

#class Makse(models.Model):
#    volgneja = models.CharField(max_length=100)
#    volgnetav = models.CharField(max_length=100)
#    raha = models.TextField()

class Transaction(models.Model):

    maksja = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    saaja = models.CharField(max_length= 100)
    rahahulk = models.CharField(max_length=100)
    pohjus = models.CharField(max_length=150, default='Söök')
    
    def __str__(self):
        return str(self.id)

#class TransactionForm(ModelForm):
#    class Meta:
#        model = Transaction
#        fields = ["maksja", "saaja", "rahahulk"]
#        exclude = ["id"]


