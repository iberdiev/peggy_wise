# Generated by Django 4.1.2 on 2022-10-22 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_usersavings_transaction_piggybank"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="cateogry",
            new_name="category",
        ),
    ]
