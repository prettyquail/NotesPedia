# Generated by Django 3.0.5 on 2020-05-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unAuth', '0003_auto_20200506_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]