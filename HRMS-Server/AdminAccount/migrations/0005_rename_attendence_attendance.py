# Generated by Django 4.2.1 on 2023-09-22 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminAccount', '0004_remove_attendence_login_time_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendence',
            new_name='Attendance',
        ),
    ]
