# Generated by Django 3.1 on 2020-08-14 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_app', '0011_userprofileinfo_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='birthday',
            new_name='birth_date',
        ),
    ]
