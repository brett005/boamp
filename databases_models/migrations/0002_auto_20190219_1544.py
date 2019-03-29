# Generated by Django 2.1.1 on 2019-02-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases_models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverhost',
            name='user',
        ),
        migrations.AddField(
            model_name='serverhost',
            name='user',
            field=models.ManyToManyField(to='databases_models.User', verbose_name='属于哪个用户'),
        ),
    ]
