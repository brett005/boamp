# Generated by Django 2.1.1 on 2019-02-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostTmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('unique', models.CharField(max_length=40, unique=True)),
                ('host', models.CharField(max_length=32)),
                ('port', models.IntegerField()),
                ('user', models.CharField(max_length=32)),
                ('auth', models.CharField(max_length=16)),
                ('pkey', models.TextField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=180, null=True)),
            ],
        ),
    ]
