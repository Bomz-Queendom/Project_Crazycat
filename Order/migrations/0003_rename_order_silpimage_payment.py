# Generated by Django 4.0.2 on 2022-02-09 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_payment_silpimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='silpimage',
            old_name='order',
            new_name='payment',
        ),
    ]