# Generated by Django 2.0.2 on 2018-10-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20181026_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='URLField',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='URL'),
        ),
    ]
