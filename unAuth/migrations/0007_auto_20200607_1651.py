# Generated by Django 3.0.6 on 2020-06-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unAuth', '0006_auto_20200606_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
