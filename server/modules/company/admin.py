from django.contrib import admin

from modules.company.models import Company, CompanyServices


admin.site.register(Company)
admin.site.register(CompanyServices)
