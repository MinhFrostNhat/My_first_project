# Generated by Django 3.0 on 2020-06-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_cart1_user_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart1',
            name='user_product',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]