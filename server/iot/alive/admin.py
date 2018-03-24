from django.contrib import admin
from .models import Alive
# Register your models here.
@admin.register(Alive)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'ip_address', 'times', 'send_data')
