# Generated by Django 4.2.8 on 2024-01-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
