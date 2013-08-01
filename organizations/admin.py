from django.contrib import admin
from organizations.models import Organization, Branch

admin.site.register(Organization)
admin.site.register(Branch)