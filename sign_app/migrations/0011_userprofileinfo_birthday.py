# Generated by Django 3.1 on 2020-08-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_app', '0010_auto_20200812_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]