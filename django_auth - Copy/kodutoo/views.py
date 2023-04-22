from django.shortcuts import render
from kodutoo.models import Transaction
from django.contrib.auth import get_user_model
from kodutoo.forms import TransactionForm
from django.contrib import messages
from kodutoo import models

model = Transaction
# Create your views here.
def home(request):
   maksete_list = Transaction.objects.all()
   return render(request, "home.html", {"maksed":maksete_list})
   
def accountView(request):
      form = TransactionForm()
      
      if request.method == "POST":
         form = TransactionForm(request.POST)
         if form.is_valid():
            Transaction = form.save(commit=False)
            Transaction.maksja = request.user.username
            Transaction.save()
      
      
#      model = Transaction
#Kui palju raha kokku mul võlgades kas juures või miinuses :)
      x = 0
      juures = 0
      volgnen = 0
      maksjate_list = []
      saajate_list = []
      [maksjate_list.append(maksja[0]) for maksja in model.objects.values_list('maksja')]
      [saajate_list.append(saaja[0]) for saaja in model.objects.values_list('saaja')]

      for saaja, maksja in list(zip(maksjate_list, saajate_list)):
           
            if saaja == request.user.username:
               volgnen += int(model.objects.values_list('rahahulk')[x][0])

            if maksja == request.user.username:
               juures += int(model.objects.values_list('rahahulk')[x][0])

            x += 1
      kokku = juures-volgnen
      
      
      return render(request, "account.html", {"volgnen" : volgnen, "juures" : juures, "kokku" : kokku, "form": form})


def signup (request):
	return render(request,'accounts/signup.html',{})
