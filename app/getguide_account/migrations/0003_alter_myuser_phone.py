# Generated by Django 4.0.10 on 2023-05-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getguide_account', '0002_busydates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='phone number'),
        ),
    ]