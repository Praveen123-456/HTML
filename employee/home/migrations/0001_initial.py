# Generated by Django 5.0 on 2023-12-05 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
            ],
        ),
    ]
