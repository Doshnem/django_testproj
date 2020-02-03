from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'is_published', 'list_date', 'realtor')
    list_display_links = ('id', 'tittle')
    list_editable = ('is_published',)
    list_filter = ('realtor',)
    list_per_page = 10

admin.site.register(Listing, ListingAdmin)

