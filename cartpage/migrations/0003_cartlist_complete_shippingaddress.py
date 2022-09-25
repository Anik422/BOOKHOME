# Generated by Django 4.0.1 on 2022-09-19 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cartpage', '0002_cartlist_customer_alter_items_cart_alter_items_prodt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartlist',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=100)),
                ('adrs', models.CharField(default='', max_length=1000)),
                ('pincode', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cartpage.cartlist')),
            ],
        ),
    ]