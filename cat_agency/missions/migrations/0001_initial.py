# Generated by Django 5.1.2 on 2024-10-31 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('cat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cats.spycat')),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('complete', models.BooleanField(default=False)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='missions.mission')),
            ],
            options={
                'unique_together': {('mission', 'name')},
            },
        ),
    ]
