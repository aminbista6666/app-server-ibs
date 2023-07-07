# Generated by Django 4.2.1 on 2023-07-05 08:01

from django.db import migrations, models
import fiscalyear.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FiscalYear',
            fields=[
                ('fiscal_year', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, validators=[fiscalyear.utils.validate_fiscal_year])),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
