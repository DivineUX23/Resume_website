# Generated by Django 5.0.4 on 2024-04-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]