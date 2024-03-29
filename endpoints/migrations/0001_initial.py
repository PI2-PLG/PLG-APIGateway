# Generated by Django 2.2.6 on 2019-10-28 23:08

from django.db import migrations, models
import endpoints.enum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('service', models.CharField(choices=[(endpoints.enum.ServiceSet('BI'), 'BI'), (endpoints.enum.ServiceSet('NOTIFICATION'), 'NOTIFICATION')], max_length=50)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
