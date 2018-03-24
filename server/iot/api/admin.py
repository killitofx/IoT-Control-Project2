from django.contrib import admin
from .models import Port, Time

@admin.register(Port)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'port_name', 'port_type', 'port_state', 'author', 'is_change', 'last_updated_time')

@admin.register(Time)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('port_id', 'ctrl', 'loop', 's_time', 'c_time', 'is_change')
# Register your models here.
