# Generated by Django 3.1.7 on 2021-05-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_Activities', '0002_auto_20210514_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='Last_Name',
            field=models.CharField(db_column='Last Name', default='sdfgr', max_length=20),
            preserve_default=False,
        ),
    ]