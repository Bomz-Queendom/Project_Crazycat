# Generated by Django 4.0.2 on 2022-02-08 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_questionimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
