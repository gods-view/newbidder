# Generated by Django 2.0 on 2017-12-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getofferapi', '0004_auto_20171227_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False, verbose_name='用户id'),
        ),
    ]
