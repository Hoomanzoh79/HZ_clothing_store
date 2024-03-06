# Generated by Django 4.0.2 on 2024-01-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloths', '0004_alter_cloth_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='sales',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]