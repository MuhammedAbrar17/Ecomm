# Generated by Django 4.2.1 on 2023-07-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_cat_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(blank=True, upload_to='photos/categories'),
        ),
    ]