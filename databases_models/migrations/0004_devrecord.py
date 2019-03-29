# Generated by Django 2.1.1 on 2019-03-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases_models', '0003_auto_20190227_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=512, null=True, verbose_name='开发内容')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='开发人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='开发时间')),
            ],
            options={
                'verbose_name_plural': '开发记录表',
                'db_table': 'devrecord',
            },
        ),
    ]