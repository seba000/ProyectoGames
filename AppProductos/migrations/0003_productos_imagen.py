# Generated by Django 3.2.4 on 2021-06-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProductos', '0002_rename_marca_productos_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='juegos'),
        ),
    ]
