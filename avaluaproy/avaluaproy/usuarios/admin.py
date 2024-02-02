from django.contrib import admin
from usuarios.models import MyUser
# Register your models here.

#UD8.1.d
@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    pass