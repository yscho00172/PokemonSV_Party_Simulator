# Generated by Django 4.1.3 on 2022-11-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon_Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type1', models.CharField(max_length=10)),
                ('Type2', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Compatibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=10)),
                ('Opposite', models.CharField(max_length=10)),
            ],
        ),
    ]
