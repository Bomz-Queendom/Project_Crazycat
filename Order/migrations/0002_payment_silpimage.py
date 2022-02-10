# Generated by Django 4.0.2 on 2022-02-09 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_end_date', models.DateTimeField(blank=True, null=True)),
                ('No_products_in_the_order', models.IntegerField()),
                ('tracking', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('basket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Order.basket')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SilpImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip', models.ImageField(blank=True, null=True, upload_to='slip/')),
                ('proofoftransfer', models.ImageField(blank=True, null=True, upload_to='หลักฐานการโอนเงิน/')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Order.payment')),
            ],
        ),
    ]
