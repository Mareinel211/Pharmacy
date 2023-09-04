from django.contrib import admin
from .models import Phar



class PharAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')



admin.site.register(Phar, PharAdmin)
