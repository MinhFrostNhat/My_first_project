# Generated by Django 3.0 on 2020-06-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='hinhanh')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('isd', models.TextField()),
                ('special', models.BooleanField(default=False)),
            ],
        ),
    ]
