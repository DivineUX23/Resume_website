from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

# models.py
from django.db import models

class AboutMe(models.Model):
    headline = models.CharField(max_length=200)
    short_bio = models.TextField(help_text="Brief introduction that's always visible")
    detailed_bio = RichTextField(help_text="Detailed information shown when expanded")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='documents/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.headline



# models.py
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    technologies_used = models.ManyToManyField('Tool', blank=True)
    key_achievements = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_date', '-order']

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    def save(self, *args, **kwargs):
        if self.is_current:
            self.end_date = None
        super().save(*args, **kwargs)

    @property
    def duration(self):
        end = self.end_date or timezone.now().date()
        delta = relativedelta(end, self.start_date)
        years = delta.years
        months = delta.months

        if years and months:
            return f"{years} {'year' if years == 1 else 'years'}, {months} {'month' if months == 1 else 'months'}"
        elif years:
            return f"{years} {'year' if years == 1 else 'years'}"
        elif months:
            return f"{months} {'month' if months == 1 else 'months'}"
        else:
            return "Less than a month"

# models.py
# models.py (alternative version with custom colors)
from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]

    COLOR_SCHEMES = [
        ('pink', 'Pink - Beginner'),
        ('blue', 'Blue - Intermediate'),
        ('purple', 'Purple - Advanced'),
        ('green', 'Green - Expert'),
    ]

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Intermediate')
    description = models.TextField()
    order = models.IntegerField(default=0)

    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)


    color_scheme = models.CharField(
        max_length=20, 
        choices=COLOR_SCHEMES, 
        default='blue'
    )

    @property
    def level_color_classes(self):
        color_mapping = {
            'pink': 'bg-pink-100 text-pink-800 border border-pink-200',
            'blue': 'bg-blue-100 text-blue-800 border border-blue-200',
            'purple': 'bg-purple-100 text-purple-800 border border-purple-200',
            'green': 'bg-green-100 text-green-800 border border-green-200',
        }
        return color_mapping.get(self.color_scheme, 'bg-gray-100 text-gray-800')

    def save(self, *args, **kwargs):
        # Automatically set color scheme based on level if not manually set
        if not self.color_scheme:
            level_color_mapping = {
                'Beginner': 'pink',
                'Intermediate': 'blue',
                'Advanced': 'purple',
                'Expert': 'green',
            }
            self.color_scheme = level_color_mapping.get(self.level, 'blue')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





# models.py

class Tool(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('testing', 'Testing'),
        ('monitoring', 'Monitoring'),
        ('ai', 'AI'),
        ('other', 'Other')
    ]

    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='tools/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    

class Contact(models.Model):

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['timestamp']
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    message = models.TextField(verbose_name='Message')

    def __str__(self) -> str:
        return f'{self.name}'
    

class Testimonial(models.Model):

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['name']

    thumbnail = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    #timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Media(models.Model):

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media Files'
        ordering = ['name']

    image = models.ImageField(upload_to='media/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #description = models.TextField(blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name}'



class Portfolio(models.Model):

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio Profiles'
        ordering = ['name']
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    #url = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}/'
    

class Blog(models.Model):

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog Posts'
        ordering = ['timestamp']


    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)
         

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'
    


class Certificate(models.Model):

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certificate/', blank=True, null=True)
    #url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    
#REQUIRES REVIEW
class Conversation(models.Model):
    class Meta:
        verbose_name = 'Assistance'
        
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=100, unique=True)
    conversation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    chat_history = models.JSONField(blank=True, null=False)

    def __str__(self) -> str:
        return f'Assistant Session at {self.date.strftime("%Y-%m-%d %H:%M:%S")}'



class Resume_info(models.Model):

    class Meta:
        verbose_name = 'Resume_info'
    body = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(True)

    def __str__(self) -> str:
        return self.body