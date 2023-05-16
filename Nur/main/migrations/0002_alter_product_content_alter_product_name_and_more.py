# Generated by Django 4.1.7 on 2023-03-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='photos/ProductImages'),
        ),
    ]