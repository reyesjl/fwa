from django.contrib import admin
from .models import PlayerPlan

class PlayerPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_category', 'plan_file', 'plan_picture')
    list_filter = ('plan_category',)

admin.site.register(PlayerPlan, PlayerPlanAdmin)
