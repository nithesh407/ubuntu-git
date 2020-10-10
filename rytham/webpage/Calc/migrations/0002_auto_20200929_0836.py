# Generated by Django 3.1.1 on 2020-09-29 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Calc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='il',
            new_name='ct',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sp',
        ),
        migrations.AddField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateField(default=datetime.datetime(2020, 9, 29, 8, 36, 47, 171723, tzinfo=utc), verbose_name='started from'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='your_choice',
            field=models.BooleanField(default=False),
        ),
    ]