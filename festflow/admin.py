from django.contrib import admin
from .models import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'venue', 'date_time')

admin.site.register(Profile)
admin.site.register(Event, EventAdmin)
admin.site.register(organizerMember)
admin.site.register(sponsor)
