# Generated by Django 5.1.2 on 2024-10-31 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years_of_experience', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
