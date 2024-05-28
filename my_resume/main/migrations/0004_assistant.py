# Generated by Django 5.0.4 on 2024-05-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_skill_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('conversation_id', models.CharField(max_length=255)),
                ('chat_history', models.JSONField(blank=True)),
            ],
            options={
                'verbose_name': 'Assistant',
                'verbose_name_plural': 'Assistants',
            },
        ),
    ]
