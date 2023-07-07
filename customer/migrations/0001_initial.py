# Generated by Django 4.2.1 on 2023-07-05 08:01

import common.utils
import customer.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companyinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to=customer.utils.get_upload_folder, validators=[common.utils.image_validate])),
                ('image2', models.ImageField(blank=True, null=True, upload_to=customer.utils.get_upload_folder, validators=[common.utils.image_validate])),
                ('id_type', models.CharField(blank=True, choices=[('license', 'License'), ('passport', 'Passport'), ('citizenship', 'Citizenship'), ('national_id', 'National ID')], max_length=48, null=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('phone1', models.CharField(max_length=15, unique=True)),
                ('phone2', models.CharField(blank=True, max_length=15, null=True)),
                ('points_earned', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='companyinfo.companyinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
