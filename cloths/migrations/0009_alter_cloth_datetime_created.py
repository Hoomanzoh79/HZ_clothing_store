# Generated by Django 4.0.2 on 2024-03-30 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cloths', '0008_alter_cloth_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
