from django.shortcuts import render
from kodutoo.models import Transaction

# Create your views here.
def home(request):
   maksete_list = Transaction.objects.all()
   return render(request, "home.html", {"maksed":maksete_list})