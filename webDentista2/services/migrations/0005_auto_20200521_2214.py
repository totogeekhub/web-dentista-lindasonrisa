# Generated by Django 2.1.5 on 2020-05-22 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=0, null=True, verbose_name='Precio'),
        ),
    ]