from django.contrib import admin

# Register your models here.
from .models import UserIncome, Source
# Register your models here.

admin.site.register(UserIncome)
admin.site.register(Source)