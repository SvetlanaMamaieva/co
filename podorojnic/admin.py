from django.contrib import admin

# Register your models here.
from .models import Direction, Entry, Country, Info


admin.site.register(Direction)
admin.site.register(Entry)
admin.site.register(Country)
admin.site.register(Info)



