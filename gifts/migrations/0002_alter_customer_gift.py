# Generated by Django 4.1 on 2022-08-25 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gifts.gift'),
        ),
    ]
