# Generated by Django 5.0.4 on 2024-04-29 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloths', '0024_delete_showphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cloth/cloth_covers', verbose_name='Image')),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloths.cloth')),
            ],
        ),
    ]
