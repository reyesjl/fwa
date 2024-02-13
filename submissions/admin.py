from django.contrib import admin
from .models import RecruitingSubmission, ToursSubmission

class BaseSubmissionAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone', 'status']
    list_filter = ['status']

class RecruitingSubmissionAdmin(BaseSubmissionAdmin):
    list_display = BaseSubmissionAdmin.list_display + ['position', 'age', 'origin_country', 'destination_country']
    list_filter = BaseSubmissionAdmin.list_filter + ['position', 'origin_country', 'destination_country']
    ordering = ['-status', 'lastname']  # Example ordering

class ToursSubmissionAdmin(BaseSubmissionAdmin):
    list_display = BaseSubmissionAdmin.list_display + ['teamname', 'teamsize']
    list_filter = BaseSubmissionAdmin.list_filter + ['teamname']
    ordering = ['teamname']  # Example ordering

admin.site.register(RecruitingSubmission, RecruitingSubmissionAdmin)
admin.site.register(ToursSubmission, ToursSubmissionAdmin)