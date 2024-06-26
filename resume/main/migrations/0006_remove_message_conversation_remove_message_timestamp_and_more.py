# Generated by Django 5.0.4 on 2024-05-17 00:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_conversation_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='conversation',
            name='message',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='conversation', to='main.message'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conversation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
