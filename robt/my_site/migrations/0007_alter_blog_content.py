# Generated by Django 4.1 on 2022-09-15 14:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0006_alter_call_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
    ]
