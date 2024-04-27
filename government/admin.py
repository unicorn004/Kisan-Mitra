# Register your models here.
from django.contrib import admin
from .models import Farmer, FinancialInstitution, GovernmentProgram, Grant, Subsidy


# Register your models here.
admin.site.register(Farmer)
admin.site.register(FinancialInstitution)
admin.site.register(GovernmentProgram)
admin.site.register(Grant)
admin.site.register(Subsidy)
