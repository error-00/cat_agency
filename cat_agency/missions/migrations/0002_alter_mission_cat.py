# Generated by Django 5.1.2 on 2024-10-31 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='cat',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cats.spycat'),
        ),
    ]