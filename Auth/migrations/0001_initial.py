# Generated by Django 3.0.6 on 2020-06-06 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unAuth', '0006_auto_20200606_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, unique=True)),
                ('url', models.CharField(max_length=512, unique=True)),
                ('year', models.CharField(max_length=1)),
                ('semester', models.CharField(max_length=1)),
                ('accessType', models.CharField(max_length=1)),
                ('createDate', models.DateField(auto_now_add=True)),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAuth.User')),
            ],
        ),
    ]
