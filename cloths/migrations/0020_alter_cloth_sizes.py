# Generated by Django 4.0.2 on 2024-04-13 17:26

import cloths.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloths', '0019_alter_cloth_gender_alter_cloth_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='sizes',
            field=cloths.models.MultiSelectField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=17, null=True),
        ),
    ]
