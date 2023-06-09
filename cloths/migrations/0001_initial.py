# Generated by Django 4.0.2 on 2023-03-26 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('season', models.CharField(choices=[('winter', 'winter'), ('summer', 'summer'), ('fall', 'fall')], max_length=6)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
