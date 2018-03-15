from django.contrib import admin

# Register your models here.
from django.contrib import admin
from database.models import Order, Project

class ProjectInline(admin.StackedInline):
    model = Project
    extra = 10

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {'fields': ['order_name']}),
        ("日期", {'fields': ['order_time']}),
    ]
    inlines = [ProjectInline]
    
admin.site.register(Order, OrderAdmin)