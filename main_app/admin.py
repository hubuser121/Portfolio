from django.contrib import admin
from .models import AboutMe,Project, Certificate, Experience, Publication, LeadershipActivity, Skill, Education


admin.site.register(AboutMe)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed')
    search_fields = ('title',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_received')
    search_fields = ('title',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'publisher')
    search_fields = ('title', 'publisher')

@admin.register(LeadershipActivity)
class LeadershipActivityAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'start_date', 'end_date')
    search_fields = ('role', 'organization')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    search_fields = ('degree', 'institution')
