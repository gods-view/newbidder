# Generated by Django 2.0 on 2017-12-22 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getofferapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='user',
            name='update_time',
        ),
    ]