# Generated by Django 2.0.2 on 2018-02-06 09:45

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('riskapp', '0003_auto_20180206_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk_field',
            name='field_type',
            field=django_mysql.models.EnumField(choices=[('DATE', 'DATE'), ('ENUM', 'ENUM'), ('DECIMAL', 'DECIMAL'), ('TEXT', 'TEXT')]),
        ),
    ]
