# Generated by Django 4.0.3 on 2022-03-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_address_zip_code'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_2e448d_idx'),
        ),
    ]
