from django.contrib import admin
from django.db import models
#from django_json_widget.widgets import JSONEditorWidget
#from jsoneditor.forms import JSONEditor
from jsoneditor.forms import JSONEditor
from django.utils.html import format_html


# Register your models here.
from . models import (Skill, 
    UserProfile,
    Contact,
    Testimonial,
    Media, 
    Portfolio,
    Blog,
    Certificate,
    Conversation,
    Resume_info)
"""
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
"""

# admin.py
from django.contrib import admin
from .models import AboutMe

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('headline', 'email')

# admin.py
from django.contrib import admin
from .models import Company, WorkExperience

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name', 'location')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current', 'employment_type')
    list_filter = ('company', 'employment_type', 'is_current')
    search_fields = ('title', 'company__name', 'description')
    filter_horizontal = ('technologies_used',)
    raw_id_fields = ('company',)
    ordering = ('-start_date', '-end_date')


# admin.py
from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_editable = ('category', 'order')
    list_filter = ('category',)
    search_fields = ('name', 'description')


# admin.py
from django.contrib import admin
from .models import Skill, UserProfile

# admin.py
from django.contrib import admin
from .models import Skill, UserProfile

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'score', 'color_scheme', 'order')
    list_editable = ('level', 'color_scheme', 'score', 'order')
    search_fields = ('name', 'description')
    list_filter = ('level', 'color_scheme')



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'cv')
    filter_horizontal = ('skills',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'timestamp')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quote')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'body', 'description', 'is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')



@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'conversation_id',  'date', 'chat_history')
    
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'chat_history':
            kwargs['widget'] = JSONEditor
        return super().formfield_for_dbfield(db_field, **kwargs)


@admin.register(Resume_info)
class Resume_infoAdmin(admin.ModelAdmin):
    list_display  = ('body', 'is_active')

    def body_preview(self, obj):
        # Sanitize and truncate the rich text content for display
        return format_html('<div>{}</div>', obj.body[:100] + '...')

    body_preview.short_description = 'body'