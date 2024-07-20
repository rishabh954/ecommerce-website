from django.contrib import admin
from .models import  contactform,product
from . import models
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Register your models here.
admin.site.register(contactform)

@admin.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'product_image']


class showuser(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ["user_photo", "name", "email_id", "city", "password"]


admin.site.register(models.user, showuser)
