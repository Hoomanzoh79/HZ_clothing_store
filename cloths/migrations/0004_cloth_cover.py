# Generated by Django 4.0.2 on 2023-04-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloths', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='cover',
            field=models.ImageField(blank=True, upload_to='cloth/cloth_covers'),
        ),
    ]
