# Generated by Django 3.2.4 on 2021-06-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transfer',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Acc_No',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Current_Balance',
            field=models.IntegerField(),
        ),
    ]
