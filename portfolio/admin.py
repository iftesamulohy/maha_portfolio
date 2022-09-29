from atexit import register
from django.contrib import admin

from portfolio.models import AllColor, BlogImage, Category, Client, Education, IconColor, PriceTable, Project, Responsibilities, Skills, SkillsType, Style, UserDetails, VertionColor, WhatIdo, WorkExperience
from django import forms

# Register your models here.


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("name","proffession")
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'description': forms.Textarea}
        return super().get_form(request, obj, **kwargs)
    def has_add_permission(self, request, obj=None):
        return False
class SkillsTypeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
class WhatIdoAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'description': forms.Textarea}
        return super().get_form(request, obj, **kwargs)
class StyleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
class EducationAdmin(admin.ModelAdmin):
    list_display = ("title","description","institution")
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'description': forms.Textarea}
        return super().get_form(request, obj, **kwargs)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","description")
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'description': forms.Textarea}
        return super().get_form(request, obj, **kwargs)
admin.site.register(UserDetails,UserDetailsAdmin)
#admin.site.register(SkillsType,SkillsTypeAdmin)
admin.site.register(Skills)
#admin.site.register(IconColor)
admin.site.register(WhatIdo,WhatIdoAdmin)
#admin.site.register(VertionColor)
admin.site.register(Style,StyleAdmin)
#admin.site.register(AllColor)
admin.site.register(Education,EducationAdmin)
admin.site.register(Responsibilities)
admin.site.register(WorkExperience)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(PriceTable)
admin.site.register(BlogImage)
admin.site.register(Project,ProjectAdmin)