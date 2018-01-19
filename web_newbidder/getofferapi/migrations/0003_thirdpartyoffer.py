# Generated by Django 2.0 on 2017-12-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getofferapi', '0002_auto_20171222_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdPartyOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(max_length=11)),
                ('taskId', models.IntegerField(max_length=11)),
                ('status', models.IntegerField(max_length=11)),
                ('offerId', models.TextField()),
                ('name', models.CharField(default='', max_length=256)),
                ('previewLink', models.TextField()),
                ('trackingLink', models.TextField()),
                ('countryCode', models.TextField()),
                ('payoutMode', models.IntegerField(default=1, max_length=11)),
                ('payoutValue', models.DecimalField(decimal_places=5, default='0.00000', max_digits=10)),
                ('category', models.TextField()),
                ('carrier', models.TextField()),
                ('platform', models.TextField()),
                ('detail', models.TextField()),
            ],
            options={
                'db_table': 'ThirdPartyOffer',
            },
        ),
    ]
