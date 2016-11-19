from django.contrib import admin
from .models import *
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'content')

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(organizerMember)
admin.site.register(sponsor)
admin.site.register(About, AboutAdmin)
