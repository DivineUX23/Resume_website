# Generated by Django 4.2.7 on 2024-12-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_aboutme_detailed_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]