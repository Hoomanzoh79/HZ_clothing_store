# Generated by Django 5.0.4 on 2024-05-29 10:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(regex='^(?!(\\d)\x01{3})[13-9]{4}[1346-9][ -]?[013-9]{5}$|^$')], verbose_name='کد پستی'),
        ),
    ]
