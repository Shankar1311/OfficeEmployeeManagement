# Generated by Django 5.1.1 on 2024-11-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_rename_name_department_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
