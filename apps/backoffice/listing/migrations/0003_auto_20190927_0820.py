# Generated by Django 2.2.5 on 2019-09-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20190927_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.CharField(max_length=64),
        ),
    ]