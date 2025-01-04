from django.contrib import admin

from .models import Flat


class SiteAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address')
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']


admin.site.register(Flat, SiteAdmin)


