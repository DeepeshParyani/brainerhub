from django.contrib import admin
from employee.models import Employee, Company


class CustomCompany(admin.ModelAdmin):
    list_display = ["id", "company_name"]


class CustomEmployee(admin.ModelAdmin):
    list_display = ["employee_id", "first_name", "last_name", "phone_number", "company"]


admin.site.register(Employee, CustomEmployee)
admin.site.register(Company, CustomCompany)
