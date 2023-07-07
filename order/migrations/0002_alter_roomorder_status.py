# Generated by Django 4.2.1 on 2023-07-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomorder',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('cancelled', 'Cancelled'), ('issued', 'Issued'), ('ready', 'Ready')], default='issued', max_length=64),
        ),
    ]
