from django import forms
from .models import Transaction
from django.contrib.auth import get_user_model

class TransactionForm(forms.ModelForm):
#    Transaction.saaja = forms.CharField(label="Saaja", max_length=100)
#    Transaction.rahahulk = forms.CharField(label="Rahahulk", max_length=100)
#    maksja = forms.CharField(max_length=35)
#    saaja = forms.CharField(max_length=35)
#    rahahulk = forms.CharField(max_length=10)
    class Meta:
        model = Transaction
        fields = [ "saaja", "rahahulk", "pohjus"]
        exclude = ["id", "maksja"]

    def clean(self):
        cleaned_data = super().clean()
        saaja = cleaned_data.get("saaja")
        rahahulk = (cleaned_data.get("rahahulk"))

        if saaja and rahahulk:
            users = []
            [users.append(name[0]) for name in get_user_model().objects.values_list('username')]
            if saaja not in users:
                raise forms.ValidationError(("Invalid name"), code="invalid")