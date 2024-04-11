# Generated by Django 4.0.2 on 2024-04-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloths', '0012_cloth_category_alter_comment_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='category',
            field=models.CharField(blank=True, choices=[('tshirt', 'تیشرت و بلوز'), ('pants', 'شلوار'), ('jacket', 'ژاکت و مانتو'), ('suit', 'کت شلوار (رسمی)'), ('others', 'سایر')], max_length=10, null=True),
        ),
    ]