# Generated by Django 2.1.5 on 2019-02-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='update',
        ),
        migrations.AddField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion'),
        ),
    ]
