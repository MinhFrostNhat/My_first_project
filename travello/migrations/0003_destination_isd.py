# Generated by Django 3.0 on 2020-06-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='isd',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
