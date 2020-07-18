from django.contrib import admin
from .models import List


# Register your models here.

class listAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'timestamp', 'remainderTime', 'details']
    search_fields = ['keyword', 'details']
    # filter_vertical = ['category']
    list_per_page = 25

    list_filter = ['remainderTime']

    class Meta:
        Model = List


admin.site.register(List, listAdmin)
