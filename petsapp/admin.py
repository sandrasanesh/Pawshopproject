from django.contrib import admin
from petsapp.models import catedb,petdb,shopdb,fooddb

# Register your models here.
admin.site.register(catedb)
admin.site.register(petdb)
admin.site.register(shopdb)
admin.site.register(fooddb)
