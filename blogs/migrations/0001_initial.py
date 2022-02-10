# Generated by Django 4.0.2 on 2022-02-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('species_name', models.CharField(max_length=255)),
                ('species_detail', models.TextField()),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
