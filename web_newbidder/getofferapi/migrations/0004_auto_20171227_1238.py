# Generated by Django 2.0 on 2017-12-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getofferapi', '0003_thirdpartyoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirdpartyoffer',
            name='id',
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False),
        ),
    ]
