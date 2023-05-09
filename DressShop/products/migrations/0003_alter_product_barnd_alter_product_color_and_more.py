# Generated by Django 4.1.3 on 2023-05-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barnd',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.TextField(blank=True, default=1, null=True),
        ),
    ]
