# Generated by Django 3.1.1 on 2020-09-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calc', '0002_auto_20200929_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcourses',
            name='startedfrom',
            field=models.DateTimeField(verbose_name='started from'),
        ),
    ]
