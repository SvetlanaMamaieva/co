from django.contrib import admin

# Register your models here.
from .models import Direction, Entry


admin.site.register(Direction)
admin.site.register(Entry)



