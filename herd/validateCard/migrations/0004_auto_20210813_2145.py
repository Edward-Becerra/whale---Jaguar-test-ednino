# Generated by Django 3.2.6 on 2021-08-14 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('validateCard', '0003_alter_validatecard_card_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='validatecard',
            name='account_id',
        ),
        migrations.RemoveField(
            model_name='validatecard',
            name='bank_id',
        ),
        migrations.RemoveField(
            model_name='validatecard',
            name='check_digit',
        ),
    ]