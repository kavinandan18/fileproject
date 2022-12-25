from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeModelAdmin(ImportExportModelAdmin):
    list_display=['uid','ename','age','salary','location']