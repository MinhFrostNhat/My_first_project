# Generated by Django 3.0 on 2020-06-26 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200625_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart1',
            name='user_price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cart1',
            name='user_product',
            field=models.CharField(max_length=50),
        ),
    ]
