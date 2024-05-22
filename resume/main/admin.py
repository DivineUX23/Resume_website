from django.contrib import admin
from django.db import models
#from django_json_widget.widgets import JSONEditorWidget
#from jsoneditor.forms import JSONEditor
from jsoneditor.forms import JSONEditor


# Register your models here.
from . models import (Skill, 
    UserProfile,
    Contact,
    Testimonial,
    Media, 
    Portfolio,
    Blog,
    Certificate,
    Conversation)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'cv')

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