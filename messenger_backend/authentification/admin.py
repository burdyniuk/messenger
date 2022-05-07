from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = "UniAll - Control Panel"
admin.site.unregister(Group)