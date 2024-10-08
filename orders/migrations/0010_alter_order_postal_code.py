# Generated by Django 5.0.4 on 2024-05-01 08:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(regex='^(?!0)\\d(?!([0-9])\x01{3})[1-9]{3}[1346-9][013-46-9][1-9](?!\x01{8})\\d$')], verbose_name='Postal code'),
        ),
    ]
