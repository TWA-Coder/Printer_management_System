from django.contrib import admin
from .models import Department, Printer, PrintJob

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'paper_quota')
    search_fields = ('name',)

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'department', 'printer_id')
    search_fields = ('name', 'printer_id')
    list_filter = ('department',)

@admin.register(PrintJob)
class PrintJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'printer', 'department', 'pages_printed', 'timestamp')
    list_filter = ('department', 'printer', 'timestamp')
    search_fields = ('user__username',)
