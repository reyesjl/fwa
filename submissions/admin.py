from django.contrib import admin
from .models import RecruitingSubmission, ToursSubmission, CanterburyKitSubmission, TeamItemSubmission, Issue, Feedback, Design, Specialist

class BaseSubmissionAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone', 'status']
    list_filter = ['status']

class IssueSubmissionAdmin(admin.ModelAdmin):
    list_display = ['email', 'problem_description', 'status']
    list_filter = ['status']

class DesignSubmissionAdmin(admin.ModelAdmin):
    list_display = ['email', 'design_description', 'status']
    list_filter = ['status']

class FeedbackSubmissionAdmin(admin.ModelAdmin):
    list_display = ['email', 'feedback', 'status']
    list_filter = ['status']

class SpecialistSubmissionAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'cell', 'help_details', 'status']
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

class TeamItemSubmissionAdmin(BaseSubmissionAdmin):
    list_display = BaseSubmissionAdmin.list_display + ['product_name','teamname', 'teamsize']
    list_filter = BaseSubmissionAdmin.list_filter + ['product_name','teamname']

admin.site.register(RecruitingSubmission, RecruitingSubmissionAdmin)
admin.site.register(ToursSubmission, ToursSubmissionAdmin)
admin.site.register(CanterburyKitSubmission, CanterburyKitSubmissionAdmin)
admin.site.register(TeamItemSubmission, TeamItemSubmissionAdmin)
admin.site.register(Issue, IssueSubmissionAdmin)
admin.site.register(Feedback, FeedbackSubmissionAdmin)
admin.site.register(Design, DesignSubmissionAdmin)
admin.site.register(Specialist, SpecialistSubmissionAdmin)