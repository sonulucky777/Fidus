# Generated by Django 3.1 on 2020-08-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_app', '0012_auto_20200814_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='zip_code',
            field=models.CharField(blank=True, default='', max_length=12, null=True, verbose_name='Zip/Post Code'),
        ),
    ]
