from django.contrib import admin
from .models import PlayerEntry

class PlayerEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_of_residence', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'country_of_residence')

admin.site.register(PlayerEntry, PlayerEntryAdmin)

