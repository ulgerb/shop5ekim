# Generated by Django 4.1.4 on 2022-12-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_brand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.FileField(null=True, upload_to='', verbose_name='Marka Logosu'),
        ),
    ]
