from django.contrib import admin
from .models import CustomUser, Speciality, Experience, Education, Skill, Award, Project, Tag, Contact

class CustomUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomUser, CustomUserAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Speciality, SpecialityAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Experience, ExperienceAdmin)


class EducationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Education, EducationAdmin)


class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill, SkillAdmin)


class AwardAdmin(admin.ModelAdmin):
    pass
admin.site.register(Award, AwardAdmin)


class TagInline(admin.TabularInline):
    model = Tag
    extra = 2  # Number of extra forms to display


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TagInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)


class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)