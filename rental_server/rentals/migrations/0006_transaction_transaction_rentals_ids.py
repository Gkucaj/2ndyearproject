# Generated by Django 2.2.5 on 2020-04-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_transaction_transaction_product_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_rentals_ids',
            field=models.TextField(default=242),
            preserve_default=False,
        ),
    ]