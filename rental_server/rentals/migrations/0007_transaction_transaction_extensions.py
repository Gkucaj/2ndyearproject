# Generated by Django 2.2.5 on 2020-04-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_transaction_transaction_rentals_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_extensions',
            field=models.TextField(default=2525),
            preserve_default=False,
        ),
    ]
