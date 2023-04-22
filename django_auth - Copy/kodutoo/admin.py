from django.contrib import admin
from kodutoo.models import Transaction

class Adminn(admin.ModelAdmin):
    list_display = ["id", "maksja", "saaja", "rahahulk", "pohjus"]
    search_fields = ["maksja"]
    list_per_page = 8

admin.site.register(Transaction, Adminn)