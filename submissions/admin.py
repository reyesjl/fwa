from django.contrib import admin
from .models import RecruitingSubmission, ToursSubmission, CanterburyKitSubmission

class BaseSubmissionAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone', 'status']
    list_filter = ['status']

class RecruitingSubmissionAdmin(BaseSubmissionAdmin):
    list_display = BaseSubmissionAdmin.list_display + ['position', 'age', 'origin_country', 'destination_country']
    list_filter = BaseSubmissionAdmin.list_filter + ['position', 'origin_country', 'destination_country']
    ordering = ['-status', 'lastname']

class ToursSubmissionAdmin(BaseSubmissionAdmin):
    list_display = BaseSubmissionAdmin.list_display + ['teamname', 'teamsize']
    list_filter = BaseSubmissionAdmin.list_filter + ['teamname']
    ordering = ['teamname']

class CanterburyKitSubmissionAdmin(BaseSubmissionAdmin):
    list_display = BaseSubmissionAdmin.list_display + ['teamname', 'teamsize']
    list_filter = BaseSubmissionAdmin.list_filter + ['teamname']
    ordering = ['teamname']

admin.site.register(RecruitingSubmission, RecruitingSubmissionAdmin)
admin.site.register(ToursSubmission, ToursSubmissionAdmin)
admin.site.register(CanterburyKitSubmission, CanterburyKitSubmissionAdmin)